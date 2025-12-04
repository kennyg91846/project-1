#  Same design as vid13 but using the .kv file

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout



class Interface(FloatLayout):        
    def display_information(self):
        data = self.ids.textinput.text
        self.ids.label.text = data
    
    def process_hex_data(self):
        """Convert hex input (e.g., 'C87D-C8FB') to Unicode characters."""
        data = self.ids.textinput.text.strip()
        try:
            # Split by hyphen and convert each hex value to character
            parts = data.split('-')
            result = ''.join(chr(int(p, 16)) for p in parts if p)
            self.ids.label.text = result
        except (ValueError, OverflowError):
            self.ids.label.text = 'Invalid hex input'
        
class ProjectApp(App):
    pass




ProjectApp().run()