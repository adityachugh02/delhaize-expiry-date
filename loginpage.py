from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image

Window.clearcolor = (1,1,1,1)  # change background color
Window.size = (360,600)

class datescanapp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical',spacing=20, padding=60)
        img = Image(source='logo.png')
        # button_1
        button_1 = Button(text="login",size_hint=(None,None),width=100,height=50,
                          pos_hint={'center_x':0.5})
        layout.add_widget(img)
        layout.add_widget(button_1)

        return layout 


if __name__ == '__main__':
    datescanapp().run()