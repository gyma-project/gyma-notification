from typing import Union
from pydantic import BaseModel

class MessageDTO(BaseModel):
    receiverEmail: str
    title: str
    description: str