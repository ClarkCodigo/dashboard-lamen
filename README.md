# Nome do app - Dashbord Lamen

**Membros:** 
Pedro Farias Ferreira, João Pedro, Arthur Sevilha Coelho

**Dataset:**
lamens.csv + [link da fonte original](https://www.theramenrater.com/resources-2/the-list/)

**App publicado:** 
-

## Funcionalidades
- [ ] Ler os dados do arquivo CSV do dataset.
- [ ] Converter as colunas que não estão num formato apropriado para os cálculos (números escritos como texto, valores por extenso, unidades junto do número, etc)
- [ ] Mostrar no mínimo 3 métricas sobre o dataset
- [ ] Classificar os registros em faixas a partir de uma coluna numérica e mostrar a faixa na tabela
- [ ] Uma tabela com os dados e nomes de coluna legíveis
- [ ] Uma busca por texto que não diferencie maiúsculas de minúsculas
- [ ] Um filtro por categoria, com as opções dos próprios dados (sem escrever à mão) e uma opção paramostrar todos
- [ ] Busca e filtro funcionando juntos
- [ ] Uma mensagem quando nenhum resultado for encontrado
- [ ] Código organizado em funções e módulos, com nomes que façam sentido no tema do grupo
- [ ] App publicado no Streamlit Community Cloud


## Funcionalidade extra
Mais bem classificado (quantidade de estrelas), no país

## Como rodar
 **configuração basica do streamlit, deve ser configurado para esse projeto**

```
    python -m venv .venv
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # libera o script de ativação só nesta janela
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    streamlit run app.py
```