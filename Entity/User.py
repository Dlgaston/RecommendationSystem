

class User:
    def __init__(self):
        self.fName = ""
        self.lName = ""
        self.country= ""
        self.favoriteGenres = {}
        self.movieAndRating = {}

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

    def __str__(self):
        return "Fname: " + self.fName + " Lname: " + self.lName + " favoriteGenres: " + self.favoriteGenres.__str__() + "movieAndRating: " + self.movieAndRating.__str__()