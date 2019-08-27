
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

class Arrows(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        parent = Widget()
        self.add_widget(parent)
