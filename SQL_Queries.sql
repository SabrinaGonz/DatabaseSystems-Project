- SQLite
-- Database Systems Project 
-- SQL Quieries and Data Modification Statements
-- Sabrina Gonzalez & Jude Orsua 


-- needs diversity in format and complexity


-- Find shows that were released after the year 2019.
SELECT s_title
FROM Shows
 inner join Release
    WHERE re_release > '2019'
;

-- Find all movies in the Comedy genre from India 
SELECT s_title
FROM Movies
 inner join Genre
 inner join Netflix
    WHERE g_genre = 'comedy' AND n_country = "India"
;

-- Find all tv shows in the 
-- Find the 5 movies that have been added the most recently. 
-- Find the country that has the most tv shows. 

-- Find the title of tv shows that were from Germeny, America and Canada.
SELECT s_title
FROM Movies
 inner join Genre
 inner join Netflix
    WHERE g_genre = 'comedy' AND n_country = "India" 

-- Find the title of movies released in between the year 2020 and 2021.
SELECT s_title
FROM Movies
 inner join Release
    WHERE re_release between '2020' and '2021'
;

-- Find all show titles released before 1995. 
SELECT s_title
FROM Movies
 inner join Release
    WHERE re_release < '1995'
    ;

-- Find all movie titles that have Joey King included in the cast.
SELECT n_title
FROM Netflix
WHERE n_cast = 'Joey King'
;

-- Insert all movies directed by Dennis Dugan into like list
INSERT INTO LikeList (m_name)
SELECT m_name
FROM Netflix
WHERE n_director = "Dennis Dugan"
;

-- Insert all movie titles from the Horror genre into the Dislike list
INSERT INTO Dislike (m_name)
SELECT m_name
FROM Netflix
WHERE g_genre = "Horror"
;


-- Delete movies releaced after 2019 from dislike list 
DELETE FROM Dislike
WHERE m_title IN(
    SELECT m_title 
    FROM Release
    WHERE re_release < '2019')
;



