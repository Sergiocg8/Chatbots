import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
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
    
    elif answerclass == "futbol":
        print("Muy buena elección. Aqui tienes un enlace con las noticias más actuales del fútbol: https://www.marca.com/futbol.html?intcmp=MENUPROD&s_kw=futbol")
        
    elif answerclass == "baloncesto":
        print("Muy buena elección. Aqui tienes un enlace con las noticias más actuales del baloncesto: https://www.marca.com/baloncesto.html?intcmp=MENUPROD&s_kw=baloncesto")
        
    elif answerclass == "tenis":
        print("Muy buena elección. Aqui tienes un enlace con las noticias más actuales del tenis: https://www.marca.com/tenis.html?intcmp=MENUMIGA&s_kw=tenis")
               

print("¡BIENVENIDO! Elige el deporte que quieras")

while True:
    answer_question()
