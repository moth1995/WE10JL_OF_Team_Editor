import yaml
from pathlib import Path
import os

class Config:
    config_dir = os.getcwd() + '/' + "config"
    
    def __init__(self,file="default.yaml"):
        self.file_location = file
        self.load_config()
        self.get_config_files()

    def load_config(self):
        with open(self.config_dir + "/" + self.file_location) as stream:
            self.file = yaml.safe_load(stream)

    def get_config_files(self):
        self.filelist = []
        self.games_config = []
        for p in Path(self.config_dir).iterdir():
            if p.is_file():
                self.filelist.append(p.name)
                self.games_config.append(p.stem)
