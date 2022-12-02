screen_helper = '''
ScreenManager:
    LoginScreen:
    AccountScreen:
    CreateScreen:
    
<CreateScreen>:
    name: 'create'
    MDTextField:
        id: createuser
        hint_text: 'Enter Username'
        helper_text_mode: "on_focus"
        mode: 'fill'
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:400
        multiline: False
    MDTextField:
        id: createpassword
        icon_left: 'key-variant'
        hint_text: 'Enter Password'
        helper_text_mode: "on_focus"
        password: True
        mode: 'fill'
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:400
        multiline: False
    MDRectangleFlatButton:
        text: 'Create Account'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        size_hint: (0.4,0.05)
        on_press: app.create_user()
    MDIconButton:
        icon: 'eye'
        pos_hint: {'center_x':0.71,'center_y':0.5}
        on_press: app.togglevisibilty()
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "24sp"    
    
<LoginScreen>:
    name: 'login'
    MDTextField:
        id: username
        hint_text: 'Enter Username'
        helper_text_mode: "on_focus"
        mode: 'fill'
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:400
        multiline: False
    MDTextField:
        id: password
        icon_left: 'key-variant'
        hint_text: 'Enter Password'
        helper_text_mode: "on_focus"
        password: True
        mode: 'fill'
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:400
        multiline: False
    MDRectangleFlatButton:
        id: 'button'
        text: 'Login'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        size_hint: (0.4,0.05)
        on_release: app.login()
    MDRectangleFlatButton:
        id: 'button'
        text: 'Create Account'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint: (0.4,0.05)
        on_press: root.manager.current = 'create'
    MDIconButton:
        id: 'visible'
        icon: 'eye'
        pos_hint: {'center_x':0.71,'center_y':0.5}
        on_press: app.togglevisibilty()
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "24sp"


<AccountScreen>:
    name: 'account'
    MDLabel: 
        text: 'Welcome'
        halign: 'center'
    MDIconButton:
        icon:'arrow-left-circle'
        pos_hint: {'center_x':0.2,'center_y':0.075}
        on_press: root.manager.current = 'login'
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon_size: "32sp"
        
    

'''