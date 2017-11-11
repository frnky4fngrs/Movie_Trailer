import fresh_tomatoes
import media

#set up my six movie objects
secret_of_my_success = media.Movie(
    "The Secret of My Success",
    "https://upload.wikimedia.org/wikipedia/en/1/18/The_Secret_Of_My_Success.jpg",
    "https://www.youtube.com/watch?v=rGHDATIJIX8")

john_wick = media.Movie(
    "John Wick",
    "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
    "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

christmas_story = media.Movie(
    "A Christmas Story",
    "https://upload.wikimedia.org/wikipedia/en/6/65/A_Christmas_Story_film_poster.jpg",
    "https://www.youtube.com/watch?v=LBe0Bl0wYHU")

blade_runner = media.Movie(
    "Blade Runner",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
    "https://www.youtube.com/watch?v=eogpIG53Cis")

guardians_of_the_galaxy = media.Movie(
    "Guardians of the Galaxy",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
    "https://www.youtube.com/watch?v=d96cjJhvlMA")

last_starfighter = media.Movie(
    "The Last Starfighter",
    "https://upload.wikimedia.org/wikipedia/en/4/4c/Last_starfighter_post.jpg",
    "https://www.youtube.com/watch?v=H7NaxBxFWSo")

#make a list of my movies to pass to web page generator
my_movies = [john_wick, blade_runner, christmas_story,
             last_starfighter, guardians_of_the_galaxy, secret_of_my_success]

#actually generate web page
fresh_tomatoes.open_movies_page(my_movies)
