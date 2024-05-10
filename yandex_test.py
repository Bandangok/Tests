import requests
from pprint import pprint
from unittest import TestCase


base_url = 'https://cloud-api.yandex.net'
token = 'y0_AgAAAAB1Hl0xAADLWwAAAAEAJ2WDAAA8CTZjGbdGu7vwGuRVk8WkWxuXMQ'


def create_resources(token):
    url_for_creating_folder = base_url + '/v1/disk/resources'
    headers = {
        'Authorization': token
    }
    params = {
        'path': 'Image34'
    }
    response = requests.put(url_for_creating_folder, headers=headers, params=params)
    return response.status_code



def create_resources_2(token):
    url_for_creating_folder = base_url + '/v1/disk/resources'
    headers = {
        'Authorization': token
    }
    params = {
        'path': ''
    }
    response = requests.put(url_for_creating_folder, headers=headers, params=params)
    return response.status_code

class TestSomething(TestCase):
    def test_create_ok(self):
        a = 'y0_AgAAAAB1Hl0xAADLWwAAAAEAJ2WDAAA8CTZjGbdGu7vwGuRVk8WkWxuXMQ'
        exp = 201
        result = create_resources(a)
        self.assertEqual(result, exp)


    def test_create_false(self):
        a = 'y0_AgAAAAB1Hl0xAADLWwAAAAEAJ2WDAAA8CTZjGbdGu7vwGuRVk8WkWxuXMQ111'
        exp = 401
        result = create_resources(a)
        self.assertEqual(result, exp)


    def test_create_ok2(self):
        a = 'y0_AgAAAAB1Hl0xAADLWwAAAAEAJ2WDAAA8CTZjGbdGu7vwGuRVk8WkWxuXMQ'
        exp = 409
        result = create_resources(a)
        self.assertEqual(result, exp)

    def test_create_false2(self):
        a = 'y0_AgAAAAB1Hl0xAADLWwAAAAEAJ2WDAAA8CTZjGbdGu7vwGuRVk8WkWxuXMQ'
        exp = 400
        result = create_resources_2(a)
        self.assertEqual(result, exp)


