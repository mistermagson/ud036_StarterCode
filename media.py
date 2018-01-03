import webbrowser


class Movie():

    """Class stores the structure of the movies

    Attributes:
       movie_title (string): The title of the movie

       movie_storyline (string): a short description of the movie

       poster_image (string): a link to a image with the poster

       trailer_youtube(string): a link to youtube with the trailer
    """


def __init__(self, movie_title, movie_storyline, poster_image,
             trailer_youtube):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
    """It shows the trailer of the movie on Youtube"""
    webbrowser.open(self.trailer_youtube_url)
