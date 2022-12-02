from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_helper import screen_helper
from kivymd.app import MDApp

# dictionary used as a database for usernames and passwords
account = {'User1': "1234", 'User2': "4321"}


# creating screen classes


class CreateScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class AccountScreen(Screen):
    pass


# adding widgets to the screen
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(AccountScreen(name='account'))
sm.add_widget(CreateScreen(name='create'))


# class that builds the app

class DemoApp(MDApp):

    def __init__(self):
        super().__init__()
        self.screen = None

    def build(self):
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        self.screen = Builder.load_string(screen_helper)

        return self.screen

    # login function gets username and password and matches to key:value in dictionary
    def login(self):
        login_name = self.root.get_screen('login').ids.username.text
        login_password = self.root.get_screen('login').ids.password.text
        if (login_name, login_password) in account.items():
            self.root.current = 'account'

    # visibility function toggles password visibility
    def togglevisibilty(self):
        if self.root.get_screen('login').ids.password.password or self.root.get_screen(
                'create').ids.createpassword.password:
            self.root.get_screen('login').ids.password.password = False
            self.root.get_screen('create').ids.createpassword.password = False

        elif not self.root.get_screen('login').ids.password.password or self.root.get_screen(
                'create').ids.createpassword.password:
            self.root.get_screen('login').ids.password.password = True
            self.root.get_screen('create').ids.createpassword.password = True

    # create user function takes new username and password and adds it to dictionary where user can then login
    def create_user(self):
        login_name = self.root.get_screen('create').ids.createuser.text
        login_password = self.root.get_screen('create').ids.createpassword.text
        account.update({login_name: login_password})
        self.root.current = 'login'


# runs application

DemoApp().run()
