/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.1.32-community : Database - unique id
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`unique id` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `unique id`;

/*Table structure for table `cipher_text` */

DROP TABLE IF EXISTS `cipher_text`;

CREATE TABLE `cipher_text` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `emsg` text,
  `prvtkey` text,
  `pubkey` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `cipher_text` */

insert  into `cipher_text`(`id`,`uid`,`emsg`,`prvtkey`,`pubkey`) values 
(1,51,'IiakKsoHl/OHfzIMJxmdeADfKTDk2wYLOjkSQbgSkFJ5miSDyJdSSCo/BfkMocJvUecDWUhAZOc5OGMDmbJLMfuzZCw4qrwgqfwwQ+t8eqpxGtS0MmP3BawhKA51osqV1kiIVCxiK1dx0CExrogj31le1s63b7UOZulPR1KfTp8=','-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC0GUoKN2+R+T3ZFNMPvfZXHXiZ\neY0HWzutVRWIN8DStu0uEyqU0Ozah7aJkeRSV6iKgGiTcyQiCVpsmo/5xFcOt3Ou\nNOFp68TLulvpWgnv4kLCEUldfkoqf4VGcbV+Mi41EcqFITTW/ELxXhOkxhHTNNcq\n/youN3pp8d6lD0p65wIDAQAB\n-----END PUBLIC KEY-----','-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC0GUoKN2+R+T3ZFNMPvfZXHXiZeY0HWzutVRWIN8DStu0uEyqU\n0Ozah7aJkeRSV6iKgGiTcyQiCVpsmo/5xFcOt3OuNOFp68TLulvpWgnv4kLCEUld\nfkoqf4VGcbV+Mi41EcqFITTW/ELxXhOkxhHTNNcq/youN3pp8d6lD0p65wIDAQAB\nAoGAJ9z5IG3IyjyqzePoG7HmVr31NbNL3fb5rJIKpA4DJiDLOsmPQUVFR9GGO8kJ\nCpjQe2eUvh5cPxRm6WcEuzoUMpRLryNtpQBr9yY93RLUrnIFKjgCUjKicuBBX7qD\nKDKEW9Ppjcgqdra98NTNIpV4YDYT8PUQCOxlyssXghH/7yECQQDE8p9HDOt87gF5\n8MFzeRLyiziVRwsXdDCseF28yDYeo+y2wktJ0vWpumHeX+DdN2P3hQ717rarc0d2\nxaC2SupZAkEA6hlekmZ4LzgSmq/sjmbEmvGGE0bu4tqJpGKScirBE2yp1m/cEMTV\neh+rTH0aX5tCwkbwEz0gSczpNy7zTvlnPwJABOLoJMEjTpQxIS9h/VVxrObbXojG\ns6xEUOMjoD1vak8y3k3vxEMhqTZgmz3RvGtVZZy9hEiJ67MOgNniZONy8QJBAMmH\ni43XHxHvYLzARJKW0BxfXkAMKa0r26Cjp1UXj13Mhy1u4PGisfDPgKV5cZHq1H7x\nmM3HKpu+BuuVxKoxNPsCQQCZNQ6Xs/dIGHZA0jUxWvimWh9+kdCyHN9JkNHpLXzN\nAKRmELN53YU+QVCeuYeO7hfqSPZ0hCGVPt77eLiCbK+g\n-----END RSA PRIVATE KEY-----'),
(2,36,'Q0Boytp5CBynXp6OWQkgubmdqC+pxtJyiBPS8ikgB0LHdpxamWBxQF1J6K6mYqyglGuvUHa1BY1WiZXwCQseCYMysbzjZpiKJUbh/tFACF0E4A9YfghKUx85Q01C9lTB6aOKU8zKEOhtWkBjyS65LE8Wo6YFa5wSW/Vr0xu6Jso=','-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCspuvWKwCrCGe7Ft8iqWSunG3J\n6+4zjP+Ff9j0BZJmRo88mVHXDYQJwWvdNu0nIm7PlMZ2DmYCoGhS5SwmIpHXxK51\n1UTEhGglJzgY1tPJUkF+m2WCxC7CwaiLwIH4S9JtWWpryxAprK/AQmIWHwIpM7nM\nPiNMd16BRlthRyttGwIDAQAB\n-----END PUBLIC KEY-----','-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCspuvWKwCrCGe7Ft8iqWSunG3J6+4zjP+Ff9j0BZJmRo88mVHX\nDYQJwWvdNu0nIm7PlMZ2DmYCoGhS5SwmIpHXxK511UTEhGglJzgY1tPJUkF+m2WC\nxC7CwaiLwIH4S9JtWWpryxAprK/AQmIWHwIpM7nMPiNMd16BRlthRyttGwIDAQAB\nAoGBAIIxbW4XB23x7Kb8XE87BZ1WgMPfkcR18sms2uFIwlk1pBXCWCCfJI5muPwb\ny0HTiVQnkHC98tbQN1srTduD/g1Exfsb6k6Q3R8zTZ+l6IGGMbEwQv/9SZDxx+Im\nhMzVKPjnqlcK03sV/zcfrjRtfaSxVdrV3i08sxTVYEI6qq9hAkEAvsg1KxhANDSS\nkCVPoJboL5OnZEBypB8CoHaQk169LZcokkgG4GQHleuAwnp1bOsCMLEMXy7ABx3g\nnYsddfBuxwJBAOesHKSXwKe/H7baqPPj81r69w1vCIpEGWrE2O8Qm1ADYArk0eui\nGDfoQRSBGlNjPzfw1lqb7qimz/t7asbyyw0CQBm43JJG3sErJWeR4D6CmiNwAO2f\nUtWV6MDBu5Ri/Zab/rhaRbMTSYKJEf8mi5Z3yP/Pnx9mKjXLbXFQRFSWahkCQCky\nW+2Q5rttqzAS9hRYpr+4/RGweu5LadGoq4LnixbRYtTNF9809eWLMXd59bp6XZWP\nCC8Yp3nqH/XyXmx+ZEkCQEb5P9UzlTNpRjUWPgDczjb/LVo2cs9bK7qePhRWWFqP\neyCUuZx6KjcPoi0jRGY8kk46Ln5xR8aZ1f2l+sbIlxI=\n-----END RSA PRIVATE KEY-----'),
(3,53,'XseaD2FBuPsTBBq5/9vAOSkz6YqXQUIjl1Pe1wDNOwvYRmR90nRD36S+RgWNApd6NOjntAkpi2GHroiPAB9lHWAVr/g7grZauljKl1ZqEdVJXggaCoYG2USzmMeMwmG19Mi7GsZKfUxHKjXrct+YcCs8LuoypwZzg/OsWMxMu2M=','-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8SsFWI+FsO52XtixQ22ttg6Yt\nL23QVIlZwP6wP/8KIMfOXemICJ2+SzccMSyfqKMDmN0577QSm5cc6X3dQGKeBCcM\nwvLpVgY5sa9GzStzsoTesjVTeuBgIJZX357E6NzN9uKKHo3ou4U82FTzExKanaw5\nYFmWoPehnshNDQtAAwIDAQAB\n-----END PUBLIC KEY-----','-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC8SsFWI+FsO52XtixQ22ttg6YtL23QVIlZwP6wP/8KIMfOXemI\nCJ2+SzccMSyfqKMDmN0577QSm5cc6X3dQGKeBCcMwvLpVgY5sa9GzStzsoTesjVT\neuBgIJZX357E6NzN9uKKHo3ou4U82FTzExKanaw5YFmWoPehnshNDQtAAwIDAQAB\nAoGBAKxo4vkmJ548REQLei6bi5Weq0XKnQnarl2x20O1halXdL0gvtph0VbSdmbp\nHAwhlQqRKViIhWFYeJjvr+EsuF6WVyW4yx6gT01G6aNlLEk+F0VjP0Of/S2kETv5\nSUf/fwAUeZf/A7o3b7/iOqAjWMQkWkr5oPpUwgsyPXtthCoZAkEAx5kUknzGtbTr\nB8Vju3qv5/cINo19aVtK2J28nqcEq4hOGfjCLW7XBvwxQE2aIinXNV2HIh0YDs0T\nSMztJ4G75QJBAPF/zT9rOJGgLwEvIKd+TfHkpkDd8nDRyJo/CdO0iMGu/gL3sd3q\nuVnQbE8dqVSGj8IWnjFwPLrwdzionF8wXccCQASFBt46TRWYPyox4gxAvvL1uQ3j\nLk/QbWVyTO8awRRRRdN4uozk0aGq3EKkfzT+1YyzzXeMSRsssZ8YZNZcLbECQChf\nQSS0/AP8T19XTZIynz0tCE4XzIvnxi1jFHV73NDkPDqqxeVfdBT7rt+bCc/DnwzH\nUzLYnI5z3LpwFZQkNckCQGXMd7ZQs6ofQiDS8RITkWty+3w16roKK1PbaEvAtYXq\nkkf0/Fjcyb2ZBsbJSe1dJ6MLq11A3K5eXKCi4B0wCto=\n-----END RSA PRIVATE KEY-----');

