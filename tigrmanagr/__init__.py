from flask import Flask, url_for, session, redirect

from authlib.integrations.flask_client import OAuth 




def create_app():
    """ special function in Flask to use the Factory pattern """
    app = Flask(__name__)
    oauth = OAuth(app)
    google = oauth.register(
        name='google',
        client_id='710545655552-8einlsio48ddlvo58984e2kqn3qvpdda.apps.googleusercontent.com',
        client_secret='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',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
        client_kwargs={'scope': 'openid profile email'},
        jwks_uri= 'https://www.googleapis.com/oauth2/v3/certs'
    )

    app.config.from_mapping(
        SECRET_KEY='THISISASECRETKEY'
    )


    from tigrmanagr.controllers import todo
    app.register_blueprint(todo.bp)

    from tigrmanagr.controllers import board
    app.register_blueprint(board.bp)

    from tigrmanagr.controllers import home
    app.register_blueprint(home.bp)

    from . import db
    db.init_app(app)  # connect the db to app to use teardown_appcontext


    @app.route('/login')
    def login():
        google = oauth.create_client('google')
        redirect_uri = url_for('authorize', _external=True)
        return google.authorize_redirect(redirect_uri)
    
    @app.route('/authorize')
    def authorize():
        google = oauth.create_client('google')
        token = google.authorize_access_token()
        resp = google.get('userinfo', token=token)
        user_info = resp.json()
        user = oauth.google.userinfo()
        session['profile'] = user_info
        session.permanent = True
        # do something here
        return redirect('/')
    
    @app.route('/logout')
    def logout():
        for key in list(session.keys()):
            session.pop(key)
        return redirect('/')

    return app

