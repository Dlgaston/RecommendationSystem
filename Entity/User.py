
class User:
    def __init__(self):
        self.fName = ""
        self.lName = ""
        self.country= ""
        self.favoriteGenres = {}
        self.movieAndRating = {}
        self.recommendedMovies={}
        self.removedMovies=[]

    def getFname(self):
        return self.fName
    def setFname(self, fName):
        self.fName = fName
    def getLname(self):
        return self.lName
    def setLname(self, lName):
        self.lName = lName
    def getCountry(self):
        return self.country
    def setCountry(self, country):
        self.country = country

    def getfavoriteGenres(self):
        return self.favoriteGenres
    def setfavoriteGenres(self, favoriteGenres:dict):
        self.favoriteGenres = favoriteGenres
    def getmovieAndRating(self):
        return self.movieAndRating
    def setmovieAndRating(self, movieAndRating:dict):
        self.movieAndRating = movieAndRating
    def getrecommendedMovies(self):
        return self.recommendedMovies
    def setrecommendedMovies(self, recommendedMovies:list):
        self.recommendedMovies = recommendedMovies
    def getRemovedMovies(self):
        return self.removedMovies
    def setRemovedMovies(self,m:[]):
        self.removedMovies = m

    def printTop10RecommendedMovies(self):
        recommendedMovies = [movie for genre_movies in self.getrecommendedMovies().values() for movie in genre_movies]

        sorted_movies = sorted(recommendedMovies, key=lambda movie: movie.getUserWeight(), reverse=True)


        # Step 3: Select the top ten movies
        top_ten_movies = sorted_movies[:10]
        listPrintOut=""
        for movie in top_ten_movies:
            listPrintOut += f"Title: {movie.getTitle()}\n\tRating: {movie.getRating()}, userWeight: {movie.getUserWeight()}\n\tGenre: {movie.getGenre()}\n"

        return listPrintOut

    def printTopTenByGenre(self):
        listPrintOut=""
        for genre,movies in self.getrecommendedMovies().items():
            listPrintOut += f"YOUR RECOMMENDED MOVIES IN: {genre}\n"
            for i in range(10):
                listPrintOut += f"{i+1}: {movies[i].getTitle()} ({movies[i].getRating()})\t"
            listPrintOut+= "\n"
        return listPrintOut
    def __str__(self):
        moviePrintOut=""
        for key, value in self.movieAndRating.items():
            moviePrintOut+=f"{key}: "
            for movie in value:
                moviePrintOut+=f"{movie.title}, "
            moviePrintOut+="\n"
        printStatement = (f"FirstName: {self.fName}\nLastName: {self.lName}\nFav Genre: {self.favoriteGenres.__str__()}\n"
                          f"Movies and ratings: {moviePrintOut}")

        return printStatement