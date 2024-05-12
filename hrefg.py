from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        hbox = BoxLayout(orientation="horizontal")
        vbox = BoxLayout(orientation="vertical")

        txt = Label(text="Виберіть екран")
        btn1 = Button(text="1 екран")
        btn1.on_press = self.goToBtn1
        btn2 = Button(text="2 екран")

        vbox.add_widget(btn1)
        vbox.add_widget(btn2)

        hbox.add_widget(txt)
        hbox.add_widget(vbox)

        self.add_widget(hbox)

    def goToBtn1(self):
        self.manager.current = "123321"



class Btn1Screen(Screen):
    def __init__(self, name="123321"):
        super().__init__(name=name)
        hbox = BoxLayout(orientation="horizontal")
        btn1 = Button(text="назад")
        btn1.on_press = self.goToFirst
        hbox.add_widget(btn1)

        self.add_widget(hbox)


    def goToFirst(self):
        self.manager.current = "first"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(Btn1Screen())
        return sm

app = MyApp()
app.run()