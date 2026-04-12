# W2 - Books and Authors

## Description
This task demonstrates:
- Creating two tables
- Linking them with a foreign key
- Inserting data
- Querying data using JOIN

## Tables
- authors (author_id, author_name, country)
- books (book_id, title, genre, author_id)

## Relationship
- One author can have many books
- books.author_id → authors.author_id

## SQL Features Used
- CREATE TABLE
- INSERT INTO
- SELECT with INNER JOIN