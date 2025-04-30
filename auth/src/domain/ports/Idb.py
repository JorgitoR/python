from abc import ABC, abstractmethod

class IDatabase(ABC):

    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def close_sql_connection(self):
        pass

    @abstractmethod  
    def save(self, data:dict):
        pass 

    @abstractmethod 
    def get(self, id:str):
        pass 

    @abstractmethod 
    def update(self):
        pass 
