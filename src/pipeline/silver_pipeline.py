import pandas as pd
from pandas import DataFrame
import datetime
import re
import ast

from src.drivers.file_manager import FileManager

class PipelineSilver:

    def __init__(self) -> None:
        self.filemanager = FileManager()

    def run(self) -> None:
        bronze_files_path = self.filemanager.get_dados_bronze_path()
        df = pd.read_csv(bronze_files_path[0])
        
        print("Fazendo a transformação dos dados.")
        df_publi_cleaned = self.__clean_publicacao_info_column(df)
        df_preco_cleaned = self.__clean_preco(df_publi_cleaned)
        df_carac_cleaned = self.__clean_Caracteristicas_and_Opcionais_columns(df_preco_cleaned)

        path_dados_silver = 'src/data/silver'
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = 'dados_veiculos_silver'
        file_path = rf'{path_dados_silver}/{now}_{file_name}.csv'

        self.filemanager.check_path(path_dados_silver)
        df_carac_cleaned.to_csv(file_path, index=False)
        print(f"Dados salvos em {path_dados_silver}.")

        print("Pipeline finalizado com sucesso.")

    def __clean_publicacao_info_column(self, dataframe:DataFrame) -> DataFrame:
        """
        Função que limpa a coluna 'publicacao_info' e cria 4 novas colunas a partir dela.
        """
        def pegar_data(linha:str):
            publicacao_tempo = re.sub(r"[\[\]\']", '', linha.publicacao_info).split('-')[0]
            dia, mes = publicacao_tempo.split()[2].split('/')
            return datetime.date(2024, int(mes), int(dia))
        
        def pegar_tempo(linha:str):
            publicacao_tempo = re.sub(r"[\[\]\']", '', linha.publicacao_info).split('-')[0]
            return publicacao_tempo.split()[-1]
        
        def pegar_codigo_publi(linha:str):
            info = re.sub(r"[\[\]\']", '', linha.publicacao_info).split('-')
            cod = [elemento.split()[-1] for elemento in info if str('cód') in elemento]
            return cod[0] if len(cod) > 0 else pd.NA
        
        def pegar_tipo_anuncio(linha:str):
            info = re.sub(r"[\[\]\']", '', linha.publicacao_info).split('-')
            tipo_anuncio = [elemento.split()[-1] for elemento in info if str('anúncio') in elemento]
            return tipo_anuncio[0] if len(tipo_anuncio) > 0 else pd.NA
        
        df = dataframe
        df['data_publicacao'] = df.apply(pegar_data, axis=1)
        df['tempo_publicacao'] = df.apply(pegar_tempo, axis=1)
        df['cod_publicacao'] = df.apply(pegar_codigo_publi, axis=1)
        df['tipo_anuncio'] = df.apply(pegar_tipo_anuncio, axis=1)
        df = df.drop(columns=['publicacao_info'])

        return df
    
    def __clean_preco(self, dataframe: DataFrame) -> DataFrame:
        """Função que limpa a coluna preco."""
        df = dataframe
        df.preco = df.preco.str.replace('R$', '').str.replace('.', '').str.strip()
        df.preco = pd.to_numeric(df.preco, errors='coerce')
        df = df.rename(columns={'preco': 'preco_brl'})

        return df
    
    def __clean_Caracteristicas_and_Opcionais_columns(self, dataframe:DataFrame) -> DataFrame:
        """
        Função que limpa as colunas 'caracteristicas' e 'opcionais' e criar novas colunas
        a partir de cada caracteristica.
        """
        df = dataframe
        df.opcionais = df.opcionais.apply(lambda x: ast.literal_eval(x))
        df.caracteristicas = df.caracteristicas.apply(lambda x: ast.literal_eval(x))

        chaves_unicas = list(df.caracteristicas[0].keys())
        for i in df.caracteristicas:
            chaves_unicas = list(set(chaves_unicas + list(i.keys())))

        for chave in chaves_unicas:
            df[chave] = df.caracteristicas.apply(lambda x: x.get(chave, pd.NA))

        df = df.drop(columns=['caracteristicas'])
        df.columns = df.columns.str.replace('í', 'i')\
                               .str.replace('â', 'a')\
                               .str.replace('ê', 'e')
        df.columns = df.columns.str.upper().str.replace(' ', '_')

        return df
    