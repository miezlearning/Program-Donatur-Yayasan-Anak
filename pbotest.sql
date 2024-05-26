-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 26, 2024 at 09:21 PM
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
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `akun`
--

INSERT INTO `akun` (`id_akun`, `nama`, `username`, `password`, `notelp`, `role`, `email`) VALUES
(1, 'Muhammad Alif', 'alip', '123', '081345028895', 'Donatur', 'm.alif7890@gmail.com'),
(2, 'Muhammad Khairrudin', 'admin', '123', '081388888888', 'Admin', 'khoirudin044@gmail.com'),
(7, 'Siti Putri Lenggo Geni', 'siti', '123', '081345028895', 'Donatur', 'lenggo.geni0305@gmail.com'),
(8, 'Felisitas Merry', 'merry', '123', '3849732947982', 'Donatur', 'merry@gmail.com'),
(11, 'Kevin Rafif', 'kevin', '123', '0813432952893', 'Donatur', 'kevin@gmail.com'),
(12, 'Muhammad Nizam', 'nizam', '123', '081338247287', 'Donatur', 'ijamnizam224@gmail.com'),
(13, 'Judiono', 'papa', '123', '101203', 'Donatur', 'wadawd'),
(14, 'Yanto', 'lala', '123', '021300', 'Donatur', 'weaod'),
(15, 'Moik', 'aaa', '123', '23912', 'Donatur', 'alip@gmail.com'),
(16, 'Putri Nadilla Maharani', 'putri', 'hahahahaha', '0813101010110', 'Donatur', 'putrinadilla80@gmail.com'),
(17, 'Apalah', 'rangga', 'rangga123', '081345028261', 'Donatur', 'rangga@gmail.com'),
(18, 'Yusuf', 'ucup', '123', '081345020000', 'Donatur', 'ucup@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `akun`
--
ALTER TABLE `akun`
  ADD PRIMARY KEY (`id_akun`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `akun`
--
ALTER TABLE `akun`
  MODIFY `id_akun` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
