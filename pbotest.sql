-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2024 at 09:41 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbotest`
--

-- --------------------------------------------------------

--
-- Table structure for table `adik_asuh`
--

CREATE TABLE `adik_asuh` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `tempat_tinggal` varchar(255) NOT NULL,
  `umur` int(11) NOT NULL,
  `kebutuhan` text NOT NULL,
  `status` enum('Sudah di Asuh','Belum di Asuh','Kebutuhan Terpenuhi') NOT NULL,
  `target_donasi` decimal(10,2) DEFAULT 0.00,
  `donasi_terkumpul` decimal(10,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `akun`
--

CREATE TABLE `akun` (
  `id_akun` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `notelp` varchar(45) NOT NULL,
  `role` enum('Admin','Donatur','','') NOT NULL,
  `email` varchar(255) NOT NULL,
  `dompet` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `akun`
--

INSERT INTO `akun` (`id_akun`, `nama`, `username`, `password`, `notelp`, `role`, `email`, `dompet`) VALUES
(1, 'Muhammad Alif', 'alip', '1', '081345028895', 'Donatur', 'm.alif7890@gmail.com', 66200.00),
(2, 'Muhammad Khairrudin', 'admin', '123', '081388888888', 'Admin', 'khoirudin044@gmail.com', 10500.00),
(7, 'Siti Putri Lenggo Geni', 'siti', '123', '081345028895', 'Donatur', 'lenggo.geni0305@gmail.com', 0.00),
(8, 'Felisitas Merry', 'merry', '123', '3849732947982', 'Donatur', 'merry@gmail.com', 0.00),
(11, 'Kevin Rafif', 'kevin', '123', '0813432952893', 'Donatur', 'kevinrafif33@gmail.com', 4600.00),
(12, 'Muhammad Nizam', 'nizam', '123', '081338247287', 'Donatur', 'ijamnizam224@gmail.com', 5500.00),
(13, 'Judiono', 'papa', '123', '101203', 'Donatur', 'wadawd', 0.00),
(14, 'Yanto', 'lala', '123', '021300', 'Donatur', 'weaod', 0.00),
(15, 'Moik', 'aaa', '123', '23912', 'Donatur', 'alip@gmail.com', 0.00),
(16, 'Putri Nadilla Maharani', 'putri', 'hahahahaha', '0813101010110', 'Donatur', 'putrinadilla80@gmail.com', 0.00),
(17, 'Apalah', 'rangga', 'rangga123', '081345028261', 'Donatur', 'rangga@gmail.com', 0.00),
(18, 'Yusuf', 'ucup', '123', '081345020000', 'Donatur', 'ucup@gmail.com', 0.00),
(19, 'Junaidi', 'hakim', '123', '0123123', 'Donatur', 'hakim@gmail.com', 0.00),
(20, 'Gerry Conglomerate', 'GerryTampan', '123', '0812589800', 'Donatur', 'gerryhasrom25@gmail.com', 0.00),
(21, 'Muhammad Faqih Ajiputra', 'faqih', '123', '08134939393', 'Donatur', 'mfaqihajiputra66@gmail.com', 0.00),
(22, 'aassa', 'saas', '11', '1222', 'Donatur', 'ksaisaihi@gmail.com', 0.00),
(23, 'Joko Tole', 'alif', '123', '08329292922', 'Donatur', 'jokotole@gmail.com', 0.00),
(24, 'Yanto Kabir', 'mukil', '123', '23987289', 'Donatur', 'tano@gmail.com', 0.00),
(25, 'a', 'a', 'a', 'a', 'Donatur', 'kevinrafif33@gmail.com', 71000.00),
(26, 'Juned Kabir', 'juned', 'test', '32948329493', 'Donatur', 'juned@gmail.com', 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `donasi`
--

CREATE TABLE `donasi` (
  `id_donasi` bigint(20) UNSIGNED NOT NULL,
  `id_akun` int(11) DEFAULT NULL,
  `id_program` int(11) DEFAULT NULL,
  `jumlah_donasi` decimal(10,2) DEFAULT NULL,
  `tanggal_donasi` timestamp NOT NULL DEFAULT current_timestamp(),
  `pesan` varchar(255) DEFAULT NULL,
  `nama_donatur` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `donasi`
--

INSERT INTO `donasi` (`id_donasi`, `id_akun`, `id_program`, `jumlah_donasi`, `tanggal_donasi`, `pesan`, `nama_donatur`) VALUES
(2, 1, 8, 500.00, '2024-05-31 18:37:41', 'Semoga ga disabilitas lagi', 'Muhammad Alif'),
(3, 11, 8, 2000.00, '2024-05-31 19:36:36', 'Semangat !', 'Kevin Rafif'),
(14, 1, 16, 1000.00, '2024-06-04 19:09:35', 'Donasi otomatis', 'Muhammad Alif'),
(15, 1, 16, 1000.00, '2024-06-04 19:09:45', 'Donasi otomatis', 'Muhammad Alif'),
(16, 1, 16, 1000.00, '2024-06-04 19:09:55', 'Donasi otomatis', 'Muhammad Alif'),
(17, 1, 16, 1000.00, '2024-06-04 19:10:01', 'Donasi otomatis', 'Muhammad Alif'),
(18, 1, 16, 1000.00, '2024-06-04 19:10:05', 'Donasi otomatis', 'Muhammad Alif'),
(19, 1, 16, 1000.00, '2024-06-04 19:10:11', 'Donasi otomatis', 'Muhammad Alif'),
(20, 1, 16, 1000.00, '2024-06-04 19:10:15', 'Donasi otomatis', 'Muhammad Alif'),
(21, 1, 16, 1000.00, '2024-06-04 19:10:21', 'Donasi otomatis', 'Muhammad Alif'),
(22, 1, 16, 1000.00, '2024-06-04 19:10:25', 'Donasi otomatis', 'Muhammad Alif'),
(23, 1, 16, 1000.00, '2024-06-04 19:10:31', 'Donasi otomatis', 'Muhammad Alif'),
(24, 1, 16, 1000.00, '2024-06-04 19:10:35', 'Donasi otomatis', 'Muhammad Alif'),
(25, 1, 16, 1000.00, '2024-06-04 19:10:41', 'Donasi otomatis', 'Muhammad Alif'),
(26, 1, 16, 1000.00, '2024-06-04 19:10:45', 'Donasi otomatis', 'Muhammad Alif'),
(27, 1, 16, 1000.00, '2024-06-04 19:10:51', 'Donasi otomatis', 'Muhammad Alif'),
(28, 1, 16, 1000.00, '2024-06-04 19:10:55', 'Donasi otomatis', 'Muhammad Alif'),
(29, 1, 16, 1000.00, '2024-06-04 19:11:01', 'Donasi otomatis', 'Muhammad Alif'),
(30, 1, 16, 1000.00, '2024-06-04 19:11:05', 'Donasi otomatis', 'Muhammad Alif'),
(31, 1, 16, 1000.00, '2024-06-04 19:11:11', 'Donasi otomatis', 'Muhammad Alif'),
(32, 1, 16, 1000.00, '2024-06-04 19:11:15', 'Donasi otomatis', 'Muhammad Alif'),
(33, 1, 16, 1000.00, '2024-06-04 19:11:21', 'Donasi otomatis', 'Muhammad Alif'),
(34, 1, 16, 1000.00, '2024-06-04 19:11:25', 'Donasi otomatis', 'Muhammad Alif'),
(35, 1, 16, 1000.00, '2024-06-04 19:11:31', 'Donasi otomatis', 'Muhammad Alif'),
(36, 1, 16, 1000.00, '2024-06-04 19:11:35', 'Donasi otomatis', 'Muhammad Alif'),
(37, 1, 16, 1000.00, '2024-06-04 19:11:41', 'Donasi otomatis', 'Muhammad Alif'),
(38, 1, 16, 1000.00, '2024-06-04 19:11:45', 'Donasi otomatis', 'Muhammad Alif'),
(39, 1, 16, 1000.00, '2024-06-04 19:11:51', 'Donasi otomatis', 'Muhammad Alif'),
(40, 1, 16, 1000.00, '2024-06-04 19:11:55', 'Donasi otomatis', 'Muhammad Alif'),
(41, 1, 16, 1000.00, '2024-06-04 19:12:01', 'Donasi otomatis', 'Muhammad Alif'),
(42, 1, 16, 1000.00, '2024-06-04 19:12:05', 'Donasi otomatis', 'Muhammad Alif'),
(43, 1, 16, 1000.00, '2024-06-04 19:12:11', 'Donasi otomatis', 'Muhammad Alif'),
(44, 1, 16, 1000.00, '2024-06-04 19:12:15', 'Donasi otomatis', 'Muhammad Alif'),
(45, 1, 16, 1000.00, '2024-06-04 19:12:21', 'Donasi otomatis', 'Muhammad Alif'),
(46, 1, 16, 1000.00, '2024-06-04 19:12:25', 'Donasi otomatis', 'Muhammad Alif'),
(47, 1, 16, 1000.00, '2024-06-04 19:12:31', 'Donasi otomatis', 'Muhammad Alif'),
(48, 1, 16, 1000.00, '2024-06-04 19:12:35', 'Donasi otomatis', 'Muhammad Alif'),
(49, 1, 16, 1000.00, '2024-06-04 19:12:41', 'Donasi otomatis', 'Muhammad Alif'),
(50, 1, 16, 1000.00, '2024-06-04 19:12:45', 'Donasi otomatis', 'Muhammad Alif'),
(51, 1, 16, 1000.00, '2024-06-04 19:12:51', 'Donasi otomatis', 'Muhammad Alif'),
(52, 1, 16, 1000.00, '2024-06-04 19:12:55', 'Donasi otomatis', 'Muhammad Alif'),
(53, 1, 16, 1000.00, '2024-06-04 19:13:01', 'Donasi otomatis', 'Muhammad Alif'),
(54, 1, 16, 1000.00, '2024-06-04 19:13:05', 'Donasi otomatis', 'Muhammad Alif'),
(55, 1, 16, 1000.00, '2024-06-04 19:13:11', 'Donasi otomatis', 'Muhammad Alif'),
(56, 1, 16, 1000.00, '2024-06-04 19:13:15', 'Donasi otomatis', 'Muhammad Alif'),
(57, 1, 16, 1000.00, '2024-06-04 19:13:21', 'Donasi otomatis', 'Muhammad Alif'),
(58, 1, 16, 1000.00, '2024-06-04 19:13:25', 'Donasi otomatis', 'Muhammad Alif'),
(59, 1, 16, 1000.00, '2024-06-04 19:13:31', 'Donasi otomatis', 'Muhammad Alif'),
(60, 1, 16, 1000.00, '2024-06-04 19:13:35', 'Donasi otomatis', 'Muhammad Alif'),
(61, 1, 16, 1000.00, '2024-06-04 19:13:41', 'Donasi otomatis', 'Muhammad Alif'),
(62, 1, 16, 1000.00, '2024-06-04 19:13:45', 'Donasi otomatis', 'Muhammad Alif'),
(63, 1, 16, 1000.00, '2024-06-04 19:13:51', 'Donasi otomatis', 'Muhammad Alif'),
(64, 1, 16, 1000.00, '2024-06-04 19:13:55', 'Donasi otomatis', 'Muhammad Alif'),
(65, 1, 16, 1000.00, '2024-06-04 19:14:01', 'Donasi otomatis', 'Muhammad Alif'),
(66, 1, 16, 1000.00, '2024-06-04 19:14:05', 'Donasi otomatis', 'Muhammad Alif'),
(67, 1, 16, 1000.00, '2024-06-04 19:14:11', 'Donasi otomatis', 'Muhammad Alif'),
(68, 1, 16, 1000.00, '2024-06-04 19:14:15', 'Donasi otomatis', 'Muhammad Alif'),
(69, 1, 16, 1000.00, '2024-06-04 19:14:21', 'Donasi otomatis', 'Muhammad Alif'),
(70, 1, 16, 1000.00, '2024-06-04 19:14:25', 'Donasi otomatis', 'Muhammad Alif'),
(71, 1, 16, 1000.00, '2024-06-04 19:14:31', 'Donasi otomatis', 'Muhammad Alif'),
(72, 1, 16, 1000.00, '2024-06-04 19:14:35', 'Donasi otomatis', 'Muhammad Alif'),
(73, 1, 16, 1000.00, '2024-06-04 19:14:41', 'Donasi otomatis', 'Muhammad Alif'),
(74, 1, 16, 1000.00, '2024-06-04 19:14:45', 'Donasi otomatis', 'Muhammad Alif'),
(75, 1, 16, 1000.00, '2024-06-04 19:14:51', 'Donasi otomatis', 'Muhammad Alif'),
(76, 1, 16, 1000.00, '2024-06-04 19:14:55', 'Donasi otomatis', 'Muhammad Alif'),
(77, 1, 16, 1000.00, '2024-06-04 19:15:01', 'Donasi otomatis', 'Muhammad Alif'),
(78, 1, 16, 1000.00, '2024-06-04 19:15:05', 'Donasi otomatis', 'Muhammad Alif'),
(79, 1, 16, 1000.00, '2024-06-04 19:15:11', 'Donasi otomatis', 'Muhammad Alif'),
(80, 1, 16, 1000.00, '2024-06-04 19:15:15', 'Donasi otomatis', 'Muhammad Alif'),
(81, 1, 16, 1000.00, '2024-06-04 19:15:21', 'Donasi otomatis', 'Muhammad Alif'),
(82, 1, 16, 1000.00, '2024-06-04 19:15:25', 'Donasi otomatis', 'Muhammad Alif'),
(83, 1, 16, 1000.00, '2024-06-04 19:15:31', 'Donasi otomatis', 'Muhammad Alif'),
(84, 1, 16, 1000.00, '2024-06-04 19:15:35', 'Donasi otomatis', 'Muhammad Alif'),
(85, 1, 16, 1000.00, '2024-06-04 19:15:41', 'Donasi otomatis', 'Muhammad Alif'),
(86, 1, 16, 1000.00, '2024-06-04 19:15:45', 'Donasi otomatis', 'Muhammad Alif'),
(87, 1, 16, 1000.00, '2024-06-04 19:15:51', 'Donasi otomatis', 'Muhammad Alif'),
(88, 1, 16, 1000.00, '2024-06-04 19:15:55', 'Donasi otomatis', 'Muhammad Alif'),
(89, 1, 16, 1000.00, '2024-06-04 19:16:01', 'Donasi otomatis', 'Muhammad Alif'),
(90, 1, 16, 1000.00, '2024-06-04 19:16:05', 'Donasi otomatis', 'Muhammad Alif'),
(91, 1, 16, 1000.00, '2024-06-04 19:16:11', 'Donasi otomatis', 'Muhammad Alif'),
(92, 1, 16, 1000.00, '2024-06-04 19:16:15', 'Donasi otomatis', 'Muhammad Alif'),
(93, 1, 16, 1000.00, '2024-06-04 19:19:51', 'Donasi otomatis', 'Muhammad Alif'),
(94, 1, 16, 1000.00, '2024-06-04 19:20:01', 'Donasi otomatis', 'Muhammad Alif'),
(95, 1, 16, 1000.00, '2024-06-04 19:20:11', 'Donasi otomatis', 'Muhammad Alif'),
(96, 1, 16, 1000.00, '2024-06-04 19:20:21', 'Donasi otomatis', 'Muhammad Alif'),
(97, 1, 16, 500.00, '2024-06-04 19:23:38', 'Donasi otomatis', 'Muhammad Alif'),
(98, 1, 16, 500.00, '2024-06-04 19:23:48', 'Donasi otomatis', 'Muhammad Alif'),
(99, 1, 16, 500.00, '2024-06-04 19:23:58', 'Donasi otomatis', 'Muhammad Alif'),
(100, 1, 16, 500.00, '2024-06-04 19:24:08', 'Donasi otomatis', 'Muhammad Alif'),
(101, 1, 16, 500.00, '2024-06-04 19:24:18', 'Donasi otomatis', 'Muhammad Alif'),
(102, 1, 16, 500.00, '2024-06-04 19:24:28', 'Donasi otomatis', 'Muhammad Alif'),
(103, 1, 16, 500.00, '2024-06-04 19:24:38', 'Donasi otomatis', 'Muhammad Alif'),
(104, 1, 16, 500.00, '2024-06-04 19:24:48', 'Donasi otomatis', 'Muhammad Alif'),
(105, 1, 16, 500.00, '2024-06-04 19:24:58', 'Donasi otomatis', 'Muhammad Alif'),
(106, 1, 16, 500.00, '2024-06-04 19:25:08', 'Donasi otomatis', 'Muhammad Alif'),
(107, 1, 16, 500.00, '2024-06-04 19:25:18', 'Donasi otomatis', 'Muhammad Alif'),
(108, 1, 16, 500.00, '2024-06-04 19:25:28', 'Donasi otomatis', 'Muhammad Alif'),
(109, 1, 16, 500.00, '2024-06-04 19:25:38', 'Donasi otomatis', 'Muhammad Alif'),
(110, 1, 16, 500.00, '2024-06-04 19:25:48', 'Donasi otomatis', 'Muhammad Alif'),
(111, 1, 16, 500.00, '2024-06-04 19:25:58', 'Donasi otomatis', 'Muhammad Alif'),
(112, 1, 16, 500.00, '2024-06-04 19:26:08', 'Donasi otomatis', 'Muhammad Alif'),
(113, 1, 16, 500.00, '2024-06-04 19:26:18', 'Donasi otomatis', 'Muhammad Alif'),
(114, 1, 16, 500.00, '2024-06-04 19:26:28', 'Donasi otomatis', 'Muhammad Alif'),
(115, 1, 16, 500.00, '2024-06-04 19:26:38', 'Donasi otomatis', 'Muhammad Alif'),
(116, 1, 16, 500.00, '2024-06-04 19:26:48', 'Donasi otomatis', 'Muhammad Alif'),
(117, 1, 16, 500.00, '2024-06-04 19:26:58', 'Donasi otomatis', 'Muhammad Alif'),
(118, 1, 16, 500.00, '2024-06-04 19:27:08', 'Donasi otomatis', 'Muhammad Alif'),
(119, 1, 16, 500.00, '2024-06-04 19:27:18', 'Donasi otomatis', 'Muhammad Alif'),
(120, 1, 16, 500.00, '2024-06-04 19:27:28', 'Donasi otomatis', 'Muhammad Alif'),
(121, 1, 16, 500.00, '2024-06-04 19:27:38', 'Donasi otomatis', 'Muhammad Alif'),
(122, 1, 16, 500.00, '2024-06-04 19:27:48', 'Donasi otomatis', 'Muhammad Alif'),
(123, 1, 16, 500.00, '2024-06-04 19:27:58', 'Donasi otomatis', 'Muhammad Alif'),
(124, 1, 16, 100.00, '2024-06-04 19:31:19', 'Donasi otomatis', 'Muhammad Alif'),
(125, 1, 16, 100.00, '2024-06-04 19:31:29', 'Donasi otomatis', 'Muhammad Alif'),
(126, 1, 16, 100.00, '2024-06-04 19:33:22', 'Donasi otomatis', 'Muhammad Alif'),
(127, 1, 16, 100.00, '2024-06-04 19:33:32', 'Donasi otomatis', 'Muhammad Alif'),
(128, 1, 16, 100.00, '2024-06-04 19:33:42', 'Donasi otomatis', 'Muhammad Alif'),
(129, 12, 16, 10000.00, '2024-06-04 19:33:49', 'Donasi otomatis', 'Muhammad Nizam'),
(130, 1, 16, 100.00, '2024-06-04 19:33:52', 'Donasi otomatis', 'Muhammad Alif'),
(131, 1, 16, 100.00, '2024-06-04 19:34:02', 'Donasi otomatis', 'Muhammad Alif'),
(132, 1, 16, 100.00, '2024-06-04 19:34:12', 'Donasi otomatis', 'Muhammad Alif'),
(133, 1, 16, 100.00, '2024-06-04 19:34:22', 'Donasi otomatis', 'Muhammad Alif'),
(134, 1, 16, 100.00, '2024-06-04 19:34:32', 'Donasi otomatis', 'Muhammad Alif'),
(135, 1, 16, 100.00, '2024-06-04 19:34:42', 'Donasi otomatis', 'Muhammad Alif'),
(136, 12, 16, 1000.00, '2024-06-04 19:34:51', 'Donasi otomatis', 'Muhammad Nizam'),
(137, 1, 16, 100.00, '2024-06-04 19:34:52', 'Donasi otomatis', 'Muhammad Alif'),
(138, 12, 16, 1000.00, '2024-06-04 19:35:01', 'Donasi otomatis', 'Muhammad Nizam'),
(139, 1, 16, 100.00, '2024-06-04 19:35:02', 'Donasi otomatis', 'Muhammad Alif'),
(140, 12, 16, 1000.00, '2024-06-04 19:35:11', 'Donasi otomatis', 'Muhammad Nizam'),
(141, 1, 16, 100.00, '2024-06-04 19:35:12', 'Donasi otomatis', 'Muhammad Alif'),
(142, 12, 16, 1000.00, '2024-06-04 19:35:21', 'Donasi otomatis', 'Muhammad Nizam'),
(143, 1, 16, 100.00, '2024-06-04 19:35:22', 'Donasi otomatis', 'Muhammad Alif'),
(144, 12, 16, 1000.00, '2024-06-04 19:35:31', 'Donasi otomatis', 'Muhammad Nizam'),
(145, 1, 16, 100.00, '2024-06-04 19:35:32', 'Donasi otomatis', 'Muhammad Alif'),
(146, 1, 16, 100.00, '2024-06-04 19:35:42', 'Donasi otomatis', 'Muhammad Alif'),
(147, 1, 16, 100.00, '2024-06-04 19:35:53', 'Donasi otomatis', 'Muhammad Alif'),
(148, 1, 16, 100.00, '2024-06-04 19:36:03', 'Donasi otomatis', 'Muhammad Alif'),
(149, 1, 16, 100.00, '2024-06-04 19:36:13', 'Donasi otomatis', 'Muhammad Alif'),
(150, 1, 16, 100.00, '2024-06-04 19:36:23', 'Donasi otomatis', 'Muhammad Alif'),
(151, 1, 16, 100.00, '2024-06-04 19:36:33', 'Donasi otomatis', 'Muhammad Alif'),
(152, 1, 16, 100.00, '2024-06-04 19:36:43', 'Donasi otomatis', 'Muhammad Alif'),
(153, 1, 16, 100.00, '2024-06-04 19:36:53', 'Donasi otomatis', 'Muhammad Alif'),
(154, 1, 16, 100.00, '2024-06-04 19:37:03', 'Donasi otomatis', 'Muhammad Alif'),
(155, 1, 16, 100.00, '2024-06-04 19:37:13', 'Donasi otomatis', 'Muhammad Alif'),
(156, 1, 16, 100.00, '2024-06-04 19:37:23', 'Donasi otomatis', 'Muhammad Alif'),
(157, 1, 16, 100.00, '2024-06-04 19:37:33', 'Donasi otomatis', 'Muhammad Alif'),
(158, 1, 16, 100.00, '2024-06-04 19:37:43', 'Donasi otomatis', 'Muhammad Alif'),
(159, 1, 16, 100.00, '2024-06-04 19:37:53', 'Donasi otomatis', 'Muhammad Alif'),
(160, 1, 16, 100.00, '2024-06-04 19:38:03', 'Donasi otomatis', 'Muhammad Alif'),
(161, 1, 16, 100.00, '2024-06-04 19:38:13', 'Donasi otomatis', 'Muhammad Alif'),
(162, 1, 16, 100.00, '2024-06-04 19:38:23', 'Donasi otomatis', 'Muhammad Alif'),
(163, 1, 16, 100.00, '2024-06-04 19:38:33', 'Donasi otomatis', 'Muhammad Alif'),
(164, 1, 16, 100.00, '2024-06-04 19:39:04', 'Donasi otomatis', 'Muhammad Alif'),
(165, 1, 16, 100.00, '2024-06-04 19:39:14', 'Donasi otomatis', 'Muhammad Alif'),
(166, 1, 16, 100.00, '2024-06-04 19:39:24', 'Donasi otomatis', 'Muhammad Alif'),
(167, 1, 16, 100.00, '2024-06-04 19:39:34', 'Donasi otomatis', 'Muhammad Alif'),
(168, 1, 16, 100.00, '2024-06-04 19:39:44', 'Donasi otomatis', 'Muhammad Alif'),
(169, 1, 16, 100.00, '2024-06-04 19:39:54', 'Donasi otomatis', 'Muhammad Alif'),
(170, 1, 16, 100.00, '2024-06-04 19:40:04', 'Donasi otomatis', 'Muhammad Alif'),
(171, 1, 16, 100.00, '2024-06-04 19:40:14', 'Donasi otomatis', 'Muhammad Alif'),
(172, 1, 16, 100.00, '2024-06-04 19:40:24', 'Donasi otomatis', 'Muhammad Alif'),
(173, 1, 16, 100.00, '2024-06-04 19:40:34', 'Donasi otomatis', 'Muhammad Alif'),
(174, 1, 16, 100.00, '2024-06-04 19:40:44', 'Donasi otomatis', 'Muhammad Alif'),
(175, 1, 16, 100.00, '2024-06-04 19:40:54', 'Donasi otomatis', 'Muhammad Alif'),
(176, 12, 16, 100.00, '2024-06-04 19:41:02', 'Donasi otomatis', 'Muhammad Nizam'),
(177, 1, 16, 100.00, '2024-06-04 19:41:04', 'Donasi otomatis', 'Muhammad Alif'),
(178, 12, 16, 100.00, '2024-06-04 19:41:12', 'Donasi otomatis', 'Muhammad Nizam'),
(179, 1, 16, 100.00, '2024-06-04 19:41:14', 'Donasi otomatis', 'Muhammad Alif'),
(180, 12, 16, 100.00, '2024-06-04 19:41:22', 'Donasi otomatis', 'Muhammad Nizam'),
(181, 1, 16, 100.00, '2024-06-04 19:41:24', 'Donasi otomatis', 'Muhammad Alif'),
(182, 12, 16, 100.00, '2024-06-04 19:41:32', 'Donasi otomatis', 'Muhammad Nizam'),
(183, 1, 16, 100.00, '2024-06-04 19:41:34', 'Donasi otomatis', 'Muhammad Alif'),
(184, 12, 16, 100.00, '2024-06-04 19:41:42', 'Donasi otomatis', 'Muhammad Nizam'),
(185, 1, 16, 100.00, '2024-06-04 19:46:00', 'Donasi otomatis', 'Muhammad Alif'),
(186, 1, 16, 100.00, '2024-06-04 19:46:10', 'Donasi otomatis', 'Muhammad Alif'),
(187, 1, 16, 100.00, '2024-06-04 19:46:20', 'Donasi otomatis', 'Muhammad Alif'),
(188, 1, 16, 100.00, '2024-06-04 19:47:45', 'Donasi otomatis', 'Muhammad Alif'),
(189, 1, 16, 100.00, '2024-06-04 19:47:55', 'Donasi otomatis', 'Muhammad Alif'),
(190, 1, 16, 100.00, '2024-06-04 19:54:41', 'Donasi otomatis', 'Muhammad Alif'),
(191, 1, 16, 100.00, '2024-06-04 19:54:51', 'Donasi otomatis', 'Muhammad Alif'),
(192, 1, 16, 100.00, '2024-06-04 19:55:01', 'Donasi otomatis', 'Muhammad Alif'),
(193, 1, 16, 100.00, '2024-06-04 19:55:11', 'Donasi otomatis', 'Muhammad Alif'),
(194, 1, 16, 100.00, '2024-06-04 19:55:21', 'Donasi otomatis', 'Muhammad Alif'),
(195, 1, 16, 100.00, '2024-06-04 19:55:31', 'Donasi otomatis', 'Muhammad Alif'),
(196, 1, 16, 100.00, '2024-06-04 19:55:41', 'Donasi otomatis', 'Muhammad Alif'),
(197, 1, 16, 100.00, '2024-06-04 19:55:51', 'Donasi otomatis', 'Muhammad Alif'),
(198, 1, 16, 100.00, '2024-06-04 19:56:01', 'Donasi otomatis', 'Muhammad Alif'),
(199, 1, 16, 100.00, '2024-06-04 19:56:11', 'Donasi otomatis', 'Muhammad Alif'),
(200, 1, 16, 100.00, '2024-06-04 19:56:21', 'Donasi otomatis', 'Muhammad Alif'),
(201, 1, 16, 100.00, '2024-06-04 19:56:31', 'Donasi otomatis', 'Muhammad Alif'),
(202, 1, 16, 100.00, '2024-06-04 19:56:41', 'Donasi otomatis', 'Muhammad Alif'),
(203, 1, 16, 100.00, '2024-06-04 19:56:51', 'Donasi otomatis', 'Muhammad Alif'),
(204, 1, 16, 100.00, '2024-06-04 19:57:01', 'Donasi otomatis', 'Muhammad Alif'),
(205, 1, 16, 100.00, '2024-06-04 19:57:11', 'Donasi otomatis', 'Muhammad Alif'),
(206, 1, 16, 100.00, '2024-06-04 19:57:21', 'Donasi otomatis', 'Muhammad Alif'),
(207, 1, 16, 100.00, '2024-06-04 19:57:31', 'Donasi otomatis', 'Muhammad Alif'),
(208, 1, 16, 100.00, '2024-06-04 19:57:41', 'Donasi otomatis', 'Muhammad Alif'),
(209, 1, 16, 100.00, '2024-06-04 19:57:51', 'Donasi otomatis', 'Muhammad Alif'),
(210, 1, 16, 100.00, '2024-06-04 19:58:01', 'Donasi otomatis', 'Muhammad Alif'),
(211, 1, 16, 100.00, '2024-06-04 19:58:11', 'Donasi otomatis', 'Muhammad Alif'),
(212, 1, 16, 100.00, '2024-06-04 19:58:21', 'Donasi otomatis', 'Muhammad Alif'),
(213, 1, 16, 100.00, '2024-06-04 19:58:31', 'Donasi otomatis', 'Muhammad Alif'),
(214, 1, 16, 100.00, '2024-06-04 19:58:41', 'Donasi otomatis', 'Muhammad Alif'),
(215, 1, 16, 100.00, '2024-06-04 19:58:50', 'Donasi otomatis', 'Muhammad Alif'),
(216, 1, 16, 100.00, '2024-06-04 20:06:12', 'Donasi otomatis', 'Muhammad Alif'),
(217, 1, 16, 100.00, '2024-06-04 20:06:22', 'Donasi otomatis', 'Muhammad Alif'),
(218, 1, 16, 100.00, '2024-06-04 20:06:32', 'Donasi otomatis', 'Muhammad Alif'),
(219, 1, 16, 100.00, '2024-06-04 20:06:42', 'Donasi otomatis', 'Muhammad Alif'),
(220, 1, 16, 100.00, '2024-06-04 20:06:52', 'Donasi otomatis', 'Muhammad Alif'),
(221, 1, 16, 100.00, '2024-06-04 20:07:02', 'Donasi otomatis', 'Muhammad Alif'),
(222, 1, 16, 100.00, '2024-06-04 20:07:12', 'Donasi otomatis', 'Muhammad Alif'),
(223, 1, 16, 100.00, '2024-06-04 20:07:22', 'Donasi otomatis', 'Muhammad Alif'),
(224, 1, 16, 100.00, '2024-06-04 20:10:50', 'Donasi otomatis', 'Muhammad Alif'),
(225, 1, 16, 100.00, '2024-06-04 20:11:00', 'Donasi otomatis', 'Muhammad Alif'),
(226, 1, 16, 100.00, '2024-06-04 20:11:10', 'Donasi otomatis', 'Muhammad Alif'),
(227, 1, 16, 100.00, '2024-06-04 20:11:20', 'Donasi otomatis', 'Muhammad Alif'),
(228, 1, 16, 100.00, '2024-06-04 20:11:30', 'Donasi otomatis', 'Muhammad Alif'),
(229, 1, 16, 100.00, '2024-06-04 20:11:40', 'Donasi otomatis', 'Muhammad Alif'),
(230, 1, 16, 100.00, '2024-06-04 20:11:50', 'Donasi otomatis', 'Muhammad Alif'),
(231, 1, 16, 100.00, '2024-06-04 20:12:10', 'Donasi otomatis', 'Muhammad Alif'),
(232, 1, 16, 100.00, '2024-06-04 20:12:20', 'Donasi otomatis', 'Muhammad Alif'),
(233, 1, 16, 100.00, '2024-06-04 20:13:26', 'Donasi otomatis', 'Muhammad Alif'),
(234, 1, 16, 100.00, '2024-06-04 20:13:36', 'Donasi otomatis', 'Muhammad Alif'),
(235, 1, 16, 100.00, '2024-06-04 20:13:46', 'Donasi otomatis', 'Muhammad Alif'),
(236, 1, 16, 100.00, '2024-06-04 20:46:21', 'Donasi otomatis', 'Muhammad Alif'),
(237, 1, 16, 100.00, '2024-06-04 20:46:31', 'Donasi otomatis', 'Muhammad Alif'),
(238, 1, 16, 100.00, '2024-06-04 20:46:34', 'Donasi otomatis', 'Muhammad Alif'),
(239, 1, 16, 100.00, '2024-06-04 20:46:41', 'Donasi otomatis', 'Muhammad Alif'),
(240, 1, 16, 100.00, '2024-06-04 20:46:44', 'Donasi otomatis', 'Muhammad Alif'),
(241, 1, 16, 100.00, '2024-06-04 20:46:51', 'Donasi otomatis', 'Muhammad Alif'),
(242, 1, 16, 100.00, '2024-06-04 20:46:54', 'Donasi otomatis', 'Muhammad Alif'),
(243, 1, 16, 100.00, '2024-06-04 20:47:01', 'Donasi otomatis', 'Muhammad Alif'),
(244, 1, 16, 100.00, '2024-06-04 20:47:04', 'Donasi otomatis', 'Muhammad Alif'),
(245, 1, 16, 100.00, '2024-06-04 20:47:11', 'Donasi otomatis', 'Muhammad Alif'),
(246, 1, 16, 100.00, '2024-06-04 20:47:14', 'Donasi otomatis', 'Muhammad Alif'),
(247, 1, 16, 100.00, '2024-06-04 20:47:21', 'Donasi otomatis', 'Muhammad Alif'),
(248, 1, 16, 100.00, '2024-06-04 20:47:24', 'Donasi otomatis', 'Muhammad Alif'),
(249, 1, 16, 100.00, '2024-06-04 20:47:31', 'Donasi otomatis', 'Muhammad Alif'),
(250, 1, 16, 100.00, '2024-06-04 20:47:41', 'Donasi otomatis', 'Muhammad Alif'),
(251, 1, 16, 100.00, '2024-06-04 20:47:51', 'Donasi otomatis', 'Muhammad Alif'),
(252, 1, 16, 100.00, '2024-06-04 20:48:01', 'Donasi otomatis', 'Muhammad Alif'),
(253, 1, 16, 100.00, '2024-06-04 20:48:11', 'Donasi otomatis', 'Muhammad Alif'),
(254, 1, 16, 100.00, '2024-06-04 20:48:21', 'Donasi otomatis', 'Muhammad Alif'),
(255, 1, 16, 100.00, '2024-06-04 20:48:31', 'Donasi otomatis', 'Muhammad Alif'),
(256, 1, 16, 100.00, '2024-06-04 20:48:41', 'Donasi otomatis', 'Muhammad Alif'),
(257, 1, 16, 100.00, '2024-06-04 20:48:51', 'Donasi otomatis', 'Muhammad Alif'),
(258, 1, 16, 100.00, '2024-06-04 20:50:15', 'Donasi otomatis', 'Muhammad Alif'),
(259, 1, 16, 100.00, '2024-06-04 20:50:25', 'Donasi otomatis', 'Muhammad Alif'),
(260, 1, 16, 100.00, '2024-06-04 20:51:03', 'Donasi otomatis', 'Muhammad Alif'),
(261, 1, 16, 100.00, '2024-06-04 20:51:13', 'Donasi otomatis', 'Muhammad Alif'),
(262, 1, 16, 100.00, '2024-06-04 20:51:23', 'Donasi otomatis', 'Muhammad Alif'),
(263, 1, 16, 100.00, '2024-06-04 20:51:33', 'Donasi otomatis', 'Muhammad Alif'),
(264, 1, 16, 100.00, '2024-06-04 20:51:35', 'Donasi otomatis', 'Muhammad Alif'),
(265, 1, 16, 100.00, '2024-06-04 20:51:43', 'Donasi otomatis', 'Muhammad Alif'),
(266, 1, 16, 100.00, '2024-06-04 20:51:53', 'Donasi otomatis', 'Muhammad Alif'),
(267, 1, 16, 100.00, '2024-06-04 20:52:03', 'Donasi otomatis', 'Muhammad Alif'),
(268, 1, 16, 100.00, '2024-06-04 20:52:13', 'Donasi otomatis', 'Muhammad Alif'),
(269, 1, 16, 100.00, '2024-06-04 20:52:23', 'Donasi otomatis', 'Muhammad Alif'),
(270, 1, 16, 100.00, '2024-06-04 20:52:33', 'Donasi otomatis', 'Muhammad Alif'),
(271, 1, 16, 100.00, '2024-06-04 20:52:43', 'Donasi otomatis', 'Muhammad Alif'),
(272, 1, 16, 100.00, '2024-06-04 20:52:53', 'Donasi otomatis', 'Muhammad Alif'),
(273, 1, 16, 100.00, '2024-06-04 20:53:03', 'Donasi otomatis', 'Muhammad Alif'),
(274, 1, 16, 100.00, '2024-06-04 20:53:13', 'Donasi otomatis', 'Muhammad Alif'),
(275, 1, 16, 100.00, '2024-06-04 20:53:23', 'Donasi otomatis', 'Muhammad Alif'),
(276, 1, 16, 100.00, '2024-06-04 20:53:33', 'Donasi otomatis', 'Muhammad Alif'),
(277, 1, 16, 100.00, '2024-06-04 21:17:48', 'Donasi otomatis', 'Muhammad Alif'),
(278, 1, 16, 100.00, '2024-06-04 21:21:29', 'Donasi otomatis', 'Muhammad Alif'),
(279, 1, 16, 100.00, '2024-06-04 21:21:39', 'Donasi otomatis', 'Muhammad Alif'),
(280, 1, 16, 100.00, '2024-06-04 21:21:49', 'Donasi otomatis', 'Muhammad Alif'),
(281, 1, 16, 100.00, '2024-06-04 21:21:59', 'Donasi otomatis', 'Muhammad Alif'),
(282, 1, 16, 100.00, '2024-06-04 21:22:42', 'Donasi otomatis', 'Muhammad Alif'),
(283, 1, 16, 100.00, '2024-06-04 21:23:03', 'Donasi otomatis', 'Muhammad Alif'),
(284, 1, 16, 100.00, '2024-06-04 21:23:13', 'Donasi otomatis', 'Muhammad Alif'),
(285, 1, 16, 100.00, '2024-06-04 21:23:23', 'Donasi otomatis', 'Muhammad Alif'),
(286, 1, 16, 100.00, '2024-06-04 21:23:33', 'Donasi otomatis', 'Muhammad Alif'),
(287, 1, 16, 100.00, '2024-06-04 21:23:43', 'Donasi otomatis', 'Muhammad Alif'),
(288, 1, 16, 100.00, '2024-06-04 21:23:55', 'Donasi otomatis', 'Muhammad Alif'),
(289, 1, 16, 100.00, '2024-06-04 21:24:05', 'Donasi otomatis', 'Muhammad Alif'),
(290, 11, 16, 100.00, '2024-06-04 21:25:55', 'Donasi otomatis', 'Kevin Rafif'),
(291, 11, 16, 100.00, '2024-06-04 21:26:05', 'Donasi otomatis', 'Kevin Rafif'),
(292, 11, 16, 100.00, '2024-06-04 21:26:24', 'Donasi otomatis', 'Kevin Rafif'),
(293, 11, 16, 100.00, '2024-06-04 21:26:34', 'Donasi otomatis', 'Kevin Rafif'),
(294, 11, 16, 100.00, '2024-06-04 21:26:44', 'Donasi otomatis', 'Kevin Rafif'),
(295, 11, 16, 100.00, '2024-06-04 21:26:54', 'Donasi otomatis', 'Kevin Rafif'),
(296, 11, 16, 100.00, '2024-06-04 21:27:00', 'Donasi otomatis', 'Kevin Rafif'),
(297, 11, 16, 100.00, '2024-06-04 21:27:04', 'Donasi otomatis', 'Kevin Rafif'),
(298, 11, 16, 100.00, '2024-06-04 21:27:14', 'Donasi otomatis', 'Kevin Rafif'),
(299, 11, 16, 100.00, '2024-06-04 21:27:24', 'Donasi otomatis', 'Kevin Rafif'),
(300, 11, 16, 100.00, '2024-06-04 21:27:34', 'Donasi otomatis', 'Kevin Rafif'),
(301, 11, 16, 100.00, '2024-06-04 21:27:44', 'Donasi otomatis', 'Kevin Rafif'),
(302, 11, 16, 100.00, '2024-06-04 21:27:54', 'Donasi otomatis', 'Kevin Rafif'),
(303, 11, 16, 100.00, '2024-06-04 21:28:04', 'Donasi otomatis', 'Kevin Rafif'),
(304, 11, 16, 100.00, '2024-06-04 21:28:14', 'Donasi otomatis', 'Kevin Rafif'),
(305, 11, 16, 100.00, '2024-06-04 21:28:24', 'Donasi otomatis', 'Kevin Rafif'),
(306, 11, 16, 100.00, '2024-06-04 21:28:34', 'Donasi otomatis', 'Kevin Rafif'),
(307, 11, 16, 100.00, '2024-06-04 21:28:44', 'Donasi otomatis', 'Kevin Rafif'),
(308, 11, 16, 100.00, '2024-06-04 21:28:54', 'Donasi otomatis', 'Kevin Rafif'),
(309, 11, 16, 100.00, '2024-06-04 21:29:04', 'Donasi otomatis', 'Kevin Rafif'),
(310, 11, 16, 100.00, '2024-06-04 21:29:14', 'Donasi otomatis', 'Kevin Rafif'),
(311, 11, 16, 100.00, '2024-06-04 21:29:24', 'Donasi otomatis', 'Kevin Rafif'),
(312, 11, 16, 100.00, '2024-06-04 21:29:34', 'Donasi otomatis', 'Kevin Rafif'),
(313, 11, 16, 100.00, '2024-06-04 21:29:44', 'Donasi otomatis', 'Kevin Rafif'),
(314, 1, 16, 100.00, '2024-06-04 21:34:54', 'Donasi otomatis', 'Muhammad Alif'),
(315, 1, 16, 100.00, '2024-06-04 21:35:04', 'Donasi otomatis', 'Muhammad Alif'),
(316, 1, 16, 100.00, '2024-06-04 21:35:42', 'Donasi otomatis', 'Muhammad Alif'),
(317, 1, 16, 100.00, '2024-06-04 21:36:50', 'Donasi otomatis', 'Muhammad Alif'),
(318, 1, 16, 100.00, '2024-06-04 21:37:00', 'Donasi otomatis', 'Muhammad Alif'),
(319, 1, 16, 100.00, '2024-06-04 21:37:10', 'Donasi otomatis', 'Muhammad Alif'),
(320, 1, 16, 100.00, '2024-06-04 21:37:20', 'Donasi otomatis', 'Muhammad Alif'),
(321, 1, 16, 100.00, '2024-06-04 21:37:30', 'Donasi otomatis', 'Muhammad Alif');

-- --------------------------------------------------------

--
-- Table structure for table `donatur_anak_asuh`
--

CREATE TABLE `donatur_anak_asuh` (
  `id` int(11) NOT NULL,
  `donatur_id` int(11) DEFAULT NULL,
  `anak_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `programs`
