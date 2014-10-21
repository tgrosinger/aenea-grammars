# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for writing SQL queries
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea import Choice
from aenea.lax import Text
import dragonfly


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


sql_mapping = aenea.configuration.make_grammar_commands('sql', {
    '<sqlKeyword>': Text("%(text)s"),
})


class SQL(dragonfly.MappingRule):
    mapping = sql_mapping
    extras = [
        Choice('sqlKeyword', sql_map,)
    ]

def get_grammar(context):
    sql_grammar = dragonfly.Grammar('sql', context=context)
    sql_grammar.add_rule(SQL())
    return sql_grammar
