from flask import Flask
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
    published_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Game {self.name}>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Add test data
        game1 = Game(name='Super Mario', url='https://example.com/super-mario', author='Nintendo', published_date=datetime.strptime('2022-01-01 12:00:00', '%Y-%m-%d %H:%M:%S'))
        game2 = Game(name='Minecraft', url='https://example.com/minecraft', author='Mojang', published_date=datetime.strptime('2022-02-01 12:00:00', '%Y-%m-%d %H:%M:%S'))
        game3 = Game(name='Fortnite', url='https://example.com/fortnite', author='Epic Games', published_date=datetime.strptime('2022-03-01 12:00:00', '%Y-%m-%d %H:%M:%S'))

        db.session.add_all([game1, game2, game3])
        db.session.commit()
