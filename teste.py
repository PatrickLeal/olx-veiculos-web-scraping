import json
import datetime
from src.logs.logger import get_logger

logger = get_logger(__name__)
# anuncios = []
# with open(r'src\data\raw\links_anuncios_raw\links_anuncios.jsonl', 'r', encoding='utf-8') as file:
#     for line in file:
#         anuncio = json.loads(line)
#         anuncios.append(anuncio)

# for ad in anuncios[:5]:
#     print(f"""
# {ad['nome_anuncio']}
# {ad['link_anuncio']}""")
if __name__ == "__main__":
    logger.info("Iniciando o projeto")
    for i in range(1, 5+1):
        logger.info("executando loop %d de 5", i)
