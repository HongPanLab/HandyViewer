import os.path
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

ROOT_DIR = os.path.join(os.path.abspath(__file__), '../')

# factory producing different actions
def new_action(parent, text, icon_name=None, shortcut=None, slot=None, checkable=False):
    action = QAction(text, parent)
    if icon_name:
        action.setIcon(QIcon(os.path.join(ROOT_DIR, 'icons/{}.png'.format(icon_name))))
    if shortcut:
        action.setShortcut(shortcut)
    # trigger
    action.triggered.connect(slot)
    if checkable:
        action.setCheckable(True)
    return action

##################################
# MenuBar
##################################

def open(parent):
    # open an image. Also update image list.
    return new_action(parent, 'Open...', icon_name='open_w', shortcut='Ctrl+O', \
        slot=parent.open_file_dialog)


def open_tool(parent):
    # open an image. Also update image list.
    return new_action(parent, 'Open...', icon_name='open', shortcut='Ctrl+O', \
        slot=parent.open_file_dialog)


def new(parent):
    # open an image. Also update image list.
    return new_action(parent, 'New', icon_name='new_w', shortcut='Ctrl+N', \
        slot=print_slot)

def resize(parent):
    # open an image. Also update image list.
    return new_action(parent, 'Resize', icon_name='new_w', shortcut=None, \
        slot=print_slot)

def crop(parent):
    # open an image. Also update image list.
    return new_action(parent, 'Crop', icon_name='new_w', shortcut=None, \
        slot=print_slot)

def print_slot():
    print('slot')
