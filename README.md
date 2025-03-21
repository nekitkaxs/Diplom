Дипломный проект на курсе Инженер по тестированию (расширенный)
Яндекс Практикум
Описание проекта:

Практический блок: первая часть
1. Тестирование функциональности веб-приложения. 
Чек-лист для функционального тестирования web приложения. Результаты в итоговом отчете (pdf файл в репозитории) 

2. Ретест багов в мобильном приложении. Результаты в итоговом отчете (pdf файл в репозитории) 

3. Регрессионное тестирование мобильного приложения по готовым тест-кейсам. Результаты в итоговом отчете (pdf файл в репозитории)

Практический блок: вторая часть
Работа с базой данных

Задание 1.
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных. Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

Для выполнения задания необходимо подключиться к базе данных.
Делать это будем следующим образом:
1) Открываем консоль cygwin;
2) Генерируем ключи для сервера - "ssh-keygen -t rsa";
3) Выводим публичный ключ - "cat ~/.ssh/id_rsa.pub";
4) Публичный ключ используем для запуска удаленного сервера;
5) Подключаемся к удаленному серверу - ssh 894343bc-f2a5-40a8-b171-9899e279f5cf@serverhub.praktikum-services.ru -4554;
6) Доступ к базе осуществляется с помощью команды "psql -U morty -d scooter_rent". Пароль: smith;
7) Создаем курьеров и заказы через запросы в Postman (как в первом практическом блоке);
8) При помощи Android Studio заходим в приложение "Scooter", авторизуемся за курьеров и принимаем заказы;
9) Делаем SQL запрос.

Запрос:
SELECT C.login, COUNT(O.id) 
FROM "Couriers" C JOIN "Orders" O ON C.id = O."courierId" 
WHERE O."inDelivery" = TRUE 
GROUP BY C.login;

Скриншот результата запроса Задание 1.png (директория /Diplom)

Задание 2.
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно. Для этого: выведи все трекеры заказов и их статусы. Статусы определяются по следующему правилу: Если поле finished == true, то вывести статус 2. Если поле canсelled == true, то вывести статус -1. Если поле inDelivery == true, то вывести статус 1. Для остальных случаев вывести 0.

Для выполнения задания №2 необходимо проделать шаги, как для задания №1.

Запрос:
SELECT track, (CASE WHEN finished=true THEN 2 WHEN cancelled=true THEN -1 WHEN "inDelivery"=true THEN 1 ELSE 0 END) AS status 
FROM "Orders";

Скриншот результата запроса Задание 2.png (директория /Diplom)

5. Автоматизация теста.
Для запуска теста необходимо в файл configuration скопировить URL стенда https://d1b5fdb0-9707-45f6-bb90-500d5b7ca0ff.serverhub.praktikum-services.ru

Для запуска теста воспользуемся pycharm.

Результаты теста приложены в виде скриншота test_scooter.png (директория /Diplom)

После выполнения тестов загружаем данные на Github.