from flask import Flask

app = Flask(__name__)

def create_app():
    # app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
    