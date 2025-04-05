from fastapi import FastAPI
from database import connection

# ROUTES
from routes import router as routes
# ROUTES

app = FastAPI()


app.include_router(routes)
