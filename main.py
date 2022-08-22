import os, json

def get_datatype(data):
    if isinstance(data, int):
        return 'INTEGER'
    elif isinstance(data, str):
        return 'STRING'
    elif isinstance(data, list):
        if all(isinstance(item, str) for item in data):
            return 'ENUM'
        elif all(isinstance(item, str) for item in data):
            return 'ARRAY'
        else:
            return 'LIST'
    else:
        return 'UNHANDLED TYPE'

def get_schema(data, result={}):
    for key in data:
        if key != 'attributes':
            if isinstance(data[key], dict):
                result[key] = get_schema(data[key], {})
            else:
                result[key] = {
                    "type": get_datatype(data[key]),
                    "tag": "",
                    "description": "",
                    "required": False
                }
    return result

def generate_schema(data_directory, schema_directory):
    for file in os.listdir(data_directory):
        with open(f'{data_directory}/{file}') as in_file:
            input_json = json.load(in_file)
            message = input_json['message']
            file_schema = get_schema(message, {})
            with open(f"{schema_directory}/schema_{file}", "w") as out_file:
                json.dump(file_schema, out_file)

generate_schema('data', 'schema')