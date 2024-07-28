from fastapi import APIRouter, HTTPException
from .schemas import UserCreate, UserLogin
from .service import create_user, login_user, get_user, logout_user

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate):
    try:
        new_user = await create_user(user.email, user.password)
        return {"message": "User created successfully", "user": new_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(user: UserLogin):
    try:
        logged_in_user = await login_user(user.email, user.password)
        return {"message": "User logged in successfully", "user": logged_in_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/me")
async def get_current_user():
    try:
        current_user = await get_user()
        return {"user": current_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/logout")
async def logout():
    try:
        await logout_user()
        return {"message": "User logged out successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))