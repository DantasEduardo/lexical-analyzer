import json


def read_data(filename):
    if "s3://" in filename:
        pass
    else:
         return read_data_local(filename)


def read_data_local(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return  json.load(file)