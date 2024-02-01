import bcrypt
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel

def register(self):
    # Retrieve values from input fields
    reg_user = self.root.get_screen('register_screen').ids.reg_user.text
    reg_password = self.root.get_screen('register_screen').ids.reg_pwd.text
    f_name = self.root.get_screen('register_screen').ids.f_name.text
    l_name = self.root.get_screen('register_screen').ids.l_name.text
    email = self.root.get_screen('register_screen').ids.email.text

    # Check if all required fields are filled
    if not all([reg_user, reg_password, f_name, l_name, email]):
        print("Please fill in all fields.")
        return

    # Hashing the password before inserting into the database
    password_hash = self.hash_password(reg_password)

    # Check if all required fields are filled
    if not all([reg_user, reg_password, f_name, l_name, email]):
        self.show_error_popup("Please fill in all fields.")
        return

    # Check if the username and email are unique
    if self.check_username_exists(reg_user):
        self.show_error_popup("Username already exists.")
        return
    
    if self.check_email_exists(email):
        self.show_error_popup("Email already exists.")
        return
    
    # Inserting data into the users table
    self.c.execute("""
        INSERT INTO users (first_name, last_name, email, username, password_hash)
        VALUES (%s, %s, %s, %s, %s)
    """, (f_name, l_name, email, reg_user, password_hash))

    self.conn.commit()
    
    # Clear input fields after successful registration
    self.root.get_screen('register_screen').ids.reg_first_name.text = ''
    self.root.get_screen('register_screen').ids.reg_last_name.text = ''
    self.root.get_screen('register_screen').ids.reg_email.text = ''
    self.root.get_screen('register_screen').ids.reg_user.text = ''
    self.root.get_screen('register_screen').ids.reg_pwd.text = ''

def check_username_exists(self, username):
    # Check if the username already exists in the users table
    self.c.execute("SELECT * FROM users WHERE username = %s", (username,))
    return bool(self.c.fetchone())

def check_email_exists(self, email):
    # Check if the email already exists in the users table
    self.c.execute("SELECT * FROM users WHERE email = %s", (email,))
    return bool(self.c.fetchone())

def hash_password(self, password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def show_error_popup(self, message):
        content = MDLabel(font_style='Body1', theme_text_color="Secondary", text=message)
        popup = Popup(title="Error", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

print("Registration successful")