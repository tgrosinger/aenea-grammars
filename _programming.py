# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for writing in the various programming languages
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Function, Text
from aenea import Choice
import dragonfly

# Languages
import go_grammar
import python_grammar
import sql_grammar


vim_context = aenea.ProxyPlatformContext('linux')
generic_grammar = dragonfly.Grammar('generic', context=vim_context)

language_map = {
    "gopher": go_grammar.get_grammar(vim_context),
    "python": python_grammar.get_grammar(vim_context),
    "sql":    sql_grammar.get_grammar(vim_context),
}


def clear_mode():
    for _, grammar in language_map.iteritems():
        grammar.disable()


def switch_mode(language):
    clear_mode()
    language.enable()


basics_mapping = aenea.configuration.make_grammar_commands('python', {
    'var': Text("var "),
    'mode <language>': Function(switch_mode),
    'clear mode': Function(clear_mode),

    #  Common words
    'util': Text("util"),
    'query': Text("query"),
    '(Jason|json)': Text("json"),
    'upper (Jason|json)': Text("JSON"),
    'extrahop': Text("extrahop"),  # Company name
    'app': Text("app"),
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


class Basics(dragonfly.MappingRule):
    mapping = basics_mapping
    extras = [
        Choice("language", language_map)
    ]


class Operators(dragonfly.MappingRule):
    mapping = operators_mapping

generic_grammar.add_rule(Basics())
generic_grammar.add_rule(Operators())
generic_grammar.load()

# Start with no modes active
for _, grammar in language_map.iteritems():
    grammar.load()
    grammar.disable()


def unload():
    generic_grammar.unload()
    for _, grammar in language_map.iteritems():
        grammar.unload()
