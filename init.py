import json
import fresh_tomatoes
import urllib.request
import codecs
#from urllib2 import urlopen
from movie import Movie
from tvshow import TvShow

def get_videos(path):
    videosFile = open(path)
    videos = videosFile.read()
    videosFile.close()
    videos = videos.split("\n")
    return videos

def get_movies (path):
    movies = get_videos(path);
    movieList = []
    for movie in movies:
        movie = movie.split(" - ")
        movieData = get_info(movie[0])
        newMovie = Movie(movie[0], movieData["Plot"], movieData["Poster"], movie[1])
        movieList.append(newMovie)
    return movieList

def get_tvshows (path):
    tvShows = get_videos(path)
    tvShowsList = []
    for tvShow in tvShows:
        tvShow = tvShow.split(" - ")
        tvShowData = get_info(tvShow[0])
        newTVShow = TvShow(tvShow[0], tvShowData["Plot"], tvShowData["Poster"])
        tvShowsList.append(newTVShow)
    return tvShowsList
    
def get_info(title):
    info = urllib.request.urlopen("http://www.omdbapi.com/?t=" + title.replace(" ", "+") + "&y=&plot=full&r=json")
    reader = codecs.getreader("utf-8")
    data = json.load(reader(info))
    return data


movieList = get_movies("movies.txt")
tvShowList = get_tvshows("tvshows.txt")

fresh_tomatoes.open_movies_page(movieList, tvShowList)

