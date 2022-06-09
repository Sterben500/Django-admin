CREATE TABLE `applications` (
  `id` int NOT NULL,
  `name_of_application` varchar(45) DEFAULT NULL,
  `logo` varchar(45) DEFAULT NULL,
  `server` varchar(45) NOT NULL,
  `users` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`server`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `server` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `server_type` varchar(45) DEFAULT NULL,
  `processor_number` int DEFAULT NULL,
  `memory_capacity` int DEFAULT NULL,
  `storage_capacity` int DEFAULT NULL,
  PRIMARY KEY (`id`,`name`),
  KEY `server_type_idx` (`server_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `server_type` (
  `id` int NOT NULL,
  `server_type` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `services` (
  `id` int NOT NULL,
  `name_of_service` varchar(45) DEFAULT NULL,
  `date_of_launch` datetime DEFAULT NULL,
  `memory_used` int DEFAULT NULL,
  `RAM_min` int DEFAULT NULL,
  `server_launch_onto` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `users` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `sur_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
