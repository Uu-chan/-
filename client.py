import socket
from datetime import datetime


if __name__ == '__main__':
    server = "127.0.0.1"
    recf = ('', 9091)
    send_to = (server, 9090)

    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    reciver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    reciver.bind(recf)
    while True:
        message = input('отправить сообщение: ').encode('utf-8')
        sender.sendto(message, send_to)
        data, addr = reciver.recvfrom(1024)
        print('{t} - {ip[0]} : ответ сервера: {d}\n'.format(t = datetime.now().strftime('%H:%M:%S'), d = data.decode('utf-8'), ip = addr))
