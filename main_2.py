from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from kivy.utils import get_color_from_hex
from ruffier import test
from second import Seconds
from sits import Sits
from runner import Runner

Window.clearcolor = get_color_from_hex("#0000FF")
age = 7
name = ""
p1, p2, p3 = 0, 0, 0
leters = "qwertyuioplkjhgfdsazxcvbnmйцукенгшщзхїфівапролджєячсмитьбю "



def check_int(str_num):
    try:
        return int(str_num)
    except:
        return -1


class bk_image(Image):
    def build(self):
        layout = BoxLayout()

        background_image = Image(source='heart.jpg')

        layout.background = background_image.texture

        return layout




class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text="Введіть ім'я:", halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Введіть вік:", halign='right')
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text="Почати",
                          size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global name, age
        name = self.in_name.text
        if len(name) == 0:
            self.in_name.background_color = '#FF0000'
            return
        for sym in name:
            if sym.lower() not in leters:
                self.in_name.background_color = "#FF0000"
                return

        age = check_int(self.in_age.text)
        if age < 7:
            age = 7
            self.in_age.background_color = '#FF0000'
            self.in_age.text = '7'
            return
        self.manager.current = 'pulse1'


class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text=txt_test1)

        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Введіть результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)

        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        self.btn = Button(text='Почати',
                          size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})

        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)

        outer.add_widget(instr)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def sec_finished(self, *args):
        self.btn.set_disabled(False)
        self.in_result.set_disabled(False)
        self.btn.text = "Продовжити"
        self.next_screen = True

    def next(self):
        global p1
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            p1 = int(self.in_result.text)
            self.manager.current = 'sits'
        if p1 > 0:
            self.in_result.background_color = '#FF0000'
            return




class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text=txt_sits)

        self.lbl_sits = Sits(30)
        self.run = Runner(30, 1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.run_finished)

        line = BoxLayout()
        vlay = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        vlay.add_widget(self.lbl_sits)
        line.add_widget(instr)
        line.add_widget(vlay)
        line.add_widget(self.run)

        self.btn = Button(text="Почати",
                          size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})

        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def run_finished(self, *args):
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 1

        instr = Label(text=txt_test3)
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        lbl1 = Label(text="Результат:", halign='right')
        lbl2 = Label(text="Результат після відпочинку:", halign='right')

        self.in_result1 = TextInput(text='0', multiline=False)
        self.in_result2 = TextInput(text='0', multiline=False)
        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')

        self.btn = Button(text="Почати",
                          size_hint=(0.3, 0.2),
                          pos_hint={"center_x": 0.5})

        self.btn.on_press = self.next

        line1.add_widget(lbl1)
        line1.add_widget(self.in_result1)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_result2)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 1:
                self.btn.text = "Відпочивайте"
                self.stage = 2
                self.in_result1.set_disabled(False)
                self.lbl_sec.restart(30)
            elif self.stage == 2:
                self.btn.text = "Міряйте пульс"
                self.stage = 3
                self.lbl_sec.restart(15)
            elif self.stage == 3:
                self.btn.set_disabled(False)
                self.btn.text = "Завершити"
                self.in_result2.set_disabled(False)
                self.next_screen = True

    def next(self):
        global p2, p3
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.btn.text = "Міряйте пульс"
            self.lbl_sec.start()
        else:
            p2 = int(self.in_result1.text)
            p3 = int(self.in_result2.text)
            self.manager.current = 'result'


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text='')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)

        self.on_enter = self.before

    def before(self):
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


class HeartCheck(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm


app = HeartCheck()
app.run() 

