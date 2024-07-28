from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bloodcore.api.auth.router import router as auth_router
from bloodcore.api.pdf.router import router as pdf_router
from bloodcore.api.email.router import router as email_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(pdf_router, prefix="/pdf", tags=["PDF"])
app.include_router(email_router, prefix="/email", tags=["Email"])

@app.get("/test-endpoint-1")
async def test_endpoint_1():
    return {"message": "Test endpoint 1 accessed successfully"}

@app.get("/test-endpoint-1")
async def test_endpoint_2():
    return {"message": "Test endpoint 2 accessed successfully"}