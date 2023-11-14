from config import getConfig

def main():
    config, err = getConfig('./config/config.json')
    
    if err != None:
        print(err)

main()