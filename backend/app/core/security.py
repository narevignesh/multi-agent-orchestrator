from passlib.context import CryptContext
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
import re

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def validate_input(input_string: str):
    if not re.match("^[a-zA-Z0-9_]*$", input_string):
        raise HTTPException(status_code=400, detail="Invalid input: Only alphanumeric characters and underscores are allowed.")

def get_current_user(token: str = Security(oauth2_scheme)):
    # Placeholder for token verification logic
    # This should be replaced with actual token verification and user retrieval logic
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid authentication credentials.")
    return {"username": "user"}  # Replace with actual user retrieval logic