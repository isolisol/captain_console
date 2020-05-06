INSERT INTO product_brand (name, logo) VALUES ('Sony', 'playstation_logo.png');
INSERT INTO product_brand (name, logo) VALUES ('Nintendo', 'nintendo_logo.png');
INSERT INTO product_brand (name, logo) VALUES ('Gameboy', 'gameboy_logo.png');
INSERT INTO product_brand (name, logo) VALUES ('Xbox', 'xbox_logo.png');
INSERT INTO product_brand (name, logo) VALUES ('Sega', 'sega_logo.png');
INSERT INTO product_brand (name, logo) VALUES ('Game Freak', 'game_freak_logo.png');


INSERT INTO product_genre (name) VALUES ('Action');
INSERT INTO product_genre (name) VALUES ('Adventure');
INSERT INTO product_genre (name) VALUES ('Racing');
INSERT INTO product_genre (name) VALUES ('Puzzle');
INSERT INTO product_genre (name) VALUES ('Sports');


INSERT INTO product_console (name, price, description, release_date, brand_id, image)
    VALUES ('PlayStation 1', 129.95, 'PlayStation 1 description', '12-03-1994', 1, '');
INSERT INTO product_console (name, price, description, release_date, brand_id, image)
    VALUES ('PlayStation 2', 159.99, 'PlayStation 2 description', '03-04-2000', 1, '');
INSERT INTO product_console (name, price, description, release_date, brand_id, image)
    VALUES ('Nintendo NES', 89.95, 'Nintendo NES description', '07-15-1983', 2, '');
INSERT INTO product_console (name, price, description, release_date, brand_id, image)
    VALUES ('Nintendo 64', 105.99, 'Nintendo 64 description', '06-23-1996', 2, '');
INSERT INTO product_console (name, price, description, release_date, brand_id, image)
    VALUES ('Gameboy Advance SP', 120.95, 'Gameboy Advance SP description', '02-14-2003', 3, '');
INSERT INTO product_console (name, price, description, release_date, brand_id, image)
    VALUES ('Original Gameboy', 300.95, 'Original Gameboy description', '04-21-1989', 3, '');
INSERT INTO product_console (name, price, description, release_date, brand_id, image)
    VALUES ('Original Xbox', 190.95, 'Original Xbox description', '11-15-2001', 4, '');


INSERT INTO product_accessory (name, price, description, release_date, brand_id, image)
    VALUES ('PS1 Original DualShock Controller', 49.95, 'PS1 Original DualShock Controller Description', '08-27-1997', 1, '');
INSERT INTO product_accessory (name, price, description, release_date, brand_id, image)
    VALUES ('1MB PlayStation 1 Memory Card', 5.95, '1MB PlayStation 1 Memory Card Description', '12-12-1994', 1, '');
INSERT INTO product_accessory (name, price, description, release_date, brand_id, image)
    VALUES ('PS2 Original DualShock Controller', 49.95, 'PS2 Original DualShock Controller Description', '03-04-2000', 1, '');
INSERT INTO product_accessory (name, price, description, release_date, brand_id, image)
    VALUES ('8MB PlayStation 2 Memory Card', 14.95, '8MB PlayStation 2 Memory Card Description', '12-12-2000', 1, '');
INSERT INTO product_accessory (name, price, description, release_date, brand_id, image)
    VALUES ('Original NES Nintendo Controller', 29.95, 'Original NES Nintendo Controller Description', '07-12-1983', 2, '');
INSERT INTO product_accessory (name, price, description, release_date, brand_id, image)
    VALUES ('Original Xbox Controller', 35.95, 'Original Xbox Controller Description', '11-15-2001', 4, '');
INSERT INTO product_accessory (name, price, description, release_date, brand_id, image)
    VALUES ('Scart Cable', 5.95, 'Scart Cable Description', '12-09-2002', 5, '');


INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('Sonic And The HedgeHog 2', 19.95, 'Sonic And The HedgeHog videogame for playstation 1', '11-21-1992', 3, 5, 1, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('Mario Kart 64', 155.95, 'Mario Kart 64 for nintendo 64', '12-14-1996', 3, 2, 4, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('Grand Theft Auto San Andreas', 29.99, 'Grand Theft Auto San Andreas VideoGame for Xbox original', '10-26-2004', 18, 4, 7, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('SOCOM US Navy Seals', 2.24, 'SOCOM US Navy Seals VideoGame for PlayStation 2', '08-27-2002', 18, 1, 2, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('Tetris', 18.44, 'Tetris VideoGame for Nintendo NES', '06-06-1984', 3, 2, 3, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('Pokemon Fire Red', 78.74, 'Pokemon Fire Red VideoGame for GamBoy Advanced SP', '01-29-2004', 3, 6, 5, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('Dr.Mario', 21.95, 'Dr.Mario VideoGame for original GameBoy', '04-15-1990', 3, 2, 6, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('Star Wars', 29.99, 'Star Wars VideoGame for Original GameBoy', '11-15-1991', 3, 2, 6, '');
INSERT INTO product_videogame (name, price, description, release_date, age_limit, brand_id, console_id, image)
    VALUES ('The Legend of Zelda Ocarina of Time', 83.94, 'The Legend of Zelda Ocarina of Time VideoGame for Nintendo 64', '11-21-1998', 3, 2, 4, '');


