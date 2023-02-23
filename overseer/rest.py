from requests import get
from typing import List
import json
import collections

Board = collections.namedtuple('Board', ['id', 'name', 'type'])

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
