<h1 align="center">Python Backend</h1>

## Описание

**Что из себя представляет сервер:**

Backend-сервер, отвечающий на http запросы, написан на фреймворке sanic

## Доступные запросы (routes):

<h3>HealthEndpoint</h3>
uri = '/'

Методы = GET, POST

Проверка работоспособности сервера

<h3>CreateUserEndpoint</h3>
uri = '/user'

Методы = POST

Создание пользователя для работы с сервером. Поля в body запроса:

<ul>
<li>login - str, обязательное</li>
<li>password - str, обязательное</li>
<li>first_name - str, обязательное</li>
<li>last_name - str, обязательное</li>
</ul>

<h3>AuthUserEndpoint</h3>
uri = '/user/auth'

Методы = POST

Авторизация пользователя. Поля в body запроса:

<ul>
<li>login - str, обязательное</li>
<li>password - str, обязательное</li>
</ul>

Полученный токен нужно вставить в заголовки последующих запросов, в которых требуется авторизация, в виде:
Authorization: "token"

<h3>UserEndpoint (user auth)</h3>
uri = '/user/{id пользователя}'

Методы = PATCH, DELETE

Редактирование или удаление пользователя (доступно только самому пользователю). Поля в body запроса PATCH:

<ul>
<li>first_name - str</li>
<li>last_name - str</li>
</ul>

<h3>AllUserEndpoint (user auth)</h3>
uri = '/user/all'

Методы = GET

Получение списка всех пользователей

<h3>CreateCustomerEndpoint</h3>
uri = /customers

Методы = POST, OPTIONS

Создание пользователей сайта (регистрация)

Необходимые поля в body:
<ul>
<li>first_name - str, обязательное</li>
<li>second_name - str, обязательное</li>
<li>last_name - str, обязательное</li>
<li>phone_number - str, обязательное</li>
<li>login - str</li>
<li>password - str</li>
<li>email - str</li>
<li>birthday - date</li>
</ul>

<h3>AuthCustomerEndpoint</h3>
uri = /customers/auth

Методы = POST, OPTIONS

Авторизация пользователя(клиента) сайта
<ul>
<li>login - str, обязательное</li>
<li>password - str, обязательное</li>
</ul>

Полученный токен нужно вставить в заголовки последующих запросов, в которых требуется авторизация, в виде:
Authorization: "token"

<h3>CustomerEndpoint (customer auth)</h3>
uri = /customers/<customer_id:int>

Методы = GET, PATCH, OPTIONS

Получение, изменение покупателя по его id (доступно только самому покупателю)

Доступные поля для PATCH:
<ul>
<li>first_name - str</li>
<li>second_name - str</li>
<li>last_name - str</li>
<li>login - str</li>
<li>password - str</li>
<li>email - str</li>
<li>birthday - date</li>
<li>phone_number - str</li>
</ul>

<h3>GetAllMaterialsEndpoint</h3>
uri = /materials/all

Методы = GET

Получение всех записей из таблицы materials

<h3>CreateMaterialEndpoint (user auth)</h3>
uri = /materials

Методы = POST, OPTIONS

Создание записей в таблице materials

Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>

<h3>MaterialEndpoint (user auth)</h3>
uri = /materials/<material_id:int>

Методы = GET, PATCH, DELETE

GET запрос позволит получить материал по его id, DELETE для удаления материала по его id, PATCH - изменение названия
материала

Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>

<h3>GetAllCategoriesEndpoint</h3>
uri = /categories/all

Методы = GET

Получение всех записей из таблицы categories

<h3>CreateCategoryEndpoint (user auth)</h3>
uri = /categories

Методы = POST, OPTIONS

Создание записей в таблице categories

Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>

<h3>CategoryEndpoint (user auth)</h3>
uri = /categories/<category_id:int>

Методы = GET (доступен без auth), PATCH, DELETE

GET запрос позволит получить категорию по ее id, DELETE для удаления категории по ее id, PATCH - изменение названия
категории

Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>

<h3>GetAllStructuresEndpoint</h3>
uri = /structures/all

