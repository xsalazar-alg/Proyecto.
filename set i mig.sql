-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: set i mig
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `card`
--

DROP TABLE IF EXISTS `card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `card` (
  `card_id` char(3) NOT NULL,
  `card_value` float(3,1) DEFAULT NULL,
  `card_priority` tinyint DEFAULT NULL,
  `card_real_value` float(2,1) DEFAULT NULL,
  `deck_id` char(3) DEFAULT NULL,
  `card_name` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`card_id`),
  KEY `deck_id` (`deck_id`),
  CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deck_id`) REFERENCES `deck` (`deck_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card`
--

LOCK TABLES `card` WRITE;
/*!40000 ALTER TABLE `card` DISABLE KEYS */;
INSERT INTO `card` VALUES ('B01',1.0,1,1.0,'1','Ace of Clubs'),('B02',2.0,1,2.0,'1','Two of Clubs'),('B03',3.0,1,3.0,'1','Three of Clubs'),('B04',4.0,1,4.0,'1','Four of Clubs'),('B05',5.0,1,5.0,'1','Five of Clubs'),('B06',6.0,1,6.0,'1','Six of Clubs'),('B07',7.0,1,7.0,'1','Seven of Clubs'),('B08',8.0,1,0.5,'1','Eight of Clubs'),('B09',9.0,1,0.5,'1','Nine of Clubs'),('B10',10.0,1,0.5,'1','Jack of Clubs'),('B11',11.0,1,0.5,'1','Horse of Clubs'),('B12',12.0,1,0.5,'1','King of Clubs'),('C01',1.0,3,1.0,'1','Ace of Cups'),('C02',2.0,3,2.0,'1','Two of Cups'),('C03',3.0,3,3.0,'1','Three of Cups'),('C04',4.0,3,4.0,'1','Four of Cups'),('C05',5.0,3,5.0,'1','Five of Cups'),('C06',6.0,3,6.0,'1','Six of Cups'),('C07',7.0,3,7.0,'1','Seven of Cups'),('C08',8.0,3,0.5,'1','Eight of Cups'),('C09',9.0,3,0.5,'1','Nine of Cups'),('C10',10.0,3,0.5,'1','Jack of Cups'),('C11',11.0,3,0.5,'1','Horse of Cups'),('C12',12.0,3,0.5,'1','King of Cups'),('D01',1.0,1,1.0,'2','Ace of Diamond'),('D02',2.0,1,2.0,'2','Two of Diamond'),('D03',3.0,1,3.0,'2','Three of Diamond'),('D04',4.0,1,4.0,'2','Four of Diamond'),('D05',5.0,1,5.0,'2','Five of Diamond'),('D06',6.0,1,6.0,'2','Six of Diamond'),('D07',7.0,1,7.0,'2','Seven of Diamond'),('D08',8.0,1,0.5,'2','Eight of Diamond'),('D09',9.0,1,0.5,'2','Nine of Diamond'),('D10',10.0,1,0.5,'2','Ten of Diamond'),('D11',11.0,1,0.5,'2','Jack of Diamond'),('D12',12.0,1,0.5,'2','Queen of Diamond'),('D13',13.0,1,0.5,'2','King of Diamond'),('G01',1.0,4,1.0,'1','Ace of Coins'),('G02',2.0,4,2.0,'1','Two of Coins'),('G03',3.0,4,3.0,'1','Three of Coins'),('G04',4.0,4,4.0,'1','Four of Coins'),('G05',5.0,4,5.0,'1','Five of Coins'),('G06',6.0,4,6.0,'1','Six of Coins'),('G07',7.0,4,7.0,'1','Seven of Coins'),('G08',8.0,4,0.5,'1','Eight of Coins'),('G09',9.0,4,0.5,'1','Nine of Coins'),('G10',10.0,4,0.5,'1','Jack of Coins'),('G11',11.0,4,0.5,'1','Horse of Coins'),('G12',12.0,4,0.5,'1','King of Coins'),('H01',1.0,2,1.0,'2','Ace of Hearts'),('H02',2.0,2,2.0,'2','Two of Hearts'),('H03',3.0,2,3.0,'2','Three of Hearts'),('H04',4.0,2,4.0,'2','Four of Hearts'),('H05',5.0,2,5.0,'2','Five of Hearts'),('H06',6.0,2,6.0,'2','Six of Hearts'),('H07',7.0,2,7.0,'2','Seven of Hearts'),('H08',8.0,2,0.5,'2','Eight of Hearts'),('H09',9.0,2,0.5,'2','Nine of Hearts'),('H10',10.0,2,0.5,'2','Ten of Hearts'),('H11',11.0,2,0.5,'2','Jack of Hearts'),('H12',12.0,2,0.5,'2','Queen of Hearts'),('H13',13.0,2,0.5,'2','King of Hearts'),('P01',1.0,3,1.0,'2','Ace of Spades'),('P02',2.0,3,2.0,'2','Two of Spades'),('P03',3.0,3,3.0,'2','Three of Spades'),('P04',4.0,3,4.0,'2','Four of Spades'),('P05',5.0,3,5.0,'2','Five of Spades'),('P06',6.0,3,6.0,'2','Six of Spades'),('P07',7.0,3,7.0,'2','Seven of Spades'),('P08',8.0,3,0.5,'2','Eight of Spades'),('P09',9.0,3,0.5,'2','Nine of Spades'),('P10',10.0,3,0.5,'2','Ten of Spades'),('P11',11.0,3,0.5,'2','Jack of Spades'),('P12',12.0,3,0.5,'2','Queen of Spades'),('P13',13.0,3,0.5,'2','King of Spades'),('S01',1.0,2,1.0,'1','Ace of Swords'),('S02',2.0,2,2.0,'1','Two of Swords'),('S03',3.0,2,3.0,'1','Three of Swords'),('S04',4.0,2,4.0,'1','Four of Swords'),('S05',5.0,2,5.0,'1','Five of Swords'),('S06',6.0,2,6.0,'1','Six of Swords'),('S07',7.0,2,7.0,'1','Seven of Swords'),('S08',8.0,2,0.5,'1','Eight of Swords'),('S09',9.0,2,0.5,'1','Nine of Swords'),('S10',10.0,2,0.5,'1','Jack of Swords'),('S11',11.0,2,0.5,'1','Horse of Swords'),('S12',12.0,2,0.5,'1','King of Swords'),('T01',1.0,4,1.0,'2','Ace of Clubs'),('T02',2.0,4,2.0,'2','Two of Clubs'),('T04',4.0,4,4.0,'2','Four of Clubs'),('T05',5.0,4,5.0,'2','Five of Clubs'),('T06',6.0,4,6.0,'2','Six of Clubs'),('T07',7.0,4,7.0,'2','Seven of Clubs'),('T08',8.0,4,0.5,'2','Eight of Clubs'),('T09',9.0,4,0.5,'2','Nine of Clubs'),('T10',10.0,4,0.5,'2','Ten of Clubs'),('T11',11.0,4,0.5,'2','Jack of Clubs'),('T12',12.0,4,0.5,'2','Queen of Clubs'),('T13',13.0,4,0.5,'2','King of Clubs');
/*!40000 ALTER TABLE `card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cardgame`
--

DROP TABLE IF EXISTS `cardgame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardgame` (
  `cardgame_id` int NOT NULL,
  `players` varchar(100) DEFAULT NULL,
  `rounds` tinyint DEFAULT NULL,
  `start_hour` varchar(5) DEFAULT NULL,
  `end_hour` varchar(5) DEFAULT NULL,
  `deck_id` char(3) DEFAULT NULL,
  PRIMARY KEY (`cardgame_id`),
  KEY `deck_id` (`deck_id`),
  CONSTRAINT `cardgame_ibfk_1` FOREIGN KEY (`deck_id`) REFERENCES `deck` (`deck_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardgame`
--

LOCK TABLES `cardgame` WRITE;
/*!40000 ALTER TABLE `cardgame` DISABLE KEYS */;
INSERT INTO `cardgame` VALUES (1,'20855563Z, 06272572N',5,'17:24','17:30','1'),(2,'20855563Z, 21021634W',7,'17:36','17:40','1'),(3,'20855563Z, 21021634W',5,'17:43','17:48','2');
/*!40000 ALTER TABLE `cardgame` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deck`
--

DROP TABLE IF EXISTS `deck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deck` (
  `deck_id` char(3) NOT NULL,
  `deck_name` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`deck_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deck`
--

LOCK TABLES `deck` WRITE;
/*!40000 ALTER TABLE `deck` DISABLE KEYS */;
INSERT INTO `deck` VALUES ('1','Spanish deck'),('2','Poker deck');
/*!40000 ALTER TABLE `deck` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `player_id` varchar(25) NOT NULL,
  `player_name` varchar(25) NOT NULL,
  `player_risk` tinyint DEFAULT NULL,
  `human` tinyint(1) DEFAULT NULL,
  `games_played` int DEFAULT NULL,
  `total_points_earned` int DEFAULT NULL,
  `total_minutes_played` int DEFAULT NULL,
  `bot` tinyint DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES ('06272572N','Joan',30,1,1,5,6,0),('20855563Z','Emilia',40,1,3,24,15,0),('21021634W','Bot',40,0,2,47,9,1);
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_game`
--

DROP TABLE IF EXISTS `player_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_game` (
  `cardgame_id` int DEFAULT NULL,
  `player_id` varchar(25) DEFAULT NULL,
  `initial_card_id` char(3) NOT NULL,
  `starting_points` tinyint DEFAULT NULL,
  `ending_points` tinyint DEFAULT NULL,
  PRIMARY KEY (`initial_card_id`),
  KEY `cardgame_id` (`cardgame_id`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `player_game_ibfk_1` FOREIGN KEY (`cardgame_id`) REFERENCES `cardgame` (`cardgame_id`),
  CONSTRAINT `player_game_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_game`
--

LOCK TABLES `player_game` WRITE;
/*!40000 ALTER TABLE `player_game` DISABLE KEYS */;
INSERT INTO `player_game` VALUES (1,'06272572N','B07',0,5),(2,'21021634W','C05',0,20),(3,'20855563Z','D07',22,24),(2,'20855563Z','G12',22,22),(3,'21021634W','H13',20,47),(1,'20855563Z','S01',0,22);
/*!40000 ALTER TABLE `player_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_game_round`
--

DROP TABLE IF EXISTS `player_game_round`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_game_round` (
  `cardgame_id` int DEFAULT NULL,
  `round_num` tinyint NOT NULL,
  `player_id` varchar(25) DEFAULT NULL,
  `is_bank` tinyint(1) DEFAULT NULL,
  `bet_points` tinyint DEFAULT NULL,
  `cards_value` decimal(4,1) DEFAULT NULL,
  `starting_round_points` tinyint DEFAULT NULL,
  `ending_round_points` tinyint DEFAULT NULL,
  PRIMARY KEY (`round_num`),
  KEY `cardgame_id` (`cardgame_id`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `player_game_round_ibfk_1` FOREIGN KEY (`cardgame_id`) REFERENCES `cardgame` (`cardgame_id`),
  CONSTRAINT `player_game_round_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_game_round`
--

LOCK TABLES `player_game_round` WRITE;
/*!40000 ALTER TABLE `player_game_round` DISABLE KEYS */;
/*!40000 ALTER TABLE `player_game_round` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-29 16:44:59
