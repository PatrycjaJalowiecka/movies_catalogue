from flask import Flask, render_template, request
import tmbd_client

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmbd_client.get_popular_movies()["results"][:8]
    return render_template("homepage.html", movies=movies)

@app.route('/pop_movie', methods=["GET"])
def get_popular_movie(movie):
    movies = tmbd_client.get_popular_movies()["results"][:8]
    movie = movies.get(movie)
    return render_template("homepage.html", movies=movies)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    return render_template("movie_details.html")

@app.context_processor
def utility_processor():
    def tmbd_image_url(path, size):
        return tmbd_client.get_poster_url(path, size)
    return {"tmbd_image_url": tmbd_image_url}

if __name__ == "__main__":
    app.run(debug=True)