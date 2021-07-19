from flask import Flask, render_template, request, redirect
# from user.py import class User
from user import User

app = Flask(__name__)
app.secret_key = 'user cr'

# This is what happens when the website is visited
@app.route('/')
def index():
# This calls on the Class to utilize its method that contains a function established to query our database
    users = User.get_all_users()
# FUNCTIONALITY TEST ONLY: For each entry in our column
    # for user in users:
# This is an early test that should spit our user id's from the database in the terminal to make sure we are connecting to db and that our query works properly
        # print(user.id)
# This will tell our homepage ('/') to use index.html to render a template and users in green is the data we are passing it, from user in pink that got its value passed to it from User.get_all_users()
    return render_template('index.html', users = users)

@app.route('/create')
def create_form():
    return render_template('create.html')

# This function is called when the URL is visited. Since it is uses methods POST you don't actually see this page, when the function is run it REDIRECTS to another page where we have a template to show the data
@app.route('/users/create', methods=['POST'])
def create_user():
    # print(request.form) FUNCTIONALITY TEST ONLY: Use this to check your terminal to see if your dictionary is being recieved by your form
# This is what calls the method inside of our User class to request the data from our "create user" form
    User.create_user(request.form)
#  REDIRECT IS REQUIRED FOR methods=['POST']
    return redirect('/')
# THIS WONT WORK >>> WHY??? return redirect('/users/<int:user_id>/show')


# The user_id is getting pulled from the data field
@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/')

# URL should be a translation of the URL from HTML,
# BUT DEFINITELY NOT COPIED AND PASTED
# The app.route will break if {{user.id}} is used
@app.route('/users/<int:user_id>/show')
def show_one_user(user_id):
    data = {
        'id': user_id
    }
    user = User.show_one_user(data)
    return render_template('show_user.html', user = user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        'id': user_id
    }
    user = User.show_one_user(data)
    return render_template('edit_user.html', user = user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)