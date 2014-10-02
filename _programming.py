# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for writing in the Python and Go programming languages
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
    Choice
)
from _generic_edit import pressKeyMap
from format import format_snake_case, format_pascal_case, format_camel_case
import dragonfly

vim_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('python', context=vim_context)

mode = "gopher"
mode_map = {
    "gopher": "gopher",
    "python": "python",
    "sql": "sql",
}

sql_map = {
    "update": "UPDATE ",
    "select": "SELECT ",
    "from": "FROM ",
    "count": "COUNT ",
    "values": "VALUES ",
    "as": "AS ",
    "when": "WHEN ",
    "in": "IN ",
    "and": "AND ",
    "all": "ALL ",
    "similar to": "SIMILAR TO ",
    "like": "LIKE ",
    "set": "SET ",
}


def switch_mode(language):
    global mode
    mode = language


def create_class(text):
    if mode == "python":
        newText = 'class %s():\n    ' % format_pascal_case(text)
        Text("%(text)s").execute({"text": newText})


def create_private_function(text):
    if mode == "python":
        newText = 'def _%s(' % format_snake_case(text)
        Text("%(text)s").execute({"text": newText})
    elif mode == "gopher":
        newText = 'func %s(' % format_camel_case(text)
        Text("%(text)s").execute({"text": newText})


def create_class_function(text, text2):
    if mode == "gopher":
        newText = 'func (x *%s) %s(' % (format_pascal_case(text),
                                        format_pascal_case(text2))
        Text("%(text)s").execute({"text": newText})


def create_public_function(text):
    if mode == "python":
        newText = 'def %s(' % format_snake_case(text)
        Text("%(text)s").execute({"text": newText})
    elif mode == "gopher":
        newText = 'func %s(' % format_pascal_case(text)
        Text("%(text)s").execute({"text": newText})


def close_function():
    if mode == "python":
        Text("):\n").execute()
    elif mode == "gopher":
        Text(") {\n\n").execute()
        Key("up, tab").execute()


def print_line():
    if mode == "python":
        Text("print()").execute()
        Key("left").execute()
    if mode == "gopher":
        Text("fmt.Println()").execute()
        Key("left").execute()


def format_string():
    if mode == "gopher":
        Text("fmt.Sprintf()").execute()
        Key("left").execute()


def comment():
    Key("escape, i").execute()
    if mode == "python":
        Text("# ").execute()
    if mode == "gopher":
        Text("// ").execute()

def sql_word(sqlKeyword):
    if mode != "sql":
        sqlKeyword = sqlKeyword.lower().strip()
    Text("%(text)s").execute({"text": sqlKeyword})


def null():
    if mode == "python":
        Text("None").execute()
    if mode == "gopher":
        Text("nil").execute()


def true():
    if mode == "python":
        Text("True")
    if mode == "gopher":
        Text("true")


def false():
    if mode == "python":
        Text("False")
    if mode == "gopher":
        Text("false")


basics_mapping = aenea.configuration.make_grammar_commands('python', {
    'var': Text("var "),
    'new class [named] <text>': Function(create_class),
    'new [public] (function|func) [named] <text>': Function(create_public_function),
    'new private (function|func) [named] <text>': Function(create_private_function),
    'new class function <text> [named] <text2>': Function(create_class_function),
    'close (function|func)': Function(close_function),
    'new array': Key("lbracket, enter, enter, up, tab"),
    'print line': Function(print_line),
    'format string': Function(format_string),
    '(null|nil)': Function(null),
    'true': Function(true),
    'false': Function(false),
    'comment': Function(comment),
    'mode <language>': Function(switch_mode),
    '<sqlKeyword>': Function(sql_word),

    #  Common words
    'util': Text("util"),
    'air': Text("err"),
    'query': Text("query"),
    '(Jason|json)': Text("json"),
    'upper (Jason|json)': Text("JSON"),
    'extrahop': Text("extrahop"),  # Company name

    # Datatypes
    'type-int': Text("int"),
    'type-int 64': Text("int64"),
    'type-int 32': Text("int32"),
    'type-int 16': Text("int16"),
    'type-bool': Text("bool"),
    'type-string': Text("string"),

    # Python
    "pie-from": Text("from"),
    "pie-none": Text("None"),
    "pie-true": Text("True"),
    "pie-false": Text("False"),
    "pie-class method": Text("@classmethod\n"),
    "pie-def": Text("def "),
    "pie-for": Text("for "),
    "pie-dict": Text("dict("),
    "pie-set": Text("set("),
    "pie-sum": Text("sum("),
    "pie-len": Text("len("),
    "pie-list": Text("list("),
    "pie-tuple": Text("tuple("),
    "pie is instance": Text("isinstance("),
    "pie init": Text("__init__("),
    "[pie] self dot": Text("self."),
    "pie iter items": Text(".iteritems("),
    "pie string join": Key("apostrophe, right")+Text(".join("),
    "dunder": Text("__"),
    "dunder main": Text("__main__"),
    "dunder init": Text("__init__(self"),
    "dunder around": Key("underscore:4, left:2"),

    # Go lang
    'go-from': Text("from"),
    'go-true': Text("true"),
    'go-false': Text("false"),
    'go-none': Text("nil"),
    'go-nil': Text("nil"),
    'go-def': Text("func "),
    'go-slice': Text("make([])") + Key("left"),
    'go-struct': Text("type  struct {\n\n}") + Key("up:2, right:4"),
    })


operators_mapping = {
    'defined [as]':          Text(':= '),
    'assign [to]':           Text('= '),
    'compare (equal|to)':    Text('== '),
    'compare not equal': Text('!= '),
    'compare greater':  Text('> '),
    'compare less':     Text('< '),
    'compare geck':     Text('>= '),
    'compare lack':     Text('<= '),
    'bit ore':          Text('| '),
    'bit and':          Text('& '),
    'bit ex or':        Text('^ '),
    'times':            Text('* '),
    'divided':          Text('/ '),
    'plus':             Text('+ '),
    'minus':            Text('- '),
    'plus equal':       Text('+= '),
    'minus equal':      Text('-= '),
    'times equal':      Text('*= '),
    'divided equal':    Text('/= '),
    'mod equal':        Text('%%= '),
    'pointer to':       Text('*'),
}

data_types_mapping = {
    'string': Text('string'),
    'int': Text('int'),
    'int 64': Text('int64'),
    'enum': Text('enum'),
    'int 32': Text('int32'),
    '(boolean|bool)': Text('bool'),
    'struct': Text('struct'),
}


class Basics(dragonfly.MappingRule):
    mapping = basics_mapping
    extras = [
        Dictation('text'),
        Dictation('text2'),
        IntegerRef('n', 1, 999),
        IntegerRef('n2', 1, 999),
        Choice("pressKey", pressKeyMap),
        Choice("language", mode_map),
        Choice("sqlKeyword", sql_map),
    ]


class Operators(dragonfly.MappingRule):
    mapping = operators_mapping

class DataTypes(dragonfly.MappingRule):
    mapping = data_types_mapping

grammar.add_rule(Basics())
grammar.add_rule(Operators())
grammar.add_rule(DataTypes())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
