import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

class MyApp(App):
    def build(self):
        line = BoxLayout(orientation="vertical")

        hello = Label(text="Hello world")
        line.add_widget(hello)

        hello2 = Label(text="123")
        line.add_widget(hello2)



class MainWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        line = BoxLayout(orientation="vertical")

        hello = Label(text="Hello world")
        line.add_widget(hello)

        hello2 = Label(text="123")
        line.add_widget(hello2)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow())

        return sm


MyApp().run()