import csv
from pathlib import Path

PASTA = Path(__file__).parent
LAMENS = PASTA / "lamens.csv"


def ler_lamen():
    lamen = []
    try:
        with open(LAMENS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                lamen.append(linha)
    except FileNotFoundError:
        print("O arquivo lamen.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return lamen

def preparar_lamen(prato):
    """Recebe as linhas lidas do CSV e devolve os dados"""
    pratos = []
    for ingredientes in prato:
        livro = {
            "variedade": ingredientes["variedade"],
            "marca": ingredientes["marca"],
            "estilo": ingredientes["estilo"],
            "pais": ingredientes["pais"],
            "estrelas": ingredientes["estrelas"]
        }
        pratos.append(livro)

    return pratos


if __name__ == "__main__":
    """ Area de testes para as funções """

    seu_lamen = preparar_lamen(ler_lamen())
    print(f" Seu prato: {seu_lamen[0]} ")