from runner import run
from config import config

@run(cwd=config.git_root_dir.joinpath('svc/client'))
def cl_run():
    return f'npm start'
