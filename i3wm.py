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


i3wm_mapping = aenea.configuration.make_grammar_commands('i3wm', {
    '(works|workspace) <n>': Key("a-%(n)d"),
    'lock screen': Key("a-d") + Text("i3lock") + Key("enter"),
    '(win|window) left': Key("a-j"),
    '(win|window) right': Key("a-semicolon"),
    '(win|window) up': Key("a-l"),
    '(win|window) down': Key("a-k"),
    'full-screen': Key("a-f"),
    '(win|window) stacking': Key("a-s"),
    '(win|window) default': Key("a-e"),
    '(win|window) tabbed': Key("a-w"),

    '(win|window) horizontal': Key("a-h"),
    '(win|window) vertical': Key("a-v"),
    '(win|window) terminal': Key("a-enter"),
    '(win|window) vertical (term|terminal)': Key("a-v, a-enter"),
    '(win|window) horizontal (term|terminal)': Key("a-h, a-enter"),

    '(win|window) (kill|close)': Key("a-s-q"),
    '(win|window) launch': Key("a-d"),
})


class Mapping(dragonfly.MappingRule):
    mapping = i3wm_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
        dragonfly.IntegerRef('appnum', 1, 99),
    ]


def get_grammar(context, config):
    i3wm_grammar = dragonfly.Grammar('i3wm', context=context)
    i3wm_grammar.add_rule(Mapping())
    return i3wm_grammar
