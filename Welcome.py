from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

nav_drawer = ObjectProperty()
def open_nav_drawer(self):
    self.ids.nav_drawer.set_state("open")

def show_welcome_screen(self):
    welcome_screen = self.root.get_screen('welcome_screen')
    welcome_screen.ids.logged_in_user.text = "{} {}".format(self.logged_in_first_name, self.logged_in_last_name)
    welcome_screen.nav_drawer = self.root.get_screen('welcome_screen').ids.nav_drawer
    self.root.current = "welcome_screen"

