# -
2-я практическая работа
"Сокеты TCP и UDP"

Клиент формирует пакет UDP по определённому принципу и отправляет его на сервер.

Сервер принимает пакет UDP, проводит над ним действие и отправляет обратно, попутно печатает, от кого пришёл пакет (IP-адрес клиента)

Клиент принимает пакет UDP и печатает его содержимое

При запуске обеих программ клиент, зная адрес сервера, готовится принимать udp с любых адресов (не только перечисленных в ipconfig данной системы, т.е.) через порт 11101, и готовится отсылать сообщения на 11100 порт сервера.

Соответственно, для этого создаются два сокета, один из которых(принимающий) биндит порт 11101, т.е. ассоциирует себя с ним для дальнейшей работы.

Далее в бесконечном цикле идет ввод и кодирование в utf-8 сообщения, а после отправка средствами ранее отведенного для этого сокета. Затем идет ожидание ответа от сервера, который после и выводится вместе с временем прибытия ответа клиенту.

Сервер отличается от клиента только наличием у него функции-обработчика входящих сообщений, поменявшимися местами портами приема себе и передачи клиенту, и частично переделанным (под постоянное ожидание без ввода) бесконечным циклом и выводом.
