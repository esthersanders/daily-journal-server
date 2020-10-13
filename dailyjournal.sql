CREATE TABLE `Entry` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date` DATE,
    `entry` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood` (`id`)
);

CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);

CREATE TABLE `Tag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `subject` TEXT NOT NULL
);

CREATE TABLE `EntryTag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id` INTEGER NOT NULL,
    `tag_id` INTEGER NOT NULL,
    FOREIGN KEY(`entry_id`) REFERENCES `Entry` (`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tag` (`id`)
);

INSERT INTO `Entry` VALUES (null, '2020-07-12', "we practiced the GitHub workflow for group projects", 5);
INSERT INTO `Entry` VALUES (null, '2020-07-14', "we talked about how to use JavaScript to dynamically populate our page", 4);
INSERT INTO `Entry` VALUES (null, '2020-07-15', "how to import and export from one module to another", 3);
INSERT INTO `Entry` VALUES (null, '2020-08-25', "API, fetch calls", 1);

INSERT INTO `Mood` VALUES (null, "upbeat");
INSERT INTO `Mood` VALUES (null, "frustrated");
INSERT INTO `Mood` VALUES (null, "tired");
INSERT INTO `Mood` VALUES (null, "OK");
INSERT INTO `Mood` VALUES (null, "alert");

INSERT INTO `Tag` VALUES (null, "API");
INSERT INTO `Tag` VALUES (null, "components");
INSERT INTO `Tag` VALUES (null, "fetch");
INSERT INTO `Tag` VALUES (null, "GitHub");
INSERT INTO `Tag` VALUES (null, "ERD");
INSERT INTO `Tag` VALUES (null, "JSON");
INSERT INTO `Tag` VALUES (null, "JavaScript");

INSERT INTO `EntryTag` VALUES (null, 1, 4);
INSERT INTO `EntryTag` VALUES (null, 2, 2);
INSERT INTO `EntryTag` VALUES (null, 3, 2);
INSERT INTO `EntryTag` VALUES (null, 4, 3);

SELECT * FROM Entry;
SELECT * FROM Mood;
SELECT * FROM Tag;
SELECT * FROM EntryTag;

INSERT INTO `Entry` VALUES (null, '2020-08-25', "API, fetch calls", 1);
INSERT INTO `Entry` VALUES (null, '2020-08-25', "API, fetch calls", 1);