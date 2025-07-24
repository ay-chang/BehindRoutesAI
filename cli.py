# cli.py
import typer
from main import scan_project, ask_question

app = typer.Typer()

@app.command()
def scan(path: str):
    """Scan a backend project directory and extract route logic"""
    scan_project(path)

@app.command()
def ask(question: str):
    """Ask a question about the scanned backend"""
    ask_question(question)

if __name__ == "__main__":
    app()
