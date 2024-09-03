from parsers.olx_veiculos_links_parser import VeiculosLinksParser

def main() -> None:
    veic_link_parser = VeiculosLinksParser()
    veic_link_parser.run()

if __name__ == "__main__":
    main()