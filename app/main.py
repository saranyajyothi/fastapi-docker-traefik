from fastapi import FastAPI,Form,Depends,HTTPException

from app.db import database, User


app = FastAPI(title="FastAPI, Docker, and Traefik")

users = {"username":"password"}
class Token:
    def __init__(self,access_token):
        self.access_token = access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

@app.post("/token",response_model = Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password - form_data.password

    if users.get(username) == password:
        return Token(access_token = username)
    else:
        raise HTTPException(status_code=400,details = "Incorrect username or password")
                                 

@app.get("/")
async def read_root(token:str = Depends(oauth2_scheme)):
    return "Welcome to the protected page"


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
        
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
