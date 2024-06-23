import gooeypie as gp

# Password Rating Functions
def password_text(text):
    text = password.text
    print(f'this is the password: {text}') 

def password_length(text):
    text = password.text
    if len(text) < 12:
        print("Password too short")
        return False
    elif len(text) >= 12:
        print("Password length good")
        return True

def uppercase_searcher(text):
    text = password.text
    for char in text:
        if char.isupper():
            print('uppercase found')
            return True
        else:
            print('no uppercase')

def lowercase_searcher(text):
    text = password.text
    for char in text:
        if char.islower():
            print('lowercase found')
            return True
        else:
            print('no uppercase')

def number_searcher(text):
    text = password.text
    for char in text:
        if char.isnumeric():
            print('number found')
            return True
        else:
            print('no number')

def common_password_searcher(text):
    text = password.text
    with open('top_100_passwords.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == text:
                print('password is extremely common')
                return True
            else:
                print('not common')

def breached_password_searcher(text):
    text = password.text
    with open('breachedpasswords.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == text:
                print('password has been found in a data breach')
                return True
            else:
                print('not breached')

def symbol_searcher(text):
    text = password.text
    for char in text:
        if not char.isalnum():
            print(f"{char} is symbol")
            return True
        else:
            print('no symbol')

        # else:
        #     print(f"{char} isn't symbol")
        #     return False
        


# Suggestions
def suggestions(text):
    good_length = password_length(text)
    uppercase_letter_found = uppercase_searcher(text)
    lowercase_letter_found = lowercase_searcher(text)
    number_found = number_searcher(text)
    password_common = common_password_searcher(text)
    password_breached = breached_password_searcher(text)
    symbol_found = symbol_searcher(text)

    suggestion_group = []
    
    points_bar.value = 0

    password_score = 0

    # check for uppercase

    if symbol_found == True:
        password_score += 1
    # else:
    #     password_score -= 1

    if uppercase_letter_found == True:
        password_score += 1
    # else:
    #     password_score -= 1

    # check for lowercase
    
    if lowercase_letter_found == True:
        password_score += 1
    # else:
    #     password_score -= 1

    # check for number
    
    if number_found == True:
        password_score += 1
    # else:
    #     password_score -= 1

    # check for length over 12 characters
        
    if good_length == True:
        password_score += 1
    else:
        suggestion_group.append("is too short")

    # breached and common passwords result in a 0 score
        
    if password_breached or password_common == True:
        password_score = 0

    if password_breached and password_common == False:
        password_score += 1

    if password_score == 0:
        points_bar.value = 0
        rating.text = 'Password is Unusable'
    elif password_score == 1:
        points_bar.value = 20
        rating.text = 'Password is Bad'
    elif password_score == 2:
        points_bar.value = 40
        rating.text = 'Password Needs Some Work'
    elif password_score == 3:
        points_bar.value = 60
        rating.text = 'Password is Ok'
    elif password_score == 4:
        points_bar.value = 80
        rating.text = 'Password is Good'
    elif password_score == 5:
        points_bar.value = 100
        rating.text = 'Password is Excellant!'
    
    print(password_score)
    print(suggestion_group)
        

    # if len(password.text) < 12:
    #     suggestion.text="to short"
    # elif len(password.text) >= 12:
    #      suggestion.text="Y suggestion"
    # else:
    #     suggestion.text="X suggestion"


    



# App Grid
app = gp.GooeyPieApp('Password Strength Evaluator')
app.width = 1000
app.height = 500
app.set_grid(6,5)


# App Name (Text)
app_name = gp.StyleLabel(app, "Password Strength Evaluator")
app_name.font_style = 'italic'


# Director (Text)
director = gp.StyleLabel(app, "Enter your password here:")
director.font_style = 'italic'


# Password Widget
password = gp.Secret(app)
password.width = 30

# Toggle Password Visibility
def toggle_password_visibility(event):
    password.toggle()

password_toggle = gp.Checkbox(app, 'Show Password')
password_toggle.add_event_listener('change', toggle_password_visibility)


# Suggestions Name (Text)
suggestions_name = gp.StyleLabel(app, "Suggestions:")

# Tips Button
def open_other_window(event):
    tip_window.show()


tip_window = gp.Window(app, 'Tips For a Good Password')
tip_window.width = 700
tip_window.height = 500
tip_window.set_grid(5, 5)

the_tips = gp.Label(tip_window, "Here I have compiled a few tips for creating a strong password:")
tip_title = gp.Label(tip_window, 'Welcome to Password Strength Checker!')
tip_paragraph = gp.Label(tip_window, "")
def tip_text():
    with open('tip_para.txt', 'r') as file:
            for line in file:
                line = line.strip()
            tip_paragraph.text = line

tip_text()

tip_window.add(the_tips, 3, 1)
tip_window.add(tip_title, 1, 1)
tip_window.add(tip_paragraph, 2, 1)

tip_btn = gp.Button(app, '💡', open_other_window)
tip_btn.width = 2

# Rating
rating = gp.Label(app, '')
app.add(rating, 5, 4, align='center')

# Points Bar

points_bar = gp.Progressbar(app)
points_bar.width = 270
app.add(points_bar, 4, 4, align='center')

# Listeners
password.add_event_listener('change', suggestions)


# App Addition

suggestion = gp.StyleLabel(app, "")
app.add(suggestion, 3,1, align='left', valign='top')

app.add(app_name, 1, 1, align='left')
app.add(director, 2, 4, align='center', valign='bottom')
app.add(password, 3 ,4, align='center', valign='top')
app.add(suggestions_name, 2, 1, align='left')
app.add(tip_btn, 6, 5, align='right', valign='bottom')
app.add(password_toggle, 3, 5, align='left', valign='top')


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
# 7) password shouldn't contain numbers in succession e.g (1, 2, 3, 4, 5)
# 8) password must contain a letter

# 9) password musn't be a common or exposed password
