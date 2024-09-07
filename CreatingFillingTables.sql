CREATE TABLE products (
	product_id     INTEGER,
	product_name   VARCHAR NOT NULL,
	category_id    INTEGER,
	calories       INTEGER,
	price          DECIMAL
);

CREATE TABLE categories (
	category_id      INTEGER,
	category_name    VARCHAR NOT NULL
);

CREATE TABLE nutrinfo (
	product_id       INTEGER,
	protein          DECIMAL,
	carbohydrates    DECIMAL,
	fat              DECIMAL,
	fiber            DECIMAL
);



INSERT INTO categories (category_id, category_name)
VALUES
(1, 'Грибы'),
(2, 'Мёд сбора 2024'),
(3, 'Здоровое питание');

INSERT INTO products (product_id, product_name, category_id, calories, price)
VALUES
(1, 'Белые грибы, сушеные, резаные, 40 г', 1, 154, 440.00),
(2, 'Лисички, грибы сушеные, 40 г', 1, 261, 390.00),
(3, 'Чага Березовая', 1, 140, 390.00),
(4, 'Мёд алтайский Горный (сбор 2024 года)', 2, 328, 675.00),
(5, 'Мёд алтайский Дягилевый (сбор 2024 года)', 2, 328, 891.00),
(6, 'Мёд алтайский с прополисом (сбор 2024 года)', 2, 328, 531.00),
(7, 'Кисель Detox овсяный', 3, 330, 170),
(8, 'Кисель Detox облепиховая косточка', 3, 345, 170.00),
(9, 'Коктейль льняной при гастрите, 10 г', 3, 268, 210.00);

INSERT INTO nutrinfo (product_id, protein, carbohydrates, fat, fiber)
VALUES
(1, 20.1, 7.6, 4.8, 0.0),
(2, 22.3, 24, 2.0, 7.6, 0.0),
(3, 18.2, 15.4, 5.2, 0.0),
(4, 0.0, 82.0, 0.0, 0.0),
(5, 0.0, 82.0, 0.0, 0.0),
(6, 0.0, 82.0, 0.0, 0.0),
(7, 15.0, 45.6, 7.0, 2.8),
(8, 18.7, 46.5, 9.2, 3.6),
(9, 30.4, 16.0, 8.4, 26.8);
