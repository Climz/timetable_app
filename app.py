from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.textinput import TextInput

from main import my_group, keys_of_my_group


class MyApp(App):
    def build(self):

        bl = BoxLayout(orientation="vertical")
        gl = GridLayout(cols=2, size_hint=[1, .6])

        bl.add_widget(TextInput(size_hint=[.4, .4]))

        gl.add_widget(Label(text="1\n9:00-10:30"))
        gl.add_widget(Label(text=str(my_group[keys_of_my_group[0]][2])))

        gl.add_widget(Label(text="2\n10:40-12:10"))
        gl.add_widget(Label(text=str(my_group[keys_of_my_group[0]][4])))

        gl.add_widget(Label(text="3\n12:40-14:10"))
        gl.add_widget(Label(text=str(my_group[keys_of_my_group[0]][6])))

        gl.add_widget(Label(text="4\n14:20-15:50"))
        gl.add_widget(Label(text=str(my_group[keys_of_my_group[0]][8])))

        gl.add_widget(Label(text="5\n16:20-17:50"))
        gl.add_widget(Label(text=str(my_group[keys_of_my_group[0]][10])))

        gl.add_widget(Label(text="6\n18:00-19:30"))
        gl.add_widget(Label(text=str(my_group[keys_of_my_group[0]][12])))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    MyApp().run()
