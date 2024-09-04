import logging
import os

# Configura o logger
# log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))

path_logs = 'src/logs'
file_name = 'links_anuncios'
os.makedirs(path_logs, exist_ok=True)  # Cria a pasta 'logs' se não existir

log_file = os.path.join(path_logs, 'scraper.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_file),  # Salva os logs em um arquivo
        logging.StreamHandler()         # Exibe os logs no console
    ]
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
