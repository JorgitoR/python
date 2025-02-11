from abc import ABC, abstractmethod

class IDatabase(ABC):

    @abstractmethod  
    def save(self, data:dict):
        pass 

    @abstractmethod 
    def get(self, id:str):
        pass 

    @abstractmethod 
    def update(self):
        pass 
