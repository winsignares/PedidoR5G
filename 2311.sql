-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 23-11-2021 a las 23:23:57
-- Versión del servidor: 5.5.24-log
-- Versión de PHP: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `2311`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `concepto`
--

CREATE TABLE IF NOT EXISTS `concepto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `concepto`
--

INSERT INTO `concepto` (`id`, `Nombre`) VALUES
(1, 'Altas'),
(2, ' Bajas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medico`
--

CREATE TABLE IF NOT EXISTS `medico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Identificacion` int(11) DEFAULT NULL,
  `tipo_id` varchar(30) DEFAULT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `especialidad` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Identificacion` (`Identificacion`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `medico`
--

INSERT INTO `medico` (`id`, `Identificacion`, `tipo_id`, `Nombre`, `especialidad`) VALUES
(1, 123, 'CC', 'Wendy', 'Interna'),
(2, 456, 'CC', 'Ricardo', 'Medicina General');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE IF NOT EXISTS `paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Identificacion` int(11) DEFAULT NULL,
  `tipo_id` varchar(30) DEFAULT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `genero` varchar(30) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Identificacion` (`Identificacion`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`id`, `Identificacion`, `tipo_id`, `Nombre`, `genero`, `edad`) VALUES
(1, 123, 'CC', 'Gower', 'Masculino', 32),
(2, 456, 'pasaporte', 'William ', 'Masculino', 32);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tratamiento`
--

CREATE TABLE IF NOT EXISTS `tratamiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Id_Paciente` int(11) DEFAULT NULL,
  `Temperatura` int(11) DEFAULT NULL,
  `Malestar` varchar(70) DEFAULT NULL,
  `FechaIngreso` varchar(70) DEFAULT NULL,
  `Id_Medico` int(11) DEFAULT NULL,
  `Procedimiento` varchar(70) DEFAULT NULL,
  `N_Cama` int(11) DEFAULT NULL,
  `Diagnostico` varchar(70) DEFAULT NULL,
  `Gravedad_Malestar` varchar(70) DEFAULT NULL,
  `Id_Concepto` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Id_Paciente` (`Id_Paciente`),
  KEY `Id_Medico` (`Id_Medico`),
  KEY `Id_Concepto` (`Id_Concepto`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcado de datos para la tabla `tratamiento`
--

INSERT INTO `tratamiento` (`id`, `Id_Paciente`, `Temperatura`, `Malestar`, `FechaIngreso`, `Id_Medico`, `Procedimiento`, `N_Cama`, `Diagnostico`, `Gravedad_Malestar`, `Id_Concepto`) VALUES
(1, 1, 32, 'General', '23/11/2021', 1, 'General', 10, 'General', 'General', 2),
(2, 2, 38, 'Fiebre', '23/11/2021', 2, 'General', 45, 'General', 'General', 2);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tratamiento`
--
ALTER TABLE `tratamiento`
  ADD CONSTRAINT `tratamiento_ibfk_1` FOREIGN KEY (`Id_Paciente`) REFERENCES `paciente` (`id`),
  ADD CONSTRAINT `tratamiento_ibfk_2` FOREIGN KEY (`Id_Medico`) REFERENCES `medico` (`id`),
  ADD CONSTRAINT `tratamiento_ibfk_3` FOREIGN KEY (`Id_Concepto`) REFERENCES `concepto` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
