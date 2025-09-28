from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from . import models, database, schemas

# Create DB Tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

#Pydentic schema for user input validation
class ContactCreate(BaseModel):
    name  : str
    email : EmailStr
    phone: str | None = None
    website: str | None = None
    message: str

    #Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/contact")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    new_contact = models.Contact(
        name=contact.name,
        email=contact.email,
        phone=contact.phone,
        website=contact.website,
        message=contact.message,
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"message": "Contact information submitted successfully", "contact_id": new_contact.id} 
# Endpoint to retrieve all contacts
@app.get("/contacts", response_model=list[schemas.Contact])
def get_contacts(db: Session = Depends(get_db)):
    contacts = db.query(models.Contact).all()
    return contacts # Return list of contacts
# Endpoint to retrieve a specific contact by ID
@app.get("/contacts/{contact_id}", response_model=schemas.Contact)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact # Return the contact details
# Endpoint to delete a contact by ID
@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return {"message": "Contact deleted successfully"}  # Return success message
# Endpoint to update a contact by ID
@app.put("/contacts/{contact_id}", response_model=schemas.Contact) 
def update_contact(contact_id: int, updated_contact: ContactCreate, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    contact.name = updated_contact.name
    contact.email = updated_contact.email
    contact.phone = updated_contact.phone
    contact.website = updated_contact.website
    contact.message = updated_contact.message
    
    db.commit()
    db.refresh(contact)
    return contact  # Return the updated contact details    
# Endpoint to check API status
# @app.get("/")
# def read_root():
#    return {"message": "API is running"}   
# Run the app with: uvicorn backend.main:app --reload
# Access the API at: http://
# localhost:8000
# Access the interactive API docs at: http://localhost:8000/docs
# Access the alternative API docs at: http://localhost:8000/redoc
# Make sure to have PostgreSQL running and the database configured in database.py
# Install dependencies from requirements.txt
# pip install -r requirements.txt
# This is a basic implementation. You can expand it with more features as needed.
# Remember to handle exceptions and edge cases in a production environment.
# Access the interactive API docs at: http://localhost:8000/docs