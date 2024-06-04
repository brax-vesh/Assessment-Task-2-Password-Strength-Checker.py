import gooeypie as gp

# Password Rating Functions
def password_text(text):
    text = password.text
    print(f'this is the password: {text}') 

def length(text):
    text = password.text
    if len(text) < 10:
        print("Password too short...")
    elif len(text) >= 10:
        print("Password length good...")

def uppercase_searcher(text):
    text = password.text
    for char in text:
        if char.isupper():
            print('uppercase true')
            break

def lowercase_searcher(text):
    text = password.text
    for char in text:
        if char.islower():
            print('lowercase true')
            break    

def number_searcher(text):
    text = password.text
    for char in text:
        if char.isnumeric():
            print('number found')
            break


# App Grid
app = gp.GooeyPieApp('Password Strength Checky')
app.width = 1000
app.height = 500
app.set_grid(5,5)

# App Name Text
app_name = gp.StyleLabel(app, "Password Strength Checky")
app_name.font_style = 'italic'

# Password Widget
password = gp.Input(app)
password.width = 30

# Listeners
# password.add_event_jlistener('change', password_text)
# password.add_event_listener('change', length)
password.add_event_listener('change', uppercase_searcher)
# password.add_event_listener('change', number_searcher)

# Director Text
director = gp.StyleLabel(app, "Enter your password here:")
director.font_style = 'italic'

# App Addition
app.add(app_name, 1, 1)
app.add(director, 2, 5, align='center', valign='bottom')
app.add(password, 3 ,5, align='center', valign='top')


app.run()

# suggestions to implement
# 1) length must be greater than 10

# 2) 1 capital letter and 1 lower case letter must be used
# 3) a special character must be used

# 4) password shouldn't be a dictionary word
# 5) shouldn't be a name

# 6) password must contain a number
# 7) password shouldn't contain numbers in succession e.g (1, 2, 3, 4, 5)
# 8) password must contain a letter

# 9) password musn't be a common or exposed password