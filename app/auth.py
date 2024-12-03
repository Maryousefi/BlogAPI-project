from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from .routers import auth  # Import the auth router

# Create an instance of FastAPI
app = FastAPI()

# Include the auth router with the specified prefix and tags
app.include_router(auth.router, prefix="/auth", tags=["authentication"])

# this secret_key should be replaced with an actual secret_key
SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")