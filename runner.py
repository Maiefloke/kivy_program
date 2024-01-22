from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation

from kivy.uix.boxlayout import BoxLayout


class Runner(BoxLayout):

    value = NumericProperty(0)
    finished = BooleanProperty(False)


    def __init__(self, total, steptime, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.btntext = "Присідання"
        self.animation = (Animation(pos_hint = {'top': 0.1}, duration = steptime/2) + Animation(pos_hint = {"top": 1.0}, duration = steptime/2))
        self.animation.repeat = True
        self.animation.on_progress = self.next
        self.btn = Button(size_hint = (1, 0.1), pos_hint = {"top": 1.0}, background_color = (.73, .15, .96, 1))
        self.add_widget(self.btn)

    def start(self):
        self.value = 0
        self.finished = False
        self.btn.text = self.btntext
        self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step):
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                self.finished = True
                self.animation.repeat = False