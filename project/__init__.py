from flask import Flask
app = Flask(__name__)
# from auth import user 
def create_app():
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    
    from .views import views
    from .auth import auth
    from .add import add
    from .search import search
    from .drop import drop
    from .admin import admin
    from .entry import entryb

  
    from .swap_home import swap_home
    from .swap_add import swap_add
    from .swap_view import swap_view
    from .swap_search import swap_search

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(add, url_prefix='/')
    app.register_blueprint(search, url_prefix='/')
    app.register_blueprint(drop, url_prefix='/')
    app.register_blueprint(swap_home, url_prefix='/')
    app.register_blueprint(swap_add, url_prefix='/')
    app.register_blueprint(swap_view, url_prefix='/')
    app.register_blueprint(swap_search, url_prefix='/')
    app.register_blueprint(entryb, url_prefix='/')

    
    return app
    
