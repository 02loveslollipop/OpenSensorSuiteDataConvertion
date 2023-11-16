import yaml

class config:
    def __init__(self) -> None:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.host = config['redis']['host']
            self.port = config['redis']['port']
            self.password = config['redis']['password']
            self.key_origin = config['redis']['key_origin']
            self.key_destination = config['redis']['key_destination']
            self.update_interval = config['service']['update_interval']

            
            
            
            