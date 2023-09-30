from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from connection import Base,engine

#import openai
from data1 import data
from connection import ScholarShips

from connection import  Session, engine
from operations import add_Data

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import and_

local_session = Session(bind=engine)
class ChatRequest(BaseModel):
    message: str
#add_Data()
    
Base.metadata.create_all(engine)

#openai.api_key = "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"
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def display():
    return {"Conclusion": "My First Hackathon"}

@app.post("/search",response_class=HTMLResponse)
def searchedData(request:Request,location_search: str = Form(), funds_search: str = Form(), degree_search: str = Form()):
    print(funds_search,degree_search)
    data = local_session.query(ScholarShips).filter(and_(ScholarShips.location==location_search,ScholarShips.degrees.like(f"%{degree_search}%"),ScholarShips.funds.like(f"%{funds_search}%"))).all()
    if data == []:
        data = local_session.query(ScholarShips).filter(and_(ScholarShips.location==location_search,ScholarShips.degrees.like(f"%{degree_search}%"))).all()

    print("data\n\n")
    return templates.TemplateResponse("demo.html",{"request":request,"data":data})



@app.get("/searchPage",response_class=HTMLResponse)
def displaySearchPage(request:Request):
    return templates.TemplateResponse("demo.html",{"request":request})




# @app.get("/demo")
# def display_pg(request:Request):
#     return templates.TemplateResponse("demo.html",{"request":request})


@app.get("/contactus")
def contact(request:Request):
    return templates.TemplateResponse("contact.html",{"request":request})
