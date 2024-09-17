from os import path
import json
from typing import List, Dict

from src.drivers.file_manager import FileManager

class PipelineBronze:
    """
    Essa classe é responsável por pegar os dados dos arquivos .jsonl e salvar 
    em um arquivo '.csv'.
    """

    def __init__(self) -> None:
        self.file_manager = FileManager()

    def run(self) -> None:
        dados_veiculos = self.__carregar_dados_veiculos()

        path_dados_bronze = 'src/data/bronze'
        file_name = 'dados_veiculos_bronze'

        self.file_manager.check_path(path_dados_bronze)
        self.__save_in_csv(path=path_dados_bronze,
                           file_name=file_name,
                           data=dados_veiculos)

        print("Dados salvos no arquivo .csv com sucesso.")

    def __carregar_dados_veiculos(self) -> List[Dict]:
        dados_veiculos_paths = self.file_manager.get_dados_veiculos_path()

        dados_veiculos_dicts = []
        for arquivo in dados_veiculos_paths:
            with open(arquivo, 'r', encoding='utf-8', newline='') as file:
                for line in file:
                    dados_veiculos_dicts.append(json.loads(line))
        
        return dados_veiculos_dicts

    def __save_in_csv(self, path:path, file_name:str, data:List[Dict]) -> None:
        colunas = data[0].keys()

        self.file_manager.create_and_save_csv(path,
                                              file_name,
                                              columns=colunas, 
                                              data=data)

def main():
    bronze = PipelineBronze()
    bronze.run()

if __name__ == "__main__"    :
    main()