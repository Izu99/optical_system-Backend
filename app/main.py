from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routers import shops, branches, users, customers, frames, lenses, prescriptions, billings, billing_items, payments

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

app.include_router(shops.router, prefix="/shops", tags=["shops"])
app.include_router(branches.router, prefix="/branches", tags=["branches"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(customers.router, prefix="/customer", tags=["customers"])
app.include_router(frames.router, prefix="/frames", tags=["frames"])
app.include_router(lenses.router, prefix="/lenses", tags=["lenses"])
app.include_router(prescriptions.router, prefix="/prescriptions", tags=["prescriptions"])
app.include_router(billings.router, prefix="/billings", tags=["billings"])
app.include_router(billing_items.router, prefix="/billing_items", tags=["billing_items"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])

