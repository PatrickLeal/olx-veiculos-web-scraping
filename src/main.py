from src.parsers.olx_veiculos_links_parser import VeiculosLinksParser
from src.parsers.olx_veiculos_dados_parser import VeiculosDadosParser
from src.pipeline.bronze_pipeline import PipelineBronze
from src.logs.logger import get_logger

logger = get_logger(__name__)

class PipelineManager:
    def __init__(self) -> None:
        pass

    def raspar_links(self) -> None:
        logger.info("Iniciando a raspagem dos links.")
        veic_link_parser = VeiculosLinksParser()
        veic_link_parser.run()
        logger.info("Raspagem de links finalizada.")

    def raspar_dados_veiculos(self) -> None:
        logger.info("Iniciando a raspagem dos dados dos anuncios.")
        veics_dados_parser = VeiculosDadosParser()
        veics_dados_parser.run()
        logger.info("Raspagem de dados finalizada.")
    
    def executar_pipeline_bronze(self) -> None:
        bronze_pipeline = PipelineBronze()
        bronze_pipeline.run()


def main() -> None:
    pipeline_manager = PipelineManager()
    # RASPANDO LINKS
    # pipeline_manager.raspar_links()

    # RASPANDO DADOS DOS CARROS
    # pipeline_manager.raspar_dados_veiculos()

    pipeline_manager.executar_pipeline_bronze()

if __name__ == "__main__":
    main()