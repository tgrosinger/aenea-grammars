# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with the i3 window manager
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Text
from aenea import IntegerRef, Dictation
import dragonfly
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise


def get_grammar(context, config):
    if "i3-mod-key" not in config:
        print("Missing required 'i3-mod-key' in config file")
        return None

    mod_key = config["i3-mod-key"]
    mod_char = "a"
    if mod_key == "ctrl":
        mod_char = "c"
    elif mod_key == "alt":
        mod_char = "a"
    elif mod_key == "win":
        mod_char == "w"
    else:
        print("Invalid value specified for 'i3-mod-key' in config file")
        return None

    # FIXME: This is nested because we need access to the mod_char
    class Mapping(dragonfly.MappingRule):
        mapping = aenea.configuration.make_grammar_commands('i3wm', {
            '(works|workspace) <n>': Key(mod_char + "-%(n)d"),
            'lock screen': Key(mod_char + "-d") + Text("i3lock") + Key("enter"),
            '(win|window) left': Key(mod_char + "-j"),
            '(win|window) right': Key(mod_char + "-semicolon"),
            '(win|window) up': Key(mod_char + "-l"),
            '(win|window) down': Key(mod_char + "-k"),
            'full-screen': Key(mod_char + "-f"),
            '(win|window) stacking': Key(mod_char + "-s"),
            '(win|window) default': Key(mod_char + "-e"),
            '(win|window) tabbed': Key(mod_char + "-w"),

            '(win|window) horizontal': Key(mod_char + "-h"),
            '(win|window) vertical': Key(mod_char + "-v"),
            '(win|window) terminal': Key(mod_char + "-enter"),
            '(win|window) vertical (term|terminal)': Key(mod_char + "-v, a-enter"),
            '(win|window) horizontal (term|terminal)': Key(mod_char + "-h, a-enter"),

            '(win|window) (kill|close)': Key(mod_char + "s-q"),
            '(win|window) launch': Key(mod_char + "-d"),
        })
        extras = [
            IntegerRef('n', 1, 99),
            Dictation('text'),
            dragonfly.IntegerRef('appnum', 1, 99),
        ]


    i3wm_grammar = dragonfly.Grammar('i3wm', context=context)
    i3wm_grammar.add_rule(Mapping(mod_char))
    return i3wm_grammar
