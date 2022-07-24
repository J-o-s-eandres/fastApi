from fastapi import FastAPI
from routes.user import user 
app = FastAPI(
    title="REST API with FastAPI and MongoDB",
    description="This is a simple REST API using fastapi and mongodb ",
    version="0.0.1"
)




app.include_router(user)

#uvicorn app:app --reload  (para estar atento a los cambios y recargar el servidor)