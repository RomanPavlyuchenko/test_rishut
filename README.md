##  Команды для запуска проекта
Подготовка к запуску
```
apt-get update
apt-get install -y docker-compose git
git clone https://github.com/RomanPavlyuchenko/test_rishut.git
cd test_rishut
cp .env.pub .env
```
для запуска без nginx и gunicorn
```
docker-compose up
```
для запуска с nginx и gunicorn
```
docker-compose -f docker-compose.prod.yml up
```



## Описание
Проект запущен на сервере и доступен по адресу <http://romanpavliuchenko.ru>  
Список эндпоинтов: [Postman Collection](https://elements.getpostman.com/redirect?entityId=10861528-9bf9e586-3ea7-4abb-bbb6-9b426ff3582b&entityType=collection)  
base_api для проекта: http://romanpavliuchenko.ru/api/orders  
[Ссылка на админку](http://romanpavliuchenko.ru/admin)   
- Логин: admin
- Пароль: test_rishut

Дефолтная струткура проекта изменена для улучшения масштабирования и более удобного рефакторинга  
## Что сделано из ТЗ
## Обязательные задачи
- создана Django Модель Item с полями (name, description, price)
- API с двумя методами:
    - [GET /buy/{id}](http://romanpavliuchenko.ru/api/orders/items/buy/1/), c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe выполняется запрос stripe.checkout.Session.create(...) и полученный session.id выдается в результате запроса
    - [GET /item/{id}](http://romanpavliuchenko.ru/api/orders/items/item/1/), c помощью которого можно получить простейшую HTML страницу, на которой есть информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходит редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
- Залито решение на Github, описан запуск в Readme.md
- Опубликовано решение, чтобы его можно было быстро и легко протестировать. 
## Бонусные задачи
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Запуск приложения на удаленном сервере, доступном для тестирования
- Модель [Order](http://romanpavliuchenko.ru/api/orders/orders/), в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- Модели Discount, Tax, которые можно прикрепить к модели [Order](http://romanpavliuchenko.ru/api/orders/orders/pay/1/) и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 

## Что сделано дополнительно
- Запуск используя docker-compose
- Настроен Nginx
- Настроен Gunicorn
- Краткая документация API
