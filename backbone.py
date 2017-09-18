import fresh_tomatoes
import movie

# Drive
drive = movie.Movie("Drive",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Drive2011Poster.jpg",
                        "https://www.youtube.com/watch?v=CWX34ShfcsE")

# Battleship
battleship = movie.Movie("Battleship",
                     "https://upload.wikimedia.org/wikipedia/en/6/6e/Battleship_Poster.jpg",
                     "https://www.youtube.com/watch?v=qcmYSxnYZV4")

# The Matrix
the_matrix = movie.Movie("The Matrix",
                             "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                             "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# List of movies
movies = [drive, battleship, the_matrix]


# This function call opens a page of movies
# generated from the input, a list of movie instances.

fresh_tomatoes.open_movies_page(movies)
