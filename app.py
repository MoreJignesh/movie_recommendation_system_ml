# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

app = Flask(__name__)

# Load movie dictionary
movies_dict = pickle.load(open('notebook/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# OPTIONAL: Load similarity matrix if you have it
similarity = pickle.load(open('notebook/similarity.pkl', 'rb'))

# Fetch poster from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Recommendation logic
def recommend(movie_name):
    try:
        movie_index = movies[movies['title'] == movie_name].index[0]

        distances = similarity[movie_index]

        movies_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        recommended_movies = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id

            recommended_movies.append({
                "title": movies.iloc[i[0]].title,
                "poster_path": fetch_poster(movie_id)
            })

        return recommended_movies   # ✅ return AFTER loop

    except Exception as e:
        print("Error:", e)
        return []


@app.route('/')
def home():
    movie_titles = movies['title'].values
    return render_template('index.html', movie_list=movie_titles)


@app.route('/recommend', methods=['POST'])
def recommend_api():
    movie_name = request.form.get('movie')
    recommendations = recommend(movie_name)
    
    return render_template('index.html',
                           movie_list=movies['title'].values,
                           recommendations=recommendations)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
# https://api.themoviedb.org/3/account/{account_id}/watchlist/movies


# app.py

# from flask import Flask, request, jsonify, render_template
# import pickle
# import pandas as pd

# app = Flask(__name__)

# # Load movie dictionary
# movies_dict = pickle.load(open('notebook\movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)

# # Load similarity matrix
# similarity = pickle.load(open('notebook\similarity.pkl', 'rb'))


# # Recommendation Function
# def recommend(movie_name):
#     try:
#         # Get index of selected movie
#         movie_index = movies[movies['title'] == movie_name].index[0]

#         # Get similarity scores
#         distances = similarity[movie_index]

#         # Sort movies based on similarity score
#         movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]  
#         # top 5 similar movies (excluding itself)

#         recommended_movies = []

#         for i in movies_list:
#             recommended_movies.append({"title": movies.iloc[i[0]].title})
#         return recommended_movies

#     except IndexError:
#         return []


# @app.route('/')
# def home():
#     movie_titles = movies['title'].values
#     return render_template('index.html', movie_list=movie_titles)


# @app.route('/recommend', methods=['POST'])
# def recommend_api():
#     movie_name = request.json['movie']
#     recommendations = recommend(movie_name)
#     return recommendations


# if __name__ == "__main__":
#     app.run(debug=True)

