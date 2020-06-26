-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 26, 2020 at 12:29 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `homestop`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
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
(25, 'Can add auth group', 7, 'add_authgroup'),
(26, 'Can change auth group', 7, 'change_authgroup'),
(27, 'Can delete auth group', 7, 'delete_authgroup'),
(28, 'Can view auth group', 7, 'view_authgroup'),
(29, 'Can add auth group permissions', 8, 'add_authgrouppermissions'),
(30, 'Can change auth group permissions', 8, 'change_authgrouppermissions'),
(31, 'Can delete auth group permissions', 8, 'delete_authgrouppermissions'),
(32, 'Can view auth group permissions', 8, 'view_authgrouppermissions'),
(33, 'Can add auth permission', 9, 'add_authpermission'),
(34, 'Can change auth permission', 9, 'change_authpermission'),
(35, 'Can delete auth permission', 9, 'delete_authpermission'),
(36, 'Can view auth permission', 9, 'view_authpermission'),
(37, 'Can add auth user', 10, 'add_authuser'),
(38, 'Can change auth user', 10, 'change_authuser'),
(39, 'Can delete auth user', 10, 'delete_authuser'),
(40, 'Can view auth user', 10, 'view_authuser'),
(41, 'Can add auth user groups', 11, 'add_authusergroups'),
(42, 'Can change auth user groups', 11, 'change_authusergroups'),
(43, 'Can delete auth user groups', 11, 'delete_authusergroups'),
(44, 'Can view auth user groups', 11, 'view_authusergroups'),
(45, 'Can add auth user user permissions', 12, 'add_authuseruserpermissions'),
(46, 'Can change auth user user permissions', 12, 'change_authuseruserpermissions'),
(47, 'Can delete auth user user permissions', 12, 'delete_authuseruserpermissions'),
(48, 'Can view auth user user permissions', 12, 'view_authuseruserpermissions'),
(49, 'Can add django admin log', 13, 'add_djangoadminlog'),
(50, 'Can change django admin log', 13, 'change_djangoadminlog'),
(51, 'Can delete django admin log', 13, 'delete_djangoadminlog'),
(52, 'Can view django admin log', 13, 'view_djangoadminlog'),
(53, 'Can add django content type', 14, 'add_djangocontenttype'),
(54, 'Can change django content type', 14, 'change_djangocontenttype'),
(55, 'Can delete django content type', 14, 'delete_djangocontenttype'),
(56, 'Can view django content type', 14, 'view_djangocontenttype'),
(57, 'Can add django migrations', 15, 'add_djangomigrations'),
(58, 'Can change django migrations', 15, 'change_djangomigrations'),
(59, 'Can delete django migrations', 15, 'delete_djangomigrations'),
(60, 'Can view django migrations', 15, 'view_djangomigrations'),
(61, 'Can add django session', 16, 'add_djangosession'),
(62, 'Can change django session', 16, 'change_djangosession'),
(63, 'Can delete django session', 16, 'delete_djangosession'),
(64, 'Can view django session', 16, 'view_djangosession'),
(65, 'Can add test11', 17, 'add_test11'),
(66, 'Can change test11', 17, 'change_test11'),
(67, 'Can delete test11', 17, 'delete_test11'),
(68, 'Can view test11', 17, 'view_test11'),
(69, 'Can add test22', 18, 'add_test22'),
(70, 'Can change test22', 18, 'change_test22'),
(71, 'Can delete test22', 18, 'delete_test22'),
(72, 'Can view test22', 18, 'view_test22'),
(73, 'Can add items', 19, 'add_items'),
(74, 'Can change items', 19, 'change_items'),
(75, 'Can delete items', 19, 'delete_items'),
(76, 'Can view items', 19, 'view_items'),
(77, 'Can add ord', 20, 'add_ord'),
(78, 'Can change ord', 20, 'change_ord'),
(79, 'Can delete ord', 20, 'delete_ord'),
(80, 'Can view ord', 20, 'view_ord'),
(81, 'Can add order details', 21, 'add_orderdetails'),
(82, 'Can change order details', 21, 'change_orderdetails'),
(83, 'Can delete order details', 21, 'delete_orderdetails'),
(84, 'Can view order details', 21, 'view_orderdetails'),
(85, 'Can add users', 22, 'add_users'),
(86, 'Can change users', 22, 'change_users'),
(87, 'Can delete users', 22, 'delete_users'),
(88, 'Can view users', 22, 'view_users'),
(89, 'Can add user verification', 23, 'add_userverification'),
(90, 'Can change user verification', 23, 'change_userverification'),
(91, 'Can delete user verification', 23, 'delete_userverification'),
(92, 'Can view user verification', 23, 'view_userverification'),
(93, 'Can add chat', 24, 'add_chat'),
(94, 'Can change chat', 24, 'change_chat'),
(95, 'Can delete chat', 24, 'delete_chat'),
(96, 'Can view chat', 24, 'view_chat'),
(97, 'Can add customers', 25, 'add_customers'),
(98, 'Can change customers', 25, 'change_customers'),
(99, 'Can delete customers', 25, 'delete_customers'),
(100, 'Can view customers', 25, 'view_customers'),
(101, 'Can add delivery personal', 26, 'add_deliverypersonal'),
(102, 'Can change delivery personal', 26, 'change_deliverypersonal'),
(103, 'Can delete delivery personal', 26, 'delete_deliverypersonal'),
(104, 'Can view delivery personal', 26, 'view_deliverypersonal'),
(105, 'Can add reviews rating', 27, 'add_reviewsrating'),
(106, 'Can change reviews rating', 27, 'change_reviewsrating'),
(107, 'Can delete reviews rating', 27, 'delete_reviewsrating'),
(108, 'Can view reviews rating', 27, 'view_reviewsrating'),
(109, 'Can add stock', 28, 'add_stock'),
(110, 'Can change stock', 28, 'change_stock'),
(111, 'Can delete stock', 28, 'delete_stock'),
(112, 'Can view stock', 28, 'view_stock'),
(113, 'Can add vendor', 29, 'add_vendor'),
(114, 'Can change vendor', 29, 'change_vendor'),
(115, 'Can delete vendor', 29, 'delete_vendor'),
(116, 'Can view vendor', 29, 'view_vendor'),
(117, 'Can add order', 30, 'add_order'),
(118, 'Can change order', 30, 'change_order'),
(119, 'Can delete order', 30, 'delete_order'),
(120, 'Can view order', 30, 'view_order'),
(121, 'Can add monthly order', 31, 'add_monthlyorder'),
(122, 'Can change monthly order', 31, 'change_monthlyorder'),
(123, 'Can delete monthly order', 31, 'delete_monthlyorder'),
(124, 'Can view monthly order', 31, 'view_monthlyorder'),
(125, 'Can add morder', 32, 'add_morder'),
(126, 'Can change morder', 32, 'change_morder'),
(127, 'Can delete morder', 32, 'delete_morder'),
(128, 'Can view morder', 32, 'view_morder');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Chat`
--

CREATE TABLE `Chat` (
  `Cid` int(11) NOT NULL,
  `Vid` int(11) NOT NULL,
  `msg` text COLLATE utf8_unicode_ci NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `Cid` int(11) NOT NULL,
  `Payment_Dets` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `balance` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Delivery_personal`
