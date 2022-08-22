import unittest
import json
import os
import main

def create_test_data(data, directory, schema):
    try: 
        os.mkdir(directory) 
        os.mkdir(schema) 
    except OSError as error: 
        print(error)
    with open(f'{directory}/test_data.json', 'w') as file:
        json.dump(data, file)

class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data_dir = 'test_data'
        self.test_schema_dir = 'test_schema'
        self.test_data = {
            "attributes": {
            "appName": "ABCDEFGHIJKLMNOPQRSTUVW",
            "eventType": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "subEventType": "ABCDEFGHIJKLMNO",
            "sensitive": False
            },
            "message": {
            "user": {
                "id": "ABCDEFGHIJKLMNOP",
                "nickname": "ABCD",
                "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
                "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
                "countryCode": "ABCDEFGHIJKLMNOPQRSTUVWX",
                "orientation": "ABCDEFGHIJKLMNOPQRSTU"
            },
            "time": 890,
            "acl": [],
            "publicFeed": False,
            "internationalCountries": [
                "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
                "ABCDEFGHIJKLMNOPQ",
                "ABCDEFGHIJKLMNOPQRSTUVW",
                "ABCDEFGHIJKLMNOPQRSTUVWXY",
                "ABCDEFGHIJK",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "ABCDEFGHIJKLMNOPQR",
                "ABCDEFG",
                "ABCDEFGHIJKLM"
            ],
            "topTraderFeed": True
            }
        }
        create_test_data(self.test_data, self.test_data_dir, self.test_schema_dir)
        return super().setUp()

    def tearDown(self) -> None:
        [os.remove(f'{self.test_data_dir}/{file}') for file in os.listdir(self.test_data_dir)]
        [os.remove(f'{self.test_schema_dir}/{file}') for file in os.listdir(self.test_schema_dir)]
        os.rmdir(self.test_data_dir)
        os.rmdir(self.test_schema_dir)
        return super().tearDown()

    def test_data_folder_exists(self):
        self.assertTrue(os.path.isdir(self.test_data_dir))

    def test_data_folder_is_not_empty(self):
        self.assertTrue(len(os.listdir(self.test_data_dir))  > 0)

    def test_datas_in_data_folder_are_json(self):
        self.assertTrue(all([item.endswith('.json') for item in os.listdir(self.test_data_dir)]))

    def test_schema_folder_exists(self):
        self.assertTrue(os.path.isdir(self.test_schema_dir))

    def test_data_is_json(self):
        with open(f'{self.test_data_dir}/test_data.json') as in_file:
            input_json = json.load(in_file)
            self.assertIs(type(input_json), dict)

    def test_generate_schema_creates_schema(self):
        main.generate_schema(self.test_data_dir, self.test_schema_dir)
        self.assertTrue(len(os.listdir(self.test_schema_dir))  > 0)

    def test_generated_schema_is_json(self):
        self.assertTrue(all([item.endswith('.json') for item in os.listdir(self.test_schema_dir)]))

if __name__ == '__main__':
    unittest.main()