import cloudscraper
from requests import Response
from bs4 import BeautifulSoup
from pprint import pprint

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

def main():
    req = Requests()

    urls = [
        'https://am.olx.com.br/regiao-de-manaus/autos-e-pecas/carroantia-1326461396',
        'https://sp.olx.com.br/sao-paulo-e-regiao/autos-e-pecas/carros-vans-e-utilitarios/fiat-fiorino-1-4-mpi-furgao-endurance-8v-flex-2p-manual-1328373018'
    ]

    carros = []
    for url in urls:
        resp = req.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        print(f'status: {resp.status_code}')
    
        # o que pegar?
        # titulo
        titulo = soup.find('h1').text
    
        # info da publi
        divs = soup.find_all('div', {'data-ds-component': 'DS-Flex'})
        div_desejada = 'publicado em'
        publicacao_info = [p.text for p in divs if div_desejada in p.text.lower()]
        
        # preço
        preco = soup.find_all('h2', {'class': 'olx-text olx-text--title-large olx-text--block ad__sc-1leoitd-0 bpLbCi'})[0].text
        
        # descricao
        descricao = soup.find('span', {'class' : 'olx-text olx-text--body-medium olx-text--block olx-text--regular ad__sc-1sj3nln-1 fMgwdS'}).text
    
        # CARATCTERISCAS:
        # - tudo
        divs_caracts = soup.find_all('div', {'class' : 'olx-d-flex olx-ml-2 olx-ai-baseline olx-fd-column'})
        caracteristicas = {}
        for caracteristica in divs_caracts:
            elementos = caracteristica.findChildren()
            caracteristicas[elementos[0].text] = elementos[1].text
        
        # OPCIONAIS:
        # - tudo
        spans_opcionais = soup.find_all('span', {'class' : "olx-text olx-text--body-medium olx-text--block olx-text--regular ad__sc-1g2w54p-0 cutgWh olx-color-neutral-130"})
        opcionais = [op.text for op in spans_opcionais]
        
        # imagem
        imagem = soup.find_all('img')[0]['src']
    
        # perfil_carro
        url = url

        # localizacao
        cep = soup.find('div', {'class' : 'ad__sc-1f2ug0x-3 efnZpq olx-d-flex olx-mt-2'}).findChildren()[1].text
        
        carros.append({
            'titulo': titulo,
            'publicacao_info':publicacao_info,
            'preco': preco,
            'descricao': descricao,
            'caracteristicas':caracteristicas,
            'opcionais': opcionais,
            'cep': cep,
            'imagem':imagem,
            'perfil_carro':url
        })

    pprint(carros)

if __name__ == '__main__':
    main()