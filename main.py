from kivy.app import App
from kivy.uix.button import Button
from canvas import Arrows

class TestApp(App):
    def build(self):
        return Arrows()

TestApp().run()