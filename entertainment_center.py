import fresh_tomatoes
import media


pulp_fiction = media.Movie("Pulp Fiction",
                     "An history about violence",
                     "https://upload.wikimedia.org/wikipedia/pt/8/82/Pulp_Fiction_cover.jpg",
                     "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

matrix = media.Movie("Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality.",
                     "https://upload.wikimedia.org/wikipedia/pt/thumb/c/c1/The_Matrix_Poster.jpg/200px-The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

star_wars = media.Movie("Star Wars",
                     "A princesa Leia é mantida refém pelas forças imperiais comandadas por Darth Vader.",
                     "https://images-na.ssl-images-amazon.com/images/I/51a222ZdtkL.jpg",
                     "https://www.youtube.com/watch?v=jVrf_bKTjo4")

shrek = media.Movie("Shrek",
                     "An Ogre fairy tale",
                     "https://images-na.ssl-images-amazon.com/images/I/41mSRxM16mL.jpg",
                     "https://www.youtube.com/watch?v=ooJJX3R42WM")

cars = media.Movie("Cars",
                     "A hot-shot race-car named Lightning McQueen gets lost",
                     "https://images-na.ssl-images-amazon.com/images/I/51YASjst5YL.jpg",
                     "https://www.youtube.com/watch?v=SbXIj2T-_uk")

django = media.Movie("Django - Unchained",
                     "The story of that yellow beings",
                     "https://upload.wikimedia.org/wikipedia/pt/8/8b/Django_Unchained_Poster.jpg",
                     "https://www.youtube.com/watch?v=eUdM9vrCbow")
movies = [pulp_fiction, matrix, star_wars, shrek, cars, django]
fresh_tomatoes.open_movies_page(movies)
