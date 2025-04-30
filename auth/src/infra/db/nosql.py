from domain.ports.Idb import IDatabase
from typing import Type
from utils.schema import BU
import boto3 as boto
from config import AWS_REGION, DYNAMODB_TABLE_NAME

class NoSQL(IDatabase):

    def __init__(self):
        pass

    @property
    def create_connection(self):
        self.dynamodb = boto.resource("dynamodb", region_name=AWS_REGION)
        table = self.dynamodb.Table(DYNAMODB_TABLE_NAME)
        return table
    
    def close_sql_connection(self):
        pass

    def save(self, data: Type[BU]):
        """ Guarda un usuario en DynamoDB """
        try:
            table = self.create_connection
            data_dict = data.model_dump()
            data_dict["sk"] = 'user'
            data_dict["pk"] = data.email
            table.put_item(Item=data_dict)
            return {"message": "Usuario guardado en DynamoDB", "user": data_dict}
        except Exception as e:
            return {"error": str(e)}

    def get(self, email:str):
        """ Obtiene un usuario en DynamoDB por email """
        try:
            table = self.create_connection
            response = table.get_item(Key={"pk": email, "sk": "user"})
            if "Item" in response:
                return response["Item"]
            return None
        except Exception as e:
            print(f"Error consultando DynamoDB: {e}")
            return {"error": str(e)}

    def update(self, update_data: Type[BU], email:str):
        """ Actualiza un usuario en DynamoDB """
        try:
            table = self.create_connection
            update_data_dict = update_data.model_dump()
            update_data_dict["pk"] = email
            table.put_item(Item=update_data_dict)
            return {"message": "Usuario actualizado en DynamoDB", "user": update_data_dict}
        except Exception as e:
            return {"error": str(e)}
