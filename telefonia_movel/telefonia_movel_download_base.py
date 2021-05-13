"""
Código criado usando Google Colab
Download da base de dados de telefonia móvel by Anatel
""""

!wget -p https://www.anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_telefonia_movel.zip

import pandas as pd
import numpy as np
import os
from zipfile import ZipFile

pasta = '/content/www.anatel.gov.br/dadosabertos/paineis_de_dados/acessos'
mobile = os.path.join(pasta, 'acessos_telefonia_movel.zip')

#decodificando os arquivos (2005-2018)
  #Anatel separa em tecnologia(tipo de conexão) e modalidade (tipo de planos: pré e pós pago)
with ZipFile(mobile) as z:
  with z.open(f'Acessos_Telefonia_Movel_2005-2018_Tecnologia.csv') as f:
   tm_tec = pd.read_csv(f,sep=';', encoding='utf-8')

#renomeando/padronizando variaveis ref. tm_tec (telefonia móvel - tecnologia)
tm_tec.rename(columns={'Ano': 'ano','Mês':'mes', 'Grupo Econômico':'grupo_economico', 'Empresa':'empresa',
                 'CNPJ':'cnpj', 'Porte da Prestadora':'porte_empresa', 'UF':'sigla_uf', 'Região PGO':'outorga', 
                 'Código Nacional':'ddd', 'Tecnologia':'tecnologia', 'Tecnologia Geração':'sinal', 'Acessos':'acessos'}, inplace=True)

#exclusão de dados NaN (ddd & sigla_uf), início das observações completas em 2009
tm_tec.dropna(inplace=True)

with ZipFile(mobile) as z:
  with z.open(f'Acessos_Telefonia_Movel_2005-2018_Modalidade.csv') as f:
   tm_mod = pd.read_csv(f,sep=';', encoding='utf-8')

#renomeando/padronizando variaveis ref. tm_mod (telefonia_movel - modalidade)
tm_mod.rename(columns={'Ano': 'ano','Mês':'mes', 'Grupo Econômico':'grupo_economico', 'Empresa':'empresa',
                 'CNPJ':'cnpj', 'Porte da Prestadora':'porte_empresa', 'UF':'sigla_uf', 'Região PGO':'outorga', 
                 'Código Nacional':'ddd', 'Modalidade de Cobrança':'modalidade', 'Acessos':'acessos'}, inplace=True)

#exportação arquivo csv
tm_tec.to_csv('/content/telefonia_movel_microdados_2009-2018_tecnologia.csv', index=False)
tm_mod.to_csv('/content/telefonia_movel_microdados_2005-2018_modalidade.csv', index=False)

#decodificando os arquivos (2019-2021)
  #Anatel separa por semestre e ano
with ZipFile(mobile) as z:
  with z.open(f'Acessos_Telefonia_Movel_201901-201906.csv') as f:
    tm_1 = pd.read_csv(f,sep=';', encoding='utf-8')

with ZipFile(mobile) as z:
  with z.open(f'Acessos_Telefonia_Movel_201907-201912.csv') as f:
    tm_2 = pd.read_csv(f,sep=';', encoding='utf-8')

with ZipFile(mobile) as z:
  with z.open(f'Acessos_Telefonia_Movel_202001-202006.csv') as f:
    tm_3 = pd.read_csv(f,sep=';', encoding='utf-8')

with ZipFile(mobile) as z:
  with z.open(f'Acessos_Telefonia_Movel_202007-202012.csv') as f:
    tm_4 = pd.read_csv(f,sep=';', encoding='utf-8')

with ZipFile(mobile) as z:
  with z.open(f'Acessos_Telefonia_Movel_2021.csv') as f:
    tm_5 = pd.read_csv(f,sep=';', encoding='utf-8')

#junção das bases
tm_nova = tm_1.append([tm_2, tm_3, tm_4, tm_5], ignore_index=True)

#renomeando variaveis
tm_nova.rename(columns={'Ano': 'ano','Mês':'mes', 'Grupo Econômico':'grupo_economico', 'Empresa':'empresa',
                                      'CNPJ':'cnpj', 'Porte da Prestadora':'porte_empresa', 'UF':'sigla_uf', 'Município':'municipio',
                                      'Código IBGE Município':'id_municipio', 'Código Nacional':'ddd', 'Código Nacional (Chip)':'ddd_chip',
                                      'Modalidade de Cobrança':'modalidade', 'Tecnologia':'tecnologia', 'Tecnologia Geração':'sinal', 
                                      'Tipo de Pessoa':'pessoa', 'Tipo de Produto':'produto', 'Acessos':'acessos'}, inplace=True)

#exportação arquivo csv
tm_nova.to_csv('/content/telefonia_movel_microdados_2019-2021.csv')

#se preferível, salvar arquivos no Drive
from google.colab import drive
drive.mount('/content/drive')
