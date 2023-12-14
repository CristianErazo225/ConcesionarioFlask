-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-12-2023 a las 23:52:43
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sitio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autos`
--

CREATE TABLE `autos` (
  `id` int(11) NOT NULL,
  `marca` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `imagen` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `autos`
--

INSERT INTO `autos` (`id`, `marca`, `nombre`, `imagen`) VALUES
(1, 'Kia', 'Sportage', '2023225017_sportage.jpg'),
(20, 'BMW', 'X3', '2023225244_pexels-mike-bird-13592325.jpg'),
(22, 'Ferrari', 'A7', '2023225318_pexels-matt-weissinger-9622979.jpg'),
(23, 'Lamborghini', 'Aventador', '2023232801_lamborghini_Aventador.jpg'),
(24, 'Ferrari', 'Suv', '2023232831_Ferrari_SUV.jpg'),
(25, 'Fenyr', 'Supersport', '2023232855_Fenyr_Supersport.jpg'),
(26, 'Chevrolet', 'Corvette Z06', '2023233146_Chevrolet_Corvette_Z06.jpg'),
(28, 'Ford', 'Raptor', '2023105121_Ford_raptor.jpg'),
(29, 'McLaren', '720s', '2023114311_McLaren_720s.jpg'),
(30, 'BMW', 'm5', '2023114348_bmw_m5.jpg'),
(31, 'BMW', 'm3', '2023122811_Toyota_supra.jpg'),
(32, 'Renault', '4', '2023122840_Renault_captur.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id2` int(11) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `imagen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id2`, `marca`, `nombre`, `imagen`) VALUES
(28, '4', 'Renault', '2023122840_Renault_captur.jpg'),
(29, '720s', 'McLaren', '2023114311_McLaren_720s.jpg'),
(30, 'm5', 'BMW', '2023114348_bmw_m5.jpg'),
(31, '720s', 'McLaren', '2023114311_McLaren_720s.jpg'),
(32, 'm5', 'BMW', '2023114348_bmw_m5.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `password`) VALUES
(1, 'cristian', '123'),
(3, 'Juan', '123'),
(7, 'Christian', '123'),
(8, 'Danilo', '12345'),
(9, 'Juan Andres', '123'),
(10, 'Profe Dávila', '123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autos`
--
ALTER TABLE `autos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id2`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autos`
--
ALTER TABLE `autos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id2` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
