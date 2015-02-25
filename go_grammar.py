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
    '(def|deaf)': Text("func()") + Key("left"),
    'slice': Text("make([])") + Key("left"),
    'struct': Text("type  struct {\n\n}") + Key("up:2, right:4"),

    # Common Constructs
    'handler params': Text("w http.ResponseWriter, r *http.Request"),
    'import statement': Text("import(\n\t\n)") + Key("up, right"),

    # Vim specific commands for Go
    # TODO: Find a way to only import these if Vim is in context
    'help format':            Key("escape, right, colon") + Text("GoFmt") + Key("enter, i"),
    'help imports':           Key("escape, right, colon") + Text("GoImports")  + Key("enter, i"),
    'help (deaf|def|definition)': Key("escape, right, colon") + Text("GoDef")  + Key("enter, i"),
    'help (dock|docks)':      Key("escape, right, colon") + Text("GoDoc")      + Key("enter, i"),
    'help browser':           Key("escape, right, colon") + Text("GoDocBrowser") + Key("enter, i"),
    'help lint':              Key("escape, right, colon") + Text("GoLint")     + Key("enter"),
    'help info':              Key("escape, right, colon") + Text("GoInfo")     + Key("enter"),
    'help describe':          Key("escape, right, colon") + Text("GoDescribe") + Key("enter"),
    'help check':             Key("escape, right, colon") + Text("GoErrCheck") + Key("enter"),
    'help (collars|callers)': Key("escape, right, colon") + Text("GoCallers")  + Key("enter"),
    'help (collies|callees)': Key("escape, right, colon") + Text("GoCallees")  + Key("enter"),
    'help (vet|pet|bet)':     Key("escape, right, colon") + Text("GoVet")      + Key("enter"),
    'help play':              Key("colon") + Text("GoPlay")             + Key("enter"),
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


