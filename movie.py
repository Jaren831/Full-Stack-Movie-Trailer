import webbrowser

class Movie():
    """Thia class constructs movie objects with movie title, movie poster, and youtube trailer. Takes array of strings as input."""
    
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        """
        movie_title(str): Title of movie
        poster_image_url(str): Url for movieposter image.
        trailer_youtube_url(str): Url for movie youtube trailer.

        """
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
