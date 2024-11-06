
import random, csv
from Entity.Movie import Movie
from Entity.User import User

MOVIE_GENRE_LISTING =['Documentaries', 'International TV Shows', 'TV Dramas',
                      'TV Mysteries', 'Crime TV Shows', 'TV Action & Adventure', 'Docuseries', 'Reality TV', 'Romantic TV Shows', 'TV Comedies', 'TV Horror', 'Children & Family Movies', 'Dramas', 'Independent Movies', 'International Movies', 'British TV Shows', 'Comedies',
                      'Spanish-Language TV Shows', 'Thrillers', 'Romantic Movies', 'Music & Musicals', 'Horror Movies', 'Sci-Fi & Fantasy', 'TV Thrillers', "Kids' TV", 'Action & Adventure', 'TV Sci-Fi & Fantasy', 'Classic Movies', 'Anime Features', 'Sports Movies', 'Anime Series', 'Korean TV Shows',
                      'Science & Nature TV', 'Teen TV Shows', 'Cult Movies', 'TV Shows', 'Faith & Spirituality', 'LGBTQ Movies', 'Stand-Up Comedy', 'Movies', 'Stand-Up Comedy & Talk Shows', 'Classic & Cult TV']


def validateMovie(arr:[]):
    return arr[1] == "Movie" and arr[2] != ""


def loadMovieDB():
    movies = []
    genreList = []
    with open("netflix_titles (1).csv", encoding="utf8", errors="ignore") as f:

        for line in f:
            input = next(csv.reader([line]))

            if validateMovie(input):
                newMovie = Movie()
                newMovie.setTitle(input[2])
                newMovie.setCountry(input[4])
                newMovie.setGenre(input[9])
                newMovie.setAuthor(input[3])

                randDouble = round(random.uniform(1, 5),1)
                newMovie.setRating(randDouble)
                newMovie.setMovieWeight(randDouble)
                movies.append(newMovie)
    return movies

def generateRandUser():
    person = User()

    person.setFname("Jackson")
    person.setLname("Montaigne")
    favGenre = {}
    for i in range(5,0,-1):
      favGenre[random.choice(MOVIE_GENRE_LISTING)] =i
    person.setfavoriteGenres(favGenre)
    return person

def generateRandMovieWatched(p:User, movieDB:[Movie]):
    moviesWatchedAndRated={}
    while len(moviesWatchedAndRated)<5:
        movieTitle = random.choice(movieDB).getTitle()
        randRating = random.randint(1,5)
        if movieTitle not in moviesWatchedAndRated:
            moviesWatchedAndRated[movieTitle] = randRating
    p.setmovieAndRating(moviesWatchedAndRated)



def main():
    movieDB = loadMovieDB()
    p = generateRandUser()
    generateRandMovieWatched(p, movieDB)
    print(p)



if __name__ == '__main__':
    main()