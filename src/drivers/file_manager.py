import os
import json
from typing import Any,Dict,List

class FileManager:

    def __init__(self) -> None:
        pass

    def check_path(self, file_path: str)-> None:
        """Verifica se o caminho existe, caso não exista cria 
        o caminho que foi passado."""
        if not os.path.exists(file_path):
            os.mkdir(file_path)

    def save_links_jsonl(self, data:List, path:str, file_name:str) -> None:
        """Salva a lista com os links dos anuncios em um arquivo 'jsonl'."""
        
        anuncios = data
        file_path = rf'{path}/{file_name}.jsonl'

        with open(file_path, 'w', encoding='utf-8') as file:
            for anuncio in anuncios:
                json_line = json.dumps(anuncio, ensure_ascii=False)
                file.write(json_line + '\n')