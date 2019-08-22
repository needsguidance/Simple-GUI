from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout
from functools import partial
global X, Y
#Initial coords.
X = 400
Y = 400

class Canvas(Widget):

    def paint(self, token, event):
        color = (1, 1, 1)  #Red Color
        global X, Y

        #Increase/Decrease of coordinates dependant on token value passed on button press

        if(token == 0):
            X -= 2
        if(token == 1):
            X += 2
        if(token == 2):
            Y += 2
        if(token == 3):
            Y -= 2

        with self.canvas:
          
          #Temporary Boundaries Example
            if(X>500):
                X = 600
            if(Y>500):
                Y = 600

            Color(*color, mode='hsv')
            d = 5.  #diameter of ellipse
            Ellipse(pos=(X - d / 2, Y - d / 2), size=(d, d))  #Draws mini circles to make a Line (Line command cant be used for one coord pixels/position)


class Arrows(FloatLayout):
  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        parent = Widget()
        self.painter = Canvas()
        parent.add_widget(self.painter)
        #------Christian's arrows implementation-----------
        self.left_button = Button(text="Left", pos_hint= {'x': .35,'top': .3}, size_hint = (.1,.1))
        self.top_button = Button(text="Top", pos_hint= {'x': .45,'top': .4}, size_hint = (.1,.1))
        self.bottom_button = Button(text="Bottom", pos_hint= {'x': .45,'top': .2}, size_hint = (.1,.1))
        self.center_button = Button(text="Center", pos_hint= {'x': .45,'top': .3}, size_hint = (.1,.1), disabled = True)
        self.right_button = Button(text="Right", pos_hint= {'x': .55,'top': .3}, size_hint = (.1,.1))
        self.clear_button = Button(text="Clear", pos_hint= {'x': .9,'top': .3}, size_hint = (.05,.05))

        self.add_widget(parent)
        self.add_widget(self.clear_button)
        self.add_widget(self.left_button)
        self.add_widget(self.top_button)
        self.add_widget(self.bottom_button)
        self.add_widget(self.center_button)
        self.add_widget(self.right_button)

        self.clear_button.bind(on_release=self.clear_canvas)
        self.left_button.bind(on_press=self.button_click)
        self.top_button.bind(on_press=self.button_click)
        self.bottom_button.bind(on_press=self.button_click)
        self.right_button.bind(on_press=self.button_click)

        #Uses partial to create an event for the button bind and to pass token value to the Canvas class depending on button press
        callback0 = partial(self.painter.paint, 0)
        callback1 = partial(self.painter.paint, 1)
        callback2 = partial(self.painter.paint, 2)
        callback3 = partial(self.painter.paint, 3)

        self.left_button.bind(on_press=callback0)
        self.right_button.bind(on_press=callback1)
        self.top_button.bind(on_press=callback2)
        self.bottom_button.bind(on_press=callback3)

    
    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        global X,Y 
        X = 400
        Y = 400
    
    def button_click(self, event):
        self.center_button.text = event.text

