import datetime
import os
import json
from typing import List

class FileManager:

    def __init__(self) -> None:
        pass

    def check_path(self, file_path: str)-> None:
        """Verifica se o caminho existe, caso não exista cria 
        o caminho que foi passado.
        
        :param path: Caminho onde os dados serao salvos.
        :type path: os.path | str(`caminho/caminho`)
        :return: None
        """

        if not os.path.exists(file_path):
            os.mkdir(file_path)

    def save_links_jsonl(self, data:List, path:str, file_name:str) -> None:
        """Salva a lista com os links dos anuncios em um arquivo 'jsonl'."""
        
        anuncios = data
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = rf'{path}/{now}_{file_name}.jsonl'

        with open(file_path, 'w', encoding='utf-8') as file:
            for anuncio in anuncios:
                json_line = json.dumps(anuncio, ensure_ascii=False)
                file.write(json_line + '\n')
    
    def save_dados_veiculos_jsonl(self, data:List, path:str, file_name:str) -> None:
        """
        Salva a lista com os dados dos veiculos em um arquivo 'jsonl'.

        :param data: Lista de dicionarios contendo os dados raspados.
        :type data: List
        :param path: Caminho onde os dados serao salvos.
        :type path: os.path | str(`caminho/caminho`)
        :param file_name: Nome do arquivo.
        :type file_name: str

        :return: None
        """
        
        veiculos = data
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = rf'{path}/{now}_{file_name}.jsonl'

        with open(file_path, 'w', encoding='utf-8') as file:
            for veiculo in veiculos:
                json_line = json.dumps(veiculo, ensure_ascii=False)
                file.write(json_line + '\n')

    @staticmethod
    def create_and_save_csv() -> None:
        ...

    @staticmethod
    def get_links_file_path() -> List[str]:
        """
        Função que retorna uma lista com o caminho dos .jsonl contendo
        os links dos anuncios

        :return: Lista de 'path' com os nomes dos arquivos em `ordem crescente`.
        """

        links_path = "src/data/raw/links_anuncios_raw"
        conteudo = os.listdir(links_path)

        files = [f for f in conteudo if os.path.isfile(os.path.join(links_path, f))]
        files_path = [os.path.join(links_path, f) for f in files]

        return sorted(files_path)

    @staticmethod
    def get_dados_veiculos_path() -> List[str]:
        """
        Função que retorna uma lista com o caminho dos .jsonl contendo
        os links dados dos veiculos.

        :return: Lista de 'path' com os nomes dos arquivos em `ordem crescente`.
        """
        links_path = "src/data/raw/dados_veiculos_raw"
        conteudo = os.listdir(links_path)

        files = [f for f in conteudo if os.path.isfile(os.path.join(links_path, f))]
        files_path = [os.path.join(links_path, f) for f in files]

        return sorted(files_path)

def main():
    file_manager = FileManager()
    conteudo = file_manager.get_dados_veiculos_path()

    for c in conteudo:
        print(c)

if __name__ == "__main__":
    main()