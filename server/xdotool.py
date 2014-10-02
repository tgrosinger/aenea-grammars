from yapsy.IPlugin import IPlugin
import subprocess
import os

enabled = True


def switch_app(appname, appnum=1):
    '''An RPC command to change the currently focused window by name
    within the focused desktop'''

    command = "xdotool windowactivate --sync $(xdotool search --desktop $(xdotool get_desktop) \"%s\" | head -%s)" % (appname, appnum)
    os.system(command)


class WindowPlugin(IPlugin):
    def register_rpcs(self, server):
        server.register_function(switch_app)
