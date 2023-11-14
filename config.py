import json

def getConfig(path):
    try:
        file = open(path)
        config = json.load(file)
        file.close()
        return config, None
    except:
        return None, "unable to get config"