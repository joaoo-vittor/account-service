import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
# SQLALCHEMY_DATABASE_URI = "postgresql://vfuufikegxphlo:40432bbf7d8bc9914823a52b42247d95aac352cdc48fb2ed4f22633373165f04@ec2-18-215-44-132.compute-1.amazonaws.com:5432/dft3op6uklavai"
HASH = os.environ.get("HASH")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
AMQP_URL = os.environ.get("AMQP_URL")
SWAGGER_URL = "/api/v1/doc"
API_URL = "/static/swagger.yaml"
