import gooeypie as gp
import pyperclip
from PyDictionary import PyDictionary

# Password Rating Functions

def letter_searcher(text):
    text = password.text
    for char in text:
        if char.isalpha():
            print('letter found')
            return True

def dictionary_searcher(text):
    text = password.text
    dictionary = PyDictionary()
    if dictionary.meaning(text,True) is None:
        print(f"'{text}' is not found in the dictionary.")
        return False
    else:
        print(f"'{text}' Is found in the dictionary")
        return True

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

    letter_found = letter_searcher(text)
    password_in_dict = dictionary_searcher(text)
    good_length = password_length(text)
    uppercase_letter_found = uppercase_searcher(text)
    lowercase_letter_found = lowercase_searcher(text)
    number_found = number_searcher(text)
    password_common = common_password_searcher(text)
    password_breached = breached_password_searcher(text)
    symbol_found = symbol_searcher(text)

    suggestion_group1 = []
    suggestion_group2 = []
    suggestion_group3 = []

    suggestions1_amount = 0
    suggestions2_amount = 0
    suggestions3_amount = 0

    points_bar.value = 0

    password_score = 0

    # check for length over 12 characters
        
    if good_length == True:
        password_score += 1
    else:
        suggestion_group2.append('to be longer')
        suggestions2_amount += 1

    # check for letter

    if letter_found == True:
        password_score += 1
    else:
        suggestions1_amount += 1


    # check for uppercase    
    if symbol_found == True:
        password_score += 1
    else:
        suggestion_group2.append('a symbol')
        suggestions2_amount += 1


    if uppercase_letter_found == True:
        password_score += 1
    else:
        suggestion_group1.append('an uppercase letter')
        suggestions1_amount += 1


    # check for lowercase
    
    if lowercase_letter_found == True:
        password_score += 1
    else:
        suggestion_group1.append('a lowercase letter')
        suggestions1_amount += 1


    # check for number
    
    if number_found == True:
        password_score += 1
    else:
        suggestion_group2.append('a number')
        suggestions2_amount += 1

    # breached, dictionary words and common passwords result in a 0 score
    
    if password_breached == True:
        suggestion_group3.append('compromised')
        suggestions3_amount += 1

    if password_common == True:
        suggestion_group3.append('too common')
        suggestions3_amount += 1

    if password_in_dict == True:
        suggestion_group3.append('in the english dictionary')
        suggestions3_amount += 1
    
    if password_breached or password_common or password_in_dict == True:
        password_score = 0

    if password_breached and password_common and password_in_dict == False:
        password_score += 1

    if password_score == 0:
        points_bar.value = 0
        rating.text = 'Password is unusable'
    elif password_score == 1:
        points_bar.value = 20
    elif password_score == 2:
        points_bar.value = 20
        rating.text = 'Password is terrible'
    elif password_score == 3:
        points_bar.value = 40
        rating.text = 'Password is weak'
    elif password_score == 4:
        points_bar.value = 60
        rating.text = 'Password is mediocre'
    elif password_score == 5:
        points_bar.value = 80
        rating.text = 'Password is decent'
    else:
        points_bar.value = 100
        rating.text = 'Password is strong'

    suggestion_words1 = ', '.join(suggestion_group1)

    if suggestions1_amount >= 1:
        suggestion1.text = f'Password should include: {suggestion_words1}'
    else:
        suggestion1.text = ''


    suggestion_words2 = ', '.join(suggestion_group2)

    if suggestions2_amount >= 1:
        suggestion2.text = f'Password needs: {suggestion_words2}'
    else:
        suggestion2.text = ''

    suggestion_words3 = ', '.join(suggestion_group3)
    
    if suggestions3_amount >= 1:
        suggestion3.text = f'Uh oh! Password is: {suggestion_words3}'
    else:
        suggestion3.text = ''

    print(password_score)
    print(suggestion_group1)
        

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
app.add(app_name, 1, 1, align='left')





# Password Widget

password = gp.Secret(app)
password.width = 30
password.text = ('Enter Your Password Here!')
app.add(password, 3 ,4, align='center', valign='top')





# Toggle Password Visibility

def toggle_password_visibility(event):
    password.toggle()

password_toggle = gp.Checkbox(app, 'Hide Password')
password_toggle.add_event_listener('change', toggle_password_visibility)

password.toggle()
app.add(password_toggle, 3, 5, align='left', valign='top')





# Suggestions Name (Text)

suggestions_name = gp.StyleLabel(app, "Suggestions:")
app.add(suggestions_name, 2, 1, align='left')





# Copy Clipboard Button

def copy_password(text):
    text = password.text
    pyperclip.copy(text)

copy_password_button = gp.Button(app, 'Copy', copy_password)
copy_password_button.width = 4
app.add(copy_password_button, 4,5, align='left', valign='top')





# Tips Button
def open_other_window(event):
    tip_window.show()

tip_window = gp.Window(app, 'Tips For a Good Password')
tip_window.width = 700
tip_window.height = 500
tip_window.set_grid(5, 5)

the_tips = gp.Label(tip_window, "Here I have compiled a few tips for creating a strong password:")
tip_title = gp.Label(tip_window, 'Here i have compiled some tips for a good password!')
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

tip_btn = gp.Button(app, 'Tips', open_other_window)
tip_btn.width = 3
app.add(tip_btn, 6, 5, align='right', valign='bottom')





# Rating

rating = gp.Label(app, '')
app.add(rating, 5, 4, align='center', valign='top')





# Points Bar

points_bar = gp.Progressbar(app)
points_bar.width = 270
app.add(points_bar, 4, 4, align='center')





#Check Button

check_button = gp.Button(app, 'Check Strength', suggestions)
check_button.width = 11
app.add(check_button, 2, 4, align='center', valign='bottom')





# Suggestions

suggestion1 = gp.Label(app, '')
app.add(suggestion1, 3,1, align='left', valign='top')

suggestion2 = gp.Label(app, '')
app.add(suggestion2, 4,1, align='left', valign='top')

suggestion3 = gp.Label(app, '')
app.add(suggestion3, 5,1, align='left', valign='top')



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
