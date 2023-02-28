# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Сияние".\
Если вы попали случайно, то не сможете запустить, ввиду отсутствия доступа к базе данных.\
Можете использовать код верстки или посмотреть реализацию запросов к БД. 

## Как работает
Позволяет:
- просматривать список сотрудников с активными картами доступа, кодом пропуска и 
датой регистрации пропуска;
- получать список лиц, находящихся в хранилище, с информацией о продолжительности пребывания.
Если длительность пребывания составляет более 10 минут, отметка **`True`** в соответствующем столбце 
обратит внимание охранника.
- список визитов каждого посетителя в хранилище, с информацией о продолжительности визита и отметкой, 
если пребывание длилось более 10 минут.

### Как установить

* Python3 должен уже быть установлен.
* Для изоляции проекта рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html).
* Чтобы развернуть зависимости, используйте **`pip`** (или **`pip3`**, если есть конфликт с Python2):

```bash
$ pip install -r requirements.txt
```

### Авторизация
Для полноценного запуска необходимо записать в файл **`.env`** 
следующие переменные окружения: **`ENGINE, HOST, PORT, NAME, USER, PASSWORD, SECRET_KEY, DEBUG`**.
Например, **`DEBUG=True`**.

### Запуск программы

Запуск программы осуществляется в терминале, из виртуального окружения, следующей командой:

```bash
$ python manage.py runserver 0.0.0.0:8000
```
После чего в браузере введите адрес: **`localhost:8000`**.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).

### Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. в файле [ЛИЦЕНЗИЯ](LICENSE).
