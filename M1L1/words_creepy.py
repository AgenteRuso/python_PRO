meme_dict = {
    "CRINGE": "Pena Ajena",
    "LOL": "rie con fuerza",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobacion",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado"
}

word = input("escribe una palabra que no entiendas (con mayusculas XD)")

if word in meme_dict.keys(): 
    print(meme_dict[word])



else:
    print("la palabra no esta")








