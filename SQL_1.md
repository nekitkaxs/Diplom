Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

Запрос: 
SELECT C.login, COUNT(O.id) 
FROM "Couriers" C JOIN "Orders" O ON C.id = O."courierId" 
WHERE O."inDelivery" = TRUE 
GROUP BY C.login;

Результат запроса:![alt text](<Задание 1.png>)