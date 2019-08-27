from kivy.app import App
from canvas3 import Arrows


class TestApp(App):
    def build(self):
        return Arrows()


TestApp().run()
