import pandas as pd #Importa a biblioteca Pandas (a principal ferramenta do Python para tabelas) e dá o apelido pd para digitarmos menos.
from datetime import datetime #Traz a ferramenta nativa do Python que consulta a data e a hora atuais do computador.

# 1. CARREGAMENTO DOS DADOS
df = pd.read_excel('estoque_bruto.xlsx') #Lê o arquivo Excel e guarda dentro da variável df (abreviação padrão para DataFrame, que é como o Pandas chama uma tabela).
print("--- TABELA ORIGINAL ---")
print(df)

# 2. LIMPEZA BÁSICA (Valores vazios e quantidades inválidas)
df_limpo = df.dropna(subset=['Preco_Unitario']).copy() #O comando dropna apaga linhas com células em branco (NaN). Passando subset=['Preco_Unitario'], dizemos: "Só apague a linha se o preço estiver vazio". Isso já elimina a linha da Cereja, que está sem preço. O .copy() no final avisa ao Python para criar uma tabela independente na memória, evitando avisos de alerta.
df_limpo = df_limpo[df_limpo['Quantidade'] > 0] #Funciona como um filtro do Excel. Ele mantém na tabela apenas as linhas onde a coluna Quantidade é maior que zero. Mesmo se a Cereja tivesse preço, ela seria barrada aqui por ter quantidade -1.

# 3. TRATAMENTO DE DATAS E VALIDADE
df_limpo['Validade'] = pd.to_datetime(df_limpo['Validade'], dayfirst=True) #Garante que o Python entenda a coluna Validade como uma data real no formato brasileiro (dia/mês/ano, como 09/11/2026 e 10/11/2026), e não apenas como um texto comum.
hoje = datetime.now()

# Separando produtos vencidos dos produtos válidos
vencidos = df_limpo[df_limpo['Validade'] < hoje] #Compara a data de cada produto com a data de hoje. Na sua planilha, o Sucrilhos (10/11/2026) vai cair direto nessa tabela de alerta de vencidos.
validos = df_limpo[df_limpo['Validade'] >= hoje].copy() #Guarda apenas os produtos dentro do prazo (no seu exemplo, o Morango com validade em 15/12/2027).

# 4. REGRA DE NEGÓCIO (Cálculo de valor total em estoque)
validos['Valor_Total'] = validos['Quantidade'] * validos['Preco_Unitario'] #No Pandas, você não precisa usar um laço for para calcular linha por linha. Basta multiplicar uma coluna pela outra que ele cria a coluna nova Valor_Total multiplicando os valores de todas as linhas de uma só vez (para o Morango, calculará 250 * 100 = 25000).

# 5. EXPORTAÇÃO DOS RELATÓRIOS
validos.to_excel('relatorio_estoque_valido.xlsx', index=False)
vencidos.to_excel('alerta_produtos_vencidos.xlsx', index=False)
# Cria os arquivos Excel novos na sua pasta. O parâmetro index=False serve para o Pandas não criar aquela coluna extra inútil numerando as linhas (0, 1, 2...) no canto esquerdo da planilha.

print("\nRelatórios gerados com sucesso!")