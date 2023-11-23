from src.config.config import *
from src.feed_processor import *
from src.entities.via import *

def main():
    config_file, err = get_config_file('./src/config/config.json')
    
    if err != None:
        print(err)

    cfg = config(config_file)
    
    viasCollection = load_data_source(cfg.config)

    viasCollection = load_analyzed_data(viasCollection)
    
    process_data(viasCollection, cfg.config.traffic_lights)

main()