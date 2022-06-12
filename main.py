#############################################################
# File Name : main.py
#
# Scrolling App to demonstrate screen scrolling
#
# Created :   May 2022 
#############################################################

from kivymd.app import MDApp

from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.core.window import Window

from kivy.clock import Clock

from Misc_DrawStuff import DrawStuff


##############################################################
##############################################################

class ScrollViewApp(MDApp):

    def __init__(self, **kwargs):
        ##########################
        super(ScrollViewApp, self).__init__(**kwargs)
        ##########################
        self.Win_To_Draw = MDFloatLayout()
        self.Label1      = MDLabel()
        self.Draw_Lines1 = DrawStuff()
        ##########################
        self.Event_Timer = Clock.create_trigger(callback = self.Callback_Timer, \
                                                timeout = 2.0, \
                                                interval = False)
        return

    def build(self):
        ScrollViewApp.title = 'Label Example'
        #############################################
        self.Win_To_Draw.size = Window.size
        #############################################
        self.Draw_Lines1.Show_Instructions(self.Win_To_Draw)
        #############################################
        Screen_Width  = self.Win_To_Draw.width
        Screen_Height = self.Win_To_Draw.height
        Xc = int(Screen_Width * 0.5)
        Yc = int(Screen_Height * 0.5)
        Screen_Xo = Xc - int(Screen_Width * 0.5)
        Screen_Yo = Yc - int(Screen_Height * 0.5)
        Screen_Xf = Screen_Xo + Screen_Width
        Screen_Yf = Screen_Yo + Screen_Height
        #############################################
        Label_Width = int(self.Win_To_Draw.width / 2)
        Label_Height = int(self.Win_To_Draw.height / 30)
        #############################################
        self.Label1.font_style = 'Subtitle2'
        self.Label1.font_size  = 14
        self.Label1.size_hint  = (None, None)
        self.Label1.width      = Label_Width
        self.Label1.height     = Label_Height * 12
        self.Label1.text_size  = (self.Label1.width, None)
        self.Label1.x          = Xc - int(self.Label1.width * 0.5)
        self.Label1.y          = Yc - int(self.Label1.height * 0.5)
        self.Label1.halign     = 'center'
        self.Label1.valign     = 'bottom'
        self.Label1.color      = (0, 0, 0, 1)
        self.Label1.text  = '  Label Width = ' + str(self.Label1.width)
        self.Label1.text += '\n  Label Height = ' + str(self.Label1.height)
        self.Label1.text += '\n  text_size.x = ' + str(self.Label1.text_size[0])
        #self.Label1.text += '\n  text_size.y = ' + str(self.Label1.text_size[1])
        self.Label1.text += '\n  text_size.y = None'
        self.Label1.text += '\n  texture_size.x = ' + str(self.Label1.texture_size[0])
        self.Label1.text += '\n  texture_size.y = ' + str(self.Label1.texture_size[1])
        self.Label1.text += '\n  halighn = center'
        self.Label1.text += '\n  valighn = bottom'
        if(self.Label1.parent == None):
            self.Win_To_Draw.add_widget(self.Label1)
        #############################################
        self.Draw_Lines1.Draw_Rectangle(pXo = self.Label1.x, \
                                        pXf = self.Label1.x + self.Label1.width, \
                                        pYo = self.Label1.y, \
                                        pYf = self.Label1.y + self.Label1.height, \
                                        pR = 0, \
                                        pG = 0, \
                                        pB = 0, \
                                        pW = 1)
        #############################################
        self.Event_Timer()
        return self.Win_To_Draw
    
    
    #################################################
    def Callback_Timer(self, dt):
        width  = self.Label1.texture_size[0]
        height = self.Label1.texture_size[1]
        self.Label1.text += '\n  texture_size[0] = ' + str(width)
        self.Label1.text += '\n  texture_size[1] = ' + str(height)
        return


ScrollViewApp().run()

##############################################################
##############################################################