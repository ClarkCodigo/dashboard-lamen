import csv
from pathlib import Path

# Define o caminho do arquivo de dados relativo ao script atual
PASTA = Path(__file__).parent
LAMENS = PASTA / "lamens.csv"


def ler_lamen():
    """Lê as linhas brutas do arquivo CSV e retorna uma lista de dicionários."""
    lamen = []
    try:
        with open(LAMENS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                lamen.append(linha)
    except FileNotFoundError:
        print("O arquivo lamens.csv não foi encontrado.")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo:", error)

    return lamen


def preparar_lamen(prato):
    """Recebe os dados brutos e formata os tipos de dados necessários."""
    pratos = []
    for ingredientes in prato:
        try:
            estrelas = float(ingredientes.get("estrelas", 0))
        except (ValueError, TypeError):
            estrelas = 0.0

        livro = {
            "variedade": ingredientes.get("variedade", "Desconhecido"),
            "marca": ingredientes.get("marca", "Desconhecido"),
            "estilo": ingredientes.get("estilo", "N/A"),
            "pais": ingredientes.get("pais", "Desconhecido"),
            "estrelas": estrelas,
        }
        pratos.append(livro)

    return pratos


def carregar_lamens():
    """Interface principal para carregamento dos dados."""
    brutos = ler_lamen()
    return preparar_lamen(brutos)


def calcular_nota_media(lamens):
    """Calcula a nota média dos lámens fornecidos."""
    if not lamens:
        return 0.0
    total = sum(item["estrelas"] for item in lamens)
    return total / len(lamens)


def contar_cinco_estrelas(lamens):
    """Conta a quantidade de lámens com nota 5.0 ou superior."""
    return sum(1 for item in lamens if item["estrelas"] >= 5.0)


def encontrar_melhor_avaliado(lamens):
    """Retorna o item com a maior avaliação."""
    if not lamens:
        return None
    return max(lamens, key=lambda item: item["estrelas"])


if __name__ == "__main__":
    # Teste de execução individual
    dados_carregados = carregar_lamens()
    if dados_carregados:
        print(f"Sucesso ao carregar. Total de registros: {len(dados_carregados)}")
        print(f"Primeiro item: {dados_carregados[0]}")
    else:
        print("Nenhum dado pôde ser carregado.")