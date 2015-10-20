#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui as p
from threading import Thread
import clipboard
import os


def showShutdown():
    print "shutdown pressed"
    if os.environ['XDG_CURRENT_DESKTOP'] == 'Unity':
        os.system('gnome-session-quit --reboot')
    elif os.environ['XDG_CURRENT_DESKTOP'].lower() == 'mate':
        os.system('mate-session-save --shutdown-dialog')


def notify(message):
    """
    this method shows the notification.
    """
    os.system('notify-send "SG-remote" "{0}" \
           -t 2000 -i ~/.slightgen/logo.png'.format(message))


def run(program, *arg):
    pid = os.fork()
    if not pid:
        print type(arg)
        os.execvp(program, (program, )+arg)
    return os.wait()[0]


def power():
    """
    this method minimizes all the windows and shows the shutdown
    dialog box.
    """
    notify('pressed power')
    show_desktop()
    t = Thread(target=showShutdown)
    t.start()


def fileviewer():
    """
    this method starts a new instance of the file manager at
    at location /media/ .
    .. note
        
        here in this case the default filemanager is caja.
        so this will start caja at /media/
    """
    notify('opening fileviewer at /media/')
    program = 'xdg-open'
    arg = '/media/'
    run(program, arg)


def show_desktop():
    """
    this method minimizes all the opened windows and will show
    the desktop.
    """
    if os.environ['XDG_CURRENT_DESKTOP'] == 'Unity':
        p.keyDown('winleft')
        p.keyDown('d')
        p.keyUp('d')
        p.keyUp('winleft')
    elif os.environ['XDG_CURRENT_DESKTOP'].lower() == 'mate':
        p.keyDown('alt')
        p.keyDown('ctrl')
        p.keyDown('d')
        p.keyUp('d')
        p.keyUp('ctrl')
        p.keyUp('alt')


def alt_tab():
    """
    this method takes the control to the previously
    opened window.
    """
    if os.environ['XDG_CURRENT_DESKTOP'] == 'Unity':
        p.keyDown('alt')
        p.keyDown('\t')
        p.keyUp('\t')
        p.keyUp('alt')
    elif os.environ['XDG_CURRENT_DESKTOP'].lower() == 'mate':
        p.keyDown('alt')
        p.keyDown('shift')
        p.keyDown('\t')
        p.keyUp('\t')
        p.keyUp('shift')
        p.keyUp('alt')


def close():
    """
    this method presses alt+f4 of the virtual key board.
    """
    p.keyDown('alt')
    p.keyDown('f4')
    p.keyUp('f4')
    p.keyUp('alt')


def cut():
    """
    this method presses ctrl+x of the virtual key board.
    """
    p.keyDown('ctrl')
    p.keyDown('x')
    p.keyUp('x')
    p.keyUp('ctrl')
    notify('cut ' + clipboard.paste())


def copy():
    """
    this method presses ctrl+c of the virtual key board.
    """
    p.keyDown('ctrl')
    p.keyDown('c')
    p.keyUp('c')
    p.keyUp('ctrl')
    notify('copy ' + clipboard.paste())


def paste():
    """
    this method presses ctrl+v of the virtual key board.
    """
    p.keyDown('ctrl')
    p.keyDown('v')
    p.keyUp('v')
    p.keyUp('ctrl')
    notify('paste ' + clipboard.paste())


def startup_menu():
    """
    this method shows the startup menu....
    """
    p.keyDown('alt')
    p.keyDown('f1')
    p.keyUp('f1')
    p.keyUp('alt')


def enter():
    p.press('\n')


def F5():
    notify('F5 pressed')
    p.press('f5')


def backspace():
    p.press('\b')


def pageup():
    p.press('pageup')


def pagedown():
    p.press('pagedown')


def left():
    p.press('left')


def right():
    p.press('right')


def up():
    p.press('up')


def down():
    p.press('down')


def home():
    p.press('home')


def end():
    p.press('end')


def tab():
    p.press('\t')


def escape():
    notify('escape pressed')
    p.press('escape')
