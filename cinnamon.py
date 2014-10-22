# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with terminal and desktop environment
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import IntegerRef, Dictation
import dragonfly
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

app_map = {
    "(chrome|browser|internet)": "chrome",
    "(term|terminal)": "terminal",
    "fire fox": "firefox",
    "g edit": "gedit",
}


def switch_app(appname):
    aenea.communications.server.switch_app(appname, 1)


def switch_app_numbered(appname, appnum):
    aenea.communications.server.switch_app(appname, appnum)


def switch_app_title(text):
    aenea.communications.server.switch_app(text, 1)

cinnamon_mapping = aenea.configuration.make_grammar_commands('cinnamon', {
    'works one': Key("ca-1"),
    'works two': Key("ca-2"),
    'works left': Key("ca-left"),
    'works right': Key("ca-right"),
    'lock screen': Key("ca-l"),

    # Switching applications
    'switch (application|app)': Key("a-tab"),
    '(focus|folk) <appname>': Function(switch_app),
    '(focus|folk) <appname> <appnum>': Function(switch_app_numbered),
    '(focus|folk) title <text>': Function(switch_app_title),
})


class Mapping(dragonfly.MappingRule):
    mapping = cinnamon_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
        dragonfly.Choice('appname', app_map),
        dragonfly.IntegerRef('appnum', 1, 99),
    ]


def get_grammar(context, config):
    cinnamon_grammar = dragonfly.Grammar('cinnamon', context=context)
    cinnamon_grammar.add_rule(Mapping())
    return cinnamon_grammar
