from flask import Flask, render_template, request
import tmbd_client
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    movies = tmbd_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list)

@app.route('/pop_movie', methods=["GET"])
def get_popular_movie(movie):
    movies = tmbd_client.get_popular_movies(how_many=8 )
    movie = movies.get(movie)
    return render_template("homepage.html", movies=movies)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmbd_client.get_single_movie(movie_id)
    cast = tmbd_client.get_single_movie_cast(movie_id)
    movie_images = tmbd_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)

@app.context_processor
def utility_processor():
    def tmbd_image_url(path, size):
        return tmbd_client.get_poster_url(path, size)
    return {"tmbd_image_url": tmbd_image_url}

if __name__ == "__main__":
    app.run(debug=True)