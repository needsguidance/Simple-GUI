from functools import partial
from random import random

from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

global X, Y, color
color = (1, 1, 1)  # Red Color
# Initial coords.
Y = 400
X = 400


class Canvas(Widget):

    def boundary(self):
        self.canvas.add(Color(1, 5, 3))
        self.canvas.add(Rectangle(pos=(100, 0), size=(600, 600)))
        self.canvas.add(Color(1., 1., 0))
        self.canvas.add(Rectangle(pos=(200, 300), size=(400, 200)))


    def paint(self, event, w, h):
        token = event.id
        # color = (1, 1, 1)  # Red Color
        global X, Y


        # Increase/Decrease of coordinates dependant on token value passed on button press

        if token == 'left':
            X -= 2
        elif token == 'right':
            X += 2
        elif token == 'top':
            Y += 2
        elif token == 'bottom':
            Y -= 2

        with self.canvas:

            # Temporary Boundaries Example
            print(w,h)
            if X > w - w/4:
                X = w - w/4
                print("right")
            elif Y > h - h/8:
                Y = h - h/8
                print("up")
            elif X < w/4:
                X = w/4
                print("left")
            elif Y < h/1.95:
                Y = h/1.95
                print("down")
            Color(*color, mode='hsv')
            d = 5.  # diameter of ellipse

            # Draws mini circles to make a Line (Line command cant be used for one coord pixels/position)
            Ellipse(pos=(X - d / 2, Y - d / 2), size=(d, d))


class Arrows(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.width,self.height)
        self.button_event = None
        parent = Widget()
        self.painter = Canvas()
        parent.add_widget(self.painter)
        self.painter.boundary()

        button_color = (0, 255, 255, .5)
        self.left_button = Button(text="Left", pos_hint={'x': .35, 'top': .3}, size_hint=(.1, .1), id='left',
                                  background_color=button_color)
        self.top_button = Button(text="Top", pos_hint={'x': .45, 'top': .4}, size_hint=(.1, .1), id='top',
                                 background_color=button_color)
        self.bottom_button = Button(text="Bottom", pos_hint={'x': .45, 'top': .2}, size_hint=(.1, .1), id='bottom',
                                    background_color=button_color)
        self.label = Label(text="Center", pos_hint={'x': .45, 'top': .3}, size_hint=(.1, .1))
        self.right_button = Button(text="Right", pos_hint={'x': .55, 'top': .3}, size_hint=(.1, .1), id='right',
                                   background_color=button_color)
        self.speed_button = Button(text="Speed", pos_hint={'x': .35, 'top': .5}, size_hint=(.1, .05), id='speed')
        self.change_color_button = Button(text="Color", pos_hint={'x': .45, 'top': .5}, size_hint=(.1, .05), id='color')
        self.clear_button = Button(text="Clear", pos_hint={'x': .55, 'top': .5}, size_hint=(.1, .05), id='clear')

        self.add_widget(parent)
        self.add_widget(self.speed_button)
        self.add_widget(self.change_color_button)
        self.add_widget(self.clear_button)
        self.add_widget(self.left_button)
        self.add_widget(self.top_button)
        self.add_widget(self.bottom_button)
        self.add_widget(self.label)
        self.add_widget(self.right_button)

        # TODO: Add function for change color button
        self.change_color_button.bind(on_press=self.change_arrow_color)
        # TODO: Add function for change speed button
        # self.speed_button.bind(on_press=self.change_arrow_speed)
        self.clear_button.bind(on_release=self.clear_canvas)
        self.left_button.bind(on_press=self._on_press, on_release=self._on_release)
        self.top_button.bind(on_press=self._on_press, on_release=self._on_release)
        self.bottom_button.bind(on_press=self._on_press, on_release=self._on_release)
        self.right_button.bind(on_press=self._on_press, on_release=self._on_release)


    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        # self.painter.boundary(self.width, self.height)
        global X, Y
        self.label.text = 'Center'
        X = self.width/2
        Y = self.height/1.5


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

        self.painter.paint(event, self.width, self.height)

    def change_arrow_color(self, event):
        """
        Change arrow color on button event
        :param event: button event
        """
        global color
        color = (random(), 1, 1)
