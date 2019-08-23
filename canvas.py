from functools import partial

from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

global X, Y
# Initial coords.
X = 400
Y = 400


class Canvas(Widget):

    def paint(self, event):
        token = event.id
        color = (1, 1, 1)  # Red Color
        global X, Y

        # Increase/Decrease of coordinates dependant on token value passed on button press

        if token == 'left':
            X -= 2
        if token == 'right':
            X += 2
        if token == 'top':
            Y += 2
        if token == 'bottom':
            Y -= 2

        with self.canvas:

            # Temporary Boundaries Example
            if X > 500:
                X = 600
            if Y > 500:
                Y = 600

            Color(*color, mode='hsv')
            d = 5.  # diameter of ellipse

            # Draws mini circles to make a Line (Line command cant be used for one coord pixels/position)
            Ellipse(pos=(X - d / 2, Y - d / 2), size=(d, d))


class Arrows(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button_event = None

        parent = Widget()
        self.painter = Canvas()
        parent.add_widget(self.painter)
        button_color = (0, 255, 255, .5)
        self.left_button = Button(text="Left", pos_hint={'x': .35, 'top': .3}, size_hint=(.1, .1), id='left', background_color=button_color)
        self.top_button = Button(text="Top", pos_hint={'x': .45, 'top': .4}, size_hint=(.1, .1), id='top', background_color=button_color)
        self.bottom_button = Button(text="Bottom", pos_hint={'x': .45, 'top': .2}, size_hint=(.1, .1), id='bottom', background_color=button_color)
        self.label = Label(text="Center", pos_hint={'x': .45, 'top': .3}, size_hint=(.1, .1))
        self.right_button = Button(text="Right", pos_hint={'x': .55, 'top': .3}, size_hint=(.1, .1), id='right', background_color=button_color)
        self.clear_button = Button(text="Clear", pos_hint={'x': .9, 'top': .3}, size_hint=(.05, .05), id='clear')

        self.add_widget(parent)
        self.add_widget(self.clear_button)
        self.add_widget(self.left_button)
        self.add_widget(self.top_button)
        self.add_widget(self.bottom_button)
        self.add_widget(self.label)
        self.add_widget(self.right_button)

        self.clear_button.bind(on_release=self.clear_canvas)
        self.left_button.bind(on_press=self._on_press, on_release=self._on_release)
        self.top_button.bind(on_press=self._on_press, on_release=self._on_release)
        self.bottom_button.bind(on_press=self._on_press, on_release=self._on_release)
        self.right_button.bind(on_press=self._on_press, on_release=self._on_release)

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        global X, Y
        X = 400
        Y = 400
        self.center_button.text = 'Center'

    def _on_press(self, event):
        """
        On button press a job is scheduled to paint the canvas, then the center button text is changed
        :param event: button event
        """
        self.button_event = Clock.schedule_interval(partial(self.paint_canvas, event), 0.05)
        self.label.text = event.text

    def _on_release(self, event):
        """
        On button release scheduled paint job is cancelled
        :param event: button event
        """
        Clock.unschedule(self.button_event)

    def on_touch_up(self, touch):
        """
        Used in conjunction with Button on_release functionality
        :param touch: event
        """
        Clock.unschedule(self.button_event)

    def paint_canvas(self, event, dt):
        """
        Paints canvas in the direction of the button event (i.e. Top, Bottom, Left or Right)
        :param event: button event
        :param dt: delta-time
        """
        self.painter.paint(event)
