# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with Git
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key
from aenea import Text
import dragonfly

git_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('git', context=git_context)

git_mapping = aenea.configuration.make_grammar_commands('git', {
    'git': Text("git"),
    'git ammend': Text("git commit --amend") + Key("enter"),
    'git commit': Text("git commit") + Key("enter"),
    'git trunk': Text("git co trunk-svn") + Key("enter"),
    'git pull': Text("git svn rebase") + Key("enter"),
    'git rebase': Text("git rebase trunk-svn") + Key("enter"),
    'git interactive rebase': Text("git rebase -i trunk-svn") + Key("enter"),
    'git branches': Text("git branch -l") + Key("enter"),
    'git checkout': Text("git co "),
    'git status': Text("git s") + Key("enter"),
    'git stat': Text("git show --stat") + Key("enter"),
    'git log': Text("git log") + Key("enter"),
    'git push': Text("git push") + Key("enter"),
})


class Mapping(dragonfly.MappingRule):
    mapping = git_mapping

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