--

CREATE TABLE `programs` (
  `id_program` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `target_donasi` decimal(15,2) NOT NULL,
  `donasi_terkumpul` decimal(15,2) NOT NULL DEFAULT 0.00,
  `tenggat` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `programs`
--

INSERT INTO `programs` (`id_program`, `nama`, `deskripsi`, `target_donasi`, `donasi_terkumpul`, `tenggat`) VALUES
(3, 'Testing Program', 'Deskripsi telah diubah', 150000000.00, 0.00, '2004-03-24'),
(8, 'testing hapus lagi', 'awodkaowd', 123123.00, 12000.00, '2001-12-02'),
(15, 'uy', '10', 1000000.00, 0.00, '2024-06-03'),
(16, 'nice', 'okey', 9999999.00, 130700.00, '2024-06-03');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adik_asuh`
--
ALTER TABLE `adik_asuh`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `akun`
--
ALTER TABLE `akun`
  ADD PRIMARY KEY (`id_akun`);

--
-- Indexes for table `donasi`
--
ALTER TABLE `donasi`
  ADD PRIMARY KEY (`id_donasi`),
  ADD KEY `id_akun` (`id_akun`),
  ADD KEY `id_program` (`id_program`);

--
-- Indexes for table `donatur_anak_asuh`
--
ALTER TABLE `donatur_anak_asuh`
  ADD PRIMARY KEY (`id`),
  ADD KEY `donatur_id` (`donatur_id`),
  ADD KEY `anak_id` (`anak_id`);

--
-- Indexes for table `programs`
--
ALTER TABLE `programs`
  ADD PRIMARY KEY (`id_program`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adik_asuh`
--
ALTER TABLE `adik_asuh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `akun`
--
ALTER TABLE `akun`
  MODIFY `id_akun` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `donasi`
--
ALTER TABLE `donasi`
  MODIFY `id_donasi` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=322;

--
-- AUTO_INCREMENT for table `donatur_anak_asuh`
--
ALTER TABLE `donatur_anak_asuh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `programs`
--
ALTER TABLE `programs`
  MODIFY `id_program` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `donasi`
--
ALTER TABLE `donasi`
  ADD CONSTRAINT `donasi_ibfk_1` FOREIGN KEY (`id_akun`) REFERENCES `akun` (`id_akun`),
  ADD CONSTRAINT `donasi_ibfk_2` FOREIGN KEY (`id_program`) REFERENCES `programs` (`id_program`);

--
-- Constraints for table `donatur_anak_asuh`
--
ALTER TABLE `donatur_anak_asuh`
  ADD CONSTRAINT `donatur_anak_asuh_ibfk_1` FOREIGN KEY (`donatur_id`) REFERENCES `akun` (`id_akun`),
  ADD CONSTRAINT `donatur_anak_asuh_ibfk_2` FOREIGN KEY (`anak_id`) REFERENCES `adik_asuh` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
