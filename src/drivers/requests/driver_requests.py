import cloudscraper

scraper = cloudscraper.CloudScraper()

class Requests:
    """Classe que utiliza o pacote 'cloudscraper' para fazer 
    requisições.
    
    Usar o método 'get' para obter a requisição."""
    def __init__(self) -> None:
        pass

    def get(self, url: str) -> str:
        """Retorna a resposta da requisição."""
        response = scraper.get(url)

        return response