import json


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        with open("config.json", "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def get(self, key):
        return self.config[key]