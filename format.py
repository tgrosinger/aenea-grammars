# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

from aenea import Text

letterMap = {
    "A\\letter": "alpha",
    "B\\letter": "bravo",
    "C\\letter": "charlie",
    "D\\letter": "delta",
    "E\\letter": "echo",
    "F\\letter": "foxtrot",
    "G\\letter": "golf",
    "H\\letter": "hotel",
    "I\\letter": "india",
    "J\\letter": "juliet",
    "K\\letter": "kilo",
    "L\\letter": "lima",
    "M\\letter": "mike",
    "N\\letter": "november",
    "O\\letter": "oscar",
    "P\\letter": "papa",
    "Q\\letter": "quebec",
    "R\\letter": "romeo",
    "S\\letter": "sierra",
    "T\\letter": "tango",
    "U\\letter": "uniform",
    "V\\letter": "victor",
    "W\\letter": "whiskey",
    "X\\letter": "x-ray",
    "Y\\letter": "yankee",
    "Z\\letter": "zulu",
}


class FormatTypes:
    camelCase = 1
    pascalCase = 2
    snakeCase = 3
    squash = 4
    upperCase = 5
    lowerCase = 6
    dashify = 7
    dotify = 8
    spokenForm = 9
    sentenceCase = 10


def strip_dragon_info(text):
    newWords = []
    words = str(text).split(" ")
    for word in words:
        if word.startswith("\\backslash"):
            word = "\\"  # Backslash requires special handling.
        elif word.find("\\") > -1:
            word = word[:word.find("\\")]  # Remove spoken form info.
        newWords.append(word)
    return newWords


def extract_dragon_info(text):
    newWords = []
    words = str(text).split(" ")
    for word in words:
        if word in letterMap.keys():
            word = letterMap[word]
        elif word.rfind("\\") > -1:
            pos = word.rfind("\\") + 1
            if (len(word) - 1) >= pos:
                word = word[pos:]  # Remove written form info.
            else:
                word = ""
        newWords.append(word)
    return newWords


def format_camel_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText == '':
            newText = word[:1].lower() + word[1:]
        else:
            newText = '%s%s' % (newText, word.capitalize())
    return newText


def format_pascal_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        newText = '%s%s' % (newText, word.capitalize())
    return newText


def format_snake_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "_" + word  # Adds underscores between normal words.
        newText += word.lower()
    return newText


def format_dashify(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "-" + word  # Adds dashes between normal words.
        newText += word
    return newText


def format_dotify(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "." + word  # Adds dashes between normal words.
        newText += word
    return newText


def format_squash(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        newText = '%s%s' % (newText, word)
    return newText

def format_sentence_case(text):
    newText = []
    words = strip_dragon_info(text)
    for word in words:
        if newText == "":
            newText.append(word.title())
        else:
            newText.append(word.lower())
    return " ".join(newText)


def format_upper_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = " " + word  # Adds spacing between normal words.
        newText += word.upper()
    return newText


def format_lower_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            if newText[-1:] != "." and word[0:1] != ".":
                word = " " + word  # Adds spacing between normal words.
        newText += word.lower()
    return newText


def format_spoken_form(text):
    newText = ""
    words = extract_dragon_info(text)
    for word in words:
        if newText != "":
            word = " " + word
        newText += word
    return newText


FORMAT_TYPES_MAP = {
    FormatTypes.sentenceCase: format_sentence_case,
    FormatTypes.camelCase: format_camel_case,
    FormatTypes.pascalCase: format_pascal_case,
    FormatTypes.snakeCase: format_snake_case,
    FormatTypes.squash: format_squash,
    FormatTypes.upperCase: format_upper_case,
    FormatTypes.lowerCase: format_lower_case,
    FormatTypes.dashify: format_dashify,
    FormatTypes.dotify: format_dotify,
    FormatTypes.spokenForm: format_spoken_form,
}


def format_text(text, formatType=None):
    if formatType:
        if type(formatType) != type([]):
            formatType = [formatType]
        result = ""
        method = None
        for value in formatType:
            if not result:
                if formatType == FormatTypes.spokenForm:
                    result = text.words
                else:
                    result = str(text)
            method = FORMAT_TYPES_MAP[value]
            result = method(result)
        Text("%(text)s").execute({"text": result})


def camel_case_text(text):
    """Formats dictated text to camel case.

    Example:
    "'camel case my new variable'" => "myNewVariable".

    """
    newText = format_camel_case(text)
    Text("%(text)s").execute({"text": newText})


def pascal_case_text(text):
    """Formats dictated text to pascal case.

    Example:
    "'pascal case my new variable'" => "MyNewVariable".

    """
    newText = format_pascal_case(text)
    Text("%(text)s").execute({"text": newText})


def snake_case_text(text):
    """Formats dictated text to snake case.

    Example:
    "'snake case my new variable'" => "my_new_variable".

    """
    newText = format_snake_case(text)
    Text("%(text)s").execute({"text": newText})


def squash_text(text):
    """Formats dictated text with whitespace removed.

    Example:
    "'squash my new variable'" => "mynewvariable".

    """
    newText = format_squash(text)
    Text("%(text)s").execute({"text": newText})


def uppercase_text(text):
    """Formats dictated text to upper case.

    Example:
    "'upper case my new variable'" => "MY NEW VARIABLE".

    """
    newText = format_upper_case(text)
    Text("%(text)s").execute({"text": newText})


def lowercase_text(text):
    """Formats dictated text to lower case.

    Example:
    "'lower case John Johnson'" => "john johnson".

    """
    newText = format_lower_case(text)
    Text("%(text)s").execute({"text": newText})
