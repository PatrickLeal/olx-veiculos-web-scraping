import cloudscraper
from requests import Response

scraper = cloudscraper.CloudScraper()

class Requests:
    """Classe que utiliza o pacote 'cloudscraper' para fazer 
    requisições.
    
    Usar o método 'get' para obter a requisição."""
    def __init__(self) -> None:
        pass

    def get(self, url: str) -> Response:
        """Retorna a resposta da requisição."""
        response = scraper.get(url)

        return response
    
if __name__ == '__main__':
    req = Requests()
    resp = req.get('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?o=1')
    print(resp.status_code)
    