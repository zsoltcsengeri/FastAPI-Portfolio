from fastapi import FastAPI, Depends 
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from backend import models, database

# Create tables if they don't exist
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Pydantic model
class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    website: str | None = None
    message: str

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/contact")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    new_contact = models.Contact(**contact.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"status": "ok", "id": new_contact.id}

@app.get("/contact/{contact_id}")
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if contact:
        return {"id": contact.id, "name": contact.name, "email": contact.email}
    return {"error": "Contact not found"}, 404