/*Table structure for table `college` */

DROP TABLE IF EXISTS `college`;

CREATE TABLE `college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_name` varchar(100) DEFAULT NULL,
  `register_number` varchar(15) DEFAULT NULL,
  `place` varchar(15) DEFAULT NULL,
  `district` varchar(15) DEFAULT NULL,
  `post` varchar(15) DEFAULT NULL,
  `pincode` bigint(10) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `phone` bigint(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

/*Data for the table `college` */

insert  into `college`(`id`,`college_name`,`register_number`,`place`,`district`,`post`,`pincode`,`email`,`phone`) values 
(7,'college1','rar2345','kkl','dsfs','ewee',6855542,'adfajfadjkjhj@jd',98984848),
(8,'college','saddas','asda','ads','sda',1323,'peekay@college.com',9947917837),
(37,'Peekay ','99905','Mathara','kozhikode','GP COLLEGE',673003,'peekay@college.com',9947917837),
(39,'Farook college','99906','farooke','kozhikode','ferook',872003,'farook@college.com',9947917837);

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(10) DEFAULT NULL,
  `duration` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`id`,`course`,`duration`) values 
(1,'BCA','3 YEAR'),
(3,'BBA','3 YEAR'),
(5,'BSC CS','3 YEAR');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(25) DEFAULT NULL,
  `exam_details` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`id`,`title`,`exam_details`,`date`) values 
