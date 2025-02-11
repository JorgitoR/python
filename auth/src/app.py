from ecase.service import ServiceAuth
from infra.db.nosql import Nosql

auth = ServiceAuth(db=Nosql(conn=""))
print(auth.login("test@gmail.com", password="123456"))

