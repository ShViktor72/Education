use shop;

insert into order_products (order_id, product_id, `count`) values (2, 3, 2);
insert into order_products (order_id, product_id, `count`) values (2, 4, 3);


SELECT * FROM shop.`order`;





SELECT sum(price * `count`) as total_price from `order` 
	inner join order_products on order_products.order_id = `order`.id
    inner join product on product.id = order_products.product_id
    where `order`.id = 2;
    
    
    
SELECT `order`.user_name, sum(price * `count`) as total_price  from `order` 
	inner join order_products on order_products.order_id = `order`.id
    inner join product on product.id = order_products.product_id
    group by `order`.user_name;
    
SELECT `order`.user_name, max(price), sum(`count`) as order_count from `order` 
	inner join order_products on order_products.order_id = `order`.id
    inner join product on product.id = order_products.product_id
    -- where user_name like 'В%'
    
    group by `order`.user_name
    having order_count >= 5; 
   
    
    