from typing import Union
from services.email import send_email_to
from DTOs.MessageDTO import MessageDTO

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Serviço em execução"}


@app.post("/send-email-notification")
def send(message: MessageDTO):
    res = send_email_to(message)
    return {"enviado": message, "status": res}