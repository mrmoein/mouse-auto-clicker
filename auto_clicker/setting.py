import json
import os
from auto_clicker.default import Default


class Setting:
    def __init__(self):
        self.__default = Default
        self.__config_path = "{repo_path}/../config.json".format(repo_path=os.path.dirname(__file__))
        self.data = self.__default.setting
        self.data = self.load_config()

    def update(self):
        data_json = json.dumps(self.data, indent=4)
        f = open(self.__config_path, "w+")
        f.write(data_json)
        f.close()

    def load_config(self):
        if not os.path.isfile(self.__config_path):
            self.update()
        f = open(self.__config_path, "r")
        data = json.loads(f.read())
        f.close()
        return data
