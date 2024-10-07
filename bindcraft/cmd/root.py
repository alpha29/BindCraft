import subprocess

import typer

from bindcraft import __version__

app = typer.Typer()

DOCKER_COMPOSE_FILE = "docker/conda.yml"
DOCKER_CONTAINER_NAME = "bindcraft"


@app.command()
def up():
    """
    Start conda docker-compose container.
    """
    cmd = f"docker compose -f {DOCKER_COMPOSE_FILE} up -d".split(" ")
    subprocess.run(cmd, check=True)


@app.command()
def status():
    """
    Check status of conda docker-compose container.
    """
    cmd = f"docker ps -a | grep {DOCKER_CONTAINER_NAME}"
    subprocess.run(cmd, check=False, shell=True)


@app.command()
def login():
    """
    Login to running conda docker-compose container.
    """
    cmd = f"docker exec -it {DOCKER_CONTAINER_NAME} /bin/bash".split(" ")
    subprocess.run(cmd, check=False)


@app.command()
def down():
    """
    Stop conda docker-compose container.
    """
    cmd = f"docker compose -f {DOCKER_COMPOSE_FILE} down".split(" ")
    subprocess.run(cmd, check=True)


@app.command()
def version():
    """
    Show the version and exit.
    """
    typer.echo(f"bindcraft {__version__}")


def main():
    app()
