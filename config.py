import json
import os

default_path = 'c:\NatLink\NatLink\MacroSystem\grammar_config.json'
loaded_config = None


# Retrieve a dictionary representation of the JSON config file
def get_configuration(config_file_path=default_path):
    global loaded_config

    if loaded_config is not None:
        return loaded_config

    if not os.path.isfile(config_file_path):
        print("Could not find configuration file")
        print("Please create %s" % config_file_path)
        print("Detailed instructions can be found in the README.md")
        return None

    with open(config_file_path) as f:
        loaded_config = json.load(f)
        return loaded_config
