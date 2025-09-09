# docker-script

## Аргументы
- Добавлена поддержка аргументов для скрипта

```bash
python main.py function arg1 ...
```

## Фукнции

- `version` Смотрим на версию **Docker**, используя **Docker API**

```bash
python main.py version
```

Функция обрабатывает две ошибки

- **APIError** Ошибка связанная с самим **Docker API**
- **DockerException** Ошибка связанная с самим **Docker**, например если она не установлена

## Тесты

- Добавлен **unit** тест

```bash
python -m unittest tests/unit_test.py
```

> Нужно запускать из корня репозитория
