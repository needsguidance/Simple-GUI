from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Arrows(FloatLayout):

 def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button_event = None
        self.button_color = (0, 255, 255, .5)

        self.button_event = None
        parent = Widget()

        # Buttons instances
        self.left_button = Button(text="Left", pos_hint={'x': .35, 'top': .3}, size_hint=(.1, .1), id='left',
                                  background_color=self.button_color)
        self.top_button = Button(text="Top", pos_hint={'x': .45, 'top': .4}, size_hint=(.1, .1), id='top',
                                 background_color=self.button_color)
        self.bottom_button = Button(text="Bottom", pos_hint={'x': .45, 'top': .2}, size_hint=(.1, .1), id='bottom',
                                    background_color=self.button_color)
        self.label = Label(text="Center", pos_hint={'x': .45, 'top': .3}, size_hint=(.1, .1))
        self.right_button = Button(text="Right", pos_hint={'x': .55, 'top': .3}, size_hint=(.1, .1), id='right',
                                   background_color=self.button_color)
        self.inc_speed_button = Button(text="Fast", pos_hint={'x': .30, 'top': .5}, size_hint=(.1, .05), id='increase')
        self.dec_speed_button = Button(text="Slow", pos_hint={'x': .40, 'top': .5}, size_hint=(.1, .05), id='decrease')
        self.change_color_button = Button(text="Color", pos_hint={'x': .50, 'top': .5}, size_hint=(.1, .05), id='color')
        self.clear_button = Button(text="Clear", pos_hint={'x': .60, 'top': .5}, size_hint=(.1, .05), id='clear')

        self.add_widget(parent)
        self.add_widget(self.inc_speed_button)
        self.add_widget(self.dec_speed_button)
        self.add_widget(self.change_color_button)
        self.add_widget(self.clear_button)
        self.add_widget(self.left_button)
        self.add_widget(self.top_button)
        self.add_widget(self.bottom_button)
        self.add_widget(self.label)
        self.add_widget(self.right_button)

