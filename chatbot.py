import random

def responseAudioMessage(message):
    responseMessage = {
        "text":"",
        "received":True,
        "audio":message,
        "image":"",
    }
    return responseMessage

def responseTextMessage(message):
    responseMessage = {
        "text":message,
        "received":True,
        "audio":"",
        "image":"",
    }
    return responseMessage

def responseImageMessage(message):
    responseMessage = {
        "text":"",
        "received":True,
        "audio":"",
        "image": message,
    }
    return responseMessage

def cavaloMessage():
    number = random.randint(0,9)
    if number < 5:
        return responseAudioMessage('https://www.myinstants.com/media/sounds/cavalo.mp3')
    else:
        return responseImageMessage('https://c.tenor.com/ZSrJrkIg5gcAAAAC/horse-cavalo.gif')

def fallbackMessage():
    number = random.randint(0,9)
    if number < 5:
        responseAudioMessage('https://www.myinstants.com/media/sounds/eu-nao-entendi-o-que-ele-falou_1.mp3')
    else:
        return responseTextMessage('Desculpe, eu não entendi ')

def greetingMessage():
    number = random.randint(0,9)
    if number < 5:
        return responseTextMessage('Eae')
    else:
        return responseTextMessage('Oiiii')

def rapaizMessage():
    return responseAudioMessage('https://www.myinstants.com/media/sounds/vinheta-xaropinho-rapaz-cut-mp3.mp3')

def cazeMessage():
    number = random.randint(0,3)
    if number < 3:
        return responseImageMessage('https://c.tenor.com/_0TzMJZezjkAAAAd/caze-dan%C3%A7ando-caze.gif')
    elif number > 3 and number <= 6:
        return responseImageMessage('https://pbs.twimg.com/media/E_LizpjXIAAirGr.jpg')
    else :
        return responseAudioMessage('https://www.myinstants.com/media/sounds/aceitas-pix-casimiro.mp3')

def rodrigoFaroMessage():
    number = random.randint(0,15)
    if number <= 4:
        return responseAudioMessage('https://www.myinstants.com/media/sounds/tmpd9mca4be.mp3')
    elif number > 4 and number <= 7:
        return responseAudioMessage('https://www.myinstants.com/media/sounds/ui-rodrigo-faro.mp3')
    elif number > 7 and number <= 11:
        return responseAudioMessage('https://www.myinstants.com/media/sounds/esqueca-tudo-rodrigo-faro.mp3')
    else :
        return responseAudioMessage('https://www.myinstants.com/media/sounds/chega-rodrigo-faro.mp3')

def calmaMessage():
    return responseAudioMessage('https://www.myinstants.com/media/sounds/que-e-isso-meu-filho-calma.mp3')

def pareMessage():
    return responseAudioMessage('https://www.myinstants.com/media/sounds/pare.mp3')

def ratinhoVinhetaMessage():
    return responseAudioMessage('https://www.myinstants.com/media/sounds/ratinhooo_1.mp3')

def tchauMessage():
    return responseAudioMessage('https://www.myinstants.com/media/tchau-pessoal-ate-a-proxima/')

cavaloList = ['CAVALO', 'cavalo', 'Cavalo']
greetingList = ['oi','olá', 'eae']
rapazList = ['rapaiz', 'rapaz', 'Rapaz']
cazeList = ['caze', 'vasco', 'casimiro']
calmaList = ['calma', 'nervoso']
ratinhoList = ['ratinho', 'vinheta']
rodrigoFaroList = ['ui', 'ele gosta', 'vai dar namoro', 'rodrigo', 'faro']
pareList = ['pare', 'para','parar','chega']
tchauList = ['tchau', 'xau', 'até mais', 'flw']

def verifyIntent(message, wordList):
    for word in wordList:
        print(word)
        if message.find(word) != -1:
            print('deu match')
            return True
    return False

def buildResponseMessage(message):
    if verifyIntent(message, cavaloList):
        return cavaloMessage()
    elif verifyIntent(message, greetingList):
        return greetingMessage()
    elif verifyIntent(message, rapazList):
        return rapaizMessage()
    elif verifyIntent(message, cazeList):
        return cazeMessage()    
    elif verifyIntent(message, calmaList):
        return calmaMessage()
    elif verifyIntent(message, ratinhoList):
        return ratinhoVinhetaMessage()
    elif verifyIntent(message, rodrigoFaroList):
        return rodrigoFaroMessage()   
    elif verifyIntent(message, pareList):
        return pareMessage()   
    elif verifyIntent(message, tchauList):
        return tchauMessage()  
    else:
        return fallbackMessage()

    