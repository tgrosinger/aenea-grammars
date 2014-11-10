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

    'git amend': Text("git commit --amend") + Key("enter"),
    'git commit': Text("git commit") + Key("enter"),
    'git pull': Text("git pull") + Key("enter"),
    'git branches': Text("git branch -l") + Key("enter"),
    'git status': Text("git status") + Key("enter"),
    'git stat': Text("git show --stat") + Key("enter"),
    'git log': Text("git log") + Key("enter"),
    'git push': Text("git push") + Key("enter"),

    # Incomplete Commands
    'git add': Text("git add "),
    'git checkout': Text("git checkout "),
    'git interactive rebase': Text("git rebase -i "),
    'git rebase': Text("git rebase "),

    # SVN Commands
    'git trunk': Text("git checkout trunk-svn") + Key("enter"),
    'git svn pull': Text("git svn rebase") + Key("enter"),
    'git svn rebase interactive': Text("git rebase -i trunk-svn") + Key("enter"),
    'git svn rebase': Text("git rebase trunk-svn") + Key("enter"),
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
