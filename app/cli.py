import click
import uvicorn


@click.group()
def cli() -> None:
    """Init microservice"""


@cli.command()
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=8000)
def serve(host: str, port: int) -> None:
    uvicorn.run(
        'app.main:app', host=host, port=port, log_level='info', reload=True,
    )


if __name__ == '__main__':
    cli()
