from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..models.schemas import User
from ..core.config import get_db

def get_user(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=400, detail="Invalid user")
    return current_user

def get_db_session():
    db = get_db()
    try:
        yield db
    finally:
        db.close()