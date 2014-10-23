# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for inserting personal details loaded from the config file
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Function, Text
from aenea import Choice
import dragonfly
from config import get_configuration

vim_context = aenea.ProxyPlatformContext('linux')
generic_grammar = dragonfly.Grammar('generic', context=vim_context)
config = get_configuration()

commands = {}
if "full-name" in config:
    commands['my full name'] = Text("%s" % config["full-name"])
if "last-name" in config:
    commands['my last name'] = Text("%s" % config["last-name"])
if "first-name" in config:
    commands['my first name'] = Text("%s" % config["first-name"])
if "email-address" in config:
    commands['my email'] = Text("%s" % config["email-address"])
if "company-name" in config:
    commands['company name'] = Text("%s" % config["company-name"])


class Mapping(dragonfly.MappingRule):
    mapping = aenea.configuration.make_grammar_commands('personal', commands)
    extras = []

generic_grammar.add_rule(Mapping())
generic_grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
