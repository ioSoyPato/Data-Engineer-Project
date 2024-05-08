from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

# Create a route to serve the static files
app.mount("/static", StaticFiles(directory="Playlist"), name="static")
app.mount("/static2", StaticFiles(directory="Home_Page"), name="static2")
app.mount("/static3", StaticFiles(directory="Users"), name="static3")

templates = Jinja2Templates(directory="Playlist")

@app.get("/playlist/{title}/{artist}/{genre}/{id}", response_class=HTMLResponse)
async def read_item(request: Request, title: str, artist: str, genre: str, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"title": title, "artist": artist, "genre": genre, "id": id}
    )

@app.get("/playlist2/{genre}/{current_song_id}/{current_song_genre}", response_class=HTMLResponse)
async def get_next_song(request: Request, genre: str, current_song_id: str, current_song_genre: str):
    if current_song_genre == genre:
        #f"{genre}_song_{int(current_song_id) + 1}.mp3"
        title = 'Side To Side'
        artist = 'Ariana Grande'
        genre = 'rock'
        id = 'rock1'
        return templates.TemplateResponse(
        request=request, name="index.html", context={"title": title, "artist": artist, "genre": genre, "id": id}
    )
    return f"{genre}_song_1.mp3"

@app.get("/helloworld")
def greeting():
    return {"message": f"Hello World. Welcome to my first web app. Add /home to the URL to see the home page."}
    
@app.get("/home")
async def home():
    return FileResponse("Home_Page/index.html") 

@app.get("/")
async def user():
    return FileResponse("Users/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4444)

