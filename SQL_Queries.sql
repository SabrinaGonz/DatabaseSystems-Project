-- SQLite
-- Database Systems Project 
-- SQL Quieries and Data Modification Statements
-- Sabrina Gonzalez & Jude Orsua 
-- needs diversity in format and complexity


-- 1. Find shows that were released after the year 2019.
SELECT s_title
FROM Shows
 inner join Release
    WHERE re_release > '2019'
;

-- 2. Find all movies in the Comedy genre from India 
SELECT s_title
FROM Movies
 inner join Genre
 inner join Netflix
    WHERE g_genre = 'comedy' AND n_country = "India"
;

-- 3. Find the title of tv shows that were from Germeny, America and Canada.
SELECT s_title
FROM Movies
 inner join Genre
 inner join Netflix
    WHERE g_genre = 'comedy' AND n_country = "India" 

-- 4. Find the title of movies released in between the year 2020 and 2021.
SELECT s_title
FROM Movies
 inner join Release
    WHERE re_release between '2020' and '2021'
;

-- 5. Find all show titles released before 1995. 
SELECT s_title
FROM Movies
 inner join Release
    WHERE re_release < '1995'
    ;

-- 6. Find all movie titles that have Joey King included in the cast.
SELECT n_title
FROM Netflix
WHERE n_cast = 'Joey King'
;

-- 7. Insert all movies directed by Dennis Dugan into like list
INSERT INTO LikeList (m_name)
SELECT m_name
FROM Netflix
WHERE n_director = "Dennis Dugan"
;

-- 8. Insert all movie titles from the Horror genre into the Dislike list
INSERT INTO Dislike (m_name)
SELECT m_name
FROM Netflix
WHERE g_genre = "Horror"
;


-- 9. Delete movies added after 2019 from dislike list 
DELETE FROM Dislike
WHERE m_title IN(
    SELECT m_title 
    FROM Release
    WHERE re_release < '2019')
;


-- 10. Delete from the like list all shows more than 3 seasons that are rated TV-MA 
DELETE FROM Dislike
WHERE ra_rating IS 'TV-MA' 
AND  s_title IN (
    SELECT s_title 
    FROM Netflix
    WHERE n_duration < '3 seasons'
;

-- 11. For every movie added between 1930 and 1940, inclusive, find the number of titles that are Dramas. Print the title name and the number of movies added.
SELECT m_name, count(re_added)
FROM Movies 
    inner join Release
    WHERE re_added BETWEEN '1930' AND '1940'
    group by m_name
;

-- 12. Find the genre with the smallest number of shows.

SELECT g_genre
FROM (SELECT g_genre, COUNT(DISTINCT s_sid) AS cus
      FROM Genre, Shows
      WHERE g_sid = g_sid
      GROUP BY g_genre) AS C
WHERE cus IN (SELECT MIN(cus)
              FROM (SELECT g_genre, COUNT(DISTINCT c_custkey) AS cus
                  FROM Genre, Shows
                  WHERE g_sid = g_sid
                  GROUP BY g_genre) AS N) 
