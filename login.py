# Barebones login screen
# Labels has to be added at a future date

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.redcolor = (1, 1, 1, 1 )
Window.size = (360, 600)


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=40)
        image = Image(source="covid.jpg")
        button = Button(text="login", size_hint=(None, None), width=100, height=50, pos_hint={"center_x": 0.5})
        layout.add_widget(image)
        layout.add_widget(button)

        return layout





MainApp().run()
