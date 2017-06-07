import webbrowser

# Constructor that creates the instance variables that will
# later be invoke when building each instance and passing through
# open_movies_page.


class Movie():
    # This function creates space in memory that will be
    # used for instance variables
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Allows for later use to open movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
