# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Wrapper which loads the window manager commands based on configuration file
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import json
import os
import aenea
import aenea.configuration

# Window Managers
import cinnamon
import i3wm

config_file_location = 'c:\NatLink\NatLink\MacroSystem\grammar_config.json'

context = aenea.ProxyPlatformContext('linux')
language_map = {
    "cinnamon":  cinnamon,
    "i3": i3wm
}

if not os.path.isfile(config_file_location):
    config_file = open(config_file_location, "w")
    json.dump({"window-manager": ""}, config_file)
    config_file.close()
    print("Created new config file in %s" % config_file_location)
else:
    config_file = open(config_file_location)
    config = json.load(config_file)
    config_file.close()

    selected_language = language_map[config["window-manager"]]
    if selected_language is None:
        print("Could not load your window manager grammar")
    else:
        grammar = selected_language.get_grammar(context, config)
        grammar.load()


def unload():
    if grammar is not None:
        grammar.unload()
