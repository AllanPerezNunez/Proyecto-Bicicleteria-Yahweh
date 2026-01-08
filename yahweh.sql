-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-06-2025 a las 01:40:34
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `yahweh`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add estado producto', 7, 'add_estadoproducto'),
(26, 'Can change estado producto', 7, 'change_estadoproducto'),
(27, 'Can delete estado producto', 7, 'delete_estadoproducto'),
(28, 'Can view estado producto', 7, 'view_estadoproducto'),
(29, 'Can add estado usuario', 8, 'add_estadousuario'),
(30, 'Can change estado usuario', 8, 'change_estadousuario'),
(31, 'Can delete estado usuario', 8, 'delete_estadousuario'),
(32, 'Can view estado usuario', 8, 'view_estadousuario'),
(33, 'Can add tipo producto', 9, 'add_tipoproducto'),
(34, 'Can change tipo producto', 9, 'change_tipoproducto'),
(35, 'Can delete tipo producto', 9, 'delete_tipoproducto'),
(36, 'Can view tipo producto', 9, 'view_tipoproducto'),
(37, 'Can add tipo tarjeta', 10, 'add_tipotarjeta'),
(38, 'Can change tipo tarjeta', 10, 'change_tipotarjeta'),
(39, 'Can delete tipo tarjeta', 10, 'delete_tipotarjeta'),
(40, 'Can view tipo tarjeta', 10, 'view_tipotarjeta'),
(41, 'Can add tipo usuario', 11, 'add_tipousuario'),
(42, 'Can change tipo usuario', 11, 'change_tipousuario'),
(43, 'Can delete tipo usuario', 11, 'delete_tipousuario'),
(44, 'Can view tipo usuario', 11, 'view_tipousuario'),
(45, 'Can add usuario', 12, 'add_usuario'),
(46, 'Can change usuario', 12, 'change_usuario'),
(47, 'Can delete usuario', 12, 'delete_usuario'),
(48, 'Can view usuario', 12, 'view_usuario'),
(49, 'Can add tarjeta', 13, 'add_tarjeta'),
(50, 'Can change tarjeta', 13, 'change_tarjeta'),
(51, 'Can delete tarjeta', 13, 'delete_tarjeta'),
(52, 'Can view tarjeta', 13, 'view_tarjeta'),
(53, 'Can add producto', 14, 'add_producto'),
(54, 'Can change producto', 14, 'change_producto'),
(55, 'Can delete producto', 14, 'delete_producto'),
(56, 'Can view producto', 14, 'view_producto'),
(57, 'Can add compra', 15, 'add_compra'),
(58, 'Can change compra', 15, 'change_compra'),
(59, 'Can delete compra', 15, 'delete_compra'),
(60, 'Can view compra', 15, 'view_compra'),
(61, 'Can add carrito', 16, 'add_carrito'),
(62, 'Can change carrito', 16, 'change_carrito'),
(63, 'Can delete carrito', 16, 'delete_carrito'),
(64, 'Can view carrito', 16, 'view_carrito'),
(65, 'Can add reparacion', 17, 'add_reparacion'),
(66, 'Can change reparacion', 17, 'change_reparacion'),
(67, 'Can delete reparacion', 17, 'delete_reparacion'),
(68, 'Can view reparacion', 17, 'view_reparacion'),
(69, 'Can add estado reparacion', 18, 'add_estadoreparacion'),
(70, 'Can change estado reparacion', 18, 'change_estadoreparacion'),
(71, 'Can delete estado reparacion', 18, 'delete_estadoreparacion'),
(72, 'Can view estado reparacion', 18, 'view_estadoreparacion'),
(73, 'Can add estado hora', 19, 'add_estadohora'),
(74, 'Can change estado hora', 19, 'change_estadohora'),
(75, 'Can delete estado hora', 19, 'delete_estadohora'),
(76, 'Can view estado hora', 19, 'view_estadohora'),
(77, 'Can add horas disponibles', 20, 'add_horasdisponibles'),
(78, 'Can change horas disponibles', 20, 'change_horasdisponibles'),
(79, 'Can delete horas disponibles', 20, 'delete_horasdisponibles'),
(80, 'Can view horas disponibles', 20, 'view_horasdisponibles'),
(81, 'Can add Estado de Envío', 21, 'add_estadoenvio'),
(82, 'Can change Estado de Envío', 21, 'change_estadoenvio'),
(83, 'Can delete Estado de Envío', 21, 'delete_estadoenvio'),
(84, 'Can view Estado de Envío', 21, 'view_estadoenvio'),
(85, 'Can add region', 22, 'add_region'),
(86, 'Can change region', 22, 'change_region'),
(87, 'Can delete region', 22, 'delete_region'),
(88, 'Can view region', 22, 'view_region'),
(89, 'Can add comuna', 23, 'add_comuna'),
(90, 'Can change comuna', 23, 'change_comuna'),
(91, 'Can delete comuna', 23, 'delete_comuna'),
(92, 'Can view comuna', 23, 'view_comuna'),
(93, 'Can add proveedor', 24, 'add_proveedor'),
(94, 'Can change proveedor', 24, 'change_proveedor'),
(95, 'Can delete proveedor', 24, 'delete_proveedor'),
(96, 'Can view proveedor', 24, 'view_proveedor'),
(97, 'Can add historial acciones', 25, 'add_historialacciones'),
(98, 'Can change historial acciones', 25, 'change_historialacciones'),
(99, 'Can delete historial acciones', 25, 'delete_historialacciones'),
(100, 'Can view historial acciones', 25, 'view_historialacciones');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_carrito`
--

CREATE TABLE `bicicletas_carrito` (
  `id` bigint(20) NOT NULL,
  `cantidadArt` int(11) NOT NULL,
  `articulo_id` bigint(20) NOT NULL,
  `comprador_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_carrito`
--

INSERT INTO `bicicletas_carrito` (`id`, `cantidadArt`, `articulo_id`, `comprador_id`) VALUES
(23, 4, 2, 7),
(24, 4, 3, 7),
(38, 5, 2, 10),
(39, 1, 3, 10),
(81, 7, 2, 3),
(139, 3, 5, 16),
(140, 4, 6, 16),
(141, 2, 3, 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_compra`
--

