# Installation instructions

## Client installation instructions

These steps are meant to be performed on a Windows machine with an attached
microphone. I suggest using a virtual machine as it will allow you to save
snapshots as you progress through the steps.

The machine should have about 2GB of ram and two processors.

1. Install Dragon NaturallySpeaking 13.0 to default location
2. Take a snapshot of the VM
3. Download and install Python 2.7.8 for x32
4. Run [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to install pip
5. Install the latest release of pywin32 for Python 2.7
6. Install the latest release of NatLink
7. python -m pip install dragonfly
8. python -m pip install pyparsing
9. python -m pip install jsonrpclib
10. Take another snapshot of the VM
11. Start a cmd window as administrator
12. Navigate to C:\NatLink\NatLink\confignatlinkvocolaunimacro
13. Run start_natlinkconfigfunctions.py then use the e option to enable
14. If problems are encountered, take a look at [this Github](https://github.com/simianhacker/code-by-voice/issues/2) issue for help
15. Copy aenea/aenea.json.example to C:\NatLink\NatLink\MacroSystem and edit the ip to the ip of the host
16. Copy the dictation client from the client directory to the NatLink directory
17. Disable the dictation window in Dragon so you can use the dictation client

## Server installation instructions

These instructions were written for an machine running ubuntu 14.04 LTS.

17. Go to the server (linux machine) and navigate in the aenea dir to server/linux_x11
18. Copy config.py.example to config.py and edit, setting the ip to 0.0.0.0
19. Install pip on the host machine (sudo apt-get install python-pip)
20. Install xsel and xdotool (sudo apt-get install xsel xdotool)
21. Use pip to install jsonrpclib, and yapsy

## Starting everything.

1. On the server, start aenea/server/linux_x11/server_x11.py
2. On the client, start Dragon Naturally Speaking
3. On the client, start the aenea_client.py
4. Give the dictation window focus so it captures anything not covered by a grammar

## Microphone recommendations

I am using the Yeti by Blue and have found it to perform very well in quiet
environments, but it does have some trouble as the noise level increases or
others start speaking. The on-mic mute button is a very nice feature.

