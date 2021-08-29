from src.infra.config import *
from src.infra.entites import *

print("loading...")
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)
print("finish...")
