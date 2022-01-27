import requests

from programy.clients.embed.datafile import EmbeddedDataFileBot

chatbot = EmbeddedDataFileBot(files={'aiml':['chatbots_aiml']}, defaults=True)


def classify(text):
    key = "5e6e3ec0-7e8b-11ec-bad4-2b59751627e90610999c-8358-4a20-b7e4-eaac9972759d"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    
    if confidence < 75:
       print("No he entendido la pregunta. Preguntame otra cosa.")
    else:
        print(chatbot.ask_question(answerclass))

print("¡BIENVENIDO! ¿Que deporte te interesa?")

answer_question()


print(chatbot.ask_question(input('> ')))


try:
    print(chatbot.ask_question(input('> ')))
except:
    pass
