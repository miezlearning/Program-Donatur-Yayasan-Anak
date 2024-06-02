-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2024 at 11:05 PM
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
(1, 'Muhammad Alif', 'alip', '123', '081345028895', 'Donatur', 'm.alif7890@gmail.com', 15000.00),
(2, 'Muhammad Khairrudin', 'admin', '123', '081388888888', 'Admin', 'khoirudin044@gmail.com', 0.00),
(7, 'Siti Putri Lenggo Geni', 'siti', '123', '081345028895', 'Donatur', 'lenggo.geni0305@gmail.com', 0.00),
(8, 'Felisitas Merry', 'merry', '123', '3849732947982', 'Donatur', 'merry@gmail.com', 0.00),
(11, 'Kevin Rafif', 'kevin', '123', '0813432952893', 'Donatur', 'kevin@gmail.com', 0.00),
(12, 'Muhammad Nizam', 'nizam', '123', '081338247287', 'Donatur', 'ijamnizam224@gmail.com', 0.00),
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
(24, 'Yanto Kabir', 'mukil', '123', '23987289', 'Donatur', 'tano@gmail.com', 0.00);

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
(4, 1, 5, 25000.00, '2024-06-01 15:29:04', 'Semangatt', 'Muhammad Alif');

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
(5, 'apa', 'apa', 1555.00, 25000.00, '2004-10-23'),
(8, 'testing hapus lagi', 'awodkaowd', 123123.00, 12000.00, '2001-12-02');

--
-- Indexes for dumped tables
--

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
-- Indexes for table `programs`
--
ALTER TABLE `programs`
  ADD PRIMARY KEY (`id_program`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `akun`
--
ALTER TABLE `akun`
  MODIFY `id_akun` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `donasi`
--
ALTER TABLE `donasi`
  MODIFY `id_donasi` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `programs`
--
ALTER TABLE `programs`
  MODIFY `id_program` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `donasi`
--
ALTER TABLE `donasi`
  ADD CONSTRAINT `donasi_ibfk_1` FOREIGN KEY (`id_akun`) REFERENCES `akun` (`id_akun`),
  ADD CONSTRAINT `donasi_ibfk_2` FOREIGN KEY (`id_program`) REFERENCES `programs` (`id_program`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
