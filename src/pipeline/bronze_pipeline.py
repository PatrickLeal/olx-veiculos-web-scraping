import json
import csv
from typing import List, Dict

from src.drivers.file_manager import FileManager

class PipelineBronze:

    def __init__(self) -> None:
        self.file_manager = FileManager()

    def run(self) -> None:
        dados_veiculos = self.__carregar_dados_veiculos()

        print(dados_veiculos[:5])

    def __carregar_dados_veiculos(self) -> List[Dict]:
        dados_veiculos_paths = self.file_manager.get_dados_veiculos_path()

        dados_veiculos_dicts = []
        for arquivo in dados_veiculos_paths:
            with open(arquivo, 'r', encoding='utf-8', newline='') as file:
                for line in file:
                    dados_veiculos_dicts.append(json.loads(line))
        
        return dados_veiculos_dicts



    def __save_in_csv(self) -> None:
        ...

def main():
    bronze = PipelineBronze()
    bronze.run()

if __name__ == "__main__"    :
    main()