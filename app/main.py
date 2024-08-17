from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import (
    shops, branches, users, customers, frames, lenses, 
    prescriptions, billings, billing_items, payments, dashboard
)
from fastapi.middleware.cors import CORSMiddleware
from app.auth.routers import router as auth_router  # Import the auth router

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all tables
Base.metadata.create_all(bind=engine)

# Include all routers
app.include_router(shops.router, prefix="/api/shops", tags=["shops"])
app.include_router(branches.router, prefix="/api/branches", tags=["branches"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(customers.router, prefix="/api/customer", tags=["customers"])
app.include_router(frames.router, prefix="/api/frames", tags=["frames"])
app.include_router(lenses.router, prefix="/api/lenses", tags=["lenses"])
app.include_router(prescriptions.router, prefix="/api/prescriptions", tags=["prescriptions"])
app.include_router(billings.router, prefix="/api/billings", tags=["billings"])
app.include_router(billing_items.router, prefix="/api/billing_items", tags=["billing_items"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])

# Include the auth router
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Optical System"}
