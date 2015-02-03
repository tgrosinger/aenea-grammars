# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interatcting with Firefox. Requires the Vimfx extension.
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
from aenea import (
    IntegerRef
)
import dragonfly


firefox_context = aenea.ProxyCustomAppContext(executable="/usr/lib/firefox/firefox")
grammar = dragonfly.Grammar('firefox', context=firefox_context)

window_mapping = {
    # Tab navigation
    'page (previous|left)': Key("cs-tab"),
    'page (next|right)': Key("c-tab"),
    'page (home|first)': Key("g, s-h"),
    'page (end|last)': Key("g, s-l"),
    'page new': Key("c-t"),
    'page reopen': Key("cs-t"),
    'page close': Key("c-w"),
    '[page] back': Key("s-h"),
    '[page] forward': Key("s-l"),
    'refresh': Key("r"),
    'link': Key("f"),
    'link new': Key("s-f"),

    #  Moving around
    'more': Key("d"),
    'less': Key("u"),
    'screen down': Key("c, f"),
    'screen up': Key("c, u"),
    'top': Key("g, g"),
    'bottom': Key("s-g"),

    #  Searching
    'find <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    'next': Key("n"),
    'prev|previous': Key("N"),
}

gmail_mapping = {
    'open': Key("o"),
    'inbox': Key("g, i"),
    '[go to] label <text>': Key("g, l") + Text("%(text)s") + Key("enter"),
    'trash': Key("hash"),
    'archive': Key("e"),
    '(earl|early|earlier)': Key("j"),
    '(late|later)': Key("k"),
}


class Mapping(dragonfly.MappingRule):
    mapping = window_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
    ]

class MappingMail(dragonfly.MappingRule):
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
