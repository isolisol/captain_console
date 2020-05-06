INSERT INTO pruduct_brand (name, logo) VALUES ('Sony', 'playstation_logo.png');
INSERT INTO pruduct_brand (name, logo) VALUES ('Nintendo', 'nintendo_logo.png');
INSERT INTO pruduct_brand (name, logo) VALUES ('Gameboy', 'gameboy_logo.png');
INSERT INTO pruduct_brand (name, logo) VALUES ('Xbox', 'xbox_logo.png');
INSERT INTO pruduct_brand (name, logo) VALUES ('GirlPower', 'xbox_logo.png');


INSERT INTO product_genre (name) VALUES ('Action');
INSERT INTO product_genre (name) VALUES ('Adventure');
INSERT INTO product_genre (name) VALUES ('Racing');
INSERT INTO product_genre (name) VALUES ('Puzzle');
INSERT INTO product_genre (name) VALUES ('Sports');


INSERT INTO product_console (name, price, description, release_date, brand_id)
    VALUES ('PlayStation 1', 129.95, 'PlayStation 1 description', '12-03-1994', 1);
INSERT INTO product_console (name, price, description, release_date, brand_id)
    VALUES ('PlayStation 2', 159.99, 'PlayStation 2 description', '03-04-2000', 1);
INSERT INTO product_console (name, price, description, release_date, brand_id)
    VALUES ('Nintendo NES', 89.95, 'Nintendo NES description', '07-15-1983', 2);
INSERT INTO product_console (name, price, description, release_date, brand_id)
    VALUES ('Nintendo 64', 105.99, 'Nintendo 64 description', '06-23-1996', 2);
INSERT INTO product_console (name, price, description, release_date, brand_id)
    VALUES ('Gameboy Advance SP', 120.95, 'Gameboy Advance SP description', '02-14-2003', 3);
INSERT INTO product_console (name, price, description, release_date, brand_id)
    VALUES ('Original Gameboy', 300.95, 'Original Gameboy description', '04-21-1989', 3);
INSERT INTO product_console (name, price, description, release_date, brand_id)
    VALUES ('Original Xbox', 190.95, 'Original Xbox description', '11-15-2001', 4);


INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('PS1 Original DualShock Controller', 49.95, 'PS1 Original DualShock Controller Description', '08-27-1997', 1);
INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('1MB PlayStation 1 Memory Card', 5.95, '1MB PlayStation 1 Memory Card Description', '12-12-1994', 1);
INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('PS2 Original DualShock Controller', 49.95, 'PS2 Original DualShock Controller Description', '03-04-2000', 1);
INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('16MB PlayStation 2 Memory Card', 14.95, '16MB PlayStation 2 Memory Card Description', '12-12-2000', 1);
INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('PS1 Original DualShock Controller', 49.95, 'PS1 Original DualShock Controller Description', '08-27-1997', 1);
INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('Original NES Nintendo Controller', 29.95, 'Original NES Nintendo Controller Description', '07-12-1983', 2);
INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('Original Xbox Controller', 35.95, 'Original Xbox Controller Description', '11-15-2001', 4);
INSERT INTO product_accessory (name, price, description, release_date, brand_id)
    VALUES ('Scart Cable', 5.95, 'Scart Cable Description', '12-09-2002', 5);




