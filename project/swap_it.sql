-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: dbproject
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `AdminID` varchar(45) NOT NULL,
  `AdminName` varchar(45) NOT NULL,
  `AdminPassword` varchar(45) NOT NULL,
  `AdminEmail` varchar(45) NOT NULL,
  PRIMARY KEY (`AdminID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('101','Mohid Tanvir','PassWord123.','mohid.tanvir@lums.edu.pk'),('102','Laiba Usman','PassWord321.','laiba.usman@lums.edu.pk'),('103','Tayyab Nasir','PassWord.123','tayyab.nasir@lums.edu.pk'),('104','Zoha Aqil','PassWord.321','zoha.aqil@lums.edu.pk'),('105','Soha Amir','PassWord12335.','soha.amir@lums.edu.pk');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `CourseID` varchar(45) NOT NULL,
  `Title` varchar(45) NOT NULL,
  `DepartmentName` varchar(45) NOT NULL,
  `Credits` int NOT NULL,
  `ModesOfInstruction` varchar(45) NOT NULL,
  PRIMARY KEY (`CourseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('CAL101','Calculus 1','Mathematics',3,'On-campus'),('CS100','Intro to Computer Science','Computer Science',3,'Online'),('CS200','Programmign 2.0','Computer Science',3,'Online'),('ECO111','MicroEconomics','Economics',3,'Online'),('HIST124','Intro to Modern History','History',3,'On-campus'),('PHY101','Mechanics','Physics',4,'Online');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instructor`
--

DROP TABLE IF EXISTS `instructor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `instructor` (
  `InstructorID` varchar(45) NOT NULL,
  `Name_` varchar(45) NOT NULL,
  `DepartmentName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`InstructorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instructor`
--

LOCK TABLES `instructor` WRITE;
/*!40000 ALTER TABLE `instructor` DISABLE KEYS */;
INSERT INTO `instructor` VALUES ('001','Naveed Arshad','Computer Science'),('002','Basit Shafeeq','Computer Science'),('003','Suleman Shahid','Computer Science'),('004','Adam Zaman','Physics'),('005','Baqar Syed','Religious Studies');
/*!40000 ALTER TABLE `instructor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prereq`
--

DROP TABLE IF EXISTS `prereq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prereq` (
  `PreReqID` varchar(45) NOT NULL,
  `CourseID` varchar(45) NOT NULL,
  PRIMARY KEY (`PreReqID`),
  KEY `CourseID` (`CourseID`),
  CONSTRAINT `prereq_ibfk_1` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prereq`
--

LOCK TABLES `prereq` WRITE;
/*!40000 ALTER TABLE `prereq` DISABLE KEYS */;
/*!40000 ALTER TABLE `prereq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `section` (
  `SectionID` varchar(45) NOT NULL,
  `CourseID` varchar(45) NOT NULL,
  `InstructorID` varchar(45) NOT NULL,
  `Semester` varchar(45) NOT NULL,
  `Year_` int NOT NULL,
  `TimeSlotID` varchar(45) NOT NULL,
  PRIMARY KEY (`SectionID`),
  KEY `CourseID` (`CourseID`),
  KEY `InstructorID` (`InstructorID`),
  KEY `TimeSlotID` (`TimeSlotID`),
  CONSTRAINT `section_ibfk_1` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`),
  CONSTRAINT `section_ibfk_2` FOREIGN KEY (`InstructorID`) REFERENCES `instructor` (`InstructorID`),
  CONSTRAINT `section_ibfk_3` FOREIGN KEY (`TimeSlotID`) REFERENCES `timeslot` (`TimeSlotID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section`
--

LOCK TABLES `section` WRITE;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
INSERT INTO `section` VALUES ('S1','CS100','001','Fall',2019,'01'),('S2','CAL101','002','Spring',2019,'02'),('S3','PHY101','003','Fall',2020,'03'),('S4','ECO111','005','Fall',2020,'04'),('S5','HIST124','004','Spring',2020,'05');
/*!40000 ALTER TABLE `section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `StudentID` varchar(45) NOT NULL,
  `StudentName` varchar(45) NOT NULL,
  `Password_` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `TotalCreditHours` int NOT NULL,
  `DepartmentName` varchar(45) NOT NULL,
  PRIMARY KEY (`StudentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('23100001','Mahnoor Malik','php01php','23100001@lums.edu.pk',32,'History'),('23100080','Abdullah Masood','ok2103asy','23100080@lums.edu.pk',115,'Economics'),('23100100','Sarah Khan','helloWorld1','23100100@lums.edu.pk',62,'Computer Science'),('23100101','Ayesha Ahmad','thisismypassword','23100101@lums.edu.pk',89,'Mathematics'),('23100276','Eman Batool','slackhi90','23100276@lums.edu.pk',18,'Physics');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swapit`
--

DROP TABLE IF EXISTS `swapit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `swapit` (
  `RequestID` varchar(45) NOT NULL,
  `HaveCourseID` varchar(45) NOT NULL,
  `WantCourseID` varchar(45) NOT NULL,
  `AcceptID` varchar(45) NOT NULL,
  PRIMARY KEY (`RequestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swapit`
--

LOCK TABLES `swapit` WRITE;
/*!40000 ALTER TABLE `swapit` DISABLE KEYS */;
INSERT INTO `swapit` VALUES ('23100115','ECO100','ECO111','6:50'),('23100126','CAL101','MGMT142','6:50'),('23100253','CS100','CS200','6:50'),('23100277','HIST100','CS200','6:50'),('23100289','ENG111','CAL101','6:50');
/*!40000 ALTER TABLE `swapit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `takes`
--
DROP TABLE IF EXISTS 'message';
CREATE TABLE 'message' (
  `StudentID` varchar(45) NOT NULL,
  `mess` varchar(65000) NOT NULL,
  PRIMARY KEY (`StudentID`),
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `takes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `takes` (
  `StudentID` varchar(45) NOT NULL,
  `CourseID` varchar(45) NOT NULL,
  `SectionID` varchar(45) NOT NULL,
  `Grade` varchar(45) NOT NULL,
  PRIMARY KEY (`StudentID`, 'CourseID'),
  CONSTRAINT `takes_ibfk_1` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`),
  CONSTRAINT `takes_ibfk_2` FOREIGN KEY (`SectionID`) REFERENCES `section` (`SectionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `takes`
--

LOCK TABLES `takes` WRITE;
/*!40000 ALTER TABLE `takes` DISABLE KEYS */;
INSERT INTO `takes` VALUES ('23100001','ECO111','S3','C'),('23100080','PHY101','S1','A-'),('23100100','CS100','S1','A'),('23100101','CAL101','S2','B+'),('23100276','HIST124','S1','F');
/*!40000 ALTER TABLE `takes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teaches`
--

DROP TABLE IF EXISTS `teaches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teaches` (
  `InstructorID` varchar(45) NOT NULL,
  `CourseID` varchar(45) NOT NULL,
  `SectionID` varchar(45) NOT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Year_` int NOT NULL,
  PRIMARY KEY (`InstructorID`,`CourseID`,`SectionID`),
  KEY `CourseID` (`CourseID`),
  KEY `SectionID` (`SectionID`),
  CONSTRAINT `teaches_ibfk_1` FOREIGN KEY (`InstructorID`) REFERENCES `instructor` (`InstructorID`),
  CONSTRAINT `teaches_ibfk_2` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`),
  CONSTRAINT `teaches_ibfk_3` FOREIGN KEY (`SectionID`) REFERENCES `section` (`SectionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teaches`
--

LOCK TABLES `teaches` WRITE;
/*!40000 ALTER TABLE `teaches` DISABLE KEYS */;
INSERT INTO `teaches` VALUES ('001','CS100','S1','Fall',2019),('001','CS200','S1','Fall',2021),('002','CAL101','S2','Spring',2019),('003','ECO111','S3','Fall',2020),('004','HIST124','S5','Spring',2020),('005','PHY101','S4','Fall',2020);
/*!40000 ALTER TABLE `teaches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timeslot`
--

DROP TABLE IF EXISTS `timeslot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timeslot` (
  `TimeSlotID` varchar(45) NOT NULL,
  `Day_` varchar(45) NOT NULL,
  `Start_Time` varchar(45) NOT NULL,
  `End_Time` varchar(45) NOT NULL,
  PRIMARY KEY (`TimeSlotID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timeslot`
--

LOCK TABLES `timeslot` WRITE;
/*!40000 ALTER TABLE `timeslot` DISABLE KEYS */;
INSERT INTO `timeslot` VALUES ('01','Monday','8:00','8:50'),('02','Tuesday','9:00','9:50'),('03','Wednesday','11:00','11:50'),('04','Thursday','5:00','5:50'),('05','Friday','6:00','6:50');
/*!40000 ALTER TABLE `timeslot` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-30 19:52:39
