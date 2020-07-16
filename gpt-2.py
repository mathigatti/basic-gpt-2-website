from aitextgen import aitextgen
from googletrans import Translator

# Funcion que traduce un texto al idioma especificado con el parametro target_lang
def translate(text,target_lang="es"):
    translator = Translator()
    return translator.translate(text, dest=target_lang).text

# Funcion que lee un texto inicial y lo trade a ingles
def initial_text():
	with open("data/texto_inicial.txt",'r') as f:
		text = f.read()
	return translate(text,target_lang="en")

# inicializamos el modelo
ai = aitextgen(model="aitextgen/pytorch_model_355M.bin", config="aitextgen/config_355M.json", to_gpu=False)

while True:
	# generamos un texto nuevo
	answer = ai.generate_one(prompt=initial_text())
	# lo traducimos a español
	answer = translate(answer,target_lang="es")
	# lo guardamos en un archivo de texto
	print("Guardando texto generado")
	print(answer)
	with open("data/texto_generado.txt",'w') as f:
		f.write(answer)