--

CREATE TABLE `Delivery_personal` (
  `Did` int(11) NOT NULL,
  `ACC_dets` text COLLATE utf8_unicode_ci NOT NULL,
  `Licence_no` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Licence_plt_no` varchar(10) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'posthandler', 'authgroup'),
(8, 'posthandler', 'authgrouppermissions'),
(9, 'posthandler', 'authpermission'),
(10, 'posthandler', 'authuser'),
(11, 'posthandler', 'authusergroups'),
(12, 'posthandler', 'authuseruserpermissions'),
(24, 'posthandler', 'chat'),
(25, 'posthandler', 'customers'),
(26, 'posthandler', 'deliverypersonal'),
(13, 'posthandler', 'djangoadminlog'),
(14, 'posthandler', 'djangocontenttype'),
(15, 'posthandler', 'djangomigrations'),
(16, 'posthandler', 'djangosession'),
(19, 'posthandler', 'items'),
(31, 'posthandler', 'monthlyorder'),
(32, 'posthandler', 'morder'),
(20, 'posthandler', 'ord'),
(30, 'posthandler', 'order'),
(21, 'posthandler', 'orderdetails'),
(27, 'posthandler', 'reviewsrating'),
(28, 'posthandler', 'stock'),
(17, 'posthandler', 'test11'),
(18, 'posthandler', 'test22'),
(22, 'posthandler', 'users'),
(23, 'posthandler', 'userverification'),
(29, 'posthandler', 'vendor'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-06-12 13:39:55.338698'),
(2, 'auth', '0001_initial', '2020-06-12 13:39:55.846673'),
(3, 'admin', '0001_initial', '2020-06-12 13:39:57.786068'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-06-12 13:39:58.215358'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-06-12 13:39:58.249845'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-06-12 13:39:58.447774'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-06-12 13:39:58.601420'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-06-12 13:39:58.630189'),
(9, 'auth', '0004_alter_user_username_opts', '2020-06-12 13:39:58.654215'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-06-12 13:39:58.727567'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-06-12 13:39:58.739547'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-06-12 13:39:58.779712'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-06-12 13:39:58.815781'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-06-12 13:39:58.862423'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-06-12 13:39:58.913628'),
(16, 'auth', '0011_update_proxy_permissions', '2020-06-12 13:39:58.944993'),
(17, 'posthandler', '0001_initial', '2020-06-12 13:39:59.005893'),
(18, 'sessions', '0001_initial', '2020-06-12 13:39:59.153285'),
(19, 'posthandler', '0002_auto_20200613_0150', '2020-06-13 01:50:56.459262'),
(20, 'posthandler', '0003_auto_20200623_0849', '2020-06-23 08:50:05.738871'),
(21, 'posthandler', '0004_monthlyorder_morder', '2020-06-26 06:28:12.162255');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `iid` int(11) NOT NULL,
  `Item_Name` varchar(30) NOT NULL,
  `Company` int(11) NOT NULL,
  `Cost` bigint(20) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Monthly_Order`
--

CREATE TABLE `Monthly_Order` (
  `Mid` int(11) NOT NULL,
  `Cid` int(11) NOT NULL,
  `Vid` int(11) NOT NULL,
  `CreatedDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `CostPerMonth` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Morder`
--

CREATE TABLE `Morder` (
  `Moid` int(11) NOT NULL,
  `iid` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `oid` int(11) NOT NULL,
  `iid` int(11) NOT NULL,
  `qty` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `Oid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE current_timestamp(),
  `did` int(11) DEFAULT NULL,
  `paymnt_method` varchar(30) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Cash',
  `order_stat` varchar(10) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Ongoing',
  `total_cost` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reviews_rating`
--

CREATE TABLE `reviews_rating` (
  `cid` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `review` text NOT NULL,
  `rating` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Stock`
--

CREATE TABLE `Stock` (
  `Vid` int(11) NOT NULL,
  `iid` int(11) NOT NULL,
  `cost` float NOT NULL,
  `units` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Uid` int(11) NOT NULL,
  `Usrname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Passwd` text COLLATE utf8_unicode_ci NOT NULL,
  `Phno` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `Email_Id` text COLLATE utf8_unicode_ci NOT NULL,
  `Fname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Mname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Lname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Lat` float(10,6) DEFAULT NULL COMMENT 'Latitude',
  `Lon` float(10,6) DEFAULT NULL COMMENT 'Longitude',
  `Address` text COLLATE utf8_unicode_ci NOT NULL,
  `Online` tinyint(1) NOT NULL DEFAULT 0,
  `Type` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `date of join` datetime NOT NULL DEFAULT current_timestamp(),
  `pt` text COLLATE utf8_unicode_ci NOT NULL,
  `api_key` text COLLATE utf8_unicode_ci NOT NULL,
  `iv` text COLLATE utf8_unicode_ci NOT NULL,
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `verified` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Uid`, `Usrname`, `Passwd`, `Phno`, `Email_Id`, `Fname`, `Mname`, `Lname`, `Lat`, `Lon`, `Address`, `Online`, `Type`, `date of join`, `pt`, `api_key`, `iv`, `updated_time`, `verified`) VALUES
(52, 'g', 'asdfgh', '6854163', 'shail.sdofij@st.niituniversity.in', 'asddfg', 'ssdfg', 'qwerty', NULL, NULL, '46,asd,awefwsd', 1, 'customer', '2020-06-25 13:33:18', 'Amb0+VTENDuv6akBwm8I0w==', 'WgFY7K/vmOm93fl7wIS2mg==', 'XFyOmDu+Uz8oUjVUzUl5eA==', '2020-06-25 13:33:18', 1),
(64, 'gh', 'asdfghasd', '123456234', 'shail.sdaasdofij@st.niituniveqwrsity.in', 'asd', 'zxc', 'qwer', NULL, NULL, '', 1, 'vendor', '2020-06-25 17:13:43', ' ', ' ', ' ', '2020-06-25 17:13:43', 0);

-- --------------------------------------------------------

--
-- Table structure for table `user_verification`
--

CREATE TABLE `user_verification` (
  `uid` int(11) NOT NULL,
  `email` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `hash` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp(),
  `stat` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vendor`
--

CREATE TABLE `vendor` (
  `Vid` int(11) NOT NULL,
  `description` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `GST_Code` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ACC Dets` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `Shop_Name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Type` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `Chat`
--
ALTER TABLE `Chat`
  ADD PRIMARY KEY (`Cid`,`Vid`),
  ADD KEY `h` (`Vid`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`Cid`);

--
-- Indexes for table `Delivery_personal`
--
ALTER TABLE `Delivery_personal`
  ADD PRIMARY KEY (`Did`),
  ADD UNIQUE KEY `a` (`Licence_no`),
  ADD UNIQUE KEY `s` (`Licence_plt_no`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`iid`);

--
-- Indexes for table `Monthly_Order`
--
ALTER TABLE `Monthly_Order`
  ADD PRIMARY KEY (`Mid`),
  ADD KEY `q` (`Cid`),
  ADD KEY `w` (`Vid`);

--
-- Indexes for table `Morder`
--
ALTER TABLE `Morder`
  ADD PRIMARY KEY (`Moid`,`iid`),
  ADD KEY `i` (`iid`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`oid`,`iid`),
  ADD KEY `item1` (`iid`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`Oid`),
  ADD KEY `d` (`cid`),
  ADD KEY `e` (`vid`),
  ADD KEY `f` (`did`);

--
-- Indexes for table `reviews_rating`
--
ALTER TABLE `reviews_rating`
  ADD PRIMARY KEY (`cid`,`vid`),
  ADD KEY `vendor2` (`vid`);

--
-- Indexes for table `Stock`
--
ALTER TABLE `Stock`
  ADD PRIMARY KEY (`Vid`,`iid`),
  ADD KEY `item2` (`iid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Uid`),
  ADD UNIQUE KEY `a` (`Usrname`),
  ADD UNIQUE KEY `s` (`Phno`),
  ADD UNIQUE KEY `q` (`Email_Id`(1000));

--
-- Indexes for table `user_verification`
--
ALTER TABLE `user_verification`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `d` (`hash`);

--
-- Indexes for table `vendor`
--
ALTER TABLE `vendor`
  ADD PRIMARY KEY (`Vid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `Cid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Delivery_personal`
--
ALTER TABLE `Delivery_personal`
  MODIFY `Did` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `Monthly_Order`
--
ALTER TABLE `Monthly_Order`
  MODIFY `Mid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order_details`
--
ALTER TABLE `order_details`
  MODIFY `Oid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `Uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `vendor`
--
ALTER TABLE `vendor`
  MODIFY `Vid` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `Chat`
--
ALTER TABLE `Chat`
  ADD CONSTRAINT `user5` FOREIGN KEY (`Cid`) REFERENCES `customers` (`Cid`),
  ADD CONSTRAINT `user6` FOREIGN KEY (`Vid`) REFERENCES `vendor` (`Vid`);

--
-- Constraints for table `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `user1` FOREIGN KEY (`Cid`) REFERENCES `users` (`Uid`);

--
-- Constraints for table `Delivery_personal`
--
ALTER TABLE `Delivery_personal`
  ADD CONSTRAINT `user3` FOREIGN KEY (`Did`) REFERENCES `users` (`Uid`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `Monthly_Order`
--
ALTER TABLE `Monthly_Order`
  ADD CONSTRAINT `q` FOREIGN KEY (`Cid`) REFERENCES `customers` (`Cid`),
  ADD CONSTRAINT `w` FOREIGN KEY (`Vid`) REFERENCES `vendor` (`Vid`);

--
-- Constraints for table `Morder`
--
ALTER TABLE `Morder`
  ADD CONSTRAINT `e` FOREIGN KEY (`Moid`) REFERENCES `Monthly_Order` (`Mid`),
  ADD CONSTRAINT `i` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `item1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`),
  ADD CONSTRAINT `order1` FOREIGN KEY (`oid`) REFERENCES `order_details` (`Oid`);

--
-- Constraints for table `reviews_rating`
--
ALTER TABLE `reviews_rating`
  ADD CONSTRAINT `customer2` FOREIGN KEY (`cid`) REFERENCES `customers` (`Cid`),
  ADD CONSTRAINT `vendor2` FOREIGN KEY (`vid`) REFERENCES `vendor` (`Vid`);

--
-- Constraints for table `Stock`
--
ALTER TABLE `Stock`
  ADD CONSTRAINT `item2` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`),
  ADD CONSTRAINT `vendor` FOREIGN KEY (`Vid`) REFERENCES `vendor` (`Vid`);

--
-- Constraints for table `user_verification`
--
ALTER TABLE `user_verification`
  ADD CONSTRAINT `user4` FOREIGN KEY (`uid`) REFERENCES `users` (`Uid`);

--
-- Constraints for table `vendor`
--
ALTER TABLE `vendor`
  ADD CONSTRAINT `user2` FOREIGN KEY (`Vid`) REFERENCES `users` (`Uid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;