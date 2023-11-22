from src.config.config import *
from src.feedprocessor import *
from src.entities.via import *

def main():
    cfg, err = getConfigOnFile('./src/config/config.json')
    
    if err != None:
        print(err)

    cfgClass = config(cfg)
    
    viasData = loadData(cfgClass.config)
    processData(cfgClass.config, viasData)
main()