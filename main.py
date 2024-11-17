
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

def genRandomGenreRating():
    favGenre = {}
    for i in range(5,0,-1):
        genreChoice = random.choice(MOVIE_GENRE_LISTING)
        while genreChoice in favGenre:
            genreChoice = random.choice(MOVIE_GENRE_LISTING)
        favGenre[genreChoice] =i
    return favGenre

def generateRandUser():
    person = User()
    person.setFname(RAND_FIRST_NAMES[random.randint(0, len(RAND_FIRST_NAMES)-1)])
    person.setLname(RAND_LAST_NAMES[random.randint(0, len(RAND_LAST_NAMES)-1)])
    person.setfavoriteGenres(genRandomGenreRating())
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
    p.setrecommendedMovies({})
    added_moves = set()
    for genre, movieList in MOVIE_DB.items():
        if genre in p.getfavoriteGenres().keys():
            if genre not in p.getrecommendedMovies():
                p.getrecommendedMovies()[genre]=[]
            genreWeight = p.getfavoriteGenres()[genre]
            movies = MOVIE_DB[genre]
            for movie in movies:
                if movie not in added_moves:
                    movie.setUserWeight((genreWeight+movie.getRating())+movie.getTotalMovieWeight())
                    p.getrecommendedMovies()[genre].append(movie)
                    added_moves.add(movie)
            # Sorts the dictionary through genre based on the weight of the user's rec system.
    for genre in p.getrecommendedMovies().keys():
        p.getrecommendedMovies()[genre] = sorted(p.getrecommendedMovies()[genre],
                                                 key=lambda m: m.userWeight, reverse=True)



def updateUserRecommendation(p:User):
    print("Would you like to update something?")
    choice = input("R: Remove from recommendation list\nG: Change favorite genre\nN: No\n").upper()

    while choice != 'N':

        match choice:
            case 'R':
                print("Here is your recommendation list by genre, please enter a genre to view:\n")
                data = p.getrecommendedMovies()
                keys = list(data.keys())
                i=1
                for key in data.keys():
                    print(f"{i}: {key}")
                    i+=1
                genreChoice = input()
                try:
                    genreChoice = int(genreChoice)-1
                    if genreChoice<0 or genreChoice>4:
                        print("invalid genre choice")
                        raise ValueError
                    print("Here are movies from genre to remove:\n")

                    genreKey = keys[genreChoice]
                    genre = data[genreKey]
                    i=1
                    for movie in genre[:10]:
                        print(f"{i}: {movie.getTitle()}: {movie.getRating()}")
                        i+=1
                    movieChoice = input("Select movie to remove\n")
                    movieIndex = int(movieChoice)-1

                    if movieIndex<0 or movieIndex>len(genre):
                        print("invalid movie index")
                        raise ValueError
                    removedMovie = genre.pop(movieIndex)
                    removedMovie.setUserWeight(removedMovie.getUserWeight()-20)
                    print(f"Movie removed: {removedMovie.getTitle()}")

                    print("Updated movie listing: ")
                    print(p.printGenreRec(genreKey))
                except ValueError:
                    print("invalid input")

            case 'G':
                print(f"Genre Rating Before: {p.getfavoriteGenres().__str__()}")
                p.setfavoriteGenres(genRandomGenreRating())

                print(f"Genre Rating After: {p.getfavoriteGenres().__str__()}")

                #Creates flattened list for looping through the recommended movie list
                oldRecList = [movie for genre_movies in p.getrecommendedMovies().values() for movie in
                                     genre_movies]
                old_sorted_movies = sorted(oldRecList, key=lambda movie: movie.getUserWeight(), reverse=True)
                oldRectDict = p.getrecommendedMovies()
                createUserRecommendation(p)
                newRecList = [movie for genre_movies in p.getrecommendedMovies().values() for movie in
                                     genre_movies]
                new_sorted_movies = sorted(newRecList, key=lambda movie: movie.getUserWeight(), reverse=True)

                print("NEW TOP TEN MOVIES:")
                for i in range(10):
                    print(f"{i+1}: Old movie: {old_sorted_movies[i].getTitle()}: {round(old_sorted_movies[i].getUserWeight(),3)}"
                          f" ----> New Movie: {new_sorted_movies[i].getTitle()}: {round(new_sorted_movies[i].getUserWeight(),3)}")
                print()
                newRecDict = p.getrecommendedMovies()

                if len(list(oldRectDict.keys()))>len(list(newRecDict.keys())):
                    p.printNewGenre(len(list(newRecDict.keys())),oldRectDict)

                else:
                    p.printNewGenre(len(list(oldRectDict.keys())), oldRectDict)
            case 'N':
                print("Goodbye")


        choice = input("Enter new option:\nR: Remove from recommendation list\nG: Change genre listings\nN: Exit").upper()


def main():
    loadMovieDB()
    userDatabase = generateUserDatabase()
    setMovieTotalWeights(userDatabase)

    createUserRecommendation(userDatabase[0])
    print(userDatabase[0].getfavoriteGenres())
    print(userDatabase[0].printTop10RecommendedMovies())
    print(userDatabase[0].printTopTenByGenre())

    updateUserRecommendation(userDatabase[0])


if __name__ == '__main__':
    main()