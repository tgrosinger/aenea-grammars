# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for writing in the Go programming language
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
from format import format_pascal_case, format_camel_case
import dragonfly


def create_private_function(text):
    Text('func %s(' % format_camel_case(text))


def create_public_function(text):
    Text('func %s(' % format_pascal_case(text)).execute()


def create_class_function(text, text2):
    newText = 'func (x *%s) %s(' % (format_pascal_case(text),
                                    format_pascal_case(text2))
    Text("%(text)s").execute({"text": newText})


go_mapping = aenea.configuration.make_grammar_commands('golang', {
    'var': Text("var "),
    'new [public] (function|func) [named] <text>': Function(create_public_function),
    'new private (function|func) [named] <text>': Function(create_private_function),
    'new class function <text> [named] <text2>': Function(create_class_function),
    'new array': Key("lbracket, enter, enter, up, tab"),
    'print line': Text("fmt.Println()") + Key("left"),
    'format string': Text("fmt.Sprintf()") + Key("left"),
    'comment': Key("escape, i") + Text("// "),

    # Common Words
    'air': Text("err"),

    # Datatypes
    'type-int': Text("int"),
    'type-int 64': Text("int64"),
    'type-int 32': Text("int32"),
    'type-int 16': Text("int16"),
    'type-bool': Text("bool"),
    'type-string': Text("string"),

    # Go lang
    'from': Text("from"),
    'true': Text("true"),
    'false': Text("false"),
    '(null|nil|none)': Text("nil"),
    'def': Text("func "),
    'slice': Text("make([])") + Key("left"),
    'struct': Text("type  struct {\n\n}") + Key("up:2, right:4"),
})


class Golang(dragonfly.MappingRule):
    mapping = go_mapping
    extras = [
        Dictation('text'),
        Dictation('text2'),
        IntegerRef('n', 1, 999),
        IntegerRef('n2', 1, 999),
    ]

def get_grammar(context):
    go_grammar = dragonfly.Grammar('go', context=context)
    go_grammar.add_rule(Golang())
    return go_grammar


