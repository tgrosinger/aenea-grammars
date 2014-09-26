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
from aenea.lax import Key
import dragonfly

window_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('windows', context=window_context)

window_mapping = aenea.configuration.make_grammar_commands('windows', {
    'workspace one': Key("ca-1"),
    'workspace two': Key("ca-2"),
    '(terminal|term) left': Key("c-pgup"),
    '(terminal|term) right': Key("c-pgdown"),
    '(terminal|term) new [tab]': Key("cs-t"),
    '(terminal|term) new window': Key("cs-n"),
    'switch (application|app)': Key("a-tab"),
})


class Mapping(dragonfly.MappingRule):
    mapping = window_mapping

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
