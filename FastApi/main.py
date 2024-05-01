from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Create a route to serve the static files
app.mount("/static", StaticFiles(directory="Playlist"), name="static")
app.mount("/static2", StaticFiles(directory="Home_Page"), name="static2")
app.mount("/static3", StaticFiles(directory="Users"), name="static3")

def get_next_song(genre: str, current_song_id: str, current_song_genre: str):
    if current_song_genre == genre:
        return f"{genre}_song_{int(current_song_id) + 1}.mp3"
    return f"{genre}_song_1.mp3"

@app.get("/helloworld")
def greeting():
    return {"message": f"Hello World. Welcome to my first web app. Add /home to the URL to see the home page."}
    
@app.get("/home")
async def home():
    return FileResponse("Home_Page/index.html") 

@app.get("/playlist/")
async def root():
    return FileResponse("Playlist/index.html")

@app.get("/")
async def user():
    return FileResponse("Users/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4444)

