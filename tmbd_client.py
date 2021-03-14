import json
import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YTE0MWU4M2U5ODY5MWE5OGYxNGRhNjRkNjQ1NWY4OSIsInN1YiI6IjYwNGEwZjc4NDM5YmUxMDAyNjU3YjIwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WXhkUNFWW-yyFcI4GjaStAkDv64TQ6T8n19gA686OTQ"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

print(get_popular_movies())

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
    