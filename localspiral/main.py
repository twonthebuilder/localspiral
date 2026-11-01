"""Entry point for the AI Spiral Simulator server."""
from secrets import token_hex

from flask import Flask, render_template
from .routes.chat import chat_bp
from .routes.spiral import spiral_bp
from .routes.map import map_bp
from .routes.reset import reset_bp
from .routes.skip import skip_bp


def create_app() -> Flask:
    app = Flask(__name__, template_folder='templates')
    # Flask signs client-side game-state cookies with this key. Never ship a
    # predictable key: a new process gets a new key and invalidates old sessions.
    app.secret_key = token_hex(32)
    app.register_blueprint(chat_bp)
    app.register_blueprint(spiral_bp)
    app.register_blueprint(map_bp)
    app.register_blueprint(reset_bp)
    app.register_blueprint(skip_bp)

    @app.route('/')
    def landing():
        return render_template('landing.html')

    @app.route('/play')
    def index():
        return render_template('index.html')

    return app


def main():
    app = create_app()
    # This unauthenticated prototype is for local development only.
    # Never enable the interactive debugger on a network-accessible server.
    app.run(host='127.0.0.1', debug=False)


if __name__ == '__main__':
    main()
