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

tmux_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('tmux', context=tmux_context)

tmux_mapping = aenea.configuration.make_grammar_commands('tmux', {
    'team (right|next)': Key("c-b, n"),
    'team (left|previous)': Key("c-b, p"),
    'team create': Key("c-b, c"),
    'team <n>': Key("c-b, %(n)d"),
    'team rename': Key("c-b, comma"),
    'team exit': Key("c-b, backslash"),
    'team detach': Key("c-b, d"),

    'team [pane] vertical': Key("c-b, percent"),
    'team [pane] horizontal': Key("c-b, dquote"),
    'team swap': Key("c-b, o"),
    'team pane up': Key("c-b, up"),
    'team pane down': Key("c-b, down"),
    'team pane left': Key("c-b, left"),
    'team pane right': Key("c-b, right"),
    'team pane close': Key("c-b, x")
})


class Mapping(dragonfly.MappingRule):
    mapping = tmux_mapping
    extras = [
        IntegerRef('n', 0, 10)
    ]

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
