from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

class ConvertMilesKmApp(App):
    km_result = StringProperty("0.0 km")

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles_text):
        try:
            miles = float(miles_text)
            kilometers = miles * 1.60934
            self.km_result = f"{kilometers:.5f} km"
        except ValueError:
            self.km_result = "0.0 km"

    def handle_increment(self, increment):
        try:
            current_value = float(self.root.ids.input_miles.text)
        except ValueError:
            current_value = 0
        new_value = current_value + increment
        self.root.ids.input_miles.text = str(new_value)
        self.handle_convert(self.root.ids.input_miles.text)

ConvertMilesKmApp().run()