from fastapi import FastAPI
from app.routes import auth_routes, member_routes, scholarship_routes, payment_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(member_routes.router)
app.include_router(scholarship_routes.router)
app.include_router(payment_routes.router)

@app.get("/")
def home():
    return {"message": "ScholarEase API running"}