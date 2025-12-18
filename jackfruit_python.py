import wx
import requests
import webbrowser

def get_movie(event):
    movie = entry.GetValue()
    url = f"http://www.omdbapi.com/?t={movie}&apikey=thewdb"
    data = requests.get(url).json()

    if data.get("Response") == "True":
        result = (
            ".Title:- " + data["Title"] + "\n" +
            ".Year:- " + data["Year"] + "\n" +
            ".Rating:- " + data["imdbRating"] + "\n" +
            ".Actors:- " + data["Actors"] + "\n" +
            ".Plot:- " + data["Plot"]
        )
    else:
        result = "Content not found! Check your spelling."

    output.SetLabel(result)


def open_trailer(event):
    movie_name = entry.GetValue()
    if movie_name.strip() == "":
        output.SetLabel("Please enter a movie name first.")
        return

    # Open YouTube search for trailer
    query = movie_name + " official trailer"
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)


app = wx.App(False)
frame = wx.Frame(None, title="Movie/Web Series 💗 Search", size=(430, 320))

panel = wx.Panel(frame)
panel.SetBackgroundColour("brown")

italic_font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)

entry = wx.TextCtrl(panel, pos=(20, 20), size=(200, 25))
entry.SetHint("Enter movie or series name…")
entry.SetFont(italic_font)

button = wx.Button(panel, label="Search 🎀", pos=(240, 18))
button.Bind(wx.EVT_BUTTON, get_movie)

trailer_btn = wx.Button(panel, label="Watch Trailer 🎬", pos=(20, 260))
trailer_btn.Bind(wx.EVT_BUTTON, open_trailer)

output = wx.StaticText(panel, label="", pos=(20, 70), size=(380, 180))
output.SetFont(italic_font)

frame.Show()
app.MainLoop()
