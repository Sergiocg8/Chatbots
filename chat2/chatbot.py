import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "2f9ef200-6cbc-11ec-9893-6b6cab01fe0dbf2f3036-ae55-4075-8802-858843f2d031"
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
    
    if answerclass == "puesto_liga_betis":
        print("El Betis va el 3º en liga")
        
    elif answerclass == "prox_rival_betis":
        print("El próximo rival del Betis es el Celta de Vigo")
        
    elif answerclass == "fecha_partido_betis":
        print("La fecha del próximo partido del Betis es el 2/01/2022")
        
    elif answerclass == "puesto_liga_madrid":
        print("El Madrid va el 1º en liga")
        
    elif answerclass == "prox_rival_madrid":
        print("El próximo rival del Madrid es el Getafe")
        
    elif answerclass == "fecha_partido_madrid":
        print("La fecha del próximo partido del Madrid es el 2/01/2022")
        
    elif answerclass == "puesto_liga_barcelona":
        print("El Barcelona va el 7º en liga")
        
    elif answerclass == "prox_rival_barcelona":
        print("El próximo rival del Barcelona es el Mallorca")
        
    elif answerclass == "fecha_partido_barcelona":
        print("La fecha del próximo partido del Barcelona es el 2/01/2022")
        
    elif answerclass == "puesto_liga_at_madrid":
        print("El Atlético de Madrid va el 5º en liga")
        
    elif answerclass == "prox_rival_at_madrid":
        print("El próximo rival del Atlético de Madrid es el Rayo Vallecano")
        
    elif answerclass == "fecha_partido_at_madrid":
        print("La fecha del próximo partido del Atlético de Madrid es el 2/01/2022")
        
    elif answerclass == "puesto_nba_lakers":
        print("Los Lakers van el 9º en la NBA")
        
    elif answerclass == "prox_rival_lakers":
        print("El próximo rival de los Lakers son los Rockest")
        
    elif answerclass == "fecha_partido_lakers":
        print("La fecha del próximo partido de los Lakers es el 29/12/2021")
        
    elif answerclass == "puesto_acb_madrid":
        print("El Madrid Basket va el 1º en la ACB")
        
    elif answerclass == "prox_rival_madrid_basket":
        print("El próximo rival del Madrid Basket es el Barcelona")
        
    elif answerclass == "fecha_partido_madrid_basket":
        print("La fecha del próximo partido del Madrid Basket es el 2/01/2022")
        
    elif answerclass == "prox_campeonato_nadal":
        print("El próximo campeonato de Nadal es el Open de Australia")
        
    elif answerclass == "fecha_campeonato_nadal":
        print("La fecha del próximo campeonato es el 1/01/2022")
        
    elif answerclass == "prox_campeonato_federer":
        print("El próximo campeonato de Federer es Wimbledon")
        
    elif answerclass == "fecha_campeonato_federer":
        print("La fecha del próximo campeonato es el 10/07/2022")
        

print("¡BIENVENIDO! Realice la pregunta que quieras")

while True:
    answer_question()