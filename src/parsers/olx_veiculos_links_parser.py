from bs4 import BeautifulSoup
from typing import Union, List
from time import sleep

from src.drivers.file_manager import FileManager
from src.drivers.requests.driver_requests import Requests
from src.logs.logger import get_logger

logger = get_logger(__name__)

class VeiculosLinksParser:
    
    def __init__(self) -> None:
        self.request = Requests()
        self.file_manager = FileManager()

    def run(self) -> None:
        lista_anuncios = self.__download_links_anuncios()

        path_links = 'src/data/raw/links_anuncios_raw'
        file_name = 'links_anuncios'
        self.file_manager.check_path(path_links)
        self.file_manager.save_links_jsonl(lista_anuncios,
                                           path_links,
                                           file_name)
        logger.info("Links salvos no arquivo .jsonl com sucesso")

    def __download_links_anuncios(self) -> List[str]:
        MAX_PAGES = 100
        
        lista_anuncios = []
        for i in range(1, MAX_PAGES+1):
    
            url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?o={i}'
            response = self.request.get(url)
            sleep(1.5)

            if response.status_code == 200:
                if (i+1) % 10 == 0:
                    logger.info(f"Raspando pagina {i+1} de {MAX_PAGES}...")

                soup = BeautifulSoup(response.text, 'html.parser')

                ads = soup.find_all('section', {'data-ds-component': 'DS-AdCard'})

                for ad in ads:      
                    anuncio = ad
                    nome_anuncio = anuncio.find('a', {'class': 'olx-ad-card__title-link'}).text
                    link_anuncio = anuncio.find('a')['href']

                    lista_anuncios.append({'nome_anuncio': nome_anuncio,
                                            'link_anuncio': link_anuncio})
                    
            else: 
                msg = f"""
                Erro ao raspar a url: {url}
                Resposta recebida: <{response.status_code}>"""
                logger.error(msg)
                continue

        logger.info("Links raspados") 
        return lista_anuncios
