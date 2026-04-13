# W3 - SQL Advanced (JOINs)

## Description
This task demonstrates:
- Creating multiple related tables
- Using foreign keys
- Inserting data
- Querying data using multiple JOINs

## Tables
- locations (location_id, location_name, building)
- equipment (equipment_id, name, type, location_id)
- user_roles (role_id, role_name)
- users (user_id, username, email, role_id)
- measurements (measurement_id, equipment_id, value, timestamp)
- maintenance (maintenance_id, equipment_id, description, date)
- reservations (reservation_id, user_id, equipment_id, reservation_date)

## Relationships
- equipment.location_id → locations.location_id
- users.role_id → user_roles.role_id
- measurements.equipment_id → equipment.equipment_id
- maintenance.equipment_id → equipment.equipment_id
- reservations.user_id → users.user_id
- reservations.equipment_id → equipment.equipment_id

## SQL Features Used
- CREATE TABLE
- INSERT INTO
- FOREIGN KEY
- SELECT with multiple INNER JOINs