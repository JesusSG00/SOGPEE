-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-06-2025 a las 04:13:50
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
-- Estructura de tabla para la tabla `asesoracademico`
--

CREATE TABLE `asesoracademico` (
  `Id` int(11) NOT NULL,
  `Nombre1` varchar(30) NOT NULL,
  `Nombre2` varchar(20) NOT NULL,
  `ApellidoP` varchar(20) NOT NULL,
  `ApellidoM` varchar(20) NOT NULL,
  `Telefono` varchar(10) NOT NULL,
  `Correo` text NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asesoracademico`
--

INSERT INTO `asesoracademico` (`Id`, `Nombre1`, `Nombre2`, `ApellidoP`, `ApellidoM`, `Telefono`, `Correo`, `password`) VALUES
(1, 'Juan', 'Carlos', 'Gómez', 'Pérez', '1234567890', 'juan.gomez@gmail.com', 'juan.gomez@gmail.com'),
(2, 'Ana', 'Maria', 'López', 'García', '2345678901', 'ana.lopez@gmail.com', 'ana.lopez@gmail.com'),
(3, 'Luis', 'Eduardo', 'Martínez', 'Hernández', '3456789012', 'luis.martinez@gmail.com', 'luis.martinez@gmail.com'),
(4, 'Carlos', 'Antonio', 'Rodríguez', 'Martín', '4567890123', 'carlos.rodriguez@gmail.com', 'carlos.rodriguez@gmail.com'),
(5, 'María', 'Elena', 'Fernández', 'López', '5678901234', 'maria.fernandez@gmail.com', 'maria.fernandez@gmail.com'),
(6, 'Pedro', 'José', 'Pérez', 'Gómez', '6789012345', 'pedro.perez@gmail.com', 'pedro.perez@gmail.com'),
(7, 'Lucía', 'Sofía', 'Sánchez', 'González', '7890123456', 'lucia.sanchez@gmail.com', 'lucia.sanchez@gmail.com'),
(8, 'José', 'Manuel', 'Ramírez', 'Hernández', '8901234567', 'jose.ramirez@gmail.com', 'jose.ramirez@gmail.com'),
(9, 'Raúl', 'Antonio', 'Jiménez', 'Mendoza', '9012345678', 'raul.jimenez@gmail.com', 'raul.jimenez@gmail.com'),
(10, 'Marta', 'Isabel', 'Álvarez', 'Torres', '0123456789', 'marta.alvarez@gmail.com', 'marta.alvarez@gmail.com'),
(11, 'Javier', 'Luis', 'Mora', 'Reyes', '1122334455', 'javier.mora@gmail.com', 'javier.mora@gmail.com'),
(12, 'Beatriz', 'Carmen', 'Vázquez', 'González', '2233445566', 'beatriz.vazquez@gmail.com', 'beatriz.vazquez@gmail.com'),
(13, 'Ricardo', 'Luis', 'Castro', 'Morales', '3344556677', 'ricardo.castro@gmail.com', 'ricardo.castro@gmail.com'),
(14, 'Carmen', 'Victoria', 'Luna', 'Ríos', '4455667788', 'carmen.luna@gmail.com', 'carmen.luna@gmail.com'),
(15, 'David', 'Francisco', 'Muñoz', 'Pérez', '5566778899', 'david.munoz@gmail.com', 'david.munoz@gmail.com'),
(16, 'Laura', 'Inés', 'Ruiz', 'Soto', '6677889900', 'laura.ruiz@gmail.com', 'laura.ruiz@gmail.com'),
(17, 'Óscar', 'Eduardo', 'Gutiérrez', 'Hernández', '7788990011', 'oscar.gutierrez@gmail.com', 'oscar.gutierrez@gmail.com'),
(18, 'Verónica', 'Susana', 'Moreno', 'Rodríguez', '8899001122', 'veronica.moreno@gmail.com', 'veronica.moreno@gmail.com'),
(19, 'Gabriel', 'Ángel', 'Torres', 'Díaz', '9900112233', 'gabriel.torres@gmail.com', 'gabriel.torres@gmail.com'),
(20, 'Alba', 'Lorena', 'Paredes', 'Vega', '1011122334', 'alba.paredes@gmail.com', 'alba.paredes@gmail.com'),
(21, 'Antonio', 'José', 'Salazar', 'Muñoz', '2122233445', 'antonio.salazar@gmail.com', 'antonio.salazar@gmail.com'),
(22, 'Sandra', 'María', 'González', 'Vásquez', '3233344556', 'sandra.gonzalez@gmail.com', 'sandra.gonzalez@gmail.com'),
(23, 'Ricardo', 'Antonio', 'Méndez', 'Fuentes', '4344455667', 'ricardo.mendez@gmail.com', 'ricardo.mendez@gmail.com'),
(24, 'Andrea', 'Rocío', 'Hidalgo', 'Ramírez', '5455566778', 'andrea.hidalgo@gmail.com', 'andrea.hidalgo@gmail.com'),
(25, 'Fernando', 'Carlos', 'Castillo', 'Martínez', '6566677889', 'fernando.castillo@gmail.com', 'fernando.castillo@gmail.com'),
(26, 'Esteban', 'Manuel', 'García', 'Muñoz', '7677788990', 'esteban.garcia@gmail.com', 'esteban.garcia@gmail.com'),
(27, 'Patricia', 'Elena', 'Blanco', 'Sánchez', '8788899001', 'patricia.blanco@gmail.com', 'patricia.blanco@gmail.com'),
(28, 'José', 'Luis', 'Cabrera', 'Martínez', '9899001122', 'jose.cabrera@gmail.com', 'jose.cabrera@gmail.com'),
(29, 'Mercedes', 'Elisabeth', 'Morales', 'Torres', '1100112233', 'mercedes.morales@gmail.com', 'mercedes.morales@gmail.com'),
(30, 'Santiago', 'Carlos', 'Hernández', 'Álvarez', '2200223344', 'santiago.hernandez@gmail.com', 'santiago.hernandez@gmail.com'),
(31, 'Ed', 'Mundo', 'Viveros', 'German', '5547462155', 'mundo.mundo@gmail.com', 'mundo.mundo@gmail.com'),
(32, 'Ed', 'Mundo', 'Pererez', 'Perereira', '5547062122', 'cristo.cristo@gmail.com', 'cristo.cristo@gmail.com'),
(33, 'Ramon', 'juan', 'Sanchez', 'Martinez', '5599762315', 'ramon12@gmail.com', 'ramon12@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asesorempresarial`
--

CREATE TABLE `asesorempresarial` (
  `AsesorID` int(11) NOT NULL,
  `Nombre1` varchar(20) DEFAULT NULL,
  `Nombre2` varchar(20) DEFAULT NULL,
  `ApellidoP` varchar(20) DEFAULT NULL,
  `ApellidoM` varchar(20) DEFAULT NULL,
  `Telefono` int(10) DEFAULT NULL,
  `Correo` text DEFAULT NULL,
  `Empresa` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asesorempresarial`
--

INSERT INTO `asesorempresarial` (`AsesorID`, `Nombre1`, `Nombre2`, `ApellidoP`, `ApellidoM`, `Telefono`, `Correo`, `Empresa`) VALUES
(1, 'Luis', 'Fernando', 'Gómez', 'Martínez', 2147483647, 'lfgomez@techsoft.com', 'TechSoft Solutions'),
(2, 'Ana', 'María', 'López', 'Hernández', 2147483647, 'amlopez@codecraft.io', 'CodeCraft'),
(3, 'Carlos', 'Eduardo', 'Ramírez', 'Pérez', 2147483647, 'ceramirez@innovdev.com', 'InnovDev'),
(4, 'María', 'José', 'Hernández', 'González', 2147483647, 'mjhernandez@softnext.com', 'SoftNext'),
(5, 'Jorge', 'Iván', 'Díaz', 'Castro', 2147483647, 'jidiaz@devpeak.com', 'DevPeak'),
(6, 'Laura', 'Beatriz', 'Sánchez', 'Morales', 2147483647, 'lbsanchez@bluecode.com', 'BlueCode Labs'),
(7, 'Fernando', 'Andrés', 'Ortiz', 'Vega', 2147483647, 'faortiz@nextgendevs.com', 'NextGen Devs'),
(8, 'Sofía', 'Elena', 'Vargas', 'Mendoza', 2147483647, 'sevargas@alphacode.com', 'AlphaCode'),
(9, 'Ricardo', 'Alonso', 'Navarro', 'Torres', 2147483647, 'ranavarro@pixelsoft.com', 'PixelSoft'),
(10, 'Gabriela', 'Isabel', 'Molina', 'Ruiz', 2147483647, 'gimolina@codesphere.com', 'CodeSphere'),
(11, 'Daniel', 'Roberto', 'Castillo', 'Jiménez', 2147483647, 'drcastillo@devmasters.com', 'DevMasters'),
(12, 'Paola', 'Andrea', 'Mejía', 'García', 2147483647, 'pamejia@skylinesoft.com', 'Skyline Software'),
(13, 'Juan', 'Pablo', 'Rojas', 'López', 2147483647, 'jprojas@logicware.com', 'LogicWare'),
(14, 'Liliana', 'Guadalupe', 'Medina', 'Flores', 2147483647, 'lgmedina@appcreators.com', 'AppCreators'),
(15, 'Francisco', 'Javier', 'Cortés', 'Valdez', 2147483647, 'fjcortes@techwave.com', 'TechWave'),
(16, 'Cecilia', 'Verónica', 'Vega', 'Ramos', 2147483647, 'cvega@techsoft.com', 'TechSoft Solutions'),
(17, 'Hugo', 'Emilio', 'Silva', 'Hernández', 2147483647, 'hesilva@codecraft.io', 'CodeCraft'),
(18, 'Diana', 'Esther', 'Gutiérrez', 'Santos', 2147483647, 'degutierrez@innovdev.com', 'InnovDev'),
(19, 'Oscar', 'Antonio', 'Luna', 'Cruz', 2147483647, 'oaluna@softnext.com', 'SoftNext'),
(20, 'Mónica', 'Rocío', 'Peña', 'Velázquez', 2147483647, 'mrpena@devpeak.com', 'DevPeak'),
(21, 'Ramón', 'Humberto', 'Campos', 'Ortiz', 2147483647, 'rhcampos@bluecode.com', 'BlueCode Labs'),
(22, 'Claudia', 'Ximena', 'Aguilar', 'Chávez', 2147483647, 'cxaguilar@nextgendevs.com', 'NextGen Devs'),
(23, 'Guillermo', 'Fabián', 'Zavala', 'Rosales', 2147483647, 'gfzavala@alphacode.com', 'AlphaCode'),
(24, 'Alejandra', 'Lucía', 'Valencia', 'Rojas', 2147483647, 'alvalencia@pixelsoft.com', 'PixelSoft'),
(25, 'Javier', 'Eduardo', 'Padilla', 'Sandoval', 2147483647, 'jepadilla@codesphere.com', 'CodeSphere'),
(26, 'Regina', 'Adriana', 'Salinas', 'Fernández', 2147483647, 'rasalinas@devmasters.com', 'DevMasters'),
(27, 'Armando', 'Israel', 'González', 'Navarrete', 2147483647, 'aigonzalez@skylinesoft.com', 'Skyline Software'),
(28, 'Beatriz', 'Inés', 'Cabrera', 'Lara', 2147483647, 'bicabrera@logicware.com', 'LogicWare'),
(29, 'José', 'Luis', 'Esquivel', 'Reyes', 2147483647, 'jlesquivel@appcreators.com', 'AppCreators'),
(30, 'Rocío', 'Margarita', 'Torres', 'Estrada', 2147483647, 'rmortiz@techwave.com', 'TechWave'),
(31, 'Felipe', 'Miguel', 'Castañeda', 'Trujillo', 2147483647, 'fmcastaneda@techsoft.com', 'TechSoft Solutions'),
(32, 'Karla', 'Fernanda', 'Pérez', 'Chavarría', 2147483647, 'kfperez@codecraft.io', 'CodeCraft'),
(33, 'Eduardo', 'Iván', 'Moreno', 'Villalobos', 2147483647, 'eimoreno@innovdev.com', 'InnovDev'),
(34, 'Jessica', 'Lorena', 'Fuentes', 'Quintana', 2147483647, 'jlfuentes@softnext.com', 'SoftNext'),
(35, 'Alberto', 'Francisco', 'Hernández', 'Ruiz', 2147483647, 'afhernandez@devpeak.com', 'DevPeak'),
(36, 'Clara', 'Luz', 'Martínez', 'Gómez', 2147483647, 'clmartinez@bluecode.com', 'BlueCode Labs'),
(37, 'Emanuel', 'Joaquín', 'Reyes', 'Domínguez', 2147483647, 'ejreyes@nextgendevs.com', 'NextGen Devs'),
(38, 'Victoria', 'Angélica', 'Núñez', 'Campos', 2147483647, 'vanunez@alphacode.com', 'AlphaCode'),
(39, 'Diego', 'Ricardo', 'Mendoza', 'Peña', 2147483647, 'drmendoza@pixelsoft.com', 'PixelSoft'),
(40, 'Montserrat', 'Alicia', 'Romero', 'Salas', 2147483647, 'maromero@codesphere.com', 'CodeSphere'),
(41, 'Ignacio', 'Julián', 'Pineda', 'Meza', 2147483647, 'ijpineda@devmasters.com', 'DevMasters'),
(42, 'Sergio', 'Adolfo', 'Quintero', 'Valle', 2147483647, 'saquintero@skylinesoft.com', 'Skyline Software'),
(43, 'Ximena', 'Carolina', 'Ortega', 'Barrios', 2147483647, 'xcortega@logicware.com', 'LogicWare'),
(44, 'Adriana', 'Elizabeth', 'Palacios', 'Campos', 2147483647, 'aepalacios@appcreators.com', 'AppCreators'),
(45, 'Marcelo', 'Rubén', 'Chávez', 'Naranjo', 2147483647, 'mrchavez@techwave.com', 'TechWave'),
(46, 'Rafael', 'Cristian', 'Solís', 'Ocampo', 2147483647, 'rcsolis@techsoft.com', 'TechSoft Solutions'),
(47, 'María', 'Alejandra', 'Figueroa', 'Hidalgo', 2147483647, 'mafigueroa@codecraft.io', 'CodeCraft'),
(48, 'Pedro', 'Tomás', 'Alvarado', 'Cárdenas', 2147483647, 'ptalvarado@innovdev.com', 'InnovDev'),
(49, 'Fernanda', 'Dulce', 'Cruz', 'Jiménez', 2147483647, 'fdcruz@softnext.com', 'SoftNext'),
(50, 'Ed', 'Mundo', 'Viveros', 'German', 2147483647, 'mundo.mundo@gmail.com', 'AlphaCode'),
(51, 'juan', 'ramon', 'sanchez', 'perez', 2147483647, 'juan12@gmail.com', 'PixelSoft');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificacionproyectop1`
--

CREATE TABLE `calificacionproyectop1` (
  `Id` int(11) NOT NULL,
  `Proyecto` text NOT NULL,
  `Antecedentes` int(11) DEFAULT NULL,
  `Planteamiento` int(11) DEFAULT NULL,
  `Justificacion` int(11) DEFAULT NULL,
  `Objetivos` int(11) DEFAULT NULL,
  `ObjetivosEspecificos` int(11) DEFAULT NULL,
  `Calificacion` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificacionproyectop1`
--

INSERT INTO `calificacionproyectop1` (`Id`, `Proyecto`, `Antecedentes`, `Planteamiento`, `Justificacion`, `Objetivos`, `ObjetivosEspecificos`, `Calificacion`) VALUES
(16, 'SOGPEE', 10, 5, 8, 8, 9, 8),
(17, 'Diseño y Optimización de un Sistema de Refrigeración para Motores de Combustión Interna', 8, 5, 5, 5, 5, 5.6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificacionproyectop2`
--

CREATE TABLE `calificacionproyectop2` (
  `id` int(11) NOT NULL,
  `Proyecto` text NOT NULL,
  `Marco` int(11) NOT NULL,
  `Metodologia` int(11) NOT NULL,
  `Cronograma` int(11) NOT NULL,
  `Desarrollo` int(11) NOT NULL,
  `Calificacion` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificacionproyectop2`
--

INSERT INTO `calificacionproyectop2` (`id`, `Proyecto`, `Marco`, `Metodologia`, `Cronograma`, `Desarrollo`, `Calificacion`) VALUES
(5, 'SOGPEE', 10, 10, 10, 10, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificacionproyectop3`
--

CREATE TABLE `calificacionproyectop3` (
  `id` int(11) NOT NULL,
  `Proyecto` text NOT NULL,
  `Resultados` int(11) NOT NULL,
  `Conclusiones` int(11) NOT NULL,
  `Referencias` int(11) NOT NULL,
  `Anexos` int(11) NOT NULL,
  `Calificacion` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificacionproyectop3`
--

INSERT INTO `calificacionproyectop3` (`id`, `Proyecto`, `Resultados`, `Conclusiones`, `Referencias`, `Anexos`, `Calificacion`) VALUES
(2, 'SOGPEE', 9, 10, 6, 10, 8.75),
(3, 'Diseño y Optimización de un Sistema de Refrigeración para Motores de Combustión Interna', 7, 8, 8, 10, 8.25);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carreras`
--

CREATE TABLE `carreras` (
  `IdCarrera` varchar(5) NOT NULL,
  `NombreCarrera` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carreras`
--

INSERT INTO `carreras` (`IdCarrera`, `NombreCarrera`) VALUES
('IF', 'Ingeniería Financiera'),
('IMA', 'Ingeniería Mecánica Automotriz'),
('IS', 'Ingeniería en Software'),
('ITM', 'Ingeniería en Tecnologías de Manufactura'),
('LNI', 'Licenciatura en Negocios Internacionales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cartas`
--

CREATE TABLE `cartas` (
  `Id` int(11) NOT NULL,
  `Matricula` int(11) NOT NULL,
  `Cartas` text NOT NULL,
  `Parcial` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cartas`
--

INSERT INTO `cartas` (`Id`, `Matricula`, `Cartas`, `Parcial`) VALUES
(1, 1322134083, 'Documentos\\1322134083\\Parcial1\\Cartas\\cartasJesusMargaritoParcial1.pdf', 'Parcial 1'),
(2, 1322134083, 'Documentos\\1322134083\\Parcial3\\Cartas\\cartasJesusMargaritoParcial3.pdf', 'Parcial 3'),
(4, 1322134083, 'Documentos\\1322134083\\Parcial2\\Cartas\\cartasJesusMargaritoParcial2.pdf', 'Parcial 2'),
(5, 1322134100, 'Documentos\\1322134100\\Parcial1\\Cartas\\cartasMonicaRocioParcial1.pdf', 'Parcial 1'),
(6, 1322130003, 'Documentos\\1322130003\\Parcial 1\\Cartas\\cartasLuisFernandoParcial_1.pdf', 'Parcial 1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coordinacion`
--

CREATE TABLE `coordinacion` (
  `Id` int(11) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Nombre2` varchar(20) NOT NULL,
  `ApellidoP` varchar(25) NOT NULL,
  `ApellidoM` varchar(20) NOT NULL,
  `Correo` varchar(50) NOT NULL,
  `Password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `coordinacion`
--

INSERT INTO `coordinacion` (`Id`, `Nombre`, `Nombre2`, `ApellidoP`, `ApellidoM`, `Correo`, `Password`) VALUES
(1, 'Carmen', '', 'Alarcon', 'Mendoza', 'carmen_mendoza@uptecamac.edu.mx', 'carmen2023');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documentos`
--

CREATE TABLE `documentos` (
  `Id` int(11) NOT NULL,
  `Matricula` int(11) NOT NULL,
  `Proyecto` text NOT NULL,
  `Parcial` text NOT NULL,
  `NombreProyecto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `documentos`
--

INSERT INTO `documentos` (`Id`, `Matricula`, `Proyecto`, `Parcial`, `NombreProyecto`) VALUES
(19, 1322134083, 'static/Documentos\\1322134083\\Parcial 3\\Proyecto\\proyetoJesusMargaritoParcial_3.pdf', 'Parcial 3', 'SOGPEE'),
(20, 1322134085, 'static/Documentos\\1322134085\\Parcial 3\\Proyecto\\proyetoAnaMariaParcial_3.pdf', 'Parcial 3', 'Iris'),
(21, 1322134099, 'static/Documentos\\1322134099\\Parcial 3\\Proyecto\\proyetoOscarEduardoParcial_3.pdf', 'Parcial 3', 'Mar'),
(22, 1322134101, 'static/Documentos\\1322134101\\Parcial 3\\Proyecto\\proyetoRamonHumbertoParcial_3.pdf', 'Parcial 3', 'Gestion'),
(23, 1322130001, 'static/Documentos\\1322130001\\Parcial 3\\Proyecto\\proyetoJuanCarlosParcial_3.pdf', 'Parcial 3', 'Sistema Integrado de Gestión de Operaciones (SIGO)'),
(24, 1322130005, 'static/Documentos\\1322130005\\Parcial 3\\Proyecto\\proyetoCarlosParcial_3.pdf', 'Parcial 3', 'Diseño y Optimización de un Sistema de Refrigeración para Motores de Combustión Interna'),
(25, 1322130019, 'static/Documentos\\1322130019\\Parcial 3\\Proyecto\\proyetoRicardoManuelParcial_3.pdf', 'Parcial 3', 'Desarrollo de un Modelo de Optimización Financiera para la Gestión de Inversiones en Pequeñas Empresas'),
(26, 1322134093, 'static/Documentos\\1322134093\\Parcial 3\\Proyecto\\proyetoRicardoAlonsoParcial_3.pdf', 'Parcial 3', 'aaa'),
(27, 1322130003, 'static/Documentos\\1322130003\\Parcial 1\\Proyecto\\proyetoLuisFernandoParcial_1.pdf', 'Parcial 1', 'Sistema Integrado de Gestión de Operaciones (SIGO)'),
(28, 1322134083, 'static/Documentos\\1322134083\\Parcial 1\\Proyecto\\proyetoJesusMargaritoParcial_1.pdf', 'Parcial 1', 'SOGPEE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
  `EmpresaID` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Domicilio` text NOT NULL,
  `Correo` text NOT NULL,
  `Telefono` int(10) NOT NULL,
  `Sector` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`EmpresaID`, `Nombre`, `Domicilio`, `Correo`, `Telefono`, `Sector`) VALUES
(1, 'TechSoft Solutions', '123 Avenida Principal, CiudadTech', 'info@techsoft.com', 2147483647, 'Desarrollo de Software'),
(2, 'CodeCraft', '456 Calle Innovación, Zona IT', 'contacto@codecraft.io', 2147483647, 'Desarrollo de Software'),
(3, 'InnovDev', '789 Bulevar Tecnología, Distrito Digital', 'hello@innovdev.com', 2147483647, 'Desarrollo de Software'),
(4, 'SoftNext', '321 Circuito Programadores, Parque Tecnológico', 'support@softnext.com', 2147483647, 'Desarrollo de Software'),
(5, 'DevPeak', '654 Camino Desarrollo, Centro Creativo', 'admin@devpeak.com', 2147483647, 'Desarrollo de Software'),
(6, 'BlueCode Labs', '1234 Calle Digital, Zona Tecnológica', 'contacto@bluecode.com', 2147483647, 'Desarrollo de Software'),
(7, 'NextGen Devs', '5678 Avenida Futuro, Ciudad Innovadora', 'info@nextgendevs.com', 2147483647, 'Desarrollo de Software'),
(8, 'AlphaCode', '9101 Bulevar Alfa, Distrito IT', 'support@alphacode.com', 2147483647, 'Desarrollo de Software'),
(9, 'PixelSoft', '1122 Calle Pixel, Parque Creativo', 'admin@pixelsoft.com', 2147483647, 'Desarrollo de Software'),
(10, 'CodeSphere', '3344 Camino Código, Zona Innovación', 'hello@codesphere.com', 2147483647, 'Desarrollo de Software'),
(11, 'DevMasters', '5566 Avenida Progreso, Distrito Digital', 'info@devmasters.com', 2147483647, 'Desarrollo de Software'),
(12, 'Skyline Software', '7788 Circuito Nube, Parque Tecnológico', 'contacto@skylinesoft.com', 2147483647, 'Desarrollo de Software'),
(13, 'LogicWare', '9900 Calle Lógica, Zona Empresarial', 'soporte@logicware.com', 2147483647, 'Desarrollo de Software'),
(14, 'AppCreators', '123 Circuito Innovación, Distrito Creativo', 'info@appcreators.com', 2147483647, 'Desarrollo de Software'),
(15, 'TechWave', '456 Bulevar Tecnología, Ciudad del Futuro', 'contact@techwave.com', 2147483647, 'Desarrollo de Software');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encuesta08`
--

CREATE TABLE `encuesta08` (
  `Id` int(11) NOT NULL,
  `Promedio` decimal(4,2) NOT NULL,
  `Veracidad` varchar(3) NOT NULL,
  `Matricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `encuesta08`
--

INSERT INTO `encuesta08` (`Id`, `Promedio`, `Veracidad`, `Matricula`) VALUES
(7, 10.00, 'si', 1322130010);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `Id` int(11) NOT NULL,
  `Matricula` int(10) NOT NULL,
  `NoEquipo` int(11) NOT NULL,
  `Id_Proyecto` int(11) NOT NULL,
  `Procedimiento` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`Id`, `Matricula`, `NoEquipo`, `Id_Proyecto`, `Procedimiento`) VALUES
(195, 1322134083, 1, 3, 'ESTNC1'),
(196, 1322134084, 1, 3, 'ESTNC1'),
(197, 1322134085, 2, 4, 'ESTNC1'),
(198, 1322134086, 2, 4, 'ESTNC1'),
(199, 1322134087, 2, 4, 'ESTNC1'),
(200, 1322134099, 3, 5, 'ESTNC2'),
(202, 1322134101, 4, 7, 'ESTNC2'),
(203, 1322130001, 5, 8, 'ESTNC2'),
(204, 1322130002, 5, 8, 'ESTNC2'),
(205, 1322130003, 5, 8, 'ESTNC2'),
(206, 1322130004, 5, 8, 'ESTNC2'),
(218, 1322130005, 6, 20, 'ESTD'),
(219, 1322130006, 6, 20, 'ESTD'),
(220, 1322130019, 7, 21, 'ESTD'),
(221, 1322130020, 7, 21, 'ESTD'),
(222, 1322134093, 8, 24, 'ESTNC1'),
(223, 1322134094, 9, 25, 'ESTNC2'),
(225, 1322134095, 10, 26, 'ESTD'),
(226, 1322130025, 11, 27, 'ESTNC2'),
(227, 1322130010, 12, 28, 'ESTD'),
(228, 1322134083, 13, 29, 'ESTNC2'),
(229, 1322134083, 14, 30, 'ESTNC1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `Matricula` int(10) NOT NULL,
  `Nombre1` varchar(20) NOT NULL,
  `Nombre2` varchar(20) NOT NULL,
  `ApellidoP` varchar(20) NOT NULL,
  `ApellidoM` varchar(20) NOT NULL,
  `Telefono` varchar(10) NOT NULL,
  `Correo` text NOT NULL,
  `Carrera` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`Matricula`, `Nombre1`, `Nombre2`, `ApellidoP`, `ApellidoM`, `Telefono`, `Correo`, `Carrera`) VALUES
(1322130001, 'Juan', 'Carlos', 'Gómez', 'Pérez', '5512345678', 'juan_1322130001@uptecamac.edu.mx', 'IMA'),
(1322130002, 'Ana', '', 'Martínez', 'López', '5523456789', 'ana_1322130002@uptecamac.edu.mx', 'IMA'),
(1322130003, 'Luis', 'Fernando', 'Hernández', 'Ruiz', '5534567890', 'luis_1322130003@uptecamac.edu.mx', 'IMA'),
(1322130004, 'María', 'José', 'Torres', 'Sánchez', '5545678901', 'maria_1322130004@uptecamac.edu.mx', 'IMA'),
(1322130005, 'Carlos', '', 'Ramírez', 'Díaz', '5556789012', 'carlos_1322130005@uptecamac.edu.mx', 'IMA'),
(1322130006, 'Fernanda', 'Sofía', 'Vargas', 'Méndez', '5567890123', 'fernanda_1322130006@uptecamac.edu.mx', 'IMA'),
(1322130007, 'Pablo', 'Andrés', 'Luna', 'García', '5578901234', 'pablo_1322130007@uptecamac.edu.mx', 'IMA'),
(1322130008, 'Samantha', '', 'Ortega', 'Flores', '5589012345', 'samantha_1322130008@uptecamac.edu.mx', 'IMA'),
(1322130009, 'Héctor', 'Iván', 'Castro', 'Morales', '5590123456', 'hector_1322130009@uptecamac.edu.mx', 'IMA'),
(1322130010, 'Valeria', 'Ximena', 'Navarro', 'Rodríguez', '5501234567', 'valeria_1322130010@uptecamac.edu.mx', 'IMA'),
(1322130011, 'Diego', 'Emiliano', 'Fernández', 'Lara', '5511223344', 'diego_1322130011@uptecamac.edu.mx', 'IF'),
(1322130012, 'Andrea', 'Isabel', 'Mendoza', 'Ríos', '5522334455', 'andrea_1322130012@uptecamac.edu.mx', 'IF'),
(1322130013, 'Oscar', '', 'Gutiérrez', 'Campos', '5533445566', 'oscar_1322130013@uptecamac.edu.mx', 'IF'),
(1322130014, 'Paola', 'Michelle', 'Hidalgo', 'Vega', '5544556677', 'paola_1322130014@uptecamac.edu.mx', 'IF'),
(1322130015, 'Jorge', 'Arturo', 'Salinas', 'Bravo', '5555667788', 'jorge_1322130015@uptecamac.edu.mx', 'IF'),
(1322130016, 'Elena', '', 'Zamora', 'Suárez', '5566778899', 'elena_1322130016@uptecamac.edu.mx', 'IF'),
(1322130017, 'Adrián', 'José', 'Escobar', 'Ochoa', '5577889900', 'adrian_1322130017@uptecamac.edu.mx', 'IF'),
(1322130018, 'Gabriela', 'Fernanda', 'León', 'Pacheco', '5588990011', 'gabriela_1322130018@uptecamac.edu.mx', 'IF'),
(1322130019, 'Ricardo', 'Manuel', 'Aguilar', 'Cortés', '5599001122', 'ricardo_1322130019@uptecamac.edu.mx', 'IF'),
(1322130020, 'Sofía', 'Beatriz', 'Estrada', 'Delgado', '5500112233', 'sofia_1322130020@uptecamac.edu.mx', 'IF'),
(1322130021, 'Martín', '', 'Pérez', 'González', '5512341122', 'martin_1322130021@uptecamac.edu.mx', 'ITM'),
(1322130022, 'Camila', 'Renata', 'Silva', 'Molina', '5523452233', 'camila_1322130022@uptecamac.edu.mx', 'ITM'),
(1322130023, 'Alberto', 'Joaquín', 'Rojas', 'Hernández', '5534563344', 'alberto_1322130023@uptecamac.edu.mx', 'ITM'),
(1322130024, 'Daniela', '', 'Santos', 'López', '5545674455', 'daniela_1322130024@uptecamac.edu.mx', 'ITM'),
(1322130025, 'Hugo', 'Esteban', 'Ortega', 'Ramírez', '5556785566', 'hugo_1322130025@uptecamac.edu.mx', 'ITM'),
(1322130026, 'Natalia', 'Paulina', 'Castillo', 'Jiménez', '5567896677', 'natalia_1322130026@uptecamac.edu.mx', 'ITM'),
(1322130027, 'Rodrigo', '', 'Delgado', 'Vázquez', '5578907788', 'rodrigo_1322130027@uptecamac.edu.mx', 'ITM'),
(1322130028, 'Isabela', 'Andrea', 'Núñez', 'Medina', '5589018899', 'isabela_1322130028@uptecamac.edu.mx', 'ITM'),
(1322130029, 'Javier', 'Raúl', 'Peña', 'Flores', '5590129900', 'javier_1322130029@uptecamac.edu.mx', 'ITM'),
(1322130030, 'Lucía', '', 'Suárez', 'Gómez', '5501230001', 'lucia_1322130030@uptecamac.edu.mx', 'ITM'),
(1322130031, 'Fabián', 'Alejandro', 'Méndez', 'Soto', '5512349988', 'fabian_1322130031@uptecamac.edu.mx', 'LNI'),
(1322130032, 'Regina', '', 'Cruz', 'García', '5523458877', 'regina_1322130032@uptecamac.edu.mx', 'LNI'),
(1322130033, 'Samuel', 'Omar', 'Lara', 'Ruiz', '5534567766', 'samuel_1322130033@uptecamac.edu.mx', 'LNI'),
(1322130034, 'Montserrat', 'Diana', 'Ramos', 'Paredes', '5545676655', 'montserrat_1322130034@uptecamac.edu.mx', 'LNI'),
(1322130035, 'Iván', '', 'Escamilla', 'Rosales', '5556785544', 'ivan_1322130035@uptecamac.edu.mx', 'LNI'),
(1322130036, 'Ximena', 'Mariana', 'Gómez', 'Aguilar', '5567894433', 'ximena_1322130036@uptecamac.edu.mx', 'LNI'),
(1322130037, 'Fernando', 'Diego', 'Carranza', 'López', '5578903322', 'fernando_1322130037@uptecamac.edu.mx', 'LNI'),
(1322130038, 'Valentina', '', 'Chávez', 'Delgado', '5589012211', 'valentina_1322130038@uptecamac.edu.mx', 'LNI'),
(1322130039, 'Cristian', 'Antonio', 'Ochoa', 'Maldonado', '5590121100', 'cristian_1322130039@uptecamac.edu.mx', 'LNI'),
(1322130040, 'Paula', 'Estrella', 'Miranda', 'Navarro', '5501230099', 'paula_1322130040@uptecamac.edu.mx', 'LNI'),
(1322134083, 'Jesus', 'Margarito', 'Santos', 'Garcia', '5547062133', 'jesus_1322134083@uptecamac.edu.mx', 'IS'),
(1322134084, 'Luis', 'Antonio', 'Hernández', 'Pérez', '5547062144', 'luis_1322134084@uptecamac.edu.mx', 'IS'),
(1322134085, 'Ana', 'María', 'López', 'Gómez', '5547062155', 'ana_1322134085@uptecamac.edu.mx', 'IS'),
(1322134086, 'Carlos', 'Eduardo', 'Martínez', 'Santos', '5547062166', 'carlos_1322134086@uptecamac.edu.mx', 'IS'),
(1322134087, 'María', 'Fernanda', 'Rodríguez', 'Hernández', '5547062177', 'maria_1322134087@uptecamac.edu.mx', 'IS'),
(1322134088, 'Jorge', 'Iván', 'García', 'Luna', '5547062188', 'jorge_1322134088@uptecamac.edu.mx', 'IS'),
(1322134089, 'Laura', 'Beatriz', 'Sánchez', 'Cruz', '5547062199', 'laura_1322134089@uptecamac.edu.mx', 'IS'),
(1322134090, 'Fernando', 'Andrés', 'Ramírez', 'Mendoza', '5547062200', 'fernando_1322134090@uptecamac.edu.mx', 'IS'),
(1322134091, 'Diana', 'Carolina', 'Morales', 'Torres', '5547062211', 'diana_1322134091@uptecamac.edu.mx', 'IS'),
(1322134092, 'Sofía', 'Isabel', 'Vargas', 'Flores', '5547062222', 'sofia_1322134092@uptecamac.edu.mx', 'IS'),
(1322134093, 'Ricardo', 'Alonso', 'Navarro', 'Valencia', '5547062233', 'ricardo_1322134093@uptecamac.edu.mx', 'IS'),
(1322134094, 'Gabriela', 'Esther', 'Castillo', 'Jiménez', '5547062244', 'gabriela_1322134094@uptecamac.edu.mx', 'IS'),
(1322134095, 'Juan', 'Pablo', 'Reyes', 'Salazar', '5547062255', 'juan_1322134095@uptecamac.edu.mx', 'IS'),
(1322134096, 'Liliana', 'Guadalupe', 'Mendoza', 'Cortés', '5547062266', 'liliana_1322134096@uptecamac.edu.mx', 'IS'),
(1322134097, 'Francisco', 'Javier', 'Ortega', 'Meza', '5547062277', 'francisco_1322134097@uptecamac.edu.mx', 'IS'),
(1322134098, 'Cecilia', 'Elena', 'Gómez', 'González', '5547062288', 'cecilia_1322134098@uptecamac.edu.mx', 'IS'),
(1322134099, 'Oscar', 'Eduardo', 'Luna', 'Moreno', '5547062299', 'oscar_1322134099@uptecamac.edu.mx', 'IS'),
(1322134100, 'Mónica', 'Rocío', 'Pérez', 'Rojas', '5547062300', 'monica_1322134100@uptecamac.edu.mx', 'IS'),
(1322134101, 'Ramón', 'Humberto', 'Campos', 'Vega', '5547062311', 'ramon_1322134101@uptecamac.edu.mx', 'IS'),
(1322134102, 'Claudia', 'Ximena', 'Aguilar', 'Zavala', '5547062322', 'claudia_1322134102@uptecamac.edu.mx', 'IS'),
(1322134103, 'Guillermo', 'Fabián', 'Zavala', 'Rosales', '5547062333', 'guillermo_1322134103@uptecamac.edu.mx', 'IS'),
(1322134104, 'Alejandra', 'Lucía', 'Valencia', 'Rojas', '5547062344', 'alejandra_1322134104@uptecamac.edu.mx', 'IS'),
(1322134105, 'Javier', 'Eduardo', 'Padilla', 'Sandoval', '5547062355', 'javier_1322134105@uptecamac.edu.mx', 'IS'),
(1322134106, 'Regina', 'Adriana', 'Salinas', 'Fernández', '5547062366', 'regina_1322134106@uptecamac.edu.mx', 'IS'),
(1322134107, 'Armando', 'Israel', 'González', 'Navarrete', '5547062377', 'armando_1322134107@uptecamac.edu.mx', 'IS'),
(1322134108, 'Beatriz', 'Inés', 'Cabrera', 'Lara', '5547062388', 'beatriz_1322134108@uptecamac.edu.mx', 'IS'),
(1322134109, 'José', 'Luis', 'Esquivel', 'Reyes', '5547062399', 'jose_1322134109@uptecamac.edu.mx', 'IS'),
(1322134110, 'Rocío', 'Margarita', 'Torres', 'Estrada', '5547062400', 'rocio_1322134110@uptecamac.edu.mx', 'IS'),
(1322134111, 'Felipe', 'Miguel', 'Castañeda', 'Trujillo', '5547062411', 'felipe_1322134111@uptecamac.edu.mx', 'IS'),
(1322134112, 'Karla', 'Fernanda', 'Pérez', 'Chavarría', '5547062422', 'karla_1322134112@uptecamac.edu.mx', 'IS'),
(1322134113, 'Eduardo', 'Iván', 'Moreno', 'Villalobos', '5547062433', 'eduardo_1322134113@uptecamac.edu.mx', 'IS'),
(1322134114, 'Jessica', 'Lorena', 'Fuentes', 'Quintana', '5547062444', 'jessica_1322134114@uptecamac.edu.mx', 'IS'),
(1322134115, 'Alberto', 'Francisco', 'Hernández', 'Ruiz', '5547062455', 'alberto_1322134115@uptecamac.edu.mx', 'IS'),
(1322134116, 'Clara', 'Luz', 'Martínez', 'Gómez', '5547062466', 'clara_1322134116@uptecamac.edu.mx', 'IS'),
(1322134117, 'Emanuel', 'Joaquín', 'Reyes', 'Domínguez', '5547062477', 'emanuel_1322134117@uptecamac.edu.mx', 'IS'),
(1322134118, 'Victoria', 'Angélica', 'Núñez', 'Campos', '5547062488', 'victoria_1322134118@uptecamac.edu.mx', 'IS'),
(1322134119, 'Diego', 'Ricardo', 'Mendoza', 'Peña', '5547062499', 'diego_1322134119@uptecamac.edu.mx', 'IS'),
(1322134120, 'Montserrat', 'Alicia', 'Romero', 'Salas', '5547062500', 'montserrat_1322134120@uptecamac.edu.mx', 'IS'),
(1322134121, 'Ignacio', 'Julián', 'Pineda', 'Meza', '5547062511', 'ignacio_1322134121@uptecamac.edu.mx', 'IS'),
(1322134122, 'Sergio', 'Adolfo', 'Quintero', 'Valle', '5547062522', 'sergio_1322134122@uptecamac.edu.mx', 'IS'),
(1322134123, 'Ximena', 'Carolina', 'Ortega', 'Barrios', '5547062533', 'ximena_1322134123@uptecamac.edu.mx', 'IS'),
(1322134124, 'Adriana', 'Elizabeth', 'Palacios', 'Campos', '5547062544', 'adriana_1322134124@uptecamac.edu.mx', 'IS'),
(1322134125, 'Marcelo', 'Rubén', 'Chávez', 'Naranjo', '5547062555', 'marcelo_1322134125@uptecamac.edu.mx', 'IS'),
(1322134126, 'Rafael', 'Cristian', 'Solís', 'Ocampo', '5547062566', 'rafael_1322134126@uptecamac.edu.mx', 'IS'),
(1322134127, 'María', 'Alejandra', 'Figueroa', 'Hidalgo', '5547062577', 'maria_1322134127@uptecamac.edu.mx', 'IS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `foest02`
--

CREATE TABLE `foest02` (
  `Id` int(11) NOT NULL,
  `FechaValoracion` date DEFAULT current_timestamp(),
  `Proyecto` varchar(100) DEFAULT NULL,
  `Miembro` int(10) DEFAULT NULL,
  `Empresa` text NOT NULL,
  `GradoEstudios` varchar(50) DEFAULT NULL,
  `AsesorEmpresarial` text NOT NULL,
  `Puntualidad` int(11) NOT NULL,
  `Responsabilidad` int(11) NOT NULL,
  `Etica` int(11) NOT NULL,
  `TomaDecisiones` int(11) NOT NULL,
  `Liderazgo` int(11) NOT NULL,
  `ExpresaIdeas` int(11) NOT NULL,
  `ComunicacionAsertiva` int(11) NOT NULL,
  `ResolucionSituaciones` int(11) NOT NULL,
  `ActitudFavorable` int(11) NOT NULL,
  `TrabajoEnEquipo` int(11) NOT NULL,
  `PromedioActitud` int(11) NOT NULL,
  `Estrategias` int(11) NOT NULL,
  `AccionesMejora` int(11) NOT NULL,
  `ProcesosOperacion` int(11) NOT NULL,
  `PlanteaSoluciones` int(11) NOT NULL,
  `RespondeNecesidades` int(11) NOT NULL,
  `CumpleTiempo` int(11) NOT NULL,
  `PromedioDesarrollo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `foest02`
--

INSERT INTO `foest02` (`Id`, `FechaValoracion`, `Proyecto`, `Miembro`, `Empresa`, `GradoEstudios`, `AsesorEmpresarial`, `Puntualidad`, `Responsabilidad`, `Etica`, `TomaDecisiones`, `Liderazgo`, `ExpresaIdeas`, `ComunicacionAsertiva`, `ResolucionSituaciones`, `ActitudFavorable`, `TrabajoEnEquipo`, `PromedioActitud`, `Estrategias`, `AccionesMejora`, `ProcesosOperacion`, `PlanteaSoluciones`, `RespondeNecesidades`, `CumpleTiempo`, `PromedioDesarrollo`) VALUES
(6, '2025-06-08', 'Iris', 1322134085, 'CodeCraft', 'Lic.', 'María Alejandra Figueroa Hidalgo', 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
(7, '2025-06-08', 'Iris', 1322134086, 'CodeCraft', 'Lic.', 'María Alejandra Figueroa Hidalgo', 10, 9, 8, 7, 7, 8, 7, 8, 7, 7, 7, 7, 9, 9, 9, 9, 8, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `foest07`
--

CREATE TABLE `foest07` (
  `Id_FOEST07` int(11) NOT NULL,
  `FechaValoracion` date DEFAULT current_timestamp(),
  `Periodo` varchar(50) DEFAULT NULL,
  `TituloProyecto` text DEFAULT NULL,
  `NoEquipo` int(11) DEFAULT NULL,
  `Procedimiento` varchar(6) NOT NULL,
  `NombreEmpresa` varchar(100) DEFAULT NULL,
  `Modalidad` varchar(50) DEFAULT NULL,
  `GradoEstudiosAsesorEmp` varchar(100) DEFAULT NULL,
  `NombreAsesorEmp` varchar(100) DEFAULT NULL,
  `TipoEmpresa` varchar(20) DEFAULT NULL,
  `GiroEmpresa` varchar(50) DEFAULT NULL,
  `Capital` varchar(20) DEFAULT NULL,
  `AniosOperacion` varchar(20) DEFAULT NULL,
  `TamanioEmpresa` varchar(50) DEFAULT NULL,
  `MercadoVenta` varchar(100) DEFAULT NULL,
  `Carrera` text DEFAULT NULL,
  `FuncionesPrioritarias` text DEFAULT NULL,
  `FuncionesPrioritarias2` text NOT NULL,
  `FuncionesPrioritarias3` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `foest07`
--

INSERT INTO `foest07` (`Id_FOEST07`, `FechaValoracion`, `Periodo`, `TituloProyecto`, `NoEquipo`, `Procedimiento`, `NombreEmpresa`, `Modalidad`, `GradoEstudiosAsesorEmp`, `NombreAsesorEmp`, `TipoEmpresa`, `GiroEmpresa`, `Capital`, `AniosOperacion`, `TamanioEmpresa`, `MercadoVenta`, `Carrera`, `FuncionesPrioritarias`, `FuncionesPrioritarias2`, `FuncionesPrioritarias3`) VALUES
(25, '2025-06-03', 'SEPTIEMBRE-DICIEMBRE - 2025', 'Iris', 2, 'ESTNC1', 'CodeCraft', 'Estudiante en empresa', 'Mtra.', 'María Alejandra Figueroa Hidalgo', 'UPT', 'Manufacturera o industrial', 'Extranjero', '1-5', 'Pequeña', 'Local-Nacional', 'Ingenieria en Software', 'Aplicación adecuada de técnicas de desarrollo software', 'Identificación de oportunidades de mejora en el área o procesos', 'chimicuil');

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
  `Promedio` float NOT NULL,
  `Veracidad` varchar(2) NOT NULL,
  `Comentarios` text NOT NULL,
  `Matricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `foest08`
--

INSERT INTO `foest08` (`IdFoest08`, `Pregunta01`, `Pregunta02`, `Pregunta03`, `Pregunta04`, `Pregunta05`, `Pregunta06`, `Pregunta07`, `Pregunta08`, `Pregunta09`, `Promedio`, `Veracidad`, `Comentarios`, `Matricula`) VALUES
(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 'Si', 'Sin comentarios', 1322134083);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `periodos`
--

CREATE TABLE `periodos` (
  `idPeriodo` varchar(11) NOT NULL,
  `PeriodoCuatrimestral` varchar(25) NOT NULL,
  `Estado` varchar(10) NOT NULL,
  `Anio` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `periodos`
--

INSERT INTO `periodos` (`idPeriodo`, `PeriodoCuatrimestral`, `Estado`, `Anio`) VALUES
('Ene-Abr', 'ENERO-ABRIL', 'inactivo', '2025'),
('May-Ago', 'MAYO-AGOSTO', 'inactivo', '2025'),
('Sep-Dic', 'SEPTIEMBRE-DICIEMBRE', 'activo', '2025');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `procedimientos`
--

CREATE TABLE `procedimientos` (
  `idProcedimiento` varchar(6) NOT NULL,
  `Procedimiento` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `procedimientos`
--

INSERT INTO `procedimientos` (`idProcedimiento`, `Procedimiento`) VALUES
('ESTD', 'Estadía'),
('ESTNC1', 'Estancia 1'),
('ESTNC2', 'Estancia 2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `ProyectoID` int(11) NOT NULL,
  `Nombre` text NOT NULL,
  `Funcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`ProyectoID`, `Nombre`, `Funcion`) VALUES
(3, 'SOGPEE', 'Estancias y estadias'),
(4, 'Iris', 'Clones de su creador'),
(5, 'Mar', 'Marrrrr'),
(7, 'Gestion', 'Automatizar'),
(8, 'Sistema Integrado de Gestión de Operaciones (SIGO)', 'optimizar y estandarizar procesos operativos a nivel globaL'),
(16, 'Desarrollo de un Sistema de Control y Seguimiento ', 'Crear una plataforma web que permita a las empresas monitorear el avance de sus proyectos en tiempo real, facilitando la gestión de tareas, asignación de recursos y generación de reportes de progreso.'),
(20, 'Diseño y Optimización de un Sistema de Refrigeración para Motores de Combustión Interna', 'Desarrollar y mejorar un sistema de enfriamiento eficiente para motores de combustión interna mediante simulaciones térmicas y pruebas experimentales, con el objetivo de optimizar el rendimiento del motor, reducir el consumo de combustible y minimizar el impacto ambiental.'),
(21, 'Desarrollo de un Modelo de Optimización Financiera para la Gestión de Inversiones en Pequeñas Empresas', 'Crear un modelo financiero basado en análisis de riesgo y rentabilidad que ayude a las pequeñas empresas a tomar decisiones estratégicas de inversión, maximizando ganancias y minimizando riesgos mediante herramientas como simulaciones de Monte Carlo y análisis de sensibilidad.'),
(24, 'aaa', 'aaaa'),
(25, 'qqqqqq', 'qqqqq'),
(26, 'wwwwww', 'wwww'),
(27, 'Submarino', 'funcionamiento'),
(28, 'GESTOR DE MECANICA', 'MANUALES'),
(29, 'Owiwiwi', 'Owiwiwi'),
(30, 'owiwiwiw2', 'ksjka');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectoasesores`
--

CREATE TABLE `proyectoasesores` (
  `Id` int(11) NOT NULL,
  `Id_asesorE` int(11) NOT NULL,
  `Id_asesorA` int(11) NOT NULL,
  `Id_proyecto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyectoasesores`
--

INSERT INTO `proyectoasesores` (`Id`, `Id_asesorE`, `Id_asesorA`, `Id_proyecto`) VALUES
(9, 21, 17, 3),
(10, 47, 2, 4),
(11, 38, 10, 5),
(13, 38, 10, 7),
(14, 17, 31, 8),
(26, 41, 17, 20),
(27, 15, 19, 21),
(30, 38, 10, 24),
(31, 38, 10, 25),
(32, 38, 10, 26),
(33, 30, 2, 27),
(34, 47, 5, 28),
(36, 23, 10, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ser`
--

CREATE TABLE `ser` (
  `ID` int(11) NOT NULL,
  `Puntualidad` int(11) NOT NULL,
  `Responsabilidad` int(11) NOT NULL,
  `Atencion` int(11) NOT NULL,
  `Etica` int(11) NOT NULL,
  `Capacidad` int(11) NOT NULL,
  `Liderazgo` int(11) NOT NULL,
  `Calificacion` float NOT NULL,
  `Matricula` int(11) NOT NULL,
  `Parcial` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ser`
--

INSERT INTO `ser` (`ID`, `Puntualidad`, `Responsabilidad`, `Atencion`, `Etica`, `Capacidad`, `Liderazgo`, `Calificacion`, `Matricula`, `Parcial`) VALUES
(18, 8, 8, 10, 10, 10, 10, 9.3, 1322134083, 'Parcial 3'),
(19, 8, 8, 9, 10, 5, 8, 8, 1322130006, 'Parcial 2');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asesoracademico`
--
ALTER TABLE `asesoracademico`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `asesorempresarial`
--
ALTER TABLE `asesorempresarial`
  ADD PRIMARY KEY (`AsesorID`),
  ADD KEY `EmpresaID` (`Empresa`);

--
-- Indices de la tabla `calificacionproyectop1`
--
ALTER TABLE `calificacionproyectop1`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `calificacionproyectop2`
--
ALTER TABLE `calificacionproyectop2`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `calificacionproyectop3`
--
ALTER TABLE `calificacionproyectop3`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `carreras`
--
ALTER TABLE `carreras`
  ADD PRIMARY KEY (`IdCarrera`);

--
-- Indices de la tabla `cartas`
--
ALTER TABLE `cartas`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Matricula` (`Matricula`);

--
-- Indices de la tabla `coordinacion`
--
ALTER TABLE `coordinacion`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `documentos`
--
ALTER TABLE `documentos`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Matricula` (`Matricula`);

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`EmpresaID`),
  ADD UNIQUE KEY `Nombre` (`Nombre`);

--
-- Indices de la tabla `encuesta08`
--
ALTER TABLE `encuesta08`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Matricula` (`Matricula`);

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Matricula` (`Matricula`),
  ADD KEY `Id_Proyecto` (`Id_Proyecto`),
  ADD KEY `Procedimiento` (`Procedimiento`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`Matricula`),
  ADD KEY `Carrera` (`Carrera`);

--
-- Indices de la tabla `foest02`
--
ALTER TABLE `foest02`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Empresa` (`Empresa`(768)),
  ADD KEY `Miembro` (`Miembro`);

--
-- Indices de la tabla `foest07`
--
ALTER TABLE `foest07`
  ADD PRIMARY KEY (`Id_FOEST07`);

--
-- Indices de la tabla `foest08`
--
ALTER TABLE `foest08`
  ADD PRIMARY KEY (`IdFoest08`),
  ADD KEY `Matricula` (`Matricula`);

--
-- Indices de la tabla `periodos`
--
ALTER TABLE `periodos`
  ADD PRIMARY KEY (`idPeriodo`);

--
-- Indices de la tabla `procedimientos`
--
ALTER TABLE `procedimientos`
  ADD PRIMARY KEY (`idProcedimiento`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`ProyectoID`),
  ADD UNIQUE KEY `Nombre` (`Nombre`) USING HASH;

--
-- Indices de la tabla `proyectoasesores`
--
ALTER TABLE `proyectoasesores`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Id_asesorA` (`Id_asesorA`),
  ADD KEY `Id_asesorE` (`Id_asesorE`),
  ADD KEY `Id_proyecto` (`Id_proyecto`);

--
-- Indices de la tabla `ser`
--
ALTER TABLE `ser`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Matricula` (`Matricula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asesoracademico`
--
ALTER TABLE `asesoracademico`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT de la tabla `asesorempresarial`
--
ALTER TABLE `asesorempresarial`
  MODIFY `AsesorID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT de la tabla `calificacionproyectop1`
--
ALTER TABLE `calificacionproyectop1`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `calificacionproyectop2`
--
ALTER TABLE `calificacionproyectop2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `calificacionproyectop3`
--
ALTER TABLE `calificacionproyectop3`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `cartas`
--
ALTER TABLE `cartas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `coordinacion`
--
ALTER TABLE `coordinacion`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `documentos`
--
ALTER TABLE `documentos`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `encuesta08`
--
ALTER TABLE `encuesta08`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=230;

--
-- AUTO_INCREMENT de la tabla `foest02`
--
ALTER TABLE `foest02`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `foest07`
--
ALTER TABLE `foest07`
  MODIFY `Id_FOEST07` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `foest08`
--
ALTER TABLE `foest08`
  MODIFY `IdFoest08` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `ProyectoID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `proyectoasesores`
--
ALTER TABLE `proyectoasesores`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `ser`
--
ALTER TABLE `ser`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asesorempresarial`
--
ALTER TABLE `asesorempresarial`
  ADD CONSTRAINT `asesorempresarial_ibfk_1` FOREIGN KEY (`Empresa`) REFERENCES `empresa` (`Nombre`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `cartas`
--
ALTER TABLE `cartas`
  ADD CONSTRAINT `cartas_ibfk_1` FOREIGN KEY (`Matricula`) REFERENCES `estudiante` (`Matricula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `documentos`
--
ALTER TABLE `documentos`
  ADD CONSTRAINT `documentos_ibfk_1` FOREIGN KEY (`Matricula`) REFERENCES `estudiante` (`Matricula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `encuesta08`
--
ALTER TABLE `encuesta08`
  ADD CONSTRAINT `encuesta08_ibfk_1` FOREIGN KEY (`Matricula`) REFERENCES `estudiante` (`Matricula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD CONSTRAINT `equipos_ibfk_2` FOREIGN KEY (`Matricula`) REFERENCES `estudiante` (`Matricula`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `equipos_ibfk_3` FOREIGN KEY (`Id_Proyecto`) REFERENCES `proyecto` (`ProyectoID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `equipos_ibfk_4` FOREIGN KEY (`Procedimiento`) REFERENCES `procedimientos` (`idProcedimiento`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `estudiante_ibfk_1` FOREIGN KEY (`Carrera`) REFERENCES `carreras` (`IdCarrera`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `foest02`
--
ALTER TABLE `foest02`
  ADD CONSTRAINT `foest02_ibfk_3` FOREIGN KEY (`Miembro`) REFERENCES `estudiante` (`Matricula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `foest08`
--
ALTER TABLE `foest08`
  ADD CONSTRAINT `foest08_ibfk_1` FOREIGN KEY (`Matricula`) REFERENCES `estudiante` (`Matricula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `proyectoasesores`
--
ALTER TABLE `proyectoasesores`
  ADD CONSTRAINT `proyectoasesores_ibfk_1` FOREIGN KEY (`Id_asesorA`) REFERENCES `asesoracademico` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `proyectoasesores_ibfk_2` FOREIGN KEY (`Id_asesorE`) REFERENCES `asesorempresarial` (`AsesorID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `proyectoasesores_ibfk_3` FOREIGN KEY (`Id_proyecto`) REFERENCES `proyecto` (`ProyectoID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ser`
--
ALTER TABLE `ser`
  ADD CONSTRAINT `ser_ibfk_1` FOREIGN KEY (`Matricula`) REFERENCES `estudiante` (`Matricula`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
