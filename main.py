from src.config.config import *
from src.feed_processor import *
from src.entities.via import *

def main():
    config_file, err = get_config_file('./src/config/config.json')
    
    if err != None:
        print(err)

    cfg = config(config_file)
    
    data = load_data(cfg.config)
    process_data(cfg.config, data)

main()