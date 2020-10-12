from flask import Flask, render_template, request, url_for, redirect
from block import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sender = request.form.get('sender')
        recipient = request.form.get('recipient')
        amount = request.form.get('amount')
        generate_block(sender, amount, recipient)
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/check', methods=['GET'])
def chack():
    results = check_integrity()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
