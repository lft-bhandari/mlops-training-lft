from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


from sqlalchemy.orm import Session
from database.db import SessionLocal, engine
from schemas import models, schema

app = FastAPI()

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok"}

models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.UserTaskResponse)
def create_user_task(user: schema.UserTaskCreate, db: Session = Depends(get_db)):
    db_user = models.UserTask(
        username=user.username,
        designation=user.designation,
        tasks=user.tasks
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.UserTask).all()
