from flask import Flask
# from flask_login import LoginManager, login_manager
# from flask_login.utils import login_required
app = Flask(__name__)
# from auth import user 
def create_app():
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    
    from .views import views
    from .auth import auth
    from .add import add
    from .search import search
    
    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     print("what this")
    #     # return user.query.get(int(id))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(add, url_prefix='/')
    app.register_blueprint(search, url_prefix='/')
    
    return app
    