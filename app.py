from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/requests')
def requests():
    return render_template('requests.html')

@app.route('/identities')
def identities():
    identities_data = [
        {
            'identity_id': 1,
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'role': 'Admin'
        },
        {
            'identity_id': 2,
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'role': 'User'
        }
    ]
    return render_template('identities.html', identities=identities_data)

@app.route('/reporting')
def reporting():
    return render_template('reporting.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)