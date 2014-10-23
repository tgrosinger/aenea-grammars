# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Wrapper which loads the window manager commands based on configuration file
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from config import get_configuration

# Window Managers
import cinnamon
import i3wm

context = aenea.ProxyPlatformContext('linux')
language_map = {
    "cinnamon":  cinnamon,
    "i3": i3wm
}
grammar = None

config = get_configuration()
if config is None or "window-manager" not in config:
    print("Could not find window manager configuration in config file")
    print("Aborting window manager load")
else:
    selected_language = language_map[config["window-manager"]]
    if selected_language is None:
        print("Selected window manager is invalid. Please consult the README")
    else:
        grammar = selected_language.get_grammar(context, config)
        if grammar is not None:
            grammar.load()


def unload():
    if grammar is not None:
        grammar.unload()
