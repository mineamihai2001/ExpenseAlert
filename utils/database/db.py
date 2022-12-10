import pymongo
from dotenv import load_dotenv, dotenv_values
from configs.config import ENV

env = dotenv_values(ENV)
conn_str = env["CONN_STR"]

client = pymongo.MongoClient(conn_str)
db = client.expense_alert
