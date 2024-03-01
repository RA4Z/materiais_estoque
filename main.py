import shutil
from datetime import datetime

# Obter a data e hora atuais
data_atual = datetime.now()
ano = str(data_atual.year)[-2:]

data_formatada = data_atual.strftime("%m_%d") 

caminho_origem = 'Q:/APPS/SAP/EP0/PCP_WEN/Estoque sem consumo'
caminho_destino = 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Indicadores Automatizados/Controle de estoque'

arquivos = ['Dados_1200', 'Dados_1201', 'Dados_1206', 'Dados_1208', 'Dados_1220', 'Dados_3200', 'Dados_6200', 'DADOS_6201']
for file in arquivos:
    centro = file[-4:]
    nome_arquivo = f'Dados_{centro}_{data_formatada}_{ano}.txt'
    if centro.find('12') > -1:
        shutil.copy(f'{caminho_origem}/{file}.txt', f'{caminho_destino}/1200/')
    else:
        shutil.copy(f'{caminho_origem}/{file}.txt', f'{caminho_destino}/{centro}/')
