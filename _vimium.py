# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interatcting with Chrome. Requires the Vimium extension.
# http://vimium.github.io/
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import (
    IntegerRef
)
import dragonfly


chrome_context = aenea.ProxyCustomAppContext(executable="/opt/google/chrome/chrome")
grammar = dragonfly.Grammar('chrome', context=chrome_context)

window_mapping = {
    'page (previous|left)': Key("cs-tab"),
    'page (next|right)': Key("c-tab"),
    'page <n>': Key("c-%(n)d"),
    'page new': Key("c-t"),
    'page reopen': Key("cs-t"),
    'page close': Key("c-w"),
    'page back': Key("s-l"),
    'page forward': Key("s-l"),
    'more': Key("j:10"),
    'less': Key("k:10"),
    'top': Key("g, g"),
    'bottom': Key("s-g"),
    'back': Key("s-h"),
    'forward': Key("s-l"),

}

gmail_mapping = {
    'open': Key("o"),
    'inbox': Key("g, i"),
    '[go to] label <text>': Key("g, l") + Text("%(text)s") + Key("enter")
}


class Mapping(dragonfly.MappingRule):
    mapping = window_mapping
    extras = [
        IntegerRef('n', 1, 99),
    ]

class MappingMail( dragonfly.MappingRule):
     mapping = gmail_mapping
     extras = [
        Dictation('text')
     ]


grammar.add_rule(Mapping())
grammar.add_rule(MappingMail())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
