def routes(app):
    @app.route('/')
    def hello_word():
        return 'Hola mundo !'