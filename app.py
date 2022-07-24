from fastapi import FastAPI
from routes.user import user 
app = FastAPI()



app.include_router(user)

#uvicorn app:app --reload  (para estar atento a los cambios y recargar el servidor)