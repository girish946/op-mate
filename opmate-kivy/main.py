from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import socket
import sys

#host = '127.0.0.1'
host='10.42.0.1'
#host='192.168.2.5'
port = 6789
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

current_command= "-1"

class RootWidget(FloatLayout):
    '''This the class representing your root widget.
       By default it is inherited from FloatLayout,
       you can use any other layout/widget depending on your usage.
    '''
    """def __init__(self):
        print "init"""
    def setCommand(self,cmd):
        print cmd
        try:
            s.send(cmd)
            data = s.recv(size)
            #s.shutdown(2)
            #s.close()
            #sys.exit(0)
        except:
            print "exception"

class MainApp(App):
    '''This is the main class of your app.
       Define any app wide entities here.
       This class can be accessed anywhere inside the kivy app as,
       in python::

         app = App.get_running_app()
         print (app.title)

       in kv language::

         on_release: print(app.title)
       Name of the .kv file that is auto-loaded is derived from the name
       of this class::

         MainApp = main.kv
         MainClass = mainclass.kv

       The App part is auto removed and the whole name is lowercased.
    '''

    def build(self):
        '''Your app will be build from here.
           Return your root widget here.
        '''
        print('build running')
        return RootWidget()

    def on_pause(self):
        '''This is necessary to allow your app to be paused on mobile os.
           refer http://kivy.org/docs/api-kivy.app.html#pause-mode .
        '''
        return True

if __name__ == '__main__':
    MainApp().run()
    s.send('bye')
    data = s.recv(size)
    print 'Received:', data 
    if data == 'bye':
        s.shutdown(2)
        s.close()
        sys.exit(0)

