from fastapi import FastAPI
from app.routes import email_routes, analytics_routes, response_routes
from app.database import init_db

app = FastAPI(title="AI Communication Assistant")

# Routers
app.include_router(email_routes.router, prefix="/emails", tags=["emails"])
app.include_router(analytics_routes.router, prefix="/analytics", tags=["analytics"])
app.include_router(response_routes.router, prefix="/responses", tags=["responses"])

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
def root():
    return {"message": "AI-Powered Communication Assistant API running!"}
