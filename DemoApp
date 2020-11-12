from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    MenuScreen:
    Question1Screen:
    Question2Screen:
    Question3Screen:
    Question4Screen:
    EndScreen:
    InfoScreen:

<MenuScreen>:
    name: "menu"
    MDRectangleFlatButton
        text: "Start"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = "Question1"
        
<Question1Screen>:
    name: "Question1"
    MDLabel:
        text: "Have you been exposed to COVID-19 in the last 14 days?"
        halign: "center"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.4,"center_y":0.4}
        on_press: root.manager.current = "Question2"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.6,"center_y":0.4}
        on_press: root.manager.current = "Question2"

<Question2Screen>:
    name: "Question2"
    MDLabel:
        text: "Have you had any of the following Symptoms(1): Dry Cough, Sore Throat, or Fever?"
        halign: "center"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.4,"center_y":0.4}
        on_press: root.manager.current = "Question3"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.6,"center_y":0.4}
        on_press: root.manager.current = "Question3"

<Question3Screen>:
    name: "Question3"
    MDLabel:
        text: "Have you had any of the following Symptoms(2): Shortness of breath, trouble breathing, loss sense of smell?"
        halign: "center"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.4,"center_y":0.4}
        on_press: root.manager.current = "Question4"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.6,"center_y":0.4}
        on_press: root.manager.current = "Question4"


<Question4Screen>:
    name: "Question4"
    MDLabel:
        text: "Have you tested for COVID-19 in the last 14 days?"
        halign: "center"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.4,"center_y":0.4}
        on_press: root.manager.current = "end"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.6,"center_y":0.4}
        on_press: root.manager.current = "end"   
        
<EndScreen>:    
    name: "end"
    MDLabel:
        text: "If you answered no to most of these questions, you most likely don't have COVID-19."
        halign: "center"
    MDRectangleFlatButton
        text: "Proceed screen if you answered yes to one of the following questions"
        pos_hint: {"center_x":0.5,"center_y":0.45}
        on_press: root.manager.current = "info"   

<InfoScreen>
    name: "info"
    MDLabel:
        text: "Go to schsa.org/corona-virus/testing/ for more information about testing"
        halign: "center"
    
        
            
"""

# These classes are needed to run the application and corresponds with the screens from the code above.
class MenuScreen(Screen):
    pass


class Question1Screen(Screen):
    pass


class Question2Screen(Screen):
    pass


class Question3Screen(Screen):
    pass


class Question4Screen(Screen):
    pass


class EndScreen(Screen):
    pass


class InfoScreen(Screen):
    pass


# Create screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(Question1Screen(name="Question1"))
sm.add_widget(Question2Screen(name="Question2"))
sm.add_widget(Question3Screen(name="Question3"))
sm.add_widget(Question4Screen(name="Question4"))
sm.add_widget(EndScreen(name="end"))
sm.add_widget(InfoScreen(name="info"))


# Builds the App

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "A700"
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
