DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS item;

CREATE TABLE `category` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `category_name` VARCHAR(50) NOT NULL
);

CREATE TABLE `item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `category_id` INTEGER NOT NULL,
    `item_name` VARCHAR(50) NOT NULL,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX item_category_id ON item (category_id);