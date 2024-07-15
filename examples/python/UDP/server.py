import socket

# Создаем UDP-сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к адресу и порту
s.bind(('127.0.0.1', 8888))

try:
    # Получаем данные от клиента
    result, addr = s.recvfrom(1024)
    # Выводим сообщение и адрес отправителя
    print('Сообщение:', result.decode('utf-8'), 'от', addr)
except KeyboardInterrupt:
    print("Сервер остановлен.")
finally:
    # Закрываем сокет
    s.close()
