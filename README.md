# Тестовое задание Веклич Егор Александрович

## Запуск

```
docker compose up
```
Перед запуском сервиса необходимо заполнить создать файл .env и заполнить его по образцу [env.sample](env.sample)

При этом менять уже заполненные значения не нужно.



### ТЗ (помечены выполненные доп задания)
Написать docker compose, в котором работают:
web приложение, на FastApi. У приложения должно быть несколько ендпоинтов:
1) GET 'api/v1/messages/' показывает список всех сообщений;
2) POST 'api/v1/message/' позволяет написать сообщение;
Веб сервер должен быть Nginx.
mongo как бд для сообщений.
Телеграм бот (aiogram3), который показывает сообщения и позволяет создать сообщение самому.
Будет плюсом:
1) Добавление кэширования при помощи Redis (кеш стирается, когда появляется новое сообщение) ✅ 
2) Развертывание на удалённом сервере и добавление ssl через certbot. 
3) Реализовать код так, чтобы было видно, кто написал сообщение. ✅
4) Добавление пагинации. ✅

Проект залить на Github с подробно описанным Readme

 