from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    published_date = db.Column(db.String(100), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Game {self.name}>'

@app.route('/')
def home():
    games = Game.query.order_by(Game.published_date.desc()).all()
    return render_template('home.html', games=games)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    url = request.form['url']
    author = request.form['author']
    published_date = request.form['published_date']   #datetime.utcnow()

    game = Game(name=name, url=url, author=author, published_date=published_date)

    db.session.add(game)
    db.session.commit()

    return redirect('/')

@app.route('/game/<int:id>')
def read(id):
    game = Game.query.get_or_404(id)
    return jsonify({
        'name': game.name,
        'url': game.url,
        'author': game.author,
        'published_date': game.published_date
    })

@app.route('/games')
def read_all():
    games = Game.query.all()
    result = []
    for game in games:
        game_data = {
            'id': game.id,
            'name': game.name,
            'url': game.url,
            'author': game.author,
            'published_date': game.published_date
        }
        result.append(game_data)
    return jsonify(result)

"""@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    game = Game.query.get_or_404(id)

    game.name = request.form['name']
    game.url = request.form['url']
    game.author = request.form['author']
    game.published_date = request.form['published_date']

    db.session.commit()

    return redirect('/')"""

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_game(id):
    game = Game.query.get_or_404(id)

    if request.method == 'POST':
        game.name = request.form['name']
        game.url = request.form['url']
        game.author = request.form['author']
        game.published_date = datetime.strptime(request.form['published_date'], '%Y-%m-%dT%H:%M:%S')

        db.session.commit()

        return redirect('/')

    return render_template('update_game.html', game=game)


@app.route('/delete/<int:id>')
def delete(id):
    game = Game.query.get_or_404(id)

    db.session.delete(game)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
