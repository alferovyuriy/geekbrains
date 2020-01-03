"""Launcher"""


from subprocess import Popen, CREATE_NEW_CONSOLE


PROCESSES = []

while True:
    ACTION = input('s - start server, x - close all windows, q - quite: ')
    if ACTION == 'q': break
    elif ACTION == 's':
        PROCESSES.append(Popen('python server.py', creationflags=CREATE_NEW_CONSOLE))
        for _ in range(2):
            PROCESSES.append(Popen('python client.py -m send', creationflags=CREATE_NEW_CONSOLE))
        for _ in range(3):
            PROCESSES.append(Popen('python client.py -m listen', creationflags=CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        for process in PROCESSES:
            process.kill()
        PROCESSES.clear()
