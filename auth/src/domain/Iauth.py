from abc import ABC, abstractmethod

class Iauth(ABC):

    @abstractmethod  
    def login(self):
        pass 

    @abstractmethod 
    def sign_up(self):
        pass 