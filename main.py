#  Same design as vid13 but using the .kv file

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout



class Interface(FloatLayout):        
    def display_information(self):
        data = self.ids.textinput.text
        self.ids.label.text = data
        
class ProjectApp(App):
    pass




ProjectApp().run()