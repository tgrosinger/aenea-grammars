# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for writing in the Python programming language
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import (
    IntegerRef,
    Text,
    Dictation,
)
from format import format_snake_case, format_pascal_case
import dragonfly


def create_class(text):
    Text('class %s():\n    ' % format_pascal_case(text)).execute()


def create_private_function(text):
    Text('def _%s(' % format_snake_case(text)).execute()


def create_public_function(text):
    Text('def %s(' % format_snake_case(text)).execute()


python_mapping = aenea.configuration.make_grammar_commands('python', {
    'new class [named] <text>': Function(create_class),
    'new [public] (function|func) [named] <text>': Function(create_public_function),
    'new private (function|func) [named] <text>': Function(create_private_function),
    'close (function|func)': Text("):\n"),
    'comment': Key("escape, i") + Text("# "),

    # Python
    "true": Text("True"),
    "false": Text("False"),
    '(none|null|nil)': Text("none"),
    'print line': Text("print()") + Key("left"),
    "class method": Text("@classmethod\n"),
    "(def|define)": Text("def "),
    "(dict|dictionary)": Text("dict("),
    "set": Text("set("),
    'array': Key("lbracket, enter, enter, up, tab"),
    "sum": Text("sum("),
    "(len|length)": Text("len("),
    "list": Text("list("),
    "tuple": Text("tuple("),
    "is instance": Text("isinstance("),
    "init": Text("__init__("),
    "self dot": Text("self."),
    "iter items": Text(".iteritems("),
    "string join": Key("apostrophe, right")+Text(".join("),
    "dunder": Text("__"),
    "dunder main": Text("__main__"),
    "dunder init": Text("__init__(self"),
    "dunder around": Key("underscore:4, left:2"),
})


class Python (dragonfly.MappingRule):
    mapping = python_mapping
    extras = [
        Dictation('text'),
        Dictation('text2'),
        IntegerRef('n', 1, 999),
        IntegerRef('n2', 1, 999),
    ]


def get_grammar(context):
    python_grammar = dragonfly.Grammar('python', context=context)
    python_grammar.add_rule(Python())
    return python_grammar
