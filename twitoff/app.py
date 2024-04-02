from flask import Flask, render_template
from .models import DB, User, Tweet

# so we can export the whole inner folder
def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():

        # resetting the database
        DB.drop_all()
        DB.create_all()

        # Create some fake tweets and users
        ryan = User(id=1, username='ryanallred')
        julian = User(id=2, username='julian')

        tweet1 = Tweet(id=1, text='this is ryan\'s tweet', user=ryan)
        tweet2 = Tweet(id=2, text='this is Julian\'s tweet', user=julian)

        DB.session.add(ryan)
        DB.session.add(julian)
        DB.session.add(tweet1)
        DB.session.add(tweet2)

        DB.session.commit()

        return render_template('base.html', title='Reset')
    
    return app