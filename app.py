####################################################################
#################        Importing packages      ###################
####################################################################
from flask import Flask, redirect, render_template, request, session, url_for, redirect, g


#CREATE USER CLASS TO APPEND IT LATER TO A LIST AND USE IT AS A
# GLOBAL VARIABLE

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}'
    
# GLOBAL VARIABLE
users = []
users.append(User(id=0, username='Viktoria', password='password'))
users.append(User(id=1, username='Hans', password='111'))
users.append(User(id=2, username='David', password='David'))

app = Flask(__name__)
app.secret_key = '34efdr345g'

# ALWAYS CHECKS SESSION AND IF IT EXSIST PUT USER INFO INTO G OBJECT
@app.before_request
def before_request():
    g.user = None
    
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        
        
    
    return render_template("login.html")



@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
            
    return render_template("profile.html")




#Step -7(run the app)
if __name__ == '__main__':
    app.run(debug=True)