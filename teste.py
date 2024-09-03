import json

anuncios = []
with open('anuncios.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        anuncio = json.loads(line)
        anuncios.append(anuncio)

for ad in anuncios[:5]:
    print(f"""
{ad['nome_anuncio']}
{ad['link_anuncio']}""")
