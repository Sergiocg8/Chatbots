# Chatbots
Entrega ChatBots

El ChatBots consiste en contestar información deportiva.

En el primer ChatBots he utilizado la herramienta PandoraBots.
Empezamos con saludo y nos da a elegir sobre varios deporte, en donde nosotros elegimos el que más nos interese. Luego sobre el deporte
que hayamos elegido nos pregunta sobre que equipo que somos o cual es nuestro jugador favorito en el caso de que eligas el tenis y contestamos.
Lo siguiente que sucede es aportarnos cierta información, que nosotros hayamos elegido previamente, con el equipo o jugador que nosotros
hayamos elegido.

Todo está controlado con <that> por lo tanto si nosotros respondemos una respuesta en la que no tiene sentido, el bot te dará un match failed.


El segundo ChatBots he utilizado la herramienta ML4K.
Aqui simplemente empezamos ha realizar preguntas y el bot nos la va respondiendo. No es una conversación.

Para ello le hemos creado diferentes etiquetas relacionadas con la información que queremos saber. Dentro de esas etiquetas hemos puesto
diferentes formas de preguntar para obtener esa información o respuesta. Mientras más variedad de preguntas mejor. Luego en la misma página
web le hemos entrenado. Una vez entrenado la web aporta un código en donde los exportamos, en mi caso a visual studio.

Una vez en visual studio creamo una nueva funcion en donde relaciones las etiquetas creadas con sus respectivas respuestas.
Por lo tanto cuando preguntemos, esta lo va a relacionar con la etiqueta y por lo tanto con la respuesta. Y así es como obtendriamos la
información