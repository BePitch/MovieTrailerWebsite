import fresh_tomatoes
import media

# Movie #1
toy_story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wiki"
                        "pedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4"
                        )
# Movie #2
avatar = media.Movie("Avatar",
                     "a marine on a planet fighting for resources",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0"
                     "/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     )
# Movie #3
harry_potter = media.Movie("Harry Potter and the Deathly"
                           "Hallows Part 2",
                           "Fantasy movie that takes place in"
                           "the real world about a group of kids",
                           "https://upload.wikimedia.org/wikipedia/en/d/df/"
                           "Harry_Potter_and_the_Deathly_Hallows_%E2"
                           "%80%93_Part_2.jpg",
                           "https://www.youtube.com/watch?v=9hXH0Ackz6w"
                           )
# Movie #4
step_brothers = media.Movie("Step Brothers",
                            "a comedy about the most amazing"
                            "friendship that would spawn out"
                            "of the most uncertain circumstances.",
                            "https://upload.wikimedia.org/wikipedia/en"
                            "/d/d9/StepbrothersMP08.jpg",
                            "https://youtu.be/CewglxElBK0"
                            )
# Data Structure
movies = [toy_story, avatar, harry_potter, step_brothers]

# Build the Website and pass through each movie
fresh_tomatoes.open_movies_page(movies)
