from api import app
from subprocess import call
import threading
from time import sleep
import os


def run_crawler():
    app.run(port=8000, debug=False)


def main():
    crawler_thread = threading.Thread(target=run_crawler)

    crawler_thread.start()
    sleep(3)
    call('frontend/eruri-helper.exe')
    os._exit(0)


if __name__ == "__main__":
    main()