Методы = GET

Получение всех записей из таблицы structures

<h3>CreateStructureEndpoint (user auth)</h3>
uri = /structures

Методы = POST, OPTIONS

Создание записей в таблице structures

Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>

<h3>StructureEndpoint (user auth)</h3>
uri = /structures/<structure_id:int>

Методы = GET, PATCH, DELETE, OPTIONS

GET запрос позволит получить состав по его id, DELETE для удаления состава по его id, PATCH - изменение названия
состава

Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>

<h3>GetAllProductsCareEndpoint</h3>
uri = /products_care/all

Методы = GET

Получение всех записей из таблицы products_care

<h3>CreateProductsCareEndpoint (user auth)</h3>
uri = /products_care

Методы = POST, OPTIONS

Создание записей в таблице products_care

Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>

<h3>ProductsCareEndpoint (user auth)</h3>
uri = /products_care/<products_care_id:int>

Методы = GET, PATCH, DELETE, OPTIONS

GET запрос позволит получить информацию об уходе по его id, DELETE для удаления информации об уходе по его id, PATCH - изменение 
информации об уходе

Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>

<h3>GetAllSizesEndpoint</h3>
uri = /sizes/all

Методы = GET

Получение всех записей из таблицы sizes

<h3>CreateSizeEndpoint (user auth)</h3>
uri = /sizes

Методы = POST, OPTIONS

Создание записей в таблице sizes

Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>

<h3>SizeEndpoint (user auth)</h3>
uri = /sizes/<size_id:int>

Методы = GET, PATCH, DELETE, OPTIONS

GET запрос позволит получить размер по его id, DELETE для удаления размера по его id, PATCH - изменение 
размера

Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>

<h3>GetAllColorsEndpoint</h3>
uri = /colors/all

Методы = GET

Получение всех записей из таблицы colors

<h3>CreateColorEndpoint (user auth)</h3>
uri = /colors

Методы = POST, OPTIONS

Создание записей в таблице colors

Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
<li>code - str, обязательное</li>
</ul>

<h3>ColorEndpoint (user auth)</h3>
uri = /colors/<color_id:int>

Методы = GET, PATCH, DELETE, OPTIONS

GET запрос позволит получить цвет по его id, DELETE для удаления цвета по его id, PATCH - изменение 
цвета

Доступные поля для PATCH:
<ul>
<li>name - str</li>
<li>code - str</li>
</ul>

<h3>GetAllStatusesEndpoint</h3>
uri = /statuses/all

Методы = GET

Получение всех записей из таблицы statuses

<h3>CreateStatusEndpoint (user auth)</h3>
uri = /statuses

Методы = POST, OPTIONS

Создание записей в таблице statuses

Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>

<h3>StatusEndpoint (user auth)</h3>
uri = /statuses/<status_id:int>

Методы = GET, PATCH, DELETE, OPTIONS

GET запрос позволит получить статус по его id, DELETE для удаления статуса по его id, PATCH - изменение 
статуса

Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>

## Об архитектуре сервера

<img src="https://habrastorage.org/r/w1560/files/23a/0de/4d9/23a0de4d93d747c89f1e216077c2d604.jpg">
Когда на сервер приходит request, он проходит следующий путь:
<ul>
<li>transport (sanic)</li>
<li>API (marshmallow)</li>
<li>service (endpoint)</li>
<li>DB (model)</li>
<li>DB (query)</li>
</ul>

Response от сервера проходит этот путь в обратном направлении.

Подробнее про чистую архитектуру можно почитать [тут](https://habr.com/ru/post/269589/)

## Установка и запуск сервера

Необходимо, но не обязательно, в переменных окружение указать следующие параметры:
<ul>
<li>host - str</li>
<li>port - int</li>
<li>workers - int</li>
<li>debug - bool</li>
<li>secret - str</li>
<li>ipinfo_token - токен для библиотеки ipinfo</li>
</ul>

Затем применить последнюю миграцию и создать БД командой:

```
alembic upgrade head
```

А после:

```
python main.py
```
