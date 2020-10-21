from flask import Flask, render_template

app = Flask(__name__)

@app.route('/health')
def health():
    return "OK"

@app.route('/')
def home():
    data = {
        'sitename': 'http://joaomarcuslf.com'
    }

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)