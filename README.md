<h1 align="center">Python Backend</h1>

## Описание

**Что из себя представляет сервер:**

Backend-сервер, отвечающий на http запросы, написан на фреймворке sanic<br/>
Схема данных:
![Иллюстрация к проекту](https://raw.githubusercontent.com/iparinile/backend_vinterr/master/readme_images/vinterr%20-%20public.png)
____
## Доступные запросы (routes):
<details>
<summary><b><u>HealthEndpoint</u></b></summary>
uri = '/'<br/>
Методы = GET, POST<br/>
Проверка работоспособности сервера
</details>

<h3>User</h3>
<details>
<summary><b><u>CreateUserEndpoint</u></b></summary>
uri = '/user'<br/>
Методы = POST<br/>
Создание пользователя для работы с сервером. Поля в body запроса:
<ul>
<li>login - str, обязательное</li>
<li>password - str, обязательное</li>
<li>first_name - str, обязательное</li>
<li>last_name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>AuthUserEndpoint</u></b></summary>
uri = '/user/auth'<br/>
Методы = POST<br/>
Авторизация пользователя. Поля в body запроса:
<ul>
<li>login - str, обязательное</li>
<li>password - str, обязательное</li>
</ul>

Полученный токен нужно вставить в заголовки последующих запросов, в которых требуется авторизация, в виде:
Authorization: "token"
</details>

<details>
<summary><b><u>UserEndpoint (user auth)</u></b></summary>
uri = '/user/{id пользователя}'<br/>
Методы = PATCH, DELETE<br/>
Редактирование или удаление пользователя (доступно только самому пользователю). Поля в body запроса PATCH:
<ul>
<li>first_name - str</li>
<li>last_name - str</li>
</ul>
</details>

<details>
<summary><b><u>AllUserEndpoint (user auth)</u></b></summary>
uri = '/user/all'<br/>
Методы = GET<br/>
Получение списка всех пользователей
</details>

<h3>Customer</h3>
<details>
<summary><b><u>CreateCustomerEndpoint</u></b></summary>
uri = /customers<br/>
Методы = POST, OPTIONS<br/>
Создание пользователей сайта (регистрация)<br/>
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
</details>

<details>
<summary><b><u>AuthCustomerEndpoint</u></b></summary>
uri = /customers/auth<br/>
Методы = POST, OPTIONS<br/>
Авторизация пользователя(клиента) сайта
<ul>
<li>login - str, обязательное</li>
<li>password - str, обязательное</li>
</ul>
Полученный токен нужно вставить в заголовки последующих запросов, в которых требуется авторизация, в виде:<br/>
Authorization: "token"
</details>

<details>
<summary><b><u>CustomerEndpoint (customer auth)</u></b></summary>
uri = /customers/<customer_id:int><br/>
Методы = GET, PATCH, OPTIONS<br/>
Получение, изменение покупателя по его id (доступно только самому покупателю)<br/>
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
</details>

<h3>Materials</h3>
<details>
<summary><b><u>GetAllMaterialsEndpoint</u></b></summary>
uri = /materials/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы materials
</details>

<details>
<summary><b><u>CreateMaterialEndpoint</u></b></summary>
uri = /materials<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице materials<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>MaterialEndpoint</u></b></summary>
uri = /materials/<material_id:int><br/>
Методы = GET, PATCH, DELETE<br/>
GET запрос позволит получить материал по его id, DELETE для удаления материала по его id, PATCH - изменение названия
материала<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>
</details>

<h3>Categories</h3>
<details>
<summary><b><u>GetAllCategoriesEndpoint</u></b></summary>
uri = /categories/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы categories
</details>

<details>
<summary><b><u>CreateCategoryEndpoint</u></b></summary>
uri = /categories<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице categories<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>CategoryEndpoint (user auth)</u></b></summary>
uri = /categories/<category_id:int><br/>
Методы = GET (доступен без auth), PATCH, DELETE<br/>
GET запрос позволит получить категорию по ее id, DELETE для удаления категории по ее id, PATCH - изменение названия
категории<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>
</details>

<h3>Structures</h3>
<details>
<summary><b><u>GetAllStructuresEndpoint</u></b></summary>
uri = /structures/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы structures
</details>

<details>
<summary><b><u>CreateStructureEndpoint (user auth)</u></b></summary>
uri = /structures<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице structures<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>StructureEndpoint (user auth)</u></b></summary>
uri = /structures/<structure_id:int><br/>
Методы = GET, PATCH, DELETE, OPTIONS<br/>
GET запрос позволит получить состав по его id, DELETE для удаления состава по его id, PATCH - изменение названия
состава<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>
</details>

<h3>Products_care</h3>
<details>
<summary><b><u>GetAllProductsCareEndpoint</u></b></summary>
uri = /products_care/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы products_care
</details>

<details>
<summary><b><u>CreateProductsCareEndpoint (user auth)</u></b></summary>
uri = /products_care<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице products_care<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>ProductsCareEndpoint (user auth)</u></b></summary>
uri = /products_care/<products_care_id:int><br/>
Методы = GET, PATCH, DELETE, OPTIONS<br/>
GET запрос позволит получить информацию об уходе по его id, DELETE для удаления информации об уходе по его id, PATCH - изменение 
информации об уходе<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>
</details>

<h3>Sizes</h3>
<details>
<summary><b><u>GetAllSizesEndpoint</u></b></summary>
uri = /sizes/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы sizes
</details>

<details>
<summary><b><u>CreateSizeEndpoint (user auth)</u></b></summary>
uri = /sizes<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице sizes<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>SizeEndpoint (user auth)</u></b></summary>
uri = /sizes/<size_id:int><br/>
Методы = GET, PATCH, DELETE, OPTIONS<br/>
GET запрос позволит получить размер по его id, DELETE для удаления размера по его id, PATCH - изменение 
размера<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>
</details>

<h3>Colors</h3>
<details>
<summary><b><u>GetAllColorsEndpoint</u></b></summary>
uri = /colors/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы colors
</details>

<details>
<summary><b><u>CreateColorEndpoint (user auth)</u></b></summary>
uri = /colors<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице colors<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
<li>code - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>ColorEndpoint (user auth)</u></b></summary>
uri = /colors/<color_id:int><br/>
Методы = GET, PATCH, DELETE, OPTIONS<br/>
GET запрос позволит получить цвет по его id, DELETE для удаления цвета по его id, PATCH - изменение 
цвета<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
<li>code - str</li>
</ul>
</details>

<h3>Statuses</h3>
<details>
<summary><b><u>GetAllStatusesEndpoint</u></b></summary>
uri = /statuses/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы statuses
</details>

<details>
<summary><b><u>CreateStatusEndpoint (user auth)</u></b></summary>
uri = /statuses<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице statuses<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>StatusEndpoint (user auth)</u></b></summary>
uri = /statuses/<status_id:int><br/>
Методы = GET, PATCH, DELETE, OPTIONS<br/>
GET запрос позволит получить статус по его id, DELETE для удаления статуса по его id, PATCH - изменение 
статуса<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>
</details>

<h3>Goods</h3>
<details>
<summary><b><u>CreateGoodEndpoint (user auth)</u></b></summary>
Создание номенклатуры<br/>
uri = /goods <br/>
Методы = POST, OPTIONS<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
<li>article - str, обязательное</li>
<li>good_1c_id - str</li>
<li>category_id - int, обязательное</li>
<li>barcode - str</li>
<li>structure_id - int, обязательное</li>
<li>products_care_id - int</li>
<li>description - str, обязательное</li>
<li>is_visible - bool, default=True</li>
<li>weight - float, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>GetAllGoodsEndpoint</u></b></summary>
Получение информации обо всех товарах и сопутствующих данных, необходимых для их отображения на сайте<br/>
uri = /goods/all <br/>
Методы = GET
</details>

<details>
<summary><b><u>GoodEndpoint (user auth)</u></b></summary>
uri = /goods/<good_id:int> <br/>
Методы = GET, PATCH, DELETE, OPTIONS<br/>
Получение записей из таблицы goods, их правка и удаление, в зависимости от метода запроса<br/>
Доступные поля PATCH запроса:
<ul>
<li>name - str</li>
<li>article - str</li>
<li>good_1c_id - str</li>
<li>category_id - int</li>
<li>barcode - str</li>
<li>structure_id - int</li>
<li>products_care_id - int</li>
<li>description - str</li>
<li>is_visible - bool</li>
<li>weight - float</li>
</ul>
</details>

<details>
<summary><b><u>UpdateWeightsEndpoint (user auth)</u></b></summary>
uri = /goods/update_weights <br/>
Методы = POST, OPTIONS<br/>
Обновление данных по весу товаров из отчета 1С<br/>
Файл передается в form-data запроса с наименованием "file"
</details>

<h3>Variations</h3>
<details>
<summary><b><u>GetVariationsForGoodEndpoint</u></b></summary>
Получение всех вариаций для конкретного товара<br/>
uri = /goods/<good_id:int>/variations <br/>
Методы = GET
</details>

<details>
<summary><b><u>CreateVariationEndpoint (user auth)</u></b></summary>
Создание записи в таблице variations<br/>
uri = /variations <br/>
Методы = POST, OPTIONS<br/>
Поля POST запроса:
<ul>
<li>good_id - int, обязательное</li>
<li>name - str, обязательное</li>
<li>color_id - int, обязательное</li>
<li>size_id - int, обязательное</li>
<li>price - int, обязательное</li>
<li>discounted_price - int</li>
<li>variation_1c_id - str</li>
<li>amount - int, обязательное</li>
<li>barcode - str</li>
<li>is_sale - bool</li>
<li>is_new - bool</li>
<li>is_default - bool</li>
</ul>
</details>

<details>
<summary><b><u>GetAllVariationsEndpoint</u></b></summary>
Получение всех записей из таблицы variations<br/>
uri = /variations/all <br/>
Методы = GET
</details>

<details>
<summary><b><u>GetVariationEndpoint</u></b></summary>
Получение информации об отдельной вариации<br/>
uri = /variations/<variation_id:int> <br/>
Методы = GET
</details>

<details>
<summary><b><u>VariationEndpoint (user auth)</u></b></summary>
Изменение и удаление записей из таблицы variations<br/>
uri = /variations/<variation_id:int> <br/>
Методы = PATCH, DELETE, OPTIONS
</details>

<details>
<summary><b><u>UpdateRemainsEndpoint (user auth)</u></b></summary>
Обновление остатков вариаций с помощью отчета об остатках из 1С<br/>
uri = /variations/update_remains <br/>
Методы = POST, OPTIONS
Файл передается в form-data запроса с наименованием "file"
</details>

<details>
<summary><b><u>AutoUpdateRemainsEndpoint (user auth)</u></b></summary>
Обновление остатков вариаций из JSON<br/>
uri = /variations/auto_update_remains<br/>
Методы = POST, OPTIONS<br/>
Ожидается массив объектов, с данными об остатках. Поля объектов:
<ul>
<li>one_c_id - str, обязательное</li>
<li>amount - int, обязательное</li>
</ul>
</details>

<h3>Images</h3>
<details>
<summary><b><u>ImageEndpoint</u></b></summary>
Получение изображений и их удаление(user auth) по ссылке<br/>
uri = /images/<img_path:path> <br/>
Методы = GET, DELETE
</details>

<details>
<summary><b><u>CreateImageEndpoint (user auth)</u></b></summary>
Загрузка изображений с помощью form-data. Наименование поля - "image"<br/>
uri = /images <br/>
Методы = POST, OPTIONS
</details>

<h3>Orders</h3>
<details>
<summary><b><u>CreateOrderEndpoint</u></b></summary>
Создание заказа<br/>
uri = /orders <br/>
Методы = POST, OPTIONS<br/>
Поля POST запроса:
<ul>
<li>first_name - str, обязательное</li>
<li>second_name - str, обязательное</li>
<li>last_name - str</li>
<li>phone_number - str, обязательное</li>
<li>email - str, обязательное</li>
<li>status_id - int, обязательное</li>
<li>delivery_type_id - int, обязательное</li>
<li>city - str, обязательное</li>
<li>street - str, обязательное</li>
<li>house_number - str</li>
<li>apartment - str</li>
<li>other_info - str</li>
<li>delivery_address - str, обязательное</li>
<li>delivery_cost - float, обязательное</li>
<li>is_cash_payment - bool</li>
<li>variations - list, обязательное<br/>
Поля списка variations:
<ul>
<li>variation_id - int, обязательное</li>
<li>amount - int, обязательное</li>
<li>current_price - int, обязательное</li>
</ul></li>
</ul>
</details>

<details>
<summary><b><u>GetAllOrdersEndpoint (user auth)</u></b></summary>
Получение всех заказов с сопутствующей информацией <br/>
uri = /orders/all <br/>
Методы = GET, OPTIONS
</details>

<details>
<summary><b><u>OrderEndpoint (user auth)</u></b></summary>
Получение отдельного заказа или его изменение<br/>
uri = /orders/<order_id:int> <br/>
Методы = GET, PATCH, OPTIONS<br/>
Доступные поля в PATCH:
<ul>
<li>id - int</li>
<li>is_payed - bool</li>
<li>customer_id - int</li>
<li>status_id - int</li>
<li>delivery_type_id - int</li>
<li>sberbank_id - str</li>
<li>delivery_address - str</li>
<li>delivery_cost - float</li>
</ul>
</details>

<details>
<summary><b><u>GetAllStatusChangesForOrderEndpoint (user auth)</u></b></summary>
Получение всех изменений статусов конкретного заказа <br/>
uri = /orders/<order_id:int>/status_changes <br/>
Методы = GET
</details>

<details>
<summary><b><u>GetAllStatusChangesEndpoint (user auth)</u></b></summary>
Получение всех изменений статусов <br/>
uri = /status_changes/all <br/>
Методы = GET
</details>

<h3>Payments</h3>
<details>
<summary><b><u>RegisterPaymentsEndpoint</u></b></summary>
Регистрация оплаты для получения ссылки на платежный шлюз <br/>
uri = /register_payment <br/>
Методы = POST, OPTIONS
Доступные поля в POST:
<ul>
<li>order_id - int, обязательное</li>
<li>return_url - str, обязательное</li>
<li>fail_url - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>GetStatusPaymentsEndpoint</u></b></summary>
Получение статуса оплаты конкретного заказа по sberbank_id <br/>
uri = /orders/<sberbank_order_id:uuid>/status_payment <br/>
Методы = GET
</details>

<h3>Contact_forms (beta)</h3>
<details>
<summary><b><u>CreateContactFormEndpoint</u></b></summary>
Получение информации с формы обратной связи <br/>
uri = /contact_forms <br/>
Методы = POST, OPTIONS
Доступные поля в POST:
<ul>
<li>customer_name - str, обязательное</li>
<li>phone_number - str, обязательное</li>
<li>text - str</li>
<li>email - str</li>
</ul>
</details>

<h3>Delivery_types</h3>
<details>
<summary><b><u>GetAllDeliveryTypesEndpoint</u></b></summary>
uri = /delivery_types/all<br/>
Методы = GET<br/>
Получение всех записей из таблицы delivery_types
</details>

<details>
<summary><b><u>CreateDeliveryTypeEndpoint (user auth)</u></b></summary>
uri = /delivery_types<br/>
Методы = POST, OPTIONS<br/>
Создание записей в таблице delivery_types<br/>
Доступные поля для POST:
<ul>
<li>name - str, обязательное</li>
</ul>
</details>

<details>
<summary><b><u>DeliveryTypeEndpoint (user auth)</u></b></summary>
uri = /statuses/<status_id:int><br/>
Методы = GET, PATCH, DELETE, OPTIONS<br/>
GET запрос позволит получить тип доставки по его id, DELETE для удаления типа доставки по его id, PATCH - изменение 
типа доставки<br/>
Доступные поля для PATCH:
<ul>
<li>name - str</li>
</ul>
</details>

<h3>Telegram_users</h3>
<details>
<summary><b><u>CreateTelegramUserEndpoint (telegram auth token)</u></b></summary>
uri = /telegram_users<br/>
Методы = POST<br/>
Создание пользователя бота для подбора ассортимента в telegram
</details>

<details>
<summary><b><u>TelegramUserEndpoint (telegram auth token)</u></b></summary>
uri = /telegram_users/<telegram_user_id:int><br/>
Методы = PATCH, GET<br/>
Получение отдельных пользователей бота и их изменение<br/>
Доступные поля для PATCH:
<ul>
<li>chat_id - int</li>
<li>status_id - int</li>
</ul>
</details>

____

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
____
## Установка и запуск сервера

Переменные окружения для работы сервера:
<ul>
<li>host - str, адрес сервера</li>
<li>db_name - str, наименование используемой БД</li>
<li>db_host - str, адрес БД</li>
<li>db_user - str, пользователь БД с необходимым доступом</li>
<li>password - str, пароль вышеуказанного пользователя БД</li>
<li>telegram_token - str, токен доступа к телеграм боту</li>
<li>telegram_chat_id - str, id чата с заказами</li>
<li>telegram_errors_chat_id - str, id чата для вывода ошибок</li>
<li>telegram_secret_password - str, секретный пароль доступа бота телеграм</li>
<li>email_server - str, сервер для отправки email писем</li>
<li>email_port - str, его порт</li>
<li>email_from - str, адрес отправителя</li>
<li>email_to - str, адрес на который отправлять информацию о заказах</li>
<li>email_passwd - str, пароль от адреса отправителя</li>
<li>debug - bool, режим работы сервера</li>
<li>sber_username - str, логин для платежного шлюза сбербанка</li>
<li>sber_password - str, пароль от платежного шлюза сбербанка</li>
</ul>

Применение изменений в БД:

```
alembic revision --autogenerate -m '<описание изменений>'

alembic upgrade head
```

Запуск сервера:

```
python main.py
```
