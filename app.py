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
        if not lamen["estrelas"] == 0.0:
            qtd_estrelas = int(round(lamen["estrelas"]))
            nota_lamen = f"{lamen['estrelas']:.1f} " + ("🍜" * qtd_estrelas)
        else:
            nota_lamen = "NA"

        linha = {
            "Variedade / Nome": lamen["variedade"],
            "Marca": lamen["marca"],
            "Estilo": lamen["estilo"],
            "País": lamen["pais"],
            "Nota": nota_lamen,
            "Avaliação": classificar_nota(lamen["estrelas"]),
        }
        tabela.append(linha)
    return tabela


def buscar_por_termo(paises, marcas, busca):
    """Filtra lámens por marca ou variedade."""
    if not busca:
        if not paises:
            return marcas
        else:
            return paises
    
    termo = busca.lower().strip()
    return [
        prato
        for prato in paises or marcas
            if termo in prato["variedade"].lower() or termo in prato["marca"].lower() or termo in prato["pais"].lower()
    ]


def listar_paises(lamens):
    """Retorna a lista de países sem repetição e ordenada."""
    paises = sorted(list({lamen["pais"] for lamen in lamens if "pais" in lamen}))
    return paises

def listar_marcas(lamens):
    """Retorna a lista de países sem repetição e ordenada."""
    sabores = sorted(list({lamen["marca"] for lamen in lamens if "marca" in lamen}))
    return sabores


def filtrar_por_pais(lamens, pais):
    """Filtra por país escolhido."""
    if pais == "Todos":
        return lamens
    return [prato for prato in lamens if prato["pais"] == pais]

def filtrar_por_marca(lamens, sabor):
    """Filtra por país escolhido."""
    if sabor == "Todos":
        return lamens
    return [sabor for sabor in lamens if sabor["marca"] == sabor]


def main():
    st.set_page_config(page_title="Lámens pelo mundo", page_icon="🍜", layout="wide")
    st.title("Lámens do Mundo")

    lamens = dados.carregar_lamens()

    if not lamens:
        st.error("Nenhum dado encontrado no arquivo CSV.")
        return

    # Métricas Principais em 4 colunas na parte superior
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total de Lámens", len(lamens))

    nota_media = dados.calcular_nota_media(lamens)
    col2.metric("Nota Média Geral", f"{nota_media:.2f} 🍜")

    qtd_top = dados.contar_cinco_estrelas(lamens)
    col3.metric("Lámens nota 5", qtd_top)

    melhor = dados.encontrar_melhor_avaliado(lamens)
    if melhor:
        col4.metric("Lámen mais bem avaliado", f"{melhor['estrelas']:.1f} 🍜")
        col4.caption(f"{melhor['marca']} - {melhor['variedade']}")

    st.divider()

    # Filtros
    col_busca, col_pais, col_marca = st.columns(3)
    busca = col_busca.text_input("Buscar por Nome ou Marca")
    pais_selecionado = col_pais.selectbox(
        "Filtrar por País", ["Todos"] + listar_paises(lamens)
    )
    marca_selecionada = col_marca.selectbox(
        "Filtrar por Marca", ["Todos"] + listar_marcas(lamens)
    )

    # Aplicação dos filtros
    dados_de_paises = filtrar_por_pais(lamens, pais_selecionado)
    dados_de_marcar = filtrar_por_marca(lamens, marca_selecionada)
    encontrados = buscar_por_termo(dados_de_paises, dados_de_marcar, busca)

    qtd_encontrados = len(encontrados)

    if qtd_encontrados == 0:
        st.warning("Nenhum lámen encontrado com os filtros aplicados.")
    else:
        st.write(f"Lámens encontrados: {qtd_encontrados}")
        st.dataframe(montar_tabela(encontrados), use_container_width=True)


if __name__ == "__main__":
    main()