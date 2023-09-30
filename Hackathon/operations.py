from connection import engine

from data1 import data

from connection import ScholarShips, Session, engine
local_session = Session(bind=engine)


def add_Data():
    a = 1
    for i in data :
        scholarship_data = ScholarShips(name = i.get("name",None),degrees = i.get("degrees", "None"), funds= i.get("funds"), date = i.get("date",None), location = i.get("location","not specified") )
        local_session.add(scholarship_data)
        local_session.commit()
        print("\n\nDATA ADDED :",a)
        a = a+1