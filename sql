CREATE TABLE `applications` (
  `id` int NOT NULL,
  `name_of_application` varchar(45) DEFAULT NULL,
  `logo` varchar(45) DEFAULT NULL,
  `id server` int NOT NULL,
  `id users` int NOT NULL,
  KEY `id servers_idx` (`id server`),
  KEY `id users_idx` (`id users`),
  CONSTRAINT `id servers` FOREIGN KEY (`id server`) REFERENCES `server` (`id`),
  CONSTRAINT `id users` FOREIGN KEY (`id users`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `server` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `server_type` int NOT NULL,
  `processor_number` int DEFAULT NULL,
  `memory_capacity` int DEFAULT NULL,
  `storage_capacity` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `server_type_idx` (`server_type`),
  CONSTRAINT `id server type` FOREIGN KEY (`server_type`) REFERENCES `server_type` (`id`)
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
  `id server_launch_onto` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id serverlaunch_idx` (`id server_launch_onto`),
  CONSTRAINT `id serverlaunch` FOREIGN KEY (`id server_launch_onto`) REFERENCES `server` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `users` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `sur_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
