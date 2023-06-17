from invoke import Collection, task
from invokees.tasks import code, stderr, test  # noqa: E402


@task
def init(ctx):
    """Initializes the workspace, only should be run after initial checkout"""
    ctx.run("poetry install")
    stderr.print("[blue]Setting up Workspace[/blue]")
    stderr.print("[yellow]Installing pre-commit hooks[/yellow]")
    ctx.run("pre-commit install")


ns = Collection(init, code, test)
