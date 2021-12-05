from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def response():
    text = request.form['text']
    with open("database.txt", 'a') as store_data:
        store_data.write(f'{text}\n')
    return render_template('response.html', test=text)

@app.route('/responses')
def responses():
    with open('database.txt', 'r') as read:
        response = read.readline()
    return render_template('response.html', test=response)

if __name__ == '__main__':
    app.run()