from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Arrows(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.left_button = Button(text="Left", pos_hint= {'x': .35,'top': .3}, size_hint = (.1,.1))
        self.top_button = Button(text="Top", pos_hint= {'x': .45,'top': .4}, size_hint = (.1,.1))
        self.bottom_button = Button(text="Bottom", pos_hint= {'x': .45,'top': .2}, size_hint = (.1,.1))
        self.center_button = Button(text="Center", pos_hint= {'x': .45,'top': .3}, size_hint = (.1,.1), disabled = True)
        self.right_button = Button(text="Right", pos_hint= {'x': .55,'top': .3}, size_hint = (.1,.1))

        self.add_widget(self.left_button)
        self.add_widget(self.top_button)
        self.add_widget(self.bottom_button)
        self.add_widget(self.center_button)
        self.add_widget(self.right_button)

        self.left_button.bind(on_press=self.button_click)
        self.top_button.bind(on_press=self.button_click)
        self.bottom_button.bind(on_press=self.button_click)
        self.right_button.bind(on_press=self.button_click)

    
    def button_click(self, event):
        self.center_button.text = event.text
