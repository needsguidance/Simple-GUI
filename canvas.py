from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout



class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            # d = 30.
            # Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


# class MyPaintApp(App):

    # def build(self):
    #     parent = Widget()
    #     self.painter = MyPaintWidget()
    #     clearbtn = Button(text='Clear')
    #     clearbtn.bind(on_release=self.clear_canvas)
    #     parent.add_widget(self.painter)
    #     parent.add_widget(clearbtn)
        
    #     return parent



class Arrows(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        App.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        # parent.add_widget(App.painter)
        # parent.add_widget(clearbtn)

        self.left_button = Button(text="Left", pos_hint= {'x': .35,'top': .3}, size_hint = (.1,.1))
        self.top_button = Button(text="Top", pos_hint= {'x': .45,'top': .4}, size_hint = (.1,.1))
        self.bottom_button = Button(text="Bottom", pos_hint= {'x': .45,'top': .2}, size_hint = (.1,.1))
        self.center_button = Button(text="Center", pos_hint= {'x': .45,'top': .3}, size_hint = (.1,.1), disabled = True)
        self.right_button = Button(text="Right", pos_hint= {'x': .55,'top': .3}, size_hint = (.1,.1))

        self.add_widget(App.painter)
        self.add_widget(self.left_button)
        self.add_widget(self.top_button)
        self.add_widget(self.bottom_button)
        self.add_widget(self.center_button)
        self.add_widget(self.right_button)

        self.left_button.bind(on_press=self.button_click)
        self.top_button.bind(on_press=self.button_click)
        self.bottom_button.bind(on_press=self.button_click)
        self.right_button.bind(on_press=self.button_click)
    
    def clear_canvas(self, obj):
        App.painter.canvas.clear()

        
    
    def button_click(self, event):
        self.center_button.text = event.text

