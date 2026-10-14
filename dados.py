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

if __name__ == "__main__":
    lamen = ler_lamen()
    print(f"{len(lamen)} opções de lamens")