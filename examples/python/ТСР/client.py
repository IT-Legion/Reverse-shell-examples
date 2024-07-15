import socket

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
s.bind(('127.0.0.1', 8888))

# Начинаем прослушивание порта
s.listen(5)

# Бесконечный цикл для ожидания подключений
while True:
    try:
        # Принимаем соединение от клиента
        client, addr = s.accept()
    except KeyboardInterrupt:
        # Закрываем сокет при прерывании с клавиатуры
        s.close()
        break
    else:
        # Получаем сообщение от клиента
        result = client.recv(1024)
        # Выводим сообщение в консоль
        print('Сообщение:', result.decode('utf-8'))
