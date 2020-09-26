-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 26, 2020 at 02:47 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_detail`
--

CREATE TABLE `student_detail` (
  `id` int(11) NOT NULL,
  `name` varchar(225) NOT NULL,
  `course` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_detail`
--

INSERT INTO `student_detail` (`id`, `name`, `course`, `phone`, `age`) VALUES
(1, 'xZx', 'asdas', 'dsa', 1),
(2, 'as', 'sasa', 'asdas', 0),
(3, 'as', 'sasa', 'asdas', 0),
(4, 'sasd', 'asda', 'asdas', 0),
(5, 'manorma', 'web designing ', '98745612', 45),
(6, 'dadsa', 'dasd', 'adsa', 0),
(7, '', '', '', 0),
(8, '', '', '', 0),
(9, 'dada', '', 'dada', 0),
(10, 'asd', '', '', 0),
(11, 'asd', '', '', 0),
(12, 'sdasd', 'sdad', 'daa', 0),
(13, 'manu', 'dasd', 'dadsa', 0),
(14, 'dads', 'dasd', 'da', 0),
(15, 'asdas', 'dasd', 'asda', 0),
(16, 'asdas', 'dasd', 'asda', 0),
(17, 'asda', 'dad', 'ada', 0),
(18, 'asdad', 'dads', 'dasd', 0),
(19, 'df', 'sdf', 'fsdf', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student_detail`
--
ALTER TABLE `student_detail`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student_detail`
--
ALTER TABLE `student_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
