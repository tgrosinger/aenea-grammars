# Using This Repository

Chances are you do not work in exactly the same way as I do. I use Vim (find my
[.vimrc here](https://github.com/tgrosinger/dotfiles/blob/master/.vimrc)) as my
primary editor, and generally program in either Go or Python. The commands and
grammars that are shared in this repository reflect that and are designed to
work in my workflow.

That said, the grammars found here should be a good starting point either as
examples or templates to help you write your own. It takes a while, but if they
are built up over time I have found they can be very powerful.

## Contributing

Want to help make getting started with voice coding easier? Send me a pull
request!

I would love to add more languages and more features. There are plenty
of commands that are missing, and even more that not work as well as they
could. Any help is welcome.

And of course if you have a friend who struggles with RSI or carpal tunnel
syndrome please tell them there is a better way.

### TO-DO List

Here are some tasks or know issues that need to be worked on:

* Add support for javascript language
* Improve editing. Currently creating new code is significantly easier 
  than refactoring old code. This means better support for selecting,
  copying, and editing words and lines.

# Grammar Configuration

Some of the grammars in this repository use a configuration file to increase
their flexibility. Rename the `grammar_config.json.sample` file to
`grammar_config.json` and use the guide below to make the required configuration
changes.

## Window Manager Options

*window-manager*

Choose from "cinnamon" or "i3" to specify what type of window manager to use.

*i3-mod-key*

If using the i3 window manager, use this option to specify the mod key. Options
are "alt", "win", and "ctrl".

*company-name*

If set, this word will be put in a grammar as-is, allowing Aenea to correctly
spell or write your company name.

*full-name*

If set, adds a command "my full name", which outputs the value specified.

*first-name*

If set, as a command "my first name", which outputs the value specified.

*last-name*

If set, adds a command "my last name", which outputs the value specified.

*email-address*

If set, adds a command "my email", which outputs the value specified.

# Installation instructions

These instructions will take you from a fresh installation of Windows and Ubuntu
to a working voice controlled setup. If you are just looking for the grammars
you can skip this section.

## Client

These steps are meant to be performed on a Windows machine with an attached
microphone. I suggest using a virtual machine as it will allow you to save
snapshots as you progress through the steps.

The machine should have about 2GB of ram and two processors.

1. Install [Dragon NaturallySpeaking 13.0](http://www.nuance.com/for-individuals/by-product/dragon-for-pc/index.htm) to default location
2. Take a snapshot of the VM
3. Download and install [Python 2.7.8 for x32](https://www.python.org/downloads/windows/)
4. Run [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to install pip
5. Install the latest release of [pywin32 for Python 2.7](http://sourceforge.net/projects/pywin32/)
6. Install the latest release of [NatLink](http://sourceforge.net/projects/natlink/)
7. Install other dependencies (`python -m pip install dragonfly jsonrpclib pyparsing`)
8. Take another snapshot of the VM
9. Start a cmd window as administrator
10. Navigate to `C:\NatLink\NatLink\confignatlinkvocolaunimacro`
11. Run `start_natlinkconfigfunctions.py` then use the `e` option to enable
12. If problems are encountered, take a look at [this Github](https://github.com/simianhacker/code-by-voice/issues/2) issue for help
13. Copy `aenea/aenea.json.example` to `C:\NatLink\NatLink\MacroSystem` and edit the ip to the ip of the host
14. Copy the dictation client from the client directory to the NatLink directory
15. Disable the dictation window in Dragon so you can use the dictation client

## Server

These instructions were written for an machine running ubuntu 14.04 LTS.

1. Go to the server (linux machine) and navigate in the aenea dir to `server/linux_x11`
2. Copy `config.py.example` to `config.py` and edit, setting the ip to 0.0.0.0
3. Install pip on the host machine (`sudo apt-get install python-pip`)
4. Install xsel and xdotool (`sudo apt-get install xsel xdotool`)
5. Use pip to install jsonrpclib, and yapsy (`sudo pip install jsonrpclib yapsy`)

## Starting everything.

1. On the server, start `aenea/server/linux_x11/server_x11.py`
2. On the client, start Dragon Naturally Speaking
3. On the client, start `aenea_client.py`
4. Give the dictation window focus so it captures anything not covered by a grammar

# Microphone recommendations

I previously used the [Yeti by Blue](http://www.amazon.com/gp/product/B002VA464S/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B002VA464S&linkCode=as2&tag=boomet03-20&linkId=Y7B7OAY6UIX6JRG5) and while it worked well in quiet environments, it slowed down greatly as the noise level increased. I am now using (and highly recommend) the [Sennheiser MD431-II](http://www.amazon.com/gp/product/B0015AAY64/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B0015AAY64&linkCode=as2&tag=boomet03-20&linkId=5SAGDVUHAUKJAJXG) with the [Focusrite Scarlett Solo](http://www.amazon.com/gp/product/B00MTXU2DG/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00MTXU2DG&linkCode=as2&tag=boomet03-20&linkId=R6JFV42AZQN6S3HC). It is certainly a price jump, but its performance is outstanding, even when others are talking very near me. Keep the gain low, and speak directly into the microphone.
