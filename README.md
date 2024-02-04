# Devops-project

# Инструкции по запуску и тестированию приложения

1. Склонируйте репозиторий.
2. В каталоге с проектом выполните `docker-compose up -d` и `docker-compose build` nginx для запуска всех сервисов.
3. Откройте браузер и перейдите по адресу http://localhost:80 для доступа к веб-приложению через Nginx.

## Тестирование PHP скрипта

1. Зайдите в контейнер Apache: `docker exec -it apache-container bash`.
2. Внутри контейнера выполните `php test.php`.
3. Проверьте, что вывод содержит "Connected successfully to MySQL!".

## Дополнительные шаги

- Для остановки контейнеров выполните `docker-compose down`
