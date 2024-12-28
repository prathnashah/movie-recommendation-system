import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8afb8ecfa3f62dd9a3d2a79b5e5bab5d&append_to_response=videos'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommended_movies = []
        recommended_movies_posters =[]
        for i in distances:
            movie_id = movies.iloc[i[0]].movie_id
            #fetch api for posters
        for i in distances[1:6]:
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
        return recommended_movies, recommended_movies_posters
    except IndexError:
        print("Movie not found. Please check the title.")

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies Recommendation System')
selected_movie_name = st.selectbox('Movies?', movies['title'].values)

if st.button('Recommend') :
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0], use_column_width=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 16px;'>{names[0]}</p>", unsafe_allow_html=True)
    with col2:
        st.image(posters[1], use_column_width=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 16px;'>{names[1]}</p>", unsafe_allow_html=True)
    with col3:
        st.image(posters[2],use_column_width=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 16px;'>{names[2]}</p>", unsafe_allow_html=True)
    with col4:
        st.image(posters[3], use_column_width=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 16px;'>{names[3]}</p>", unsafe_allow_html=True)
    with col5:
        st.image(posters[4], use_column_width=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 16px;'>{names[4]}</p>", unsafe_allow_html=True)


