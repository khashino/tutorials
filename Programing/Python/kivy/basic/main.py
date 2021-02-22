from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_file("main.kv")

class Screen1(Screen):


    def test(self):
        popup = Popup(title='Test popup',
            content=Label(text='Hello world'),
            size_hint=(None, None), size=(400, 400))
        print("ooops")
        popup.open()


class Screen2(Screen):
    pass

class MainApp(App):
    def build(self):
        return sm

#create Screen Manager
sm = ScreenManager(transition=NoTransition())
sm.add_widget(Screen1(name='screen1'))
sm.add_widget(Screen2(name='screen2'))

sm.current = 'screen1'

if __name__ == '__main__':
    MainApp().run()
