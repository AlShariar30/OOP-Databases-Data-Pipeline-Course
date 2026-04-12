-- Drop tables if they already exist
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- Create authors table
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL,
    country TEXT NOT NULL
);

-- Create books table
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Insert authors
INSERT INTO authors (author_name, country) VALUES ('J.K. Rowling', 'United Kingdom');
INSERT INTO authors (author_name, country) VALUES ('George Orwell', 'United Kingdom');
INSERT INTO authors (author_name, country) VALUES ('Paulo Coelho', 'Brazil');

-- Insert books
INSERT INTO books (title, genre, author_id) VALUES ('Harry Potter and the Philosopher''s Stone', 'Fantasy', 1);
INSERT INTO books (title, genre, author_id) VALUES ('1984', 'Dystopian', 2);
INSERT INTO books (title, genre, author_id) VALUES ('Animal Farm', 'Political Satire', 2);
INSERT INTO books (title, genre, author_id) VALUES ('The Alchemist', 'Adventure', 3);

-- Select query to show books with their authors
SELECT
    books.book_id,
    books.title,
    books.genre,
    authors.author_name,
    authors.country
FROM books
INNER JOIN authors
    ON books.author_id = authors.author_id;