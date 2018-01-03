import requests
import fresh_tomatoes
import media
import json

# API token // Obtain your at https://www.themoviedb.org/documentation/api
apitoken = 'a05f95920c53f46d7c8e672625412603'

# list with IMDb ID´s of favorite movies
imdbid = ['tt0076759','tt1853728','tt0110912','tt0133093','tt0126029','tt0317219']

#list with the results of favorite movies
movie_list = []

for i in range(0, 6):
    response = requests.get('https://api.themoviedb.org/3/movie/'+imdbid[i]
                            +'?api_key='+apitoken+'&append_to_response=videos')
    json_data = json.loads(response.text)
    #print(json_data['videos']['results'][0]['key'])
    #print(json.dumps(json_data, indent=4,sort_keys=True))
    youtube_key = json_data['videos']['results'][0]['key']
    poster_path = 'http://image.tmdb.org/t/p/w185'+ json_data['poster_path']
    movie_list.append(media.Movie(json_data['original_title'],
                     json_data['overview'],
                     poster_path,
                     'https://www.youtube.com/watch?v='+ youtube_key))

fresh_tomatoes.open_movies_page(movie_list)
