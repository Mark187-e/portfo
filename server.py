from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


def email_me():
    pass


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f"\n{name}, {email}, {message}")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        name = data.get('name', '')  # Get the 'name' from the form data
        return render_template('thank_you.html', name=name)
    else:
        return 'Something went wrong, Try again!'
