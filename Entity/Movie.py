
from Entity.User import User


class Movie:

    def __init__(self):
        self.title = ""
        self.author = ""
        self.genre = []
        self.country = []
        self.hasWatched = []
        self.rating= 0
        self.totalMovieWeight=0
        self.userWeight =0

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title
    def getAuthor(self):
        return self.author
    def setAuthor(self, author):
        self.author = author
    def getGenre(self):
        return self.genre
    def setGenre(self, genre):
        self.genre = genre
    def getCountry(self):
        return self.country
    def setCountry(self, country):
        self.country = country
    def getHasWatched(self):
        return self.hasWatched
    def setHasWatched(self, hasWatched):
        self.hasWatched = hasWatched
    def getTotalMovieWeight(self):
        return self.totalMovieWeight
    def setTotalMovieWeight(self, totalMovieWeight):
        self.totalMovieWeight = totalMovieWeight
    def getRating(self):
        return self.rating
    def setRating(self, rating):
        self.rating = rating
    def getUserWeight(self):
        return self.userWeight
    def setUserWeight(self, userWeight):
        self.userWeight = userWeight

    def __str__(self):
        return "Title: " + self.title + " Author: "+ self.author  + " Rating: " + self.rating.__str__() +" Movie Weight: "+ self.totalMovieWeight.__str__() + " User Weight: "+ self.userWeight.__str__() +  " Genre: " + self.genre.__str__() + " Country: " + self.country.__str__()




