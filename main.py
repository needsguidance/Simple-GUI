from kivy.app import App
from canvas import Arrows


class TestApp(App):
    def build(self):
        return Arrows()


TestApp().run()
