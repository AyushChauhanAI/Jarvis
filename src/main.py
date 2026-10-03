import uvicorn
from fastapi import FastAPI
from router.conservation import router


app = FastAPI()


app.include_router(router,
    prefix="/conversation",
    tags=["Conversation"]
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)