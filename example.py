from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/html')
def html():
    return render_template('index.html')

@app.route('/postexample', methods=['GET','POST'])
def postExample():
    error = None
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            if attempted_username == "admin" and attempted_password == "password":
                return "Successful login!"
            else:
                error = "invalid. Try again"
        return render_template('login.html', error=error)
    except Exception as e:
        return "Horrible error. What did you do?"


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method =='POST':
        f = request.files['the file']
        f.save('var/www/uploads/' + secure_filename(f.filename))


if __name__ == "__main__":
    app.run()