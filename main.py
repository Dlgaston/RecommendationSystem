
import random, csv
from Entity.Movie import Movie
from Entity.User import User

MOVIE_GENRE_LISTING =['Documentaries','Docuseries','Children & Family Movies',
                      'Dramas', 'Independent Movies', 'International Movies','Comedies',
                      'Thrillers', 'Romantic Movies', 'Music & Musicals', 'Horror Movies',
                      'Sci-Fi & Fantasy','Action & Adventure',
                      'Classic Movies', 'Anime Features', 'Sports Movies', 'Anime Series',
                       'Cult Movies','Faith & Spirituality',
                      'LGBTQ Movies', 'Stand-Up Comedy', 'Movies']

MOVIE_DB={}

RAND_FIRST_NAMES = [
    "Oliver", "Emma", "Liam", "Sophia", "James",
    "Isabella", "Benjamin", "Mia", "Elijah", "Charlotte",
    "Lucas", "Amelia", "Henry", "Ava", "Alexander",
    "Harper", "Sebastian", "Evelyn", "Jack", "Scarlett"
]
RAND_LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

def validateMovie(arr:[]):
    return arr[1] == "Movie" and arr[2] != ""

def loadMovieDB():
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
                newMovie.setTotalMovieWeight(randDouble)

                for genre in newMovie.getGenre().split(','):
                    genre = genre.strip()
                    if genre not in MOVIE_DB:
                        MOVIE_DB[genre] = []
                    MOVIE_DB[genre].append(newMovie)

def generateRandUser():
    person = User()
    person.setFname(RAND_FIRST_NAMES[random.randint(0, len(RAND_FIRST_NAMES)-1)])
    person.setLname(RAND_LAST_NAMES[random.randint(0, len(RAND_LAST_NAMES)-1)])
    favGenre = {}
    for i in range(5,0,-1):
        genreChoice = random.choice(MOVIE_GENRE_LISTING)
        while genreChoice in favGenre:
            genreChoice = random.choice(MOVIE_GENRE_LISTING)
        favGenre[genreChoice] =i
    person.setfavoriteGenres(favGenre)
    return person

def generateRandMovieWatched(p:User, movieDB:{}):
    moviesWatchedAndRated={5:[],4:[],3:[],2:[],1:[]}

    selectedMovies=[]
    all_movies = [movie for movies in movieDB.values() for movie in movies]
    while len(selectedMovies)<100:
        movie = random.choice(all_movies)
        randRating = random.randint(1,5)
        if movie not in selectedMovies:
            moviesWatchedAndRated[randRating].append(movie)
            selectedMovies.append(movie)
            movie.getHasWatched().append(p)
    p.setmovieAndRating(moviesWatchedAndRated)

def generateUserDatabase():
    userDatabase =[]
    for _ in range(5):
        p = generateRandUser()
        generateRandMovieWatched(p, MOVIE_DB)
        userDatabase.append(p)
    return userDatabase

#Loads and updates the total movie weight based on user reviews.
def setMovieTotalWeights(userDatabase:[User]):
    for user in userDatabase:
        for rating, movieList in user.getmovieAndRating().items():
            for genre, movies in MOVIE_DB.items():
                for m in movieList:
                    if m in movies:
                        weight = m.getTotalMovieWeight()+rating
                        m.setTotalMovieWeight(weight)

##Populates the user recommendation list, based on a multitude of factors.
## Weighted scale is based around the user's genre rating and if others have watched the movie, based on what they rated it.
def createUserRecommendation(p:User):
    for genre, movieList in MOVIE_DB.items():
        if genre in p.getfavoriteGenres().keys():
            if genre not in p.getrecommendedMovies():
                p.getrecommendedMovies()[genre]=[]
            genreWeight = p.getfavoriteGenres()[genre]
            movies = MOVIE_DB[genre]
            for movie in movies:
                if movie not in p.getrecommendedMovies():
                    movie.setUserWeight((genreWeight+movie.getRating())+movie.getTotalMovieWeight())
                    p.getrecommendedMovies()[genre].append(movie)
            # Sorts the dictionary through genre based on the weight of the user's rec system.
            p.getrecommendedMovies()[genre] = sorted(p.getrecommendedMovies()[genre],
                                                key=lambda m: m.userWeight, reverse=True)

# def updateUserRecommendation(p:User):
#     print("Would you like to update something?")
#     choice = input("R: Remove from recommendation list\nG: Change genre listings")
#
#     while choice is not 'N':
#         choice = input("Enter new option:\nR: Remove from recommendation list\nG: Change genre listings")
#         match choice:
#             case 'R':
#                 print("Here is your recommendation list, please enter a movie to remove")
#                 for i in range(len(p.getrecommendedMovies().items())-1):
#                     print(i)
#

def main():
    loadMovieDB()
    userDatabase = generateUserDatabase()
    setMovieTotalWeights(userDatabase)

    createUserRecommendation(userDatabase[0])
    print(userDatabase[0].getfavoriteGenres())
    print(userDatabase[0].printTop10RecommendedMovies())
    print(userDatabase[0].printTopTenByGenre())


if __name__ == '__main__':
    main()