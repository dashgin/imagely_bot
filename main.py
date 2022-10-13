import multiprocessing as mp

from imagely.entrypoints.api.main import run_api
from imagely.entrypoints.tg_bot.main import run_bot

if __name__ == "__main__":

    # processes = [
    #     mp.Process(target=run_bot),
    #     mp.Process(target=run_api),
    # ]

    # for p in processes:
    #     p.start()

    # for p in processes:
    #     p.join()
    run_bot()