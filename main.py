from fastapi import FastAPI
from routers import users_db

app = FastAPI()
app.include_router(users_db.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD application!"}  
