-- Drop tables if they already exist
DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS maintenance;
DROP TABLE IF EXISTS measurements;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS locations;
-- Create locations table
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_name TEXT NOT NULL,
    building TEXT NOT NULL
);

-- Create equipment table
CREATE TABLE equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    location_id INTEGER NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);
-- Create user_roles table
CREATE TABLE user_roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT NOT NULL
);

-- Create users table
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES user_roles(role_id)
);
-- Create measurements table
CREATE TABLE measurements (
    measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    value REAL NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Create maintenance table
CREATE TABLE maintenance (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);
-- Create reservations table
CREATE TABLE reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    equipment_id INTEGER NOT NULL,
    reservation_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);
-- Insert locations
INSERT INTO locations (location_name, building) VALUES ('Lab A', 'Building 1');
INSERT INTO locations (location_name, building) VALUES ('Lab B', 'Building 2');

-- Insert equipment
INSERT INTO equipment (name, type, location_id) VALUES ('Temperature Sensor', 'Sensor', 1);
INSERT INTO equipment (name, type, location_id) VALUES ('Pressure Sensor', 'Sensor', 2);

-- Insert roles
INSERT INTO user_roles (role_name) VALUES ('Admin');
INSERT INTO user_roles (role_name) VALUES ('User');

-- Insert users
INSERT INTO users (username, email, role_id) VALUES ('john_doe', 'john@email.com', 1);
INSERT INTO users (username, email, role_id) VALUES ('jane_doe', 'jane@email.com', 2);

-- Insert measurements
INSERT INTO measurements (equipment_id, value, timestamp) VALUES (1, 25.5, '2025-02-12 10:00');
INSERT INTO measurements (equipment_id, value, timestamp) VALUES (2, 101.3, '2025-02-12 11:00');

-- Insert maintenance
INSERT INTO maintenance (equipment_id, description, date) VALUES (1, 'Battery replaced', '2025-02-10');
INSERT INTO maintenance (equipment_id, description, date) VALUES (2, 'Calibration done', '2025-02-11');

-- Insert reservations
INSERT INTO reservations (user_id, equipment_id, reservation_date) VALUES (1, 1, '2025-02-15');
INSERT INTO reservations (user_id, equipment_id, reservation_date) VALUES (2, 2, '2025-02-16');
-- Select equipment with location, user, and reservation info
SELECT 
    equipment.name AS equipment_name,
    equipment.type,
    locations.location_name,
    locations.building,
    users.username,
    user_roles.role_name,
    reservations.reservation_date
FROM reservations
INNER JOIN users 
    ON reservations.user_id = users.user_id
INNER JOIN user_roles 
    ON users.role_id = user_roles.role_id
INNER JOIN equipment 
    ON reservations.equipment_id = equipment.equipment_id
INNER JOIN locations 
    ON equipment.location_id = locations.location_id;