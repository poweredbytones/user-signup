from flask import Flask, request, redirect, render_template
import cgi, re

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', watchlist=["blank"], error=encoded_error and cgi.escape(encoded_error, quote=True))
    
@app.route("/sub",methods=['POST'])
def submission():
    isErr = False
    
    ######-------------------------------------------------------------------
    # user text box logic
    # requires a text box named 'username'
    # returns Usererror if there was an error pertaining to the box 'username'


    # look inside the request to figure out what the user in the user field
    UserNameInput = request.form['username']
    user_error = ""

    # if the user typed nothing at all, redirect and tell them the error
    if (not UserNameInput):
        user_error="User name can not be blank"
        isErr = True
    
    for char in UserNameInput:
        if char == ' ':
            user_error="Username can not include a space"
            isErr = True
            
    
    if ( len(UserNameInput) < 3 and UserNameInput):
        user_error="User name can not be less then 3 characters"
        isErr = True

    if ( len(UserNameInput) > 20 ):
        user_error="User name can not be more then 20 characters"
        isErr = True


    #
    #
    #########################################################################

    ######-------------------------------------------------------------------
    # password box logic
    # requires a password box named 'password'
    # returns Usererror if there was an error pertaining to the box 'password'

    password_error = ""
    # look inside the request to figure out what the user in the user field
    PasswordInput = request.form['password']
    
    verifyInput = request.form['verify']

    ## TODO add logic to see if to passwords are equal
    if not (PasswordInput == verifyInput ):
        isErr = True
        password_error = "Both Passwords must match"

        ##
        
    if (not PasswordInput):
        password_error="Password cannot be blank"
        isErr = True
    ##
    for char in PasswordInput:
        if char == ' ':
            password_error="password cannot include a space"
            isErr = True
            
    ## 
    if ( len(PasswordInput) < 3 and PasswordInput):
        password_error="Password can not be less then 3 characters"
        isErr = True

##
    if ( len(PasswordInput) > 20 ):
        password_error="Password can not be more then 20 characters"
        isErr = True


#
    #
    #########################################################################

    ######-------------------------------------------------------------------
    # email box logic
    # requires a text box named 'email'
    # returns emailerror if there was an error pertaining to the box 'email'


    email_error = ""
    # look inside the request to figure out what the email is in the email field
    EmailInput = request.form['email']
    email_error = ""
    

    ## TODO add logic to see if to passwords are equal
    if EmailInput != "":
        if not re.match("[^@]+@[^@]+\.[^@]+", EmailInput): 
            email_error = "Not a vaild email address"
            isErr = True


#
    #
    #########################################################################

    

    encoded_error = request.args.get("error")

    if isErr:
        return render_template('base.html', user_error=user_error,UserNameInput =UserNameInput,
                                PasswordInput=PasswordInput,password_error=password_error,
                                EmailError=email_error,EmailInput=EmailInput,
                                 error=encoded_error and cgi.escape(encoded_error, quote=True))
    else:
        return render_template('accept.html', UserName=UserNameInput,
                                 error=encoded_error and cgi.escape(encoded_error, quote=True))
    

app.run()