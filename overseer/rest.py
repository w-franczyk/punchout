from requests import get, post
from typing import List
import json
import collections

Board = collections.namedtuple('Board', ['id', 'name', 'type'])
Category = collections.namedtuple('Board', ['id', 'name', 'colour', 'boardId'])

class Rest:
    url = 'http://localhost:8000'

    @staticmethod
    def getBoards() -> List[Board]:
        response = get(Rest.url + '/getboards')
        if response.status_code != 200:
            print(response.text)
            raise "Bad return code!"
        
        try:
            items = [Board(**item) for item in response.json()]
        except:
            print(response.text)
            raise

        return items
    
    @staticmethod
    def addCategory(name, colour, boardId):
        data = {'name': name, 'colour': colour, 'boardId': boardId}
        #data = {'name': 'dupa', 'colour': 'ff0000', 'boardId': 2}
        print(data)
        response = post(Rest.url + '/categories/', json=data)
        print(response.text)
        print(response.json())
