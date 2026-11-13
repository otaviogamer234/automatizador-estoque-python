# Automatizador de Relatórios e Auditoria de Estoque em Python

Script de automação desenvolvido em **Python** para leitura, limpeza (higienização de dados), validação de prazos de validade e geração automática de relatórios gerenciais em Excel (`.xlsx`).

## O Problema que o Projeto Resolve
Em rotinas administrativas e de controle de estoque, planilhas preenchidas manualmente costumam apresentar inconsistências como:
* Cadastros com preços em branco;
* Lançamentos com quantidades negativas por erro de digitação;
* Lotes com data de validade vencida misturados ao estoque ativo;
* Falta de consolidação do valor financeiro total por item.

Este projeto automatiza toda a triagem em segundos, separando os itens prontos para venda daqueles que exigem ação imediata (descarte ou baixa).

---

## Funcionalidades
1. **Higienização de Dados (`Data Cleaning`):** Remove automaticamente registros incompletos (sem preço unitário) e filtra lançamentos com quantidades inválidas ($\le 0$).
2. **Auditoria de Validade:** Converte datas no padrão brasileiro (`DD/MM/AAAA`) e compara com a data atual do sistema para separar lotes vencidos de lotes regulares.
3. **Cálculo Financeiro Automatizado:** Gera a coluna `Valor_Total` multiplicando a quantidade válida pelo preço unitário de cada lote.
4. **Exportação Segmentada:** Gera duas planilhas finais limpas e formatadas:
   * `relatorio_estoque_valido.xlsx` (Apenas produtos aptos e com cálculo de valor em estoque);
   * `alerta_produtos_vencidos.xlsx` (Relatório de auditoria para controle de perdas).

---

## Exemplo Prático (Entrada vs. Saída)

**Planilha Bruta de Entrada (`estoque_bruto.xlsx`):**
| Produto | Quantidade | Preco_Unitario | Validade | Status Esperado |
| :--- | :---: | :---: | :---: | :--- |
| Cereja | -1 | *(vazio)* | 09/11/2026 | Removido (Sem preço / Qtd negativa) |
| Sucrilhos | 10 | 10.99 | 10/11/2026 | Movido para Alerta de Vencidos |
| Morango | 250 | 100.00 | 15/12/2027 | Aprovado (`Valor_Total`: R$ 25.000,00) |

---

## Tecnologias Utilizadas
* **Python 3**
* **Pandas:** Manipulação, filtragem vetorial e tratamento de datas (`DataFrames`).
* **OpenPyXL:** Leitura e escrita nativa de arquivos Microsoft Excel (`.xlsx`).

---

## Como Executar o Projeto Localmente

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
   cd NOME-DO-REPOSITORIO
