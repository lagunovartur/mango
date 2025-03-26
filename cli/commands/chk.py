from runner import run


def chk_style():
    """ruff check | ruff format --check | black --check --diff | isort --check --diff"""

    @run(from_env='src', check=True)
    def chk_black():
        return 'black --check --diff'

    @run(from_env='src', check=True)
    def chk_isort():
        return 'isort --check --diff'

    @run(from_env='src', check=True)
    def chk_ruff():
        return 'ruff check'

    @run(from_env='src', check=True)
    def chk_ruff_format():
        return 'ruff format --check'

    chk_black()
    chk_isort()
    chk_ruff()
    chk_ruff_format()


@run(from_env='src', check=True)
def chk_mypy():
    """mypy check"""
    return 'mypy --explicit-package-bases --enable-error-code ignore-without-code'


def chk():
    """chk-style | chk-poetry | chk-mypy"""
    chk_test()
    chk_style()
    chk_mypy()


def chk_test():

    @run(from_env='docker', check=True)
    def be_test():
        return f'run --rm -T api pytest -n 2'

    be_test()
