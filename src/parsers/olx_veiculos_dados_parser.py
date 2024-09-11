from bs4 import BeautifulSoup
from typing import List, Generator, Any
import json

from src.drivers.file_manager import FileManager
from src.drivers.requests.driver_requests import Requests
from src.logs.logger import get_logger

logger = get_logger(__name__)

class VeiculosDadosParser:

    def __init__(self) -> None:
        self.request = Requests()
        self.file_manager = FileManager()

    def run(self) -> None:
        urls = self.__get_urls()
        veiculos_data = list(self.__download_dados_veiculos(urls=urls))

        path_dados_raw = 'src/data/raw/dados_veiculos_raw'
        file_name = 'dados_veiculos'
        self.file_manager.check_path(path_dados_raw)
        self.file_manager.save_dados_veiculos_jsonl(veiculos_data,
                                                    path_dados_raw,
                                                    file_name)

        logger.info("Dados salvos no arquivo .jsonl com sucesso")


    def __download_dados_veiculos(self, urls:List[str]) -> Generator[Any, Any, Any]:
        # raspar os dados dos anuncios
        urls = urls
        qtd_links = len(urls)
        
        for i, url in enumerate(urls):
            response = self.request.get(url)

            if response.status_code == 200:
                if i == 0:
                    logger.info(f"Raspando anuncio {i+1} de {qtd_links}...")

                if (i+1) % 100 == 0:
                    logger.info(f"Raspando anuncio {i+1} de {qtd_links}...")

                soup = BeautifulSoup(response.text, 'html.parser')
                
                # INFO DA PUBLICACAO
                divs = soup.find_all('div', {'data-ds-component': 'DS-Flex'})
                div_desejada = 'publicado em'
                publicacao_info = [p.text for p in divs if div_desejada in p.text.lower()]

                # CARATCTERISCAS:
                divs_caracts = soup.find_all('div', {'class' : 'olx-d-flex olx-ml-2 olx-ai-baseline olx-fd-column'})
                caracteristicas = {}
                for caracteristica in divs_caracts:
                    elementos = caracteristica.findChildren()
                    caracteristicas[elementos[0].text] = elementos[1].text

                # OPCIONAIS:
                spans_opcionais = soup.find_all('span', {'class' : "olx-text olx-text--body-medium olx-text--block olx-text--regular ad__sc-1g2w54p-0 cutgWh olx-color-neutral-130"})
                opcionais = [op.text for op in spans_opcionais]
                
                yield {
                    'titulo': soup.find('h1').text,
                    'publicacao_info':publicacao_info,
                    'preco': soup.find_all('h2', {'class': 'olx-text olx-text--title-large olx-text--block ad__sc-1leoitd-0 bpLbCi'})[0].text,
                    'descricao': soup.find('span', {'class' : 'olx-text olx-text--body-medium olx-text--block olx-text--regular ad__sc-1sj3nln-1 fMgwdS'}).text,
                    'caracteristicas':caracteristicas,
                    'opcionais': opcionais,
                    'cep': soup.find('div', {'class' : 'ad__sc-1f2ug0x-3 efnZpq olx-d-flex olx-mt-2'}).findChildren()[1].text,
                    'imagem':soup.find_all('img')[0]['src'],
                    'perfil_carro':url
                }

            else: 
                msg = f"""
                Erro ao raspar a url: {url}
                Resposta recebida: <{response.status_code}>
                **CONTINUANDO...**"""
                logger.error(msg)
                continue
        
        logger.info("Dados raspados.")

    def __get_urls(self) -> List[str]:
        files_path = self.file_manager.get_links_file_path()

        # como isso não vai ser um processo que vai se repetir várias vezes
        # vou manter a leitura apenas de um arquivo dentro do diretorio
        path_links = files_path[0] # pode passar o caminho do arquivo tbm
        with open(path_links, 'r', encoding='utf-8') as file:
            ads = [json.loads(line) for line in file] 
        
        urls = [ad['link_anuncio'] for ad in ads]

        return urls

def main():
    ...

if __name__ == "__main__":
    main()