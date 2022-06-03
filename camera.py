from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

# step1-create the app, 2-create the camera 3-build the camera 4-run the app
# uix- user interface
# Window.clearcolor = (1,1,1,1)  # change background color
Window.size = (360,600)

class datescanapp(App):

    def build(self):
        # create camera object
        self.camera_obj = Camera()
        self.camera_obj.resolution = (888,888)
        
        # button_1
        button_1 = Button(text="Scan date")
        button_1.size_hint = (.5, .2)
        button_1.pos_hint = {'x':.25, 'y':.25}
        button_1.bind(on_press=self.take_photo)

        # button_2
        button_2 = Button(text="Insert date")
        button_2.size_hint = (.5, .2)
        button_2.pos_hint = {'x':.25, 'y':.25}
        button_2.bind(on_press=self.take_photo)

        # layout
        layout = BoxLayout(orientation='vertical',spacing=10, padding=60)
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_1)
        layout.add_widget(button_2)
        return layout 

    def take_photo(self,*args):
        print("I am taking a photo")
        self.camera_obj.export_to_png('./photo.png')

if __name__ == '__main__':
    datescanapp().run()