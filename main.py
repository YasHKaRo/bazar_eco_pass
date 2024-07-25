import random
import time

from fastapi import FastAPI, Body, Depends
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from contextlib import asynccontextmanager

import crypto
import database


@asynccontextmanager
async def start(app: FastAPI):
    await database.delete_tables()
    await database.create_tables()
    yield
    print("ЗАКРЫВАЕМСЯ")


app = FastAPI(lifespan=start)


@app.get("/")
def root():
    return FileResponse("bazar.html")


actual_id = {
    "basic": 0,
    "cool": 0,
    "weekend": 0,
    "special": 0
}


@app.post("/pass_system")
async def pass_answer(data: dict = Body(), db: Session = Depends(database.get_db)):
    password = crypto.caesar_cipher_encrypt(data["password"], crypto.crypt_word_numb)
    date = time.time()
    rating = data["rating"]
    new_password = database.TaskOrm(password=password, date=date, rating=rating)
    db.flush()
    actual_id[rating] = new_password.id
    db.add(new_password)
    await db.commit()
    await db.close()
    return {"password": crypto.caesar_cipher_deencrypt(password, -crypto.crypt_word_numb)}

@app.post("/random")
async def random_pass(data: dict = Body()):
    flag = data["react"]
    if flag:
        file = open("filter_crypto_russian.txt", "r", encoding="utf-8")
        word_list = file.readlines()
        password = crypto.caesar_cipher_deencrypt(word_list[random.randint(0, len(word_list))], -crypto.crypt_word_numb)
        file.close()
        return {"password": password}
# Пока не реализованно, да и нах надо, тоже пока что хз
@app.get("/get_passwords")
async def get_passwords(db: Session = Depends(database.get_db)):
    passwords = db.query(database.TaskOrm).all()
    password_list = [{"password": crypto.caesar_cipher_deencrypt(password.password, -crypto.crypt_word_numb)} for password in passwords[0:10]]
    return {"password_list": password_list}
