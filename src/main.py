from parsers.olx_veiculos_links_parser import VeiculosLinksParser
from logs.logger import get_logger

logger = get_logger(__name__)

def main() -> None:
    logger.info("Iniciando a raspagem dos links.")
    veic_link_parser = VeiculosLinksParser()
    veic_link_parser.run()
    logger.info("Raspagem de links finalizada.")

if __name__ == "__main__":
    main()