'''
from imdb import IMDb

ia = IMDb()

movie_name = input("Enter the movie name: ") 
movies =ia.search_movie(movie_name)

if movies:
    movie = movies [0]

    ia.update(movie)

    directors = movie.get('directors')

    if directors:

        print("Director(s):") 
        for director in directors:
             print(director['name'])

    else: 
        print("No director information found.")

else: 
        print("Movie not found.")

'''

        """
        imdbpy is library
        **To work with IMDb data in Python, you can use the IMDbPY library. 
        It allows you to access data from the IMDb movie database.
        pip install IMDbpy --upgrade
        Here are some useful methods you can use with the IMDb class:

Search for Movies: ia.search_movie('movie name')
Get Movie Information: ia.get_movie(movie_id) where movie_id is the unique identifier for the movie.
Get People (e.g., actors, directors): ia.get_person(person_id)
Get Top Movies: ia.get_top250_movies()



        """