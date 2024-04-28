import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

class MainWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        line = BoxLayout(orientation="vertical")

        mert = Label(text="Виберіть карти")
        line.add_widget(mert)
        ktt = Button(text="1")
        line.add_widget(ktt)
        ktt5 = Button(text="2")
        line.add_widget(ktt5)
        ktt2 = Button(text="3")
        line.add_widget(ktt2)
        kty = Button(text="4")
        line.add_widget(kty)


        self.add_widget(line)




class MyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow())

        return sm

MyApp().run()