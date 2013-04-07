#!/usr/bin/python -o
"""
    NAME
        party_print.py -- Printing Support for Python

    AUTHOR
        Samuel Messing <sbm2158@columbia.edu>
"""
__author__ = 'Samuel Messing <sbm2158@columbia.edu>'

import inspect
import sys

# TODOS
# - print thread ids when multithreaded
# - logging levels?
# - animations
# - auto-detect tty to turn on/off printing escape characters

# Set for verbose printing.
DEBUG = False

# Set to disable sending escape sequences (for piping std.out)
NO_ESCAPE = False

# Colors used by print methods below.
NC = "\033[0m"
WHITE = "\033[1;37m"
BLACK = "\033[0;30m"
BLUE = "\033[0;34m"
LIGHT_BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
LIGHT_GREEN = "\033[1;32m"
CYAN = "\033[0;36m"
LIGHT_CYAN = "\033[1;36m"
RED = "\033[0;31m"
LIGHT_RED = "\033[1;31m"
PURPLE = "\033[0;35m"
LIGHT_PURPLE = "\033[1;35m"
BROWN = "\033[0;33m"
YELLOW = "\033[1;33m"
GRAY = "\033[1;30m"


def set_no_escape():
    self = sys.modules[__name__]
    self.NO_ESCAPE = True


def unset_no_escape():
    self = sys.modules[__name__]
    self.NO_ESCAPE = False


def set_debug():
    self = sys.modules[__name__]
    self.DEBUG = True


def unset_debug():
    self = sys.modules[__name__]
    self.DEBUG = False


def white(text):
    return color(WHITE, text)


def black(text):
    return color(BLACK, text)


def blue(text):
    return color(BLUE, text)


def light_blue(text):
    return color(LIGHT_BLUE, text)


def green(text):
    return color(GREEN, text)


def light_green(text):
    return color(LIGHT_GREEN, text)


def cyan(text):
    return color(CYAN, text)


def light_cyan(text):
    return color(LIGHT_CYAN, text)


def red(text):
    return color(RED, text)


def light_red(text):
    return color(LIGHT_RED, text)


def purple(text):
    return color(PURPLE, text)


def light_purple(text):
    return color(LIGHT_PURPLE, text)


def brown(text):
    return color(BROWN, text)


def yellow(text):
    return color(YELLOW, text)


def gray(text):
    return color(GRAY, text)


def color(color, text):
    return text if NO_ESCAPE else color + text + NC


# Width for printing numbers.
NUMBER_PRINT_WIDTH = 7


def format_number(number):
    return light_cyan(repr(number).rjust(NUMBER_PRINT_WIDTH))

# Colors used in formatted printing.
MODULE_COLOR = BLUE
LINE_COLOR = YELLOW
FN_COLOR = GREEN


def print_message(msg, debug_only=True, call_level=1, error=False):
    """Print a message to stdout."""
    def strip_line(line):
        return line.rstrip('___').lstrip('___')

    if (DEBUG):
        # Grab the callee function's name and prepend to the outgoing message.
        callee_stack_frame = inspect.stack()[call_level]
        callee_module = inspect.getmodule(callee_stack_frame[0])
        if callee_module is not None:
          callee_module_name = strip_line(callee_module.__name__)
        else:
          callee_module_name = ''
        callee_src_line = '(' + \
            color(LINE_COLOR, repr(callee_stack_frame[2]).rjust(4)) + \
            ')'
        callee_fn_name = strip_line(callee_stack_frame[3].upper())
        error_string = ''
        if (error):
            error_string = color(ERROR_COLOR, 'ERR! ')
        print error_string + color(MODULE_COLOR, callee_module_name) + ' ' + \
            callee_src_line, color(FN_COLOR, callee_fn_name) + ' ' + msg
    elif not debug_only:
        print msg


# Colors used in printing errors.
ERROR_COLOR = RED


def print_error(msg):
    """Print an error message."""
    msg = 'ERR! ' + msg
    msg = color(ERROR_COLOR, msg)
    print_message(msg, debug_only=False, call_level=2, error=True)
