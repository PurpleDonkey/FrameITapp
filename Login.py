import bcrypt

def logger(self):
    entered_user = self.root.get_screen('login_screen').ids.user.text
    entered_password = self.root.get_screen('login_screen').ids.pwd.text

    # Check if the entered user exists in the database
    self.c.execute("""
        SELECT * FROM users
        WHERE username = %s
    """, (entered_user,))

    user_data = self.c.fetchone()

    if user_data:
        # Check if the entered password matches the hashed password in the database
        hashed_password = user_data[5] if len(user_data) > 5 else None
        self.logged_in_username = entered_user
        self.logged_in_first_name = user_data[1]  
        self.logged_in_last_name = user_data[2]
        print("Login successful. Welcome, {}!".format(entered_user))
        print("Logged-in First Name:", self.logged_in_first_name)
        print("Logged-in Last Name:", self.logged_in_last_name)
        if hashed_password and bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password.encode('utf-8')):
            print(f"Login successful. Welcome, {entered_user}!")
            self.show_welcome_screen()
        else:
            print("Login failed. Invalid password.")
    else:
        print("Login failed. User not found.")

def logout(self):
    self.root.current = "login_screen"
