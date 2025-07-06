CREATE DATABASE IF NOT EXISTS airline_db;

USE airline_db;

CREATE TABLE
    IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        role ENUM ('user', 'admin') DEFAULT 'user'
    );

CREATE TABLE
    IF NOT EXISTS flights (
        flight_id VARCHAR(10) PRIMARY KEY,
        source VARCHAR(50) NOT NULL,
        destination VARCHAR(50) NOT NULL,
        seats INT NOT NULL,
        booked_seats INT DEFAULT 0,
        date DATE NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        status ENUM ('Scheduled', 'Delayed', 'Cancelled') DEFAULT 'Scheduled'
    );

CREATE TABLE IF NOT EXISTS reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    flight_id VARCHAR(10) NOT NULL,
    seat_number VARCHAR(10),
    booking_date DATE DEFAULT(CURRENT_DATE),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (flight_id) REFERENCES flights (flight_id) ON DELETE CASCADE
);
