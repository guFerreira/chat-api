from fastapi import FastAPI
import uvicorn

app = FastAPI()

messages = [
    {
        "text":"Lorem Ipsum is simply dummy text of the printing and " +
        "typesetting industry. Lorem Ipsum has been the industry's standard dummy"+
        " text ever since the 1500s, when an unknown printer took a galley of type" +
        "and scrambled it to make a type specimen book. It has survived not only" +
        "five centuries, but also the leap into electronic typesetting, remaining" +
        "essentially unchanged.",
        "received":"true",
        "audio":"",
        "image":""
    },
     {
        "text":'Texto de exemplo',
        "received":"true",
        "audio":'',
        "image":''
    },
    {
        "text":'Olá xaropinho, como você está? Manda o audio do CAVALO!',
        "received":"false",
        "audio":'',
        "image":''
    },
    {
        "text":'',
        "received":"true",
        "audio":'https://www.myinstants.com/media/sounds/cavalo.mp3',
        "image":''
    },
    {
        "text":'CAVALO!',
        "received":"true",
        "audio":'',
        "image":'https://c.tenor.com/ZSrJrkIg5gcAAAAC/horse-cavalo.gif'
    }
   
]

@app.get("/api/messages")
async def getMessages():
    return {"data": messages}

@app.post("/api/messages/send")
async def sendMessage():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")