(8,'BBA','WIN_20191117_14_45_02_Pro.jpg','2019-11-28');

/*Table structure for table `external` */

DROP TABLE IF EXISTS `external`;

CREATE TABLE `external` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `register_number` varchar(50) DEFAULT NULL,
  `gpa` double DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `external` */

insert  into `external`(`id`,`register_number`,`gpa`,`file`) values 
(4,'RARRBMS1',5,''),
(5,'rrrass',10,'1fbf3cd2-6a08-497f-bb2a-e457da47f106.jpg'),
(6,'RRARBCA030',8,'1BF93516-54ED-484E-993B-97D705D7C40D.jpg'),
(7,'12345',10,'dbotica_navigation_drawer_2x.jpg'),
(8,'123456',2,'dbotica_navigation_drawer_2x.jpg'),
(9,'122363',8,'WIN_20191117_14_45_02_Pro.jpg'),
(10,'335522',10,'APPHOME.JPG');

/*Table structure for table `internal_marks` */

DROP TABLE IF EXISTS `internal_marks`;

CREATE TABLE `internal_marks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `register_number` varchar(15) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `mark` float DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `sem` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `internal_marks` */

insert  into `internal_marks`(`id`,`register_number`,`subject_id`,`mark`,`course_id`,`sem`) values 
(13,'121',6,20,1,2),
(14,'111111111',7,100,1,3),
(15,'RRARBCA029',9,1,3,2),
(16,'1213564',7,100,1,3),
(17,'212323',8,10,4,3),
(18,'12344',7,50,1,3),
(19,'RRARBCA030',10,74,1,1),
(20,'RRARBCA030',11,65,1,1),
(21,'RRARBCA030',12,55,1,1),
(22,'RRARBCA030',13,78,1,1),
(23,'1213564',10,10,1,1),
(24,'12345',10,100,1,1),
(25,'123456',10,100,1,1),
(26,'123456',11,25,1,1),
(27,'123456',12,45,1,1),
(28,'123456',13,56,1,1),
(29,'12345',13,100,1,1),
(30,'335522',7,10,1,3),
(31,'335522',10,70,1,3),
(32,'335522',11,80,1,3),
(33,'335522',12,20,1,3);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin123','admin'),
(3,'pkb','pkb123','pareekshabhavan'),
(7,'college1','college123','college'),
(8,'college','college12','college'),
(14,'qqq','12','student'),
(15,'eeeee','111111111','rejected'),
(16,'ruseelrockzz@gmail.com','RRARBCA029','student'),
(18,'hello@gmail.com','RRAR321B3','rejected'),
(19,'labeebshanavas@gmail.com','12344','rejected'),
(20,'labeebshanavas@gmail.com','12344','rejected'),
(21,'labeebshanavas@gmail.com','12344','rejected'),
(22,'labeebshanavas@gmail.com','12344','pending'),
(23,'labeebshanavas@gmail.com','212323','pending'),
(24,'student','12','student'),
(29,'gggg','Gghhhh','pending'),
(30,'22','12','student'),
(31,'user','111111','student'),
(32,'ajajs','223344','pending'),
(33,'shyamjith975@gmail.com','7842286','pending'),
(36,'user1','123457','student'),
(37,'peekay','Peekay123','college'),
(39,'farook','farook123','college'),
(40,'vahab@gmail.com','882233','pending'),
(41,'labeebshanavas@gmail.com','552871','pending'),
(42,'russel@gmail.com','122363','pending'),
(43,'labeebshanavas@gmail.com','005273','pending'),
(44,'labeebshanavas@gmail.com','563832','pending'),
(45,'labeebshanavas@gmail.com','112233','student'),
(46,'user3','224477','student'),
(47,'user4','123456','student'),
(50,'labeebshanavas@gmail.com','22334','pending'),
(52,'vaishnavsudheer@gmail.com','223344','pending'),
(53,'vaishnabbvsudheer@gmail.com','556677','pending');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `register_number` varchar(15) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `score` varchar(100) DEFAULT NULL,
  `year_of_pass` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `email_id` varchar(100) DEFAULT NULL,
  `phone_no` varchar(100) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `college` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`id`,`name`,`register_number`,`course_id`,`gender`,`score`,`year_of_pass`,`image`,`email_id`,`phone_no`,`login_id`,`college`) values 
(1,'Fuhad','12345',1,'Male','FIRST CLASS','jun,2010','IMG_20200207_140156.jpg','sjjdjdjs','465+5+5',30,NULL),
(2,'labeeb','123456',1,'Male','FIRST CLASS','august,2007','IMG_3676.jpeg','user','9947911837',31,NULL),
(3,'vahab','223344',1,'Male','DISTINCTION','jan,2004','0C855737-1DA5-4DC7-8819-E2857801EAC8L0001.jpeg','ajajs','49949',32,NULL),
(4,'Russel','7842286',3,'Male','SECOND CLASS','may,2008','IMG_20200208_011811.jpg','shyamjith975@gmail.com','9947917837',33,NULL),
(5,'Rahul','5558064',1,'Male','DISTINCTION','jan,2004','1.jpg','sghggf@gma.com','1254689523',36,'rar2345'),
(6,'Vahab','882233',1,'Male','SECOND CLASS','mar,2006','photo-1542080681-b52d382432af.webp','vahab@gmail.com','8581813578',40,'99905'),
(7,'Akshay','552871',1,'Male','DISTINCTION','mar,2011','photo-1542080681-b52d382432af.webp','labeebshanavas@gmail.com','9947917837',41,'99906'),
(8,'russel','122363',1,'Male','SECOND CLASS','may,2012','photo-1542080681-b52d382432af.webp','russel@gmail.com','9947917837',42,'99906'),
(9,'shyam','005273',1,'Male','DISTINCTION','apr,2008','photo-1542080681-b52d382432af.webp','labeebshanavas@gmail.com','9947917867',43,'99905'),
(10,'labeeb','563832',1,'Male','DISTINCTION','may,2007','photo-1542080681-b52d382432af.webp','labeebshanavas@gmail.com','9947917837',44,'99906'),
(11,'sravan','112233',1,'Male','PASS CLASS','jan,2004','IMG_20200209_145525_926.jpg','labeebshanavas@gmail.com','9947917837',45,'99905'),
(12,'Shyam','224477',1,'Male','FIRST CLASS','jun,2011','IMG_20190501_152219.jpg','shyamjith975@gmail.com','9977917837',46,'99905'),
(13,'Shahid','1223445',1,'Male','DISTINCTION','mar,2017','IMG_20200210_120455.jpg','mohmdshahid@gmail.com','9947891437',47,'99905'),
(16,'fuhadd','22334',1,'Male','DISTINCTION','may,2008','IMG_20200210_120455.jpg','labeebshanavas@gmail.com','9794994498',50,'99905'),
(17,'rahul','335522',1,'Male','DISTINCTION','jan,2004','photo-1542080681-b52d382432af.webp','labeebshanavas@gmail.com','9947917837',51,'99905'),
(18,'mohmdlabeeb','223344',1,'Male','FIRST CLASS','july,2004','IMG_20200125_111000.jpg','vaishnavsudheer@gmail.com','9947917837',52,'99905'),
(19,'sujith','556677',1,'Female','DISTINCTION','jan,2004','images.jpeg','vaishnabbvsudheer@gmail.com','9947563125',53,'99905');

/*Table structure for table `studsem` */

DROP TABLE IF EXISTS `studsem`;

CREATE TABLE `studsem` (
  `lid` int(11) DEFAULT NULL,
  `sem` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `studsem` */

insert  into `studsem`(`lid`,`sem`) values 
(36,3),
(40,3),
(41,3),
(42,3),
(43,3),
(44,3),
(45,3),
(46,5),
(47,3),
(50,3),
(51,2),
(52,3),
(53,3);

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(15) DEFAULT NULL,
  `sem` varchar(10) DEFAULT NULL,
  `subject` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`id`,`course_id`,`sem`,`subject`) values 
(6,3,'3','SE'),
(7,1,'3','PHP'),
(8,4,'3','JAVA'),
(9,3,'2','E COMMERCE'),
(10,1,'3','JAVA'),
(11,1,'3','ANDROID'),
(12,1,'3','OS'),
(13,1,'1','SYSTEM SOFTWARE'),
(14,3,'2','English');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
