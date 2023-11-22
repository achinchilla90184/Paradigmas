from config import *
from feedprocessor import *
from via import *

def main():
    cfg, err = getConfigOnFile('./config/config.json')
    
    if err != None:
        print(err)

    cfgClass = config(cfg)
    
    viasData = loadData(cfgClass.config)
    processData(cfgClass.config, viasData)
main()