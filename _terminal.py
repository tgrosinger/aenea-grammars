# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with terminal and desktop environment
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Text
import dragonfly
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

terminal_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('terminal', context=terminal_context)

terminal_mapping = aenea.configuration.make_grammar_commands('terminal', {
    # Terminal commands
    # dir is hard to say and recognize. Use something else
    'deer up': Text("cd ..") + Key("enter"),
    'deer list': Text("ls") + Key("enter"),
    'deer list all': Text("ls -lha") + Key("enter"),
    'deer list details': Text("ls -lh") + Key("enter"),
    'deer into': Text("cd "),

    '(terminal|term) clear': Text("clear") + Key("enter"),
    '(terminal|term) left': Key("c-pgup"),
    '(terminal|term) right': Key("c-pgdown"),
    '(terminal|term) new [tab]': Key("cs-t"),
    '(terminal|term) (close|exit)': Key("c-c") + Text("exit") + Key("enter"),

    # Common words
    '(pseudo|sudo|pseudo-)': Text("sudo "),
    '(apt|app) get': Text("sudo apt-get "),
    '(apt|app) get install': Text("sudo apt-get install "),
})


class Mapping(dragonfly.MappingRule):
    mapping = terminal_mapping
    extras = []

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
