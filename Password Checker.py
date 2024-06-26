import gooeypie as gp
import pyperclip
from PyDictionary import PyDictionary

# Password Rating Functions

def space_failsafe(text):
    text = password.text
    if text.isspace():
        return True
    else:
        return False

def letter_searcher(text):
    text = password.text
    for char in text:
        if char.isalpha():
            return True

def dictionary_searcher(text):
    text = password.text
    dictionary = PyDictionary()
    if dictionary.meaning(text,True) is None:
        return False
    else:
        return True

def password_length(text):
    text = password.text
    if len(text) < 12:
        return False
    elif len(text) >= 12:
        return True

def uppercase_searcher(text):
    text = password.text
    for char in text:
        if char.isupper():
            return True
        else:
            print('no uppercase')

def lowercase_searcher(text):
    text = password.text
    for char in text:
        if char.islower():
            return True
        else:
            print('no uppercase')

def number_searcher(text):
    text = password.text
    for char in text:
        if char.isnumeric():
            return True
        else:
            print('no number')

def common_password_searcher(text):
    text = password.text
    with open('top_100_passwords.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == text:
                return True
            else:
                print('not common')

def breached_password_searcher(text):
    text = password.text
    with open('breachedpasswords.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == text:
                return True
            else:
                print('not breached')

def symbol_searcher(text):
    text = password.text
    for char in text:
        if not char.isalnum():
            return True
        else:
            print('no symbol')

        # else:
        #     print(f"{char} isn't symbol")
        #     return False
        


# Suggestions
def suggestions(text):
        text = password.text

        # dictionary_on = dict_check_validation(text)
        # if dictionary_on == True:
        
        only_space = space_failsafe(text)
        password_in_dict = dictionary_searcher(text)
        letter_found = letter_searcher(text)
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
            suggestion_group2.append('to contain a symbol (!,@,#,$,?)')
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
            suggestion_group2.append('to have a number')
            suggestions2_amount += 1

    # breached, dictionary words, only spaces and common passwords result in a 0 score
    
        if password_breached == True:
            suggestion_group3.append('in a data breach')
            suggestions3_amount += 1

        if password_common == True:
            suggestion_group3.append('too common')
            suggestions3_amount += 1

        if password_in_dict == True:
            if len(text) >1:
                if only_space == False:
                    suggestion_group3.append('in the english dictionary')
                    suggestions3_amount += 1

        if only_space == True:
            password_score = 0
            suggestion_group3.append('comprised of only spaces, please use other characters')
            suggestions3_amount += 1

        # if dictionary_on == True:
        #     if password_in_dict == True and len(text) >= 1:
        #         suggestion_group3.append('in the english dictionary')
        #         suggestions3_amount += 1

        #     if password_in_dict == True:
        #         password_score = 0
        #     else:
        #         print('pass not in dict')
        # else:
        #     print('password_disabled')
    
        if password_breached or password_common or password_in_dict and only_space == True:
            password_score = 0

        if password_breached and password_common and password_in_dict and only_space== False:
            password_score += 1

        if password_score == 0:
            star_rating.text = '☆☆☆☆☆'
            rating.text = '" Password is unusable "'
        elif password_score == 1:
            star_rating.text = '★☆☆☆☆'
        elif password_score == 2:
            star_rating.text = '★☆☆☆☆'
            rating.text = '" Password is terrible "'
        elif password_score == 3:
            star_rating.text = '★★☆☆☆'
            rating.text = '" Password is weak "'
        elif password_score == 4:
            star_rating.text = '★★★☆☆'
            rating.text = '" Password is mediocre "'
        elif password_score == 5:
            star_rating.text = '★★★★☆'
            rating.text = '" Password is decent "'
        else:
            star_rating.text = '★★★★★'
            rating.text = '" Password is strong "'

        suggestion_words1 = ' AND '.join(suggestion_group1)

        if suggestions1_amount >= 1:
            suggestion1.text = f'Password should include: {suggestion_words1}'
        else:
            suggestion1.text = ''


        suggestion_words2 = ' AND '.join(suggestion_group2)

        if suggestions2_amount >= 1:
            suggestion2.text = f'Password needs: {suggestion_words2}'
        else:
            suggestion2.text = ''

        suggestion_words3 = ' AND '.join(suggestion_group3)
    
        if suggestions3_amount >= 1:
            suggestion3.text = f'Warning! Password is: {suggestion_words3}'
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

app = gp.GooeyPieApp('Password Strength Evaluator!')
app.width = 1000
app.height = 500
app.set_grid(6,5)






# App Name (Text)

app_name = gp.StyleLabel(app, "Password Strength Evaluator")
app_name.font_style = 'italic'
app.add(app_name, 1, 1, align='left')
app_name.font_size = 40
app_name.font_name = 'Times New Roman'




# Password Widget

password = gp.Secret(app)
password.width = 30
password.text = ('Enter Your Password Here!')
app.add(password, 3 ,4, align='center', valign='bottom')





# Toggle Password Visibility

def toggle_password_visibility(event):
    password.toggle()

# password_toggle = gp.ImageButton(app, None, toggle_password_visibility, 'Hide Password')
password_toggle = gp.Checkbox(app, 'Hide Password')
password_toggle.add_event_listener('change', toggle_password_visibility)
password.toggle()

app.add(password_toggle, 3, 5, align='left', valign='bottom')


# Suggestions Name (Text)

suggestions_name = gp.StyleLabel(app, "Suggestions:")
suggestions_name.font_style = 'italic'
suggestions_name.font_size = 25
suggestions_name.font_name = 'Times New Roman'
app.add(suggestions_name, 2, 1, align='left', valign='bottom')





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
tip_window.set_grid(10, 5)

tip_title = gp.StyleLabel(tip_window, 'Tips For a Good Password:')
tip_title.font_name = 'Times New Roman'
tip_title.font_size = 25
tips1 = gp.Label(tip_window, "1) Include an uppercase and lowercase letter in the password")
tips2 = gp.Label(tip_window, "2) Include a number and symbol in your password")
tips3 = gp.Label(tip_window, "3) A secure password should be 12 characters long")
tips4 = gp.Label(tip_window, "4) A password should not be a dictionary word")
tips5 = gp.Label(tip_window, "5) Our program will warn you if you password has been breached or is too common. ")

# tips6 = gp.Label(tip_window, "(Tick the 'Disable Dictionary' box to reduce computer lag. Warning: this will reduce password strength.)")

tip_window.add(tip_title, 1, 1)
tip_window.add(tips1, 2, 1)
tip_window.add(tips2, 3, 1)
tip_window.add(tips3, 4, 1)
tip_window.add(tips4, 5, 1)
tip_window.add(tips5, 6, 1)
# tip_window.add(tips6, 10, 1, align='center')

tip_btn = gp.Button(app, 'Tips', open_other_window)
tip_btn.width = 3
app.add(tip_btn, 6, 5, align='right', valign='bottom')





# Rating

rating = gp.Label(app, '"  Here your password will be rated out of five stars!  "')
app.add(rating, 2, 4, align='center', valign='top')





# Star rating

star_rating = gp.Label(app, '☆☆☆☆☆')
app.add(star_rating, 1, 4, align='center', valign='bottom')





#Check Button
check_button = gp.Button(app, 'Check Strength', suggestions)
check_button.width = 11
app.add(check_button, 4, 4, align='center', valign='top')


# Disable Dictionary

# def dict_check_validation(event):
#     if dis_dict.checked:
#         return False
#     else:
#         return True

# dis_dict = gp.Checkbox(app, 'Disable Dictionary Check')
# password_toggle.add_event_listener('change', dict_check_validation)

# app.add(dis_dict, 6,4, align='right', valign='bottom')


# Suggestions

suggestion1 = gp.Label(app, '')
app.add(suggestion1, 3,1, align='left', valign='bottom')

suggestion2 = gp.Label(app, '')
app.add(suggestion2, 4,1, align='left', valign='middle')

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
