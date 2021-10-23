import typer
from src import train

app = typer.Typer()


@app.command()
def train_model():
    train.train()

if __name__ == "__main__":
    app()
