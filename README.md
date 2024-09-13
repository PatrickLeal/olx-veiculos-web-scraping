
# Web scraping de veículos da Olx

Script em python que faz a raspagem de dados dos veículos anunciados no site olx brasil.

## Objetivo
Realizar análise dos dados encontrados, **apenas para fins educacionais**.
## Ferramentas
*   beautifulsoup4
*   cloudscraper
*   requests
*   pandas
## Rodando o script

```bash
  python start.py
```

O arquivo `main.py` é responsável por organizar as etapas a serem executadas, que devem ser executas em forma **sequencial**.

```python
  def main() -> None:
    pipeline_manager = PipelineManager()
    # RASPANDO LINKS
    pipeline_manager.raspar_links()

    # RASPANDO DADOS DOS CARROS
    # pipeline_manager.raspar_dados_veiculos()

    # PASSANDO DE OS DADOS PARA .CSV  
    # pipeline_manager.executar_pipeline_bronze()

    # PASSANDO DE OS DADOS PARA .CSV DA CAMADA SILVER 
    # pipeline_manager.executar_pipeline_silver()
```

|Ordem|Método (etapa)|
|--|--|
|1° | pipeline_manager.raspar_links() |
|2° | pipeline_manager.raspar_dados_veiculos() |
|3° | pipeline_manager.executar_pipeline_bronze() |
|4° | pipeline_manager.executar_pipeline_silver() |

### IMPORTANTE🚨
No arquivo `olx_veiculos_dados_parser.py` editar o seguinte trecho de código a partir da **linha 94** de acordo com quantas vezes já foi executado :
```python
# como isso não vai ser um processo que vai se repetir várias vezes
# vou manter a leitura apenas de um arquivo dentro do diretorio
path_links  =  files_path[2] # pode passar o caminho do arquivo tbm
```
---
No arquivo `silver_pipeline.py` editar o seguinte trecho de código a partir da **linha 16** de acordo com quantas vezes já foi executado :
```python
# está lendo de forma manual o segundo arquivo
df  = pd.read_csv(bronze_files_path[1])
```

## Arquitetura do Projeto

```
📦 
├─ .vscode
│  └─ .gitkeep
├─ src
│  ├─ __init__.py
│  ├─ data
│  │  ├─ __init__.py
│  │  └─ raw
│  │     └─ __init__.py
│  ├─ drivers
│  │  ├─ __init__.py
│  │  ├─ file_manager.py
│  │  └─ requests
│  │     ├─ __init__.py
│  │     └─ driver_requests.py
│  ├─ logs
│  │  ├─ __init__.py
│  │  └─ logger.py
│  ├─ main.py
│  ├─ parsers
│  │  ├─ __init__.py
│  │  ├─ olx_veiculos_dados_parser.py
│  │  └─ olx_veiculos_links_parser.py
│  └─ pipeline
│     ├─ __init__.py
│     ├─ bronze_pipeline.py
│     └─ silver_pipeline.py
├─ .gitignore
├─ README.md
├─ __init__.py
├─ requirements.txt
└─ start.py
```
<img src="https://github.com/PatrickLeal/olx-veiculos-web-scraping/blob/main/assets/fluxo%20projeto.png" alt="drawing" width="600"/>

## Melhorias possíveis

 - [ ] Criar rotinas para fazer raspagem de tempo em tempo
