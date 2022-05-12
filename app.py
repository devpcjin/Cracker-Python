from flask import Flask

from modules import auth, place, map, blog


app = Flask(__name__)

app.register_blueprint(auth.bp)
app.register_blueprint(place.bp)
app.register_blueprint(map.bp)
app.register_blueprint(blog.bp)



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
