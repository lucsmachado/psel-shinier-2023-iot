import threading
from read_repo import read_repo
from gui import render_gui

if __name__ == '__main__':
    t1 = threading.Thread(target=render_gui)
    t2 = threading.Thread(target=read_repo)
    t1.start()
    t2.start()
