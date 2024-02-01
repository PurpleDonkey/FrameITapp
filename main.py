from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

class MainApp(MDApp):
    from Database import create_database, create_table, on_start, on_stop, connect_database, close_database
    from Login import logger, logout
    from Register import register, hash_password, check_username_exists, check_email_exists, show_error_popup
    from Welcome import show_welcome_screen, open_nav_drawer
    logged_in_username = ""
    logged_in_first_name = ""
    logged_in_last_name = ""
    conn = None
    c = None

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Login.kv"))
        screen_manager.add_widget(Builder.load_file("Register.kv"))
        screen_manager.add_widget(Builder.load_file("Welcome.kv"))
        return screen_manager

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="D:/Kivy Proj/assets/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="D:/Kivy Proj/assets/Poppins-SemiBold.ttf")
    MainApp().run()