drop schema IF EXISTS dbms_projectphase2;
create schema dbms_projectphase2;
use dbms_projectphase2;


CREATE TABLE IF NOT EXISTS Hall (
    hall_id VARCHAR(25),
    capacity VARCHAR(10),
    availability_label VARCHAR(5),
    location VARCHAR(10),
    name_hall VARCHAR(120),
    PRIMARY KEY (hall_id)
);

DELIMITER $$

DROP TRIGGER IF EXISTS dbms_projectphase2.hall_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `dbms_projectphase2`.`hall_BEFORE_INSERT` BEFORE INSERT ON `hall` FOR EACH ROW
BEGIN
IF NEW.capacity = 0 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input ';
          END IF;


END$$
DELIMITER ;



CREATE TABLE IF NOT EXISTS Auditorium (
    hall_id VARCHAR(25) NOT NULL,
    stage_size VARCHAR(25),
    green_rooms INT(5),
    CONSTRAINT FOREIGN KEY (hall_id)
        REFERENCES hall (hall_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.auditorium_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`auditorium_BEFORE_INSERT` BEFORE INSERT ON `auditorium` FOR EACH ROW
BEGIN
IF NEW.stage_size <= '0' or NEW.green_rooms <= 0
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input ';
          END IF;
 
 
END$$
DELIMITER ;



CREATE TABLE IF NOT EXISTS Screen (
    hall_id VARCHAR(25) NOT NULL,
    size VARCHAR(25),
    screen_type VARCHAR(20),
    experience VARCHAR(10),
    CONSTRAINT FOREIGN KEY (hall_id)
        REFERENCES hall (hall_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

DELIMITER $$

DROP TRIGGER IF EXISTS dbms_projectphase2.screen_AFTER_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`screen_AFTER_INSERT` AFTER INSERT ON `screen` FOR EACH ROW
BEGIN
IF size = '0' 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input ';
          END IF;
END$$
DELIMITER ;



USE `dbms_projectphase2`;

DELIMITER $$

DROP TRIGGER IF EXISTS dbms_projectphase2.hall_AFTER_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`hall_AFTER_INSERT` AFTER INSERT ON `hall` FOR EACH ROW
BEGIN
DECLARE HALLcount INT;
DECLARE SCREENcount INT;
set HALLcount = (select COUNT(HALL_ID) from HALL );
SET SCREENcount = (select COUNT(HALL_ID) from SCREEN );
IF SCREENcount > HALLcount
		THEN
			SIGNAL SQLSTATE '45000'
				  SET MESSAGE_TEXT = 'Cannot add or update row: invalid input ';
    END IF;
END$$
DELIMITER ;

CREATE TABLE IF NOT EXISTS shows (
    show_id VARCHAR(25),
    show_name VARCHAR(100),
    PRIMARY KEY (show_id)
);

USE `dbms_projectphase2`;
 
DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.shows_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `dbms_projectphase2`.`shows_BEFORE_INSERT` BEFORE INSERT ON `shows` FOR EACH ROW
BEGIN
IF NEW.show_name = '0' 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input ';
          END IF;
 
END$$
DELIMITER ;

CREATE TABLE IF NOT EXISTS reservation (
    r_id VARCHAR(25),
    r_date DATE,
    r_time TIME,
    hall_id VARCHAR(25),
    show_id VARCHAR(25),
    PRIMARY KEY (r_id),
    CONSTRAINT FOREIGN KEY (hall_id)
        REFERENCES hall (hall_id)
        ON DELETE SET NULL,
    CONSTRAINT FOREIGN KEY (show_id)
        REFERENCES shows (show_id)
        ON DELETE NO ACTION ON UPDATE NO ACTION
);


DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.reservation_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`reservation_BEFORE_INSERT` BEFORE INSERT ON `reservation` FOR EACH ROW
BEGIN
IF NEW.r_date = 0 or NEW.r_time= 0 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input';
  END IF;
 
END$$
DELIMITER ;


CREATE TABLE IF NOT EXISTS movie (
    show_id VARCHAR(25),
    release_date INT(10),
    movie_cast VARCHAR(60),
    director VARCHAR(40),
    rating VARCHAR(25),
    CONSTRAINT FOREIGN KEY (show_id)
        REFERENCES shows (show_id)
);



DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.movie_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`movie_BEFORE_INSERT` BEFORE INSERT ON `movie` FOR EACH ROW
BEGIN
IF NEW.rating <= '0' 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input ';
          END IF;
 
 
END$$
DELIMITER ;



CREATE TABLE IF NOT EXISTS performance (
    show_id VARCHAR(25),
    performers VARCHAR(50),
    performance_type VARCHAR(25),
    CONSTRAINT FOREIGN KEY (show_id)
        REFERENCES shows (show_id)
);
USE `dbms_projectphase2`;
 
DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.performance_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`performance_BEFORE_INSERT` BEFORE INSERT ON `performance` FOR EACH ROW
BEGIN
IF NEW.performers = '0' 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input';
  END IF;
 
 
END$$
DELIMITER ;


CREATE TABLE IF NOT EXISTS eventTable (
    e_id VARCHAR(25),
    show_id VARCHAR(25) NOT NULL,
    time_event TIME,
    date_event DATE,
    ticket_price VARCHAR(10),
    PRIMARY KEY (e_id),
    CONSTRAINT FOREIGN KEY (show_id)
        REFERENCES shows (show_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
USE `dbms_projectphase2`;
 
DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.eventTable_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`eventTable_BEFORE_INSERT` BEFORE INSERT ON `eventTable` FOR EACH ROW
BEGIN
IF NEW.ticket_price <= '0' 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input';
  END IF;
 
 
END$$
DELIMITER ;
DELIMITER $$

DROP TRIGGER IF EXISTS dbms_projectphase2.eventtable_AFTER_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`eventtable_AFTER_INSERT` AFTER INSERT ON `eventtable` FOR EACH ROW
BEGIN
	IF date_event < reservation.r_date
		THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input';
	END IF;
END$$
DELIMITER ;

CREATE TABLE IF NOT EXISTS customer (
    customer_id VARCHAR(15),
    customer_name VARCHAR(25),
    phone_no VARCHAR(25),
    email_id VARCHAR(70),
    payment_details VARCHAR(25),
    PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS booking (
    booking_id VARCHAR(25),
    e_id VARCHAR(25) NOT NULL,
    customer_id VARCHAR(25) NOT NULL,
    num_tickets INT(3),
    price INT(10),
    booking_date DATE,
    booking_time TIME,
    booking_lable VARCHAR(10),
    PRIMARY KEY (booking_id),
    CONSTRAINT FOREIGN KEY (e_id)
        REFERENCES eventTable (e_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FOREIGN KEY (customer_id)
        REFERENCES customer (customer_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
USE `dbms_projectphase2`;
 
DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.booking_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`booking_BEFORE_INSERT` BEFORE INSERT ON `booking` FOR EACH ROW
BEGIN
IF NEW.num_tickets <= 0 or new.price = 0 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input';
  END IF;
 
 
END$$
DELIMITER ;
CREATE TABLE IF NOT EXISTS customer (
    customer_id VARCHAR(15),
    customer_name VARCHAR(25),
    phone_no VARCHAR(25),
    email_id VARCHAR(70),
    payment_details VARCHAR(25),
    PRIMARY KEY (customer_id)
);
USE `dbms_projectphase2`;
 
DELIMITER $$
 
DROP TRIGGER IF EXISTS dbms_projectphase2.customer_BEFORE_INSERT$$
USE `dbms_projectphase2`$$
CREATE DEFINER = CURRENT_USER TRIGGER `dbms_projectphase2`.`customer_BEFORE_INSERT` BEFORE INSERT ON `customer` FOR EACH ROW
BEGIN
IF NEW.phone_no = '0' 
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot add or update row: invalid input';
  END IF;
 
 
END$$
DELIMITER ;