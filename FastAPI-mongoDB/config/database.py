from pydantic_settings import BaseSettings, SettingsConfigDict
from pymongo.mongo_client import MongoClient


# allows automatic type checking and validation
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="./config/.env")
    db_url: str
    db_name: str
    db_collection_name: str


settings = Settings()

client = MongoClient(
    settings.db_url,
)

db = client[settings.db_name]
collection_name = db[settings.db_collection_name]
