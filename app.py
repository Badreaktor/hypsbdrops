from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


#    { name: 'warden heart', tier: 'V', amount: '1', chance: '0.01%' },
#    { name: 'Smite VII', tier: 'V', amount: '1', chance: '0.05%' },
#    { name: 'Shard of the Shredded', tier: 'V',amount: '1', chance: '0.06%' },
#    { name: 'machta dye', tier: 'V', amount: '1', chance: '0.0002%' },
#    { name: 'scythe blade', tier: 'V', amount: '1', chance: '0.1%' },