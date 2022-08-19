from urllib import response
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import chatbot as chatbot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

messages = [
    {
        "text":"Lorem Ipsum is simply dummy text of the printing and " +
        "typesetting industry. Lorem Ipsum has been the industry's standard dummy"+
        " text ever since the 1500s, when an unknown printer took a galley of type" +
        "and scrambled it to make a type specimen book. It has survived not only" +
        "five centuries, but also the leap into electronic typesetting, remaining" +
        "essentially unchanged.",
        "received":True,
        "audio":"",
        "image":""
    },
     {
        "text":'Texto de exemplo',
        "received":True,
        "audio":'',
        "image":''
    },
    {
        "text":'Olá xaropinho, como você está? Manda o audio do CAVALO!',
        "received":False,
        "audio":'',
        "image":''
    },
    {
        "text":'',
        "received":True,
        "audio":'https://www.myinstants.com/media/sounds/cavalo.mp3',
        "image":''
    },
    {
        "text":'CAVALO!',
        "received":True,
        "audio":'',
        "image":'https://c.tenor.com/ZSrJrkIg5gcAAAAC/horse-cavalo.gif'
    }
   
]

class SendedMessage(BaseModel):
    text: str

@app.get("/api/messages")
async def getMessages():
    return {"data": messages}


def buildResponseMessage():
    responseMessage = {
        "text":"teste de resposta",
        "received":True,
        "audio":"",
        "image":"",
    }
    return responseMessage

@app.post("/api/messages/send")
async def sendMessage(sendedMessage: SendedMessage):
    return {"data" : chatbot.buildResponseMessage(sendedMessage.text)} 

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")