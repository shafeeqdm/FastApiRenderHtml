import uvicorn 
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

templates = Jinja2Templates(directory="templates")
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

@app.post("/token")
async def token_generate(form_data : OAuth2PasswordRequestForm = Depends()):
    return {"access_token":form_data.username, "access_type" : "bearer" }

@app.get("/", response_class=HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse("index.html",{"request": request} )
    #return {"username" : username}

@app.post("/index")
async def home(token : str = Depends(oauth_scheme),username : str = Form(...), password : str = Form(...)):
    return {"username" : username , "password" : password}
