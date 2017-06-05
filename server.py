import socket
from datetime import datetime

def handler(byte_data):
    data = byte_data.decode('utf-8')
    ret = ''
    if data == 'серверное время':
        ret = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    elif data[-6:] == '/длина':
        ret = str(len(data[:-6]))
    elif data[-9:] == '/наоборот':
        ret = data[:-9][::-1]
    else:
        ret = data.upper()
    return ret.encode('utf-8')


if __name__ == '__main__':
    client = "127.0.0.1"
    recf = ('', 9090)
    send_to = (client, 9091)

    reciver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    reciver.bind(recf)
    while True:
        data, addr = reciver.recvfrom(1024)
        print('{t} - {ip[0]} : сообщение: {d}'.format(t = datetime.now().strftime('%H:%M:%S'), d = data.decode('utf-8'), ip = addr))
        sender.sendto(handler(data), send_to)