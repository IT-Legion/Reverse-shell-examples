import socket

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
s.connect(('127.0.0.1', 8888))

# Отправляем сообщение серверу
s.send(b'Hello, Server')

# Закрываем сокет
s.close()