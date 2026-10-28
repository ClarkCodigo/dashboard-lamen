import streamlit as st
import dados

def classificar_nota(nota):
    """Classifica a avaliação em uma faixa de texto."""
    if nota >= 4.5:
        return "Excelente"
    elif nota >= 4.0:
        return "Bom"
    elif nota >= 3.5:
        return "Passável"
    elif nota >= 3.0:
        return "Ruim"
    else:
        return "Péssimo"


def montar_tabela(lamens):
    """Prepara as linhas para a tabela exibida no Streamlit."""
    tabela = []
    for lamen in lamens:
        qtd_estrelas = int(round(lamen["estrelas"]))
        linha = {
            "Variedade / Nome": lamen["variedade"],
            "Marca": lamen["marca"],
            "Estilo": lamen["estilo"],
            "País": lamen["pais"],
            "Nota": f"{lamen['estrelas']:.1f} " + ("⭐" * qtd_estrelas),
            "Avaliação": classificar_nota(lamen["estrelas"]),
        }
        tabela.append(linha)
    return tabela


def buscar_por_termo(lamens, busca):
    """Filtra lámens por marca ou variedade."""
    if not busca:
        return lamens
    termo = busca.lower().strip()
    return [
        prato
        for prato in lamens
        if termo in prato["variedade"].lower() or termo in prato["marca"].lower()
    ]

#lista de paises
def listar_paises(lamens):
    """Retorna a lista de países sem repetição e ordenada."""
    paises = sorted(list({prato["pais"] for lamen in lamens if (prato := lamen)}))
    return paises


def filtrar_por_pais(lamens, pais): 
    """Filtra por país escolhido."""
    if pais == "Todos":
        return lamens
    return [prato for prato in lamens if prato["pais"] == pais]


def main():
    st.set_page_config(page_title="Dashboard de Lámens", page_icon="🍜", layout="wide")
    st.title("Dashboard de Lámens do Mundo")

    lamens = dados.carregar_lamens()

    if not lamens:
        st.error("Nenhum dado encontrado no arquivo CSV.")
        return

    # Recupera o melhor país e sua média corretamente passando a lista completa
    # melhor_pais, melhor_nota = dados.pais_com_melhor_avaliacao(lamens)

    # Métricas Principais em 5 colunas na parte superior
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total de Lámens", len(lamens))

    nota_media = dados.calcular_nota_media(lamens)
    col2.metric("Nota Média Geral", f"{nota_media:.2f} ⭐")

    qtd_top = dados.contar_cinco_estrelas(lamens)
    col3.metric("Lámens 5 Estrelas", qtd_top)

    melhor = dados.encontrar_melhor_avaliado(lamens)
    if melhor:
        col4.metric("Melhor Avaliado", f"{melhor['estrelas']:.1f} ⭐")
        col4.caption(f"{melhor['marca']} - {melhor['variedade']}")

    # if melhor_pais:
    #     col5.metric("Melhor País (>4★)", f"{melhor_pais}")
    #     col5.caption(f"Média: {melhor_nota:.2f} ⭐")
    # else:
    #     col5.metric("Melhor País (>4★)", "N/A")

    st.divider()

    # Filtros
    col_busca, col_pais = st.columns(2)
    busca = col_busca.text_input("Buscar por Nome ou Marca")
    pais_selecionado = col_pais.selectbox(
        "Filtrar por País", ["Todos"] + listar_paises(lamens)
    )

    # Aplicação dos filtros
    dados_filtrados = filtrar_por_pais(lamens, pais_selecionado)
    encontrados = buscar_por_termo(dados_filtrados, busca)

    qtd_encontrados = len(encontrados)

    if qtd_encontrados == 0:
        st.warning("Nenhum lámen encontrado com os filtros aplicados.")
    else:
        st.write(f"Lámens encontrados: {qtd_encontrados}")
        st.dataframe(montar_tabela(encontrados), use_container_width=True)


if __name__ == "__main__":
    main()