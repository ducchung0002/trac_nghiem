import fastapi.middleware.cors
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from Router.auth_router import auth_router
from Router.teacher_router import teacher_router
from Router.student_router import student_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="Static"), name="static")

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["http://localhost:4444"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(teacher_router)
app.include_router(student_router)

import logging
logging.getLogger('passlib').setLevel(logging.ERROR)

# hypercorn main:app --worker-class trio --workers 4 --bind localhost:4444