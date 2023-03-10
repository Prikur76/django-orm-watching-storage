# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Сияние".\
Если вы попали случайно, то не сможете запустить, ввиду отсутствия доступа к базе данных.\
Можете использовать код верстки или посмотреть реализацию запросов к БД. 

### Как работает
Позволяет:
- просматривать список сотрудников с активными картами доступа, кодом пропуска и 
датой регистрации пропуска;
- получать список лиц, находящихся в хранилище, с информацией о продолжительности пребывания.
Если длительность пребывания составляет более 10 минут, отметка **`True`** в соответствующем столбце 
обратит внимание охранника.
- список визитов каждого посетителя в хранилище, с информацией о продолжительности визита и отметкой, 
если пребывание длилось более 10 минут.

### Запуск программы
Для запуска у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите сервер командой `python3 manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

### Переменные окружения

Часть настроек берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по умолчанию.

Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_URL` -  url адрес для подключения к БД в формате `postgres://USER:PASSWORD@HOST:PORT/NAME` 

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).

### Лицензия

Этот проект лицензирован по лицензии MIT - подробности см. в файле [ЛИЦЕНЗИЯ](LICENSE).
