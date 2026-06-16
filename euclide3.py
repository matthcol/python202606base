# module euclide

# solution #3 pour gérer les arguments en mode CLI
# librairie tierce typer
import typer

app = typer.Typer()

def pgcd(a: int, b: int) -> int:  # with annotation type (hints)
    while b != 0:
        t = a
        a = b
        b = t % b
    return a

@app.command()
def main(x: int, y: int):
    # utiliser les paramètres
    g = pgcd(x, y)
    print(f"Le pgcd de {x} et {y} est {g}")

if __name__ == '__main__':
    app()    