from api import app
from subprocess import call
import threading
from time import sleep
import os


def run_crawler():
    app.run(port=8000, debug=False)  # Flask Application을 실행해 Frontend와 통신한다.


def main():
    # 크롤러 스레드를 실행한다.
    crawler_thread = threading.Thread(target=run_crawler)
    crawler_thread.start()

    sleep(3)  # 프로그램 시작을 위해 3초간 대기

    call('frontend/eruri-helper.exe')  # frontend/eruri-helper.exe 파일을 실행한다.
    os._exit(0)  # 위 프로그램이 종료되면 스레드를 포함한 모든 프로세스를 종료한다.


if __name__ == "__main__":
    main()
