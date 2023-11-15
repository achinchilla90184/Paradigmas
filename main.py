from config import *
from feedprocessor import *

def main():
    cfg, err = getConfigOnFile('./config/config.json')
    
    if err != None:
        print(err)

    cfgClass = config(cfg)
    
    loadData(cfgClass.config)
main()