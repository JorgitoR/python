from domain.ports.Idb import IDatabase

class Nosql(IDatabase):

    def __init__(self, conn):
        self.conn = conn 

    def save(self, data:dict):
        # TODO: persist logic with real database
        return data

    def get(self, email:str):
        return None 

    def update(self):
        pass 


    