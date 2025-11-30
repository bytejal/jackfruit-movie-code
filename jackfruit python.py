import requests
def get_movie(movie):
    url = f"http://www.omdbapi.com/?t={movie}&apikey=thewdb"
    data = requests.get(url).json()

    if data["Response"] == "True":
        print("Title:", data["Title"])
        print("Year:", data["Year"])
        print("Rating:", data["imdbRating"])
        print("Actors:", data["Actors"])
        print("Plot:", data["Plot"])
    else:
        print("content not found!")

name = input("Movie/documentary/series name: ")
get_movie(name)
