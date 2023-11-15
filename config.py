import json
from types import SimpleNamespace

class config:

    def __init__(self, config) -> None:
        self.config = config

def getConfigOnFile(path):
    try:
        with open(path) as user_file:
            file_contents = user_file.read()
        config = json.loads(file_contents, object_hook=lambda d: SimpleNamespace(**d))
        user_file.close()
        return config, None
    except ImportError:
        return None, "unable to get config: "