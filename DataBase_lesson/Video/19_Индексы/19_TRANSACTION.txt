insert into `shop`.`user_bank_account` (id, money, user_name) values ('1', '100', 'Дмитрий');
insert into `shop`.`user_bank_account` (id, money, user_name) values ('2', '200', 'Евгений');

select * from `shop`.`user_bank_account`;

start transaction;
	update `shop`.`user_bank_account` set money = money - 100 where id = 1;
    update `shop`.`user_bank_account` set money = money + 100 where id = 2;
commit;