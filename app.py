####################################################################
#################        Importing packages      ###################
####################################################################
from flask import Flask, render_template



app = Flask(__name__)



@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")





#Step -7(run the app)
if __name__ == '__main__':
    app.run(debug=True)