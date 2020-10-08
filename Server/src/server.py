from flask import Flask

from argparse import ArgumentParser
from routes import api_bp

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=9000)

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix="/api")


    app.run(host=args.host, port=args.port, debug=True)
