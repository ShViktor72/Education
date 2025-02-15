use shop;

select * from product_type where id = 1
union
select * from product_type where id = 2;


select * from `order`
	left join order_products on order_products.order_id = `order`.id
    left join product on order_products.product_id = product.id
    
union

select * from `order`	
	inner join order_products on order_products.order_id = `order`.id
    right join product on order_products.product_id = product.id
    where `order`.id is null;
    