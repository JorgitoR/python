from domain.ports.Idb import IDatabase
from typing import Type
from utils.schema import BU
import boto3 as boto
import uuid


class NoSQL(IDatabase):

    def __init__(self):
        self.conn  = boto.resource(service_name="dynamodb", region_name="us-east-2")

    def save(self, data: Type[BU]):
        print(type(data))
        print("guardando data en nosql: ", data)
        try:
            print("dynamodb: ", self.conn)
            id = str(uuid.uuid4())
            dict = data.model_dump()
            dict["pk"] = id
            dict["sk"] = id
            print("data: ", dict)
            conn = self.conn
            table = conn.Table("auth")
            response = table.put_item(Item=dict)
        except Exception as e:
            raise e 
        
        else:
            response

    def get(self, id:str):
        pass 

    def update(self, data: Type[BU], id:str):
        try:

            data["pk"] = id
            data["sk"] = id
            print("data: ", data)
            conn = self.conn
            table = conn.Table("auth")
            response = table.put_item(Item=data)
        except Exception as e:
            raise e 
        
        else:
            response 
