-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2022 at 01:20 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user-system`
--

-- --------------------------------------------------------

--
-- Table structure for table `form`
--

CREATE TABLE `form` (
  `id` bigint(255) NOT NULL,
  `booking` bigint(255) NOT NULL,
  `type` text NOT NULL,
  `reason` text NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `form`
--

INSERT INTO `form` (`id`, `booking`, `type`, `reason`, `datetime`) VALUES
(1, 1234, 'Refund', 'testing', '2022-11-07 21:03:33'),
(2, 1234, 'Tukar Tempahan', 'testing', '2022-11-07 21:03:45'),
(3, 1234, '取消', 'testing', '2022-11-07 21:03:59'),
(4, 1234, '取消', 'testing', '2022-11-07 21:04:43'),
(5, 1234, '退款', 'testing', '2022-11-07 21:09:26'),
(6, 3324, 'Bayaran Balik', 'testing', '2022-11-09 01:30:09'),
(7, 1234, 'Refund', 'testing22', '2022-11-14 14:02:19'),
(8, 1234, 'Bayaran Balik', 'testing2', '2022-11-14 14:02:48'),
(9, 1234, '退款', 'testing2', '2022-11-14 14:03:56'),
(10, 1234, 'Change Booking', 'testing', '2022-11-14 14:04:18'),
(11, 1234, 'Bayaran Balik', 'testing', '2022-11-14 14:04:38'),
(12, 1234, '退款', 'testing', '2022-11-14 14:04:56'),
(13, 1234, 'Refund', 'testing', '2022-11-15 20:18:13'),
(14, 2234, 'Tukar Tempahan', 'testing', '2022-11-15 20:19:13'),
(15, 1234, '取消', 'testing', '2022-11-15 20:19:30'),
(16, 1234, 'Cancel Booking', 'testing2', '2022-11-15 20:19:51'),
(17, 1234, 'Bayaran Balik', 'testing2', '2022-11-15 20:20:08'),
(18, 1234, '退款', 'testing2', '2022-11-15 20:20:21');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `bookid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`name`, `email`, `password`, `bookid`) VALUES
('Alexandar', 'test1@gmail.com', '12345', 1234),
('Alexandar', 'test1@gmail.com', '12345', 2234),
('Saddiq', 'test2@gmail.com', '12345', 2324),
('Saddiq', 'test2@gmail.com', '12345', 2326),
('Kim', 'test3@gmail.com', '12345', 3324),
('Kim', 'test3@gmail.com', '12345', 3387);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `form`
--
ALTER TABLE `form`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`bookid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `form`
--
ALTER TABLE `form`
  MODIFY `id` bigint(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
