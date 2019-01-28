
import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.widget import Widget


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        #self.username = TextInput(multiline=False)
        #self.add_widget(self.username)
        self.add_widget(TextInput(multiline=False))
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)

    def btn_pressed(self, instance, pos):
        print ('pos: printed from root widget: {pos}'.format(pos=pos))

class CustomBtn(Widget):

 pressed = ListProperty([0, 0])

 def on_touch_down(self, touch):
     if self.collide_point(*touch.pos):
         self.pressed = touch.pos
         # we consumed the touch. return False here to propagate
         # the touch further to the children.
         return True
     return super(CustomBtn, self).on_touch_down(touch)

 def on_pressed(self, instance, pos):
     print('pressed at {pos}'.format(pos=pos))
     MyApp.event.cancel()


class MyApp(App):

    def build(self):

        return LoginScreen()

    def my_callback(dt):
        print("My callback is called", dt)
    event = Clock.schedule_interval(my_callback, 1 / 1.)

if __name__ == '__main__':
    MyApp().run()
