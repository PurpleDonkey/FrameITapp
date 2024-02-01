from kivy.uix.filechooser import FileChooserIconView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.popup import Popup
from kivymd.uix.filemanager import MDFileManager

def show_welcome_screen(self):
    self.root.current = "welcome_screen"

def show_file_chooser(self, file_type):
    def on_submit(instance):
        selected_file = file_chooser.selection and file_chooser.selection[0] or ""
        popup.dismiss()

        if file_type == 'photo':
            self.display_image(selected_file)
        elif file_type == 'video':
            self.display_video(selected_file)
        else:
            print(f"Selected file: {selected_file}")

    file_chooser = (
        FileChooserIconView()
    )
    file_chooser.path = "/"

    popup_content = MDBoxLayout(orientation='vertical')
    popup_content.add_widget(file_chooser)

    submit_button = MDRaisedButton(
        text="Submit", pos_hint={"center_x": 0.5}, on_press=on_submit
    )
    popup_content.add_widget(submit_button)

    popup = Popup(
        title=f"Select {file_type.capitalize()}",
        content=popup_content,
        size_hint=(None, None),
        size=("400dp", "500dp"),
        auto_dismiss=False,
    )

    popup.open()

def display_image(self, file_path):
    image_popup = Popup(
        title="Image Preview",
        content=Image(source=file_path),
        size_hint=(None, None),
        size=("300dp", "300dp"),
        auto_dismiss=True,
    )
    image_popup.open()

def display_video(self, file_path):
    video_popup = Popup(
        title="Video Preview",
        content=VideoPlayer(source=file_path),
        size_hint=(None, None),
        size=("400dp", "300dp"),
        auto_dismiss=True,
    )
    video_popup.open()