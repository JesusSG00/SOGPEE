-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-05-2025 a las 08:10:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sogpee`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `foest08`
--

CREATE TABLE `foest08` (
  `IdFoest08` int(11) NOT NULL,
  `Pregunta01` int(2) NOT NULL,
  `Pregunta02` int(2) NOT NULL,
  `Pregunta03` int(2) NOT NULL,
  `Pregunta04` int(2) NOT NULL,
  `Pregunta05` int(2) NOT NULL,
  `Pregunta06` int(2) NOT NULL,
  `Pregunta07` int(2) NOT NULL,
  `Pregunta08` int(2) NOT NULL,
  `Pregunta09` int(2) NOT NULL,
  `Veracidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `foest08`
--
ALTER TABLE `foest08`
  ADD PRIMARY KEY (`IdFoest08`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `foest08`
--
ALTER TABLE `foest08`
  MODIFY `IdFoest08` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
