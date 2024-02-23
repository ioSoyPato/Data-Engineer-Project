from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Create a route to serve the static files
app.mount("/static", StaticFiles(directory="Playlist"), name="static")
app.mount("/static2", StaticFiles(directory="Home_Page"), name="static2")

@app.get("/")
def greeting():
    return {"message": "Hello World. Welcome to my first web app. Add /home to the URL to see the home page."}

@app.get("/home")
async def home():
    return FileResponse("Home_Page/index.html")

@app.get("/playlist/")
async def root():
    return FileResponse("Playlist/index.html")

@app.get("/user")
async def user():
    return FileResponse("Users/user.html")

