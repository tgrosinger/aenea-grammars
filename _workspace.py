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
from aenea.lax import Key, Text, Function
from aenea import IntegerRef, Dictation
import dragonfly
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

window_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('windows', context=window_context)

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

window_mapping = aenea.configuration.make_grammar_commands('windows', {
    'works one': Key("ca-1"),
    'works two': Key("ca-2"),
    'works left': Key("ca-left"),
    'works right': Key("ca-right"),
    '(terminal|term) left': Key("c-pgup"),
    '(terminal|term) right': Key("c-pgdown"),
    '(terminal|term) new [tab]': Key("cs-t"),
    '(terminal|term) new window': Key("cs-n"),
    'lock screen': Key("ca-l"),

    # Switching applications
    'switch (application|app)': Key("a-tab"),
    '(focus|folk) <appname>': Function(switch_app),
    '(focus|folk) <appname> <appnum>': Function(switch_app_numbered),
    '(focus|folk) title <text>': Function(switch_app_title),

    # Terminal commands
    # dir is hard to say and recognize. Use something else
    'deer up': Text("cd ..") + Key("enter"),
    'deer list': Text("ls") + Key("enter"),
    'deer list all': Text("ls -lha") + Key("enter"),
    'deer list details': Text("ls -lh") + Key("enter"),
    'deer into': Text("cd "),
    '(terminal|term) clear': Text("clear") + Key("enter"),

    # Common words
    '(pseudo|sudo|pseudo-)': Text("sudo "),
    '(apt|app) get': Text("sudo apt-get "),
    '(apt|app) get install': Text("sudo apt-get install "),
    'Tony Grosinger': Text("Tony Grosinger"),
    'Grosinger': Text("Grosinger"),
    'email grosinger': Text("@grosinger.net"),
})


class Mapping(dragonfly.MappingRule):
    mapping = window_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
        dragonfly.Choice('appname', app_map),
        dragonfly.IntegerRef('appnum', 1, 99),
    ]

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
