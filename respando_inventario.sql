-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: inventario
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `inventario`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `inventario` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `inventario`;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'myapp','0001_initial','2024-10-11 19:05:23.448712'),(2,'myapp','0002_categoria_tipotransaccion_articulo_cat_articulo_and_more','2024-10-13 00:06:23.988638');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_articulo`
--

DROP TABLE IF EXISTS `myapp_articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_articulo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom_articulo` varchar(60) NOT NULL,
  `des_articulo` varchar(100) NOT NULL,
  `can_articulo` int NOT NULL,
  `pre_articulo` double NOT NULL,
  `cat_articulo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_articulo_cat_articulo_id_20e2fd33_fk_myapp_categoria_id` (`cat_articulo_id`),
  CONSTRAINT `myapp_articulo_cat_articulo_id_20e2fd33_fk_myapp_categoria_id` FOREIGN KEY (`cat_articulo_id`) REFERENCES `myapp_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_articulo`
--

LOCK TABLES `myapp_articulo` WRITE;
/*!40000 ALTER TABLE `myapp_articulo` DISABLE KEYS */;
INSERT INTO `myapp_articulo` VALUES (1,'Lavarropa','Automático Samsung 7kg Color Plata',5,1100000,1),(2,'Lavarropa','Automático Electrolux 9Kg Blanco',5,846000,1),(3,'Lavarropa','Asemiautomático Codini 10kg Blanco',10,163000,1),(4,'Televisión','Smart Led Google TV TCL 55\" 4K',6,780000,1),(5,'Smartphone','Celular Samsung A04 SM-A045M Negro',8,250000,2),(6,'Taladro','Taladro atornillador. Motor Brushed de alto rendimiento',5,187000,7),(7,'Escritorio','2 Cajones Platinum, correderas metalicas',2,110000,3);
/*!40000 ALTER TABLE `myapp_articulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_categoria`
--

DROP TABLE IF EXISTS `myapp_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom_categoria` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_categoria`
--

LOCK TABLES `myapp_categoria` WRITE;
/*!40000 ALTER TABLE `myapp_categoria` DISABLE KEYS */;
INSERT INTO `myapp_categoria` VALUES (1,'Electrodomésticos'),(2,'Electrónica'),(3,'Muebles y decoración'),(4,'Artículos de cocina'),(5,'Ropa y accesorios'),(6,'Productos de limpieza'),(7,'Artículos de ferretería'),(8,'Juguetes'),(9,'Deportes'),(10,'Papelería y suministros de oficina');
/*!40000 ALTER TABLE `myapp_categoria` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-14 17:50:39
