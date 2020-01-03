"""Launcher"""


from subprocess import Popen, CREATE_NEW_CONSOLE


PROCESSES = []
USER = 'user'

while True:
    ACTION = input('s - start server, x - close all windows, q - quite: ')
    if ACTION == 'q': break
    elif ACTION == 's':
        PROCESSES.append(Popen('python server.py', creationflags=CREATE_NEW_CONSOLE))
        for i in range(2):
            name = USER + str(i+1)
            PROCESSES.append(Popen(f'python client.py -n {name}', creationflags=CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        for process in PROCESSES:
            process.kill()
        PROCESSES.clear()