CREATE TABLE `bicicletas_compra` (
  `id` bigint(20) NOT NULL,
  `direccion` longtext NOT NULL,
  `fecha_compra` datetime(6) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  `tarjeta_id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `estado_compra` longtext NOT NULL,
  `fecha_entrega_estimada` datetime(6) DEFAULT NULL,
  `nro_factura` longtext DEFAULT NULL,
  `comuna_entrega_id` bigint(20) DEFAULT NULL,
  `estado_seguimiento_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_compra`
--

INSERT INTO `bicicletas_compra` (`id`, `direccion`, `fecha_compra`, `cantidad`, `producto_id`, `tarjeta_id`, `usuario_id`, `estado_compra`, `fecha_entrega_estimada`, `nro_factura`, `comuna_entrega_id`, `estado_seguimiento_id`) VALUES
(205, 'Calle Ecuador 120 ', '2025-06-23 23:36:34.483358', 3, 2, 25, 27, 'PENDIENTE', '2025-06-25 23:36:34.483358', 'B23062025-00001', 80, 1),
(206, 'Calle Ecuador 120 ', '2025-06-23 23:36:34.483358', 2, 20, 25, 27, 'PENDIENTE', '2025-06-25 23:36:34.483358', 'B23062025-00001', 80, 1),
(207, 'Calle Ecuador 120 ', '2025-06-23 23:37:08.956477', 4, 5, 25, 27, 'PENDIENTE', '2025-06-25 23:37:08.956477', 'B23062025-00002', 80, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_comuna`
--

CREATE TABLE `bicicletas_comuna` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `tiempo_estimado_horas` decimal(5,2) NOT NULL,
  `region_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_comuna`
--

INSERT INTO `bicicletas_comuna` (`id`, `nombre`, `tiempo_estimado_horas`, `region_id`) VALUES
(1, 'Arica', '120.00', 1),
(2, 'Camarones', '120.00', 1),
(3, 'Putre', '120.00', 1),
(4, 'General Lagos', '120.00', 1),
(5, 'Iquique', '120.00', 2),
(6, 'Alto Hospicio', '120.00', 2),
(7, 'Pozo Almonte', '120.00', 2),
(8, 'Huara', '120.00', 2),
(9, 'Pica', '120.00', 2),
(10, 'Colchane', '120.00', 2),
(11, 'Camiña', '120.00', 2),
(12, 'Antofagasta', '120.00', 3),
(13, 'Mejillones', '120.00', 3),
(14, 'Sierra Gorda', '120.00', 3),
(15, 'Taltal', '120.00', 3),
(16, 'Calama', '120.00', 3),
(17, 'Ollagüe', '120.00', 3),
(18, 'San Pedro de Atacama', '120.00', 3),
(19, 'Maria Elena', '120.00', 3),
(20, 'Tocopilla', '120.00', 3),
(21, 'Chañaral', '120.00', 4),
(22, 'Diego de Almagro', '120.00', 4),
(23, 'Caldera', '120.00', 4),
(24, 'Copiapo', '120.00', 4),
(25, 'Tierra Amarilla', '120.00', 4),
(26, 'Alto del Carmen', '120.00', 4),
(27, 'Freirina', '120.00', 4),
(28, 'Huasco', '120.00', 4),
(29, 'Vallenar', '120.00', 4),
(30, 'Andacollo', '72.00', 5),
(31, 'Coquimbo', '72.00', 5),
(32, 'La Higuera', '72.00', 5),
(33, 'La Serena', '72.00', 5),
(34, 'Paihuano', '72.00', 5),
(35, 'Vicuña', '72.00', 5),
(36, 'Combarbala', '72.00', 5),
(37, 'Monte Patria', '72.00', 5),
(38, 'Ovalle', '72.00', 5),
(39, 'Punitaqui', '72.00', 5),
(40, 'Rio Hurtado', '72.00', 5),
(41, 'Canela', '72.00', 5),
(42, 'Illapel', '72.00', 5),
(43, 'Los Vilos', '72.00', 5),
(44, 'Salamanca', '72.00', 5),
(47, 'Isla de Pascua', '240.00', 6),
(48, 'Calle Larga', '48.00', 6),
(49, 'Los Andes', '48.00', 6),
(50, 'Rinconada', '48.00', 6),
(51, 'San Esteban', '48.00', 6),
(52, 'Cabildo', '48.00', 6),
(53, 'La Ligua', '48.00', 6),
(54, 'Papudo', '48.00', 6),
(55, 'Petorca', '48.00', 6),
(56, 'Zapallar', '48.00', 6),
(57, 'Hijuelas', '48.00', 6),
(58, 'La Calera', '48.00', 6),
(59, 'La Cruz', '48.00', 6),
(60, 'Nogales', '48.00', 6),
(61, 'Quillota', '48.00', 6),
(62, 'Algarrobo', '48.00', 6),
(63, 'Cartagena', '48.00', 6),
(64, 'El Quisco', '48.00', 6),
(65, 'El Tabo', '48.00', 6),
(66, 'San Antonio', '48.00', 6),
(67, 'Santo Domingo', '48.00', 6),
(68, 'Catemu', '48.00', 6),
(69, 'Llay-Llay', '48.00', 6),
(70, 'Panquehue', '48.00', 6),
(71, 'Putaendo', '48.00', 6),
(72, 'San Felipe', '48.00', 6),
(73, 'Santa María', '48.00', 6),
(74, 'Casablanca', '48.00', 6),
(75, 'Concon', '48.00', 6),
(76, 'Juan Fernandez', '48.00', 6),
(77, 'Puchuncavi', '48.00', 6),
(78, 'Quintero', '48.00', 6),
(79, 'Valparaiso', '48.00', 6),
(80, 'Viña del Mar', '48.00', 6),
(81, 'Limache', '48.00', 6),
(82, 'Olmué', '48.00', 6),
(83, 'Quilpué', '48.00', 6),
(84, 'Villa Alemana', '48.00', 6),
(85, 'Colina', '48.00', 7),
(86, 'Lampa', '48.00', 7),
(87, 'Til Til', '48.00', 7),
(88, 'Pirque', '48.00', 7),
(89, 'Puente Alto', '48.00', 7),
(90, 'San Jose de Maipo', '48.00', 7),
(91, 'Buin', '48.00', 7),
(92, 'Calera de Tango', '48.00', 7),
(93, 'Paine', '48.00', 7),
(94, 'San Bernardo', '48.00', 7),
(95, 'Alhue', '48.00', 7),
(96, 'Curacavi', '48.00', 7),
(97, 'Maria Pinto', '48.00', 7),
(98, 'Melipilla', '48.00', 7),
(99, 'San Pedro', '48.00', 7),
(100, 'Cerrillos', '48.00', 7),
(101, 'Cerro Navia', '48.00', 7),
(102, 'Conchali', '48.00', 7),
(103, 'El Bosque', '48.00', 7),
(104, 'Estacion Central', '48.00', 7),
(105, 'Huechuraba', '48.00', 7),
(106, 'Independencia', '48.00', 7),
(107, 'La Cisterna', '48.00', 7),
(108, 'La Granja', '48.00', 7),
(109, 'La Florida', '48.00', 7),
(110, 'La Pintana', '48.00', 7),
(111, 'La Reina', '48.00', 7),
(112, 'Las Condes', '48.00', 7),
(113, 'Lo Barnechea', '48.00', 7),
(114, 'Lo Espejo', '48.00', 7),
(115, 'Lo Prado', '48.00', 7),
(116, 'Macul', '48.00', 7),
(117, 'Maipu', '48.00', 7),
(118, 'Ñuñoa', '48.00', 7),
(119, 'Pedro Aguirre Cerda', '48.00', 7),
(120, 'Peñalolen', '48.00', 7),
(121, 'Providencia', '48.00', 7),
(122, 'Pudahuel', '48.00', 7),
(123, 'Quilicura', '48.00', 7),
(124, 'Quinta Normal', '48.00', 7),
(125, 'Recoleta', '48.00', 7),
(126, 'Renca', '48.00', 7),
(127, 'San Miguel', '48.00', 7),
(128, 'San Joaquin', '48.00', 7),
(129, 'San Ramon', '48.00', 7),
(130, 'Santiago', '48.00', 7),
(131, 'Vitacura', '48.00', 7),
(132, 'El Monte', '48.00', 7),
(133, 'Isla de Maipo', '48.00', 7),
(134, 'Padre Hurtado', '48.00', 7),
(135, 'Peñaflor', '48.00', 7),
(136, 'Talagante', '48.00', 7),
(138, 'Codegua', '24.00', 8),
(139, 'Coinco', '24.00', 8),
(140, 'Coltauco', '24.00', 8),
(141, 'Doñihue', '24.00', 8),
(142, 'Graneros', '24.00', 8),
(143, 'Machali', '24.00', 8),
(144, 'Las Cabras', '24.00', 8),
(145, 'Malloa', '24.00', 8),
(146, 'Mostazal', '24.00', 8),
(147, 'Olivar', '24.00', 8),
(148, 'Peumo', '24.00', 8),
(149, 'Pichidegua', '24.00', 8),
(150, 'Quinta de Tilcoco', '24.00', 8),
(151, 'Rancagua', '24.00', 8),
(152, 'Rengo', '24.00', 8),
(153, 'Renquínoa', '24.00', 8),
(154, 'San Vicente de Tagua Tagua', '24.00', 8),
(155, 'La Estrella', '24.00', 8),
(156, 'Litueche', '24.00', 8),
(157, 'Marchigüe', '24.00', 8),
(158, 'Navidad', '24.00', 8),
(159, 'Paredones', '24.00', 8),
(160, 'Pichilemu', '24.00', 8),
(161, 'Chepica', '24.00', 8),
(162, 'Chimbarongo', '24.00', 8),
(163, 'Lolol', '24.00', 8),
(164, 'Nancagua', '24.00', 8),
(165, 'Palmilla', '24.00', 8),
(166, 'Peralillo', '24.00', 8),
(167, 'Placilla', '24.00', 8),
(168, 'Pumanque', '24.00', 8),
(169, 'San Fernando', '24.00', 8),
(170, 'Santa Cruz', '24.00', 8),
(171, 'Cauquenes', '24.00', 9),
(172, 'Chanco', '24.00', 9),
(173, 'Pelluhue', '24.00', 9),
(174, 'Curico', '24.00', 9),
(175, 'Hualañe', '24.00', 9),
(176, 'Lincanten', '24.00', 9),
(177, 'Molina', '24.00', 9),
(178, 'Rauco', '24.00', 9),
(179, 'Romeral', '24.00', 9),
(180, 'Sagrada Familia', '24.00', 9),
(181, 'Teno', '24.00', 9),
(182, 'Vichuquen', '24.00', 9),
(183, 'Colbun', '24.00', 9),
(184, 'Linares', '24.00', 9),
(185, 'Longavi', '24.00', 9),
(186, 'Parral', '24.00', 9),
(187, 'Retiro', '24.00', 9),
(188, 'San Javier', '24.00', 9),
(189, 'Villa Alegre', '24.00', 9),
(190, 'Yerbas Buenas', '24.00', 9),
(191, 'Constitucion', '24.00', 9),
(192, 'Curepto', '24.00', 9),
(193, 'Empedrado', '24.00', 9),
(194, 'Maule', '24.00', 9),
(195, 'Pelarco', '24.00', 9),
(196, 'Pencahue', '24.00', 9),
(197, 'Rio Claro', '24.00', 9),
(198, 'San Clemente', '24.00', 9),
(199, 'San Rafael', '24.00', 9),
(200, 'Talca', '24.00', 9),
(201, 'Cobquecura', '72.00', 10),
(202, 'Coelemu', '72.00', 10),
(203, 'Ninhue', '72.00', 10),
(204, 'Portezuelo', '72.00', 10),
(205, 'Ranquil', '72.00', 10),
(206, 'Trehuaco', '72.00', 10),
(207, 'Bulnes', '72.00', 10),
(208, 'Chillan Viejo', '72.00', 10),
(209, 'Chillan', '72.00', 10),
(210, 'El Carmen', '72.00', 10),
(211, 'Pemuco', '72.00', 10),
(212, 'Pinto', '72.00', 10),
(213, 'Quillon', '72.00', 10),
(214, 'San Ignacio', '72.00', 10),
(215, 'Yungay', '72.00', 10),
(216, 'Coihueco', '72.00', 10),
(217, 'Ñiquen', '72.00', 10),
(218, 'San Carlos', '72.00', 10),
(219, 'San Fabian', '72.00', 10),
(220, 'San Nicolas', '72.00', 10),
(221, 'Quirihue', '72.00', 10),
(222, 'Arauco', '72.00', 11),
(223, 'Cañete', '72.00', 11),
(224, 'Contulmo', '72.00', 11),
(225, 'Curanilahue', '72.00', 11),
(226, 'Lebu', '72.00', 11),
(227, 'Los Alamos', '72.00', 11),
(228, 'Tirua', '72.00', 11),
(229, 'Alto Biobio', '72.00', 11),
(230, 'Antuco', '72.00', 11),
(231, 'Cabrero', '72.00', 11),
(232, 'Laja', '72.00', 11),
(233, 'Los Angeles', '72.00', 11),
(234, 'Mulchen', '72.00', 11),
(235, 'Nacimiento', '72.00', 11),
(236, 'Negrete', '72.00', 11),
(237, 'Quilaco', '72.00', 11),
(238, 'Quilleco', '72.00', 11),
(239, 'San Rosendo', '72.00', 11),
(240, 'Santa Barbara', '72.00', 11),
(241, 'Tucapel', '72.00', 11),
(242, 'Yumbel', '72.00', 11),
(243, 'Chiguayante', '72.00', 11),
(244, 'Concepcion', '72.00', 11),
(245, 'Coronel', '72.00', 11),
(246, 'Florida', '72.00', 11),
(247, 'Hualpen', '72.00', 11),
(248, 'Hualqui', '72.00', 11),
(249, 'Lota', '72.00', 11),
(250, 'Penco', '72.00', 11),
(251, 'San Pedro de la Paz', '72.00', 11),
(252, 'Santa Juana', '72.00', 11),
(253, 'Talcahuano', '72.00', 11),
(254, 'Tome', '72.00', 11),
(255, 'Carahue', '72.00', 12),
(256, 'Cholchol', '72.00', 12),
(257, 'Cunco', '72.00', 12),
(258, 'Curarrehue', '72.00', 12),
(259, 'Freire', '72.00', 12),
(260, 'Galvarino', '72.00', 12),
(261, 'Gorbea', '72.00', 12),
(262, 'Lautaro', '72.00', 12),
(263, 'Loncoche', '72.00', 12),
(264, 'Melipeuco', '72.00', 12),
(265, 'Nueva Imperial', '72.00', 12),
(266, 'Padre Las Casas', '72.00', 12),
(267, 'Perquenco', '72.00', 12),
(268, 'Pitrufquen', '72.00', 12),
(269, 'Pucon', '72.00', 12),
(270, 'Saavedra', '72.00', 12),
(271, 'Temuco', '72.00', 12),
(272, 'Teodoro Schmidt', '72.00', 12),
(273, 'Tolten', '72.00', 12),
(274, 'Vilcun', '72.00', 12),
(275, 'Villarrica', '72.00', 12),
(276, 'Angol', '72.00', 12),
(277, 'Colipulli', '72.00', 12),
(278, 'Curacautin', '72.00', 12),
(279, 'Ercilla', '72.00', 12),
(280, 'Lonquimay', '72.00', 12),
(281, 'Los Sauces', '72.00', 12),
(282, 'Lumaco', '72.00', 12),
(283, 'Puren', '72.00', 12),
(284, 'Renaico', '72.00', 12),
(285, 'Traiguen', '72.00', 12),
(286, 'Victoria', '72.00', 12),
(287, 'Panguipulli', '72.00', 13),
(288, 'Futrono', '72.00', 13),
(289, 'Rio Bueno', '72.00', 13),
(290, 'Lago Ranco', '72.00', 13),
(291, 'La Union', '72.00', 13),
(292, 'Corral', '72.00', 13),
(293, 'Paillaco', '72.00', 13),
(294, 'Valdivia', '72.00', 13),
(295, 'Mafil', '72.00', 13),
(296, 'Lanco', '72.00', 13),
(297, 'Mariquina', '72.00', 13),
(298, 'Los Lagos', '72.00', 13),
(299, 'Guaitecas', '120.00', 14),
(300, 'Cisnes', '120.00', 14),
(301, 'Lago Verde', '120.00', 14),
(302, 'Coyahique', '120.00', 14),
(303, 'Aysen', '120.00', 14),
(304, 'Rio Ibañez', '120.00', 14),
(305, 'Chile Chico', '120.00', 14),
(306, 'Cochrane', '120.00', 14),
(307, 'O´Higgins', '120.00', 14),
(308, 'Tortel', '120.00', 14),
(309, 'Antartica', '120.00', 15),
(310, 'Cabo de Hornos', '120.00', 15),
(311, 'Laguna Blanca', '120.00', 15),
(312, 'Punta Arenas', '120.00', 15),
(313, 'Rio Verde', '120.00', 15),
(314, 'San Gregorio', '120.00', 15),
(315, 'Porvenir', '120.00', 15),
(316, 'Primavera', '120.00', 15),
(317, 'Timaukel', '120.00', 15),
(318, 'Natales', '120.00', 15),
(319, 'Torres del Paine', '120.00', 15);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_estadoenvio`
--

CREATE TABLE `bicicletas_estadoenvio` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `porcentaje_visual` int(11) NOT NULL,
  `orden` int(11) NOT NULL,
  `descripcion_cliente` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_estadoenvio`
--

INSERT INTO `bicicletas_estadoenvio` (`id`, `nombre`, `porcentaje_visual`, `orden`, `descripcion_cliente`) VALUES
(1, 'Pedido Recibido', 0, 1, '¡Gracias por tu compra! Hemos recibido tu pedido y estamos confirmando los detalles.'),
(2, 'Preparando Envio', 25, 2, 'Tu pedido está siendo cuidadosamente preparado y empaquetado por nuestro equipo.'),
(3, 'En Ruta', 50, 3, '¡Tu pedido ha salido de nuestras instalaciones y está en camino a tu domicilio!'),
(4, 'En Destino Local', 75, 4, 'Tu pedido ha llegado a la sucursal de reparto local y pronto estará contigo.'),
(5, 'Entregado', 100, 5, '¡Tu pedido ha sido entregado exitosamente!');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_estadohora`
--

CREATE TABLE `bicicletas_estadohora` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_estadohora`
--

INSERT INTO `bicicletas_estadohora` (`id`, `descripcion`) VALUES
(1, 'Disponible'),
(2, 'No disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_estadoproducto`
--

CREATE TABLE `bicicletas_estadoproducto` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_estadoproducto`
--

INSERT INTO `bicicletas_estadoproducto` (`id`, `descripcion`) VALUES
(1, 'Disponible'),
(2, 'Agotado'),
(3, 'Descontinuado'),
(4, 'Deshabilitado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_estadoreparacion`
--

CREATE TABLE `bicicletas_estadoreparacion` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_estadoreparacion`
--

INSERT INTO `bicicletas_estadoreparacion` (`id`, `descripcion`) VALUES
(1, 'Pendiente'),
(2, 'Completada'),
(3, 'Cancelada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_estadousuario`
--

CREATE TABLE `bicicletas_estadousuario` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_estadousuario`
--

INSERT INTO `bicicletas_estadousuario` (`id`, `descripcion`) VALUES
(1, 'Habilitado'),
(2, 'Deshabilitado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_historialacciones`
--

CREATE TABLE `bicicletas_historialacciones` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `tipoObjeto` varchar(50) NOT NULL,
  `objetoAfectado` varchar(200) NOT NULL,
  `accion` varchar(50) NOT NULL,
  `motivo` longtext NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_historialacciones`
--

INSERT INTO `bicicletas_historialacciones` (`id`, `fecha`, `tipoObjeto`, `objetoAfectado`, `accion`, `motivo`, `usuario_id`) VALUES
(20, '2025-06-23 22:27:13.081998', 'Producto', 'Dmr Brendog DeathGrip 2', 'Actualizacion', 'Porque no se venden bicicletas, solo repuestos', 1),
(21, '2025-06-23 22:30:03.839937', 'Producto', 'Cadena Bicicleta ', 'Actualizacion', 'Reemplazo de Productos', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_horasdisponibles`
--

CREATE TABLE `bicicletas_horasdisponibles` (
  `id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  `estado_hora_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_horasdisponibles`
--

INSERT INTO `bicicletas_horasdisponibles` (`id`, `fecha`, `hora`, `estado_hora_id`) VALUES
(13, '2025-06-05', '16:20:00.000000', 2),
(14, '2025-06-04', '16:20:00.000000', 2),
(15, '2025-06-06', '16:20:00.000000', 2),
(16, '2025-06-06', '16:00:00.000000', 2),
(17, '2025-06-17', '17:30:00.000000', 2),
(18, '2025-06-11', '10:30:00.000000', 2),
(19, '2025-06-11', '15:30:00.000000', 2),
(20, '2025-06-14', '16:13:00.000000', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_producto`
--

CREATE TABLE `bicicletas_producto` (
  `id` bigint(20) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `nombre` longtext NOT NULL,
  `descripcion` longtext NOT NULL,
  `material` longtext NOT NULL,
  `stock` int(11) NOT NULL,
  `estadoProducto_id` bigint(20) NOT NULL,
  `tipoProducto_id` bigint(20) NOT NULL,
  `numeroFactura` int(11) DEFAULT NULL,
  `proveedor_id` bigint(20) DEFAULT NULL,
  `precioCompra` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `utilidad` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_producto`
--

INSERT INTO `bicicletas_producto` (`id`, `imagen`, `nombre`, `descripcion`, `material`, `stock`, `estadoProducto_id`, `tipoProducto_id`, `numeroFactura`, `proveedor_id`, `precioCompra`, `precio`, `utilidad`) VALUES
(2, 'imagenes_bd/noborrar1_FR7tHZE_4vL6BEe.jpg', 'Dmr Brendog DeathGrip 2', 'Fortalece y Manten tu agarre en el manubrio gracias a los Dmr Brendog DeathGrip', 'Caucho', 696, 1, 7, 2, 4, 39870, 49838, 0.1),
(3, 'imagenes_bd/noborrar3.jpg', 'Luz LED Rueda de bicicleta', 'Luces para iluminar las ruedas de la bicicleta', 'Sintetico', 125, 1, 6, 3, 1, 66791, 83489, 0.25),
(4, 'imagenes_bd/noborrar4.jpg', 'Casco infantil Hello Kitty', 'Casco para niños con diseño de Hello Kitty, 46/53CM', 'Sintetico', 265, 1, 2, 4, 3, 17600, 22880, 0.3),
(5, 'imagenes_bd/noborrar5.jpg', 'Juego de accesorios de bicicleta de 7 piezas', 'Soporte de teléfono de silicona, Bocina, soporte de botella, 2 luces USB recargables, 2 espejos retrovisores convexos', 'Plastico', 69, 1, 3, 5, 4, 5000, 6250, 0.25),
(6, 'imagenes_bd/noborrar6.jpg', 'Rueda de bicicleta', 'Rueda trasera para bicicleta, plateada, aro 20\'', 'Caucho', 762, 1, 7, 6, 3, 46000, 52900, 0.15),
(20, 'imagenes_bd/noborrar2_n17fVFi_eF6CUE1.jpg', 'Cadena Bicicleta ', 'Cadena de Bicicleta 1/2\'\' x 3/32\'\' x 116L', 'Metal', 595, 1, 2, 2147483647, 1, 3000, 3600, 0.2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_proveedor`
--

CREATE TABLE `bicicletas_proveedor` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_proveedor`
--

INSERT INTO `bicicletas_proveedor` (`id`, `descripcion`) VALUES
(1, 'MKR'),
(2, 'Rafael Burgos'),
(3, 'Andes Industrial'),
(4, 'Teknobike');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_region`
--

CREATE TABLE `bicicletas_region` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_region`
--

INSERT INTO `bicicletas_region` (`id`, `nombre`) VALUES
(1, 'Arica y Parinacota'),
(2, 'Tarapaca'),
(3, 'Antofagasta'),
(4, 'Atacama'),
(5, 'Coquimbo'),
(6, 'Valparaiso'),
(7, 'Metropolitana de Santiago'),
(8, 'Libertador General Bernardo O\'Higgins'),
(9, 'Maule'),
(10, 'Ñuble'),
(11, 'Biobio'),
(12, 'La Araucania'),
(13, 'Los Rios'),
(14, 'Aysen'),
(15, 'Magallanes');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_reparacion`
--

CREATE TABLE `bicicletas_reparacion` (
  `id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `hora_agendada` time(6) NOT NULL,
  `observaciones` longtext NOT NULL,
  `estado_reparacion_id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_reparacion`
--

INSERT INTO `bicicletas_reparacion` (`id`, `fecha`, `hora_agendada`, `observaciones`, `estado_reparacion_id`, `usuario_id`) VALUES
(1, '2025-05-18', '15:25:00.000000', 'Buenas Tardes, tengo problemas con el freno de mi Bicicleta', 1, 2),
(2, '2025-05-19', '17:09:00.000000', 'Buenas Tardes, necesito que me ayude a instalar un nuevo manubrio para mi bicicleta', 3, 3),
(3, '2025-05-30', '17:01:00.000000', 'Buenas tardes, quiero añadir accesorios a mi bicicleta', 2, 8),
(4, '2025-06-05', '16:20:00.000000', 'Hola, necesito que arregle mi bicicleta, tengo una rueda ponchada', 2, 10),
(5, '2025-06-05', '16:20:00.000000', 'Hola, necesito que arregle mi bicicleta, tengo una rueda ponchada', 3, 10),
(21, '2025-06-11', '15:30:00.000000', 'El Freno de mi bicicleta no funciona', 1, 16),
(22, '2025-06-11', '10:30:00.000000', 'si que si', 1, 16),
(23, '2025-06-17', '17:30:00.000000', 'hola\r\n', 1, 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_tarjeta`
--

CREATE TABLE `bicicletas_tarjeta` (
  `id` bigint(20) NOT NULL,
  `nroTarjeta` bigint(20) NOT NULL,
  `fechaCad` date NOT NULL,
  `cvv` int(11) NOT NULL,
  `saldo` bigint(20) NOT NULL,
  `tipoTarjeta_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_tarjeta`
--

INSERT INTO `bicicletas_tarjeta` (`id`, `nroTarjeta`, `fechaCad`, `cvv`, `saldo`, `tipoTarjeta_id`) VALUES
(1, 1234567890123456, '2030-02-02', 123, 9999939759178, 2),
(4, 5554567890123343, '2030-05-29', 321, 9999993233158, 1),
(5, 1656728594863895, '2030-02-02', 921, 10000000, 1),
(6, 4606785867850579, '2030-02-02', 649, 9999993880000, 1),
(7, 2820406736751074, '2030-02-02', 720, 99999364000, 1),
(8, 6575986136951841, '2030-02-02', 687, 100000000000, 2),
(9, 1537622878777401, '2030-02-02', 334, 100000000000, 1),
(10, 1205782718598208, '2030-02-02', 898, 100000000000, 1),
(11, 5088199959490756, '2030-02-02', 739, 100000000000, 1),
(12, 5108643116304759, '2030-02-02', 787, 100000000000, 2),
(13, 5606939090244696, '2030-02-02', 505, 100000000000, 2),
(14, 5885246529945285, '2030-02-02', 267, 99994528513, 1),
(15, 5993938988465428, '2030-02-02', 232, 100000000000, 1),
(16, 9180848157976081, '2030-02-02', 819, 100000000000, 1),
(17, 8700760152989127, '2030-02-02', 407, 100000000000, 1),
(18, 8460587393288698, '2030-02-02', 897, 100000000000, 2),
(19, 9455655279744022, '2030-02-02', 836, 100000000000, 1),
(20, 5958993672222243, '2030-02-02', 822, 100000000000, 1),
(21, 8474129346405528, '2030-02-02', 771, 100000000000, 2),
(22, 3892221021539059, '2030-02-02', 322, 100000000000, 2),
(23, 7165305824985102, '2030-02-02', 627, 100000000000, 1),
(24, 4678447463936146, '2030-02-02', 735, 100000000000, 1),
(25, 7574570825038217, '2030-02-02', 135, 99999818286, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_tipoproducto`
--

CREATE TABLE `bicicletas_tipoproducto` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_tipoproducto`
--

INSERT INTO `bicicletas_tipoproducto` (`id`, `descripcion`) VALUES
(1, 'Bicicleta'),
(2, 'Casco'),
(3, 'Accesorio'),
(4, 'Bombín'),
(5, 'Candado'),
(6, 'Luz'),
(7, 'Repuesto'),
(8, 'Bocina'),
(9, 'Parches');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_tipotarjeta`
--

CREATE TABLE `bicicletas_tipotarjeta` (
  `id` bigint(20) NOT NULL,
  `tipo` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_tipotarjeta`
--

INSERT INTO `bicicletas_tipotarjeta` (`id`, `tipo`) VALUES
(1, 'Credito'),
(2, 'Debito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_tipousuario`
--

CREATE TABLE `bicicletas_tipousuario` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_tipousuario`
--

INSERT INTO `bicicletas_tipousuario` (`id`, `descripcion`) VALUES
(1, 'ADMINISTRADOR'),
(2, 'CLIENTE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bicicletas_usuario`
--

CREATE TABLE `bicicletas_usuario` (
  `id` bigint(20) NOT NULL,
  `rut` longtext NOT NULL,
  `nombre` longtext NOT NULL,
  `apellido` longtext NOT NULL,
  `correo` longtext NOT NULL,
  `contrasena` longtext NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `estadoUsuario_id` bigint(20) NOT NULL,
  `tipoUsuario_id` bigint(20) NOT NULL,
  `tarjeta_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bicicletas_usuario`
--

INSERT INTO `bicicletas_usuario` (`id`, `rut`, `nombre`, `apellido`, `correo`, `contrasena`, `telefono`, `estadoUsuario_id`, `tipoUsuario_id`, `tarjeta_id`) VALUES
(1, '16.256.976-7', 'Magdalena', 'Núñez', 'magdalena.nunez16256@gmail.com', 'pbkdf2_sha256$600000$0GXzFkR9QbvJuSvO5d2Ew1$3D+eMCG2bvfPFlZMtkb23dpEqnjk0vmDciasUV8NEXk=', 56911111111, 1, 1, 1),
(2, '21.420.962-4', 'Allan', 'Pérez', 'allan.perez@gmail.cl', 'pbkdf2_sha256$600000$Ykg3JEvjiCd03yXvWnKgT6$Cd/DKMIzV2xHfm3bZIz+ziX7nTt4SCeSuPJLAWC+1bg=', 56922222223, 2, 2, 1),
(3, '19.389.268-5', 'Maximiliano', 'Rojas', 'maximiliano.rojas@gmail.cl', 'pbkdf2_sha256$600000$qHEFO0Mkn5deNZTh8qjjt4$fOHA87h0t2e0SU4/qFs/zw2jXa281M3xecfH4jLXoIw=', 56923328791, 2, 1, 4),
(4, '16.532.889-2', 'Job', 'Vergara', 'job.vergara@gmail.cl', 'pbkdf2_sha256$600000$i7d0N2wNqOqRoLKZY20I64$ehY78n+T9N2mkgmUcYpnYQw8xH+j+T+euqNF14uO/vw=', 56922322322, 2, 1, 1),
(10, '21.876.546-6', 'Daniel', 'Saavedra', 'daniel.saavedra@gmail.cl', 'pbkdf2_sha256$600000$l96BgGilyCOMKVL22p9h4o$GgR91iS7/Sy0TsYdjcnwYDxPb7N/edXLxSvD4a9o1nY=', 56912354366, 2, 2, 9),
(27, '18.769.332-5', 'Javier', 'Avello', 'javier.avello@gmail.com', 'pbkdf2_sha256$600000$ITWbhIPQQClsFOcsLqsoa1$rLyab0yX9aN3jOpznBK8jg+Day39zjWLNihpHattgbQ=', 56908731532, 2, 2, 25);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(16, 'bicicletas', 'carrito'),
(15, 'bicicletas', 'compra'),
(23, 'bicicletas', 'comuna'),
(21, 'bicicletas', 'estadoenvio'),
(19, 'bicicletas', 'estadohora'),
(7, 'bicicletas', 'estadoproducto'),
(18, 'bicicletas', 'estadoreparacion'),
(8, 'bicicletas', 'estadousuario'),
(25, 'bicicletas', 'historialacciones'),
(20, 'bicicletas', 'horasdisponibles'),
(14, 'bicicletas', 'producto'),
(24, 'bicicletas', 'proveedor'),
(22, 'bicicletas', 'region'),
(17, 'bicicletas', 'reparacion'),
(13, 'bicicletas', 'tarjeta'),
(9, 'bicicletas', 'tipoproducto'),
(10, 'bicicletas', 'tipotarjeta'),
(11, 'bicicletas', 'tipousuario'),
(12, 'bicicletas', 'usuario'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-03-15 03:19:55.959355'),
(2, 'auth', '0001_initial', '2025-03-15 03:19:57.370166'),
(3, 'admin', '0001_initial', '2025-03-15 03:19:57.668454'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-03-15 03:19:57.683413'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-03-15 03:19:57.699673'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-03-15 03:19:57.818492'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-03-15 03:19:57.939486'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-03-15 03:19:57.963346'),
(9, 'auth', '0004_alter_user_username_opts', '2025-03-15 03:19:57.975404'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-03-15 03:19:58.073576'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-03-15 03:19:58.079779'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-03-15 03:19:58.089731'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-03-15 03:19:58.112497'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-03-15 03:19:58.128958'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-03-15 03:19:58.160490'),
(16, 'auth', '0011_update_proxy_permissions', '2025-03-15 03:19:58.173122'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-03-15 03:19:58.224554'),
(18, 'bicicletas', '0001_initial', '2025-03-15 03:19:59.868095'),
(19, 'sessions', '0001_initial', '2025-03-15 03:19:59.938079'),
(20, 'bicicletas', '0002_compra_estado_compra', '2025-05-17 04:50:37.208984'),
(21, 'bicicletas', '0003_estadoreparacion_reparacion', '2025-05-17 21:28:17.848658'),
(22, 'bicicletas', '0004_rename_estado_reparacion_id_reparacion_estado_reparacion_and_more', '2025-05-17 21:39:19.223354'),
(23, 'bicicletas', '0005_usuario_tarjeta', '2025-05-18 01:07:17.182915'),
(24, 'bicicletas', '0006_estadohora_horasdisponibles', '2025-06-08 17:59:29.577897'),
(25, 'bicicletas', '0007_alter_horasdisponibles_fecha_alter_reparacion_fecha', '2025-06-08 17:59:29.892462'),
(26, 'bicicletas', '0008_remove_horasdisponibles_usuario', '2025-06-08 17:59:30.994581'),
(27, 'bicicletas', '0009_remove_horasdisponibles_observaciones', '2025-06-08 17:59:31.019650'),
(28, 'bicicletas', '0010_rename_hora_agendada_horasdisponibles_hora', '2025-06-08 17:59:31.050717'),
(29, 'bicicletas', '0011_estadoenvio_region_compra_fecha_entrega_estimada_and_more', '2025-06-09 05:20:48.791734'),
(30, 'bicicletas', '0012_alter_compra_nro_factura', '2025-06-10 11:49:41.581318'),
(31, 'bicicletas', '0013_proveedor', '2025-06-17 02:33:15.478720'),
(32, 'bicicletas', '0014_producto_numerofactura_producto_proveedor_and_more', '2025-06-17 02:42:59.157091'),
(33, 'bicicletas', '0015_remove_producto_precio_producto_preciocompra_and_more', '2025-06-17 19:32:04.519386'),
(34, 'bicicletas', '0016_alter_producto_numerofactura_and_more', '2025-06-17 19:32:10.340445'),
(35, 'bicicletas', '0017_rename_preciocompra_producto_preciocosto', '2025-06-17 19:38:09.526430'),
(36, 'bicicletas', '0018_rename_preciocosto_producto_preciocompra', '2025-06-17 19:40:59.327063'),
(37, 'bicicletas', '0019_alter_producto_utilidad', '2025-06-17 20:29:40.229795'),
(38, 'bicicletas', '0020_rename_precioventa_producto_precio', '2025-06-17 21:04:26.417096'),
(39, 'bicicletas', '0021_historialacciones', '2025-06-20 18:58:02.641259');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7b1pb8xt4saye2q7g2gtltmr0gbe0nr4', '.eJxVzrEOgkAMBuB36YwXbJAEJn0DFyc1pkI1l9Q7Uu4WCe9uURY7fu2f_hPkMZP6CO15At9DiwVoTtACbl2FpWtq3FRQQIivu7L5QYSCAQ0s4ntLwvGSy5Ib5bd5F1V5UVoO3cDG--eLvLhOvvuQlEYOtDxBNEos_IjBQru6wXWM_RBPv3q3tRqPifp_nK_zB5IyPnA:1tulX9:O7oktbr5OFFSpbeXHHVZfU3XaAekztyGcLtGT1o9tuA', '2025-04-02 05:00:03.171056'),
('jo1txuskmb5q7iofc6ec07pacg6wevoa', '.eJxdzs8KwjAMBvB3yXkWtrq59uQLeFE8iUjcokTadfQPCGPvbqeI4DG_fAnfBCkk9OxAnybgHrQswKcIGkolZKtE1bSrGgoYnL16yr7DJ1s2jIPLjCMZw32-h717YMjUOe9pAftLCr8st3eLbERnciqSoZvLP3TdqErKqt2oMjOP7vipdFnqZKIQsf_HiP5BEd_jej5_UwcK7AbQ0SeaX4_LSN0:1uSh9A:Im2jb9zy8dluGnHc1-fCPCB0HZH5BC42-NZiNn2XoGk', '2025-07-04 19:11:32.443630'),
('kubfc2joip4k1154sq5dezz9vs4ljr2g', '.eJxdjs0OgjAQhN9lz9hQE0royRfQi_Gkxqx0ITX9IaW9QHh3q-DFPWyy38xsZoY0Jgzag7zOoBVIXkBIESRwwfaVYE0tdjUU4Lx9Bsr8iL1CQw4zxIGM0Sqn4XRLZdnhd3Oastj6EOgj2V-CueRo4iL_PfQWtWGtt9kZyVDnXfZWouHbZKwHf1nrPbZqNEZU_zBieFHE9VzuP9eZRu0dyBgSLW8kFUsy:1uTqj1:9DdU-lVsEpL8lBmCHwPh9_EXDR0a7aP1ngiBSKAPutc', '2025-07-07 23:37:19.648968'),
('u7w24vinqomkvchj18r0g46u5gk3d873', '.eJxdzs8KwjAMBvB3yXkWtrq59uQLeFE8iUjcokTadfQPCGPvbqeI4DG_fAnfBCkk9OxAnybgHrQswKcIGkolZKtE1bSrGgoYnL16yr7DJ1s2jIPLjCMZw32-h717YMjUOe9pAftLCr8st3eLbERnciqSoZvLP3TdqErKqt2oMjOP7vipdFnqZKIQsf_HiP5BEd_jej5_UwcK7AbQ0SeaX4_LSN0:1uSjMF:ociowpnh4eh0I2rsNEVbNCipNYbm4LxQ8EJU-QGQwCA', '2025-07-04 21:33:11.350830');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `bicicletas_carrito`
--
ALTER TABLE `bicicletas_carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_carrito_articulo_id_7f9f2869_fk_bicicleta` (`articulo_id`),
  ADD KEY `bicicletas_carrito_comprador_id_f7530e93_fk_bicicleta` (`comprador_id`);

--
-- Indices de la tabla `bicicletas_compra`
--
ALTER TABLE `bicicletas_compra`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_compra_producto_id_bf9908b6_fk_bicicletas_producto_id` (`producto_id`),
  ADD KEY `bicicletas_compra_tarjeta_id_6c8e7949_fk_bicicletas_tarjeta_id` (`tarjeta_id`),
  ADD KEY `bicicletas_compra_usuario_id_c77c2f81_fk_bicicletas_usuario_id` (`usuario_id`),
  ADD KEY `bicicletas_compra_comuna_entrega_id_0e27afdd_fk_bicicleta` (`comuna_entrega_id`),
  ADD KEY `bicicletas_compra_estado_seguimiento_i_6085e4b7_fk_bicicleta` (`estado_seguimiento_id`);

--
-- Indices de la tabla `bicicletas_comuna`
--
ALTER TABLE `bicicletas_comuna`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_comuna_region_id_287f03ce_fk_bicicletas_region_id` (`region_id`);

--
-- Indices de la tabla `bicicletas_estadoenvio`
--
ALTER TABLE `bicicletas_estadoenvio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD UNIQUE KEY `orden` (`orden`);

--
-- Indices de la tabla `bicicletas_estadohora`
--
ALTER TABLE `bicicletas_estadohora`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_estadoproducto`
--
ALTER TABLE `bicicletas_estadoproducto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_estadoreparacion`
--
ALTER TABLE `bicicletas_estadoreparacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_estadousuario`
--
ALTER TABLE `bicicletas_estadousuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_historialacciones`
--
ALTER TABLE `bicicletas_historialacciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_historial_usuario_id_742816d1_fk_bicicleta` (`usuario_id`);

--
-- Indices de la tabla `bicicletas_horasdisponibles`
--
ALTER TABLE `bicicletas_horasdisponibles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_horasdisp_estado_hora_id_1dd71001_fk_bicicleta` (`estado_hora_id`);

--
-- Indices de la tabla `bicicletas_producto`
--
ALTER TABLE `bicicletas_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_producto_estadoProducto_id_d9d62b8a_fk_bicicleta` (`estadoProducto_id`),
  ADD KEY `bicicletas_producto_tipoProducto_id_71d2ecdc_fk_bicicleta` (`tipoProducto_id`),
  ADD KEY `bicicletas_producto_proveedor_id_91097f71_fk_bicicleta` (`proveedor_id`);

--
-- Indices de la tabla `bicicletas_proveedor`
--
ALTER TABLE `bicicletas_proveedor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_region`
--
ALTER TABLE `bicicletas_region`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_reparacion`
--
ALTER TABLE `bicicletas_reparacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_reparacio_estado_reparacion_id_2901bd91_fk_bicicleta` (`estado_reparacion_id`),
  ADD KEY `bicicletas_reparacio_usuario_id_696f9cae_fk_bicicleta` (`usuario_id`);

--
-- Indices de la tabla `bicicletas_tarjeta`
--
ALTER TABLE `bicicletas_tarjeta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_tarjeta_tipoTarjeta_id_e77bf8b1_fk_bicicleta` (`tipoTarjeta_id`);

--
-- Indices de la tabla `bicicletas_tipoproducto`
--
ALTER TABLE `bicicletas_tipoproducto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_tipotarjeta`
--
ALTER TABLE `bicicletas_tipotarjeta`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_tipousuario`
--
ALTER TABLE `bicicletas_tipousuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bicicletas_usuario`
--
ALTER TABLE `bicicletas_usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bicicletas_usuario_estadoUsuario_id_f16203ba_fk_bicicleta` (`estadoUsuario_id`),
  ADD KEY `bicicletas_usuario_tipoUsuario_id_46c67618_fk_bicicleta` (`tipoUsuario_id`),
  ADD KEY `bicicletas_usuario_tarjeta_id_0d67fbb0_fk_bicicletas_tarjeta_id` (`tarjeta_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `bicicletas_carrito`
--
ALTER TABLE `bicicletas_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=145;

--
-- AUTO_INCREMENT de la tabla `bicicletas_compra`
--
ALTER TABLE `bicicletas_compra`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=208;

--
-- AUTO_INCREMENT de la tabla `bicicletas_comuna`
--
ALTER TABLE `bicicletas_comuna`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=320;

--
-- AUTO_INCREMENT de la tabla `bicicletas_estadoenvio`
--
ALTER TABLE `bicicletas_estadoenvio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `bicicletas_estadohora`
--
ALTER TABLE `bicicletas_estadohora`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `bicicletas_estadoproducto`
--
ALTER TABLE `bicicletas_estadoproducto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `bicicletas_estadoreparacion`
--
ALTER TABLE `bicicletas_estadoreparacion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `bicicletas_estadousuario`
--
ALTER TABLE `bicicletas_estadousuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `bicicletas_historialacciones`
--
ALTER TABLE `bicicletas_historialacciones`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `bicicletas_horasdisponibles`
--
ALTER TABLE `bicicletas_horasdisponibles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `bicicletas_producto`
--
ALTER TABLE `bicicletas_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `bicicletas_proveedor`
--
ALTER TABLE `bicicletas_proveedor`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `bicicletas_region`
--
ALTER TABLE `bicicletas_region`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `bicicletas_reparacion`
--
ALTER TABLE `bicicletas_reparacion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `bicicletas_tarjeta`
--
ALTER TABLE `bicicletas_tarjeta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `bicicletas_tipoproducto`
--
ALTER TABLE `bicicletas_tipoproducto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `bicicletas_tipotarjeta`
--
ALTER TABLE `bicicletas_tipotarjeta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `bicicletas_tipousuario`
--
ALTER TABLE `bicicletas_tipousuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `bicicletas_usuario`
--
ALTER TABLE `bicicletas_usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `bicicletas_historialacciones`
--
ALTER TABLE `bicicletas_historialacciones`
  ADD CONSTRAINT `bicicletas_historial_usuario_id_742816d1_fk_bicicleta` FOREIGN KEY (`usuario_id`) REFERENCES `bicicletas_usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
