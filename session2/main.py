from flask import Flask
from routes.route import routes
from routes.route_error import error_handler

app = Flask(__name__)

routes(app)
error_handler(app)

if __name__ == '__main__':
    app.run()