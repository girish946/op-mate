#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import commands

host = '10.42.0.1'
port = 6789
backlog = 5
size = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(backlog)


available = ['power' ,'fileviewer' ,'show_desktop' ,\
              'alt_tab' ,'enter' ,'F5' ,'close' ,'cut' ,\
              'copy' ,'paste' ,'backspace' ,'pageup' ,\
              'pagedown' ,'left' ,'right' ,'up','down' ,\
              'escape', 'home' ,'end' ,'tab' ,'startup_menu',]


print "listening"
while 1:
    try:
        client, address = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print "received "+ data
                if data =='bye':
                    client.send(data)
                    raise
                if data in available:
                    print "data in available" + data
                    getattr(commands,data)()
                else:
                    print("invalid command")                
            client.send(data)
        client.close() 
    except:
        client.close()
        #s.shutdown(1)
        #s.close()
        #sys.exit(0)

#s.shutdown(2)
#s.close()
