# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with Docker
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key
from aenea import Text
import dragonfly

docker_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('docker', context=docker_context)

docker_mapping = aenea.configuration.make_grammar_commands('docker', {
    '(docker|darker|doctor)': Text("sudo docker "),
    '(docker|darker|doctor) build': Text("sudo docker build .") + Key("enter"),
    '(docker|darker|doctor) build (tag|tagged)': Text("sudo docker build -t \"\" .") + Key("left:3"),
    '(docker|darker|doctor) list images': Text("sudo docker images") + Key("enter"),
    '(docker|darker|doctor) list containers': Text("sudo docker ps -a") + Key("enter"),
    '(docker|darker|doctor) stop': Text("sudo docker stop "),
    '(docker|darker|doctor) (remove|delete) image': Text("sudo docker rmi "),
    '(docker|darker|doctor) (remove|delete) [container]': Text("sudo docker rm "),
    '(docker|darker|doctor) run': Text("sudo docker run -d "),
    '(docker|darker|doctor) inspect': Text("sudo docker inspect "),
    '(docker|darker|doctor) enter': Text("sudo ~/bin/docker-enter "),
})


class Mapping(dragonfly.MappingRule):
    mapping = docker_mapping

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
