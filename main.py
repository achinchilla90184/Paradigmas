from config import *
from feedprocessor import *
from via import *
import json 

def main():
    cfg, err = getConfigOnFile('./config/config.json')
    
    if err != None:
        print(err)

    cfgClass = config(cfg)
    
    viasData = loadData(cfgClass.config)
    # jsonstr1 = json.dumps(viasData[0]) 
    # print(viasData)
    for via in viasData:
        if via.emergency_vehicle:
            via.calculateViaValue(cfgClass.config)    
main()