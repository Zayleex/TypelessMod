import yaml

class ConfigLoader:
    def __init__(self):
        self.filename = "config.yaml"

    def load(self):
        with open(self.filename, "r") as stream:
            data = yaml.safe_load(stream)
            return data
