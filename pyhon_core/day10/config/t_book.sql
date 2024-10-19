CREATE TABLE if not exists `db01`.`t_book`  (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `book_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci NULL DEFAULT NULL,
    `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci NULL DEFAULT NULL COMMENT '作者',
    `press` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci NULL DEFAULT NULL COMMENT '出版社',
    `price` decimal(10, 2) NULL DEFAULT NULL COMMENT '价格',
    `press_time` bigint(20) NULL DEFAULT NULL COMMENT '出版时间',
    `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci NULL DEFAULT NULL COMMENT '备注',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_as_ci ROW_FORMAT = Dynamic