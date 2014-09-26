# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with Vim
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import (
    Dictation,
    IntegerRef,
    Text,
    Choice
)
import dragonfly

from _generic_edit import pressKeyMap

vim_context = aenea.ProxyCustomAppContext(executable="gnome-terminal")
grammar = dragonfly.Grammar('vim', context=vim_context)

surroundCharsMap = {
    'quotes': '"',
    'parens': "(",
    'brackets': "[",
    'braces': "{",
}


def goto_line(n):
    for c in str(n):
        Key(c).execute()
    Key("G").execute()

def yank_lines(n, n2):
    goto_line(n)
    Key("V").execute()
    goto_line(n2)
    Key("y").execute()

def delete_lines(n, n2):
    goto_line(n)
    Key("V").execute()
    goto_line(n2)
    Key("d").execute()


basics_mapping = aenea.configuration.make_grammar_commands('vim', {
    'vim': Text("vim"),

    'window left': Key("escape, c-h"),
    'window right': Key("escape, c-l"),
    'window up': Key("escape, c-k"),
    'window down': Key("escape, c-j"),
    'window close': Key("escape, colon, q, enter"),

    'open [in] split': Key("s"),
    'open [in] tab': Key("t"),

    'tab <n>': Key("escape, comma, %(n)d"),

    '(F|half) up': Key("escape, 2, 0, c-y"),
    '(F|half) down': Key("escape, 2, 0, c-e"),
    'screen down': Key("escape, c-f"),
    'screen up': Key("escape, c-b"),

    'append to [end of] [line] <n>': Key("escape") + Function(goto_line) + Key("A"),
    'append': Key("escape, A"),
    'prepend': Key("escape, I"),
    'insert': Key("i"),
    'insert below': Key("escape, o"),
    'insert above': Key("escape, O"),
    'undo': Key("escape, u, i"),
    'scratch': Key("escape, u, i"),
    'escape': Key("escape"),
    'filename': Key("escape, c-g"),
    'save': Key("escape, colon, w, enter"),
    'save and quit': Key("escape, colon, w, q, enter"),
    'discard': Key("colon, q, exclamation"),
    'change case':Key("escape, right, s-backtick, i, left"),

    'find <text>': Key("escape, slash") + Text("%(text)s")+ Key("enter"),
    'next': Key("n"),
    'prev|previous': Key("N"),
    'clear search': Key("colon, n, o, h, enter"),

    'replace letter': Key("r"),
    'replace mode': Key("R"),

    'easy motion': Key("escape, comma, comma, s"),
    'en': Key("end"),

    'select word': Key("escape, right, v, e"),
    'select until <pressKey>': Key("escape, v, t") + Text("%(pressKey)s"),
    'select including <pressKey>': Key("escape, v, f") + Text("%(pressKey)s"),
    'dell until <pressKey>': Key("escape, d, t") + Text("%(pressKey)s"),
    'dell including <pressKey>': Key("escape, d, f") + Text("%(pressKey)s"),

    'change [<n>] (word|words)': Key("escape, c, %(n)d, w"),
    'change word': Key("right, escape, c, i, w"),
    'dell [<n>] (word|words)': Key("escape, d, %(n)d, w"),
    'dell [this] line': Key("escape, V, d"),
    'dell line <n> (thru|through|to) <n2>': Key("escape") + Function(delete_lines),

    'yank': Key("y"),
    'extract': Key("x"),
    'yank this line': Key("escape, y:2"),
    'yank line <n>': Key("escape") + Function(goto_line) + Key("y:2"),
    'yank line <n> (thru|through|to) <n2>': Key("escape") + Function(yank_lines),
    'glue': Key('p'),

    'up <n> (lines|line)': Key("%(n)d, up"),
    'down <n> (lines|line)': Key("%(n)d, down"),
    'go to [line] <n>': Key("escape") + Function(goto_line),
    'forward':  Key("escape, right, w, i"),
    'forward <n>': Key("escape, %(n)d, w, i"),
    'forend': Key("escape, e, i"),
    'backward': Key("escape, b, i"),
    'backward <n>': Key("escape, %(n)d, b, i"),
    'matching': Key("escape, percent")
    })


class Basics(dragonfly.MappingRule):
    mapping = basics_mapping
    extras = [
        Dictation('text'),
        IntegerRef('n', 1, 999),
        IntegerRef('n2', 1, 999),
        Choice("pressKey", pressKeyMap),
        Choice("surroundChar", surroundCharsMap),
    ]

grammar.add_rule(Basics())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
