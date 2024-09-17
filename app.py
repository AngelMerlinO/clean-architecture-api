from flask import Flask
from controllers.user_controller import user_blueprint
from controllers.store_controller import store_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/api/v1')
app.register_blueprint(store_blueprint, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
