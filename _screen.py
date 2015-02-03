# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with Git
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key
from aenea import IntegerRef
import dragonfly

screen_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('screen', context=screen_context)

screen_mapping = aenea.configuration.make_grammar_commands('screen', {
    'screen (right|next)': Key("c-a, n"),
    'screen (left|previous)': Key("c-a, p"),
    'screen create': Key("c-a, c"),
    'screen <n>': Key("c-a, %(n)d"),
    'screen rename': Key("c-a, s-a"),
    'screen exit': Key("c-a, backslash"),

    'screen [split] vertical': Key("c-a, bar"),
    'screen [split] horizontal': Key("c-a, s-s"),
    'screen split next': Key("c-a, tab")
})


class Mapping(dragonfly.MappingRule):
    mapping = screen_mapping
    extras = [
        IntegerRef('n', 1, 9)
    ]

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
