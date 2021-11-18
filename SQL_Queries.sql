-- SQLite
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
-- Find the 5 movies that have been added the most recently. (Kinda goes go but whatever)
-- Find the country that has the most tv shows. 
-- Find the title of tv shows that were frfom Germeny, America and Canada.
-- Find the title of movies released in between the year 2020 and 2021.
SELECT s_title
FROM Movies
 inner join Release
    WHERE re_release between '2020' and '2021'
;

-- Find all titles released before 1995. 
SELECT s_title
FROM Movies
 inner join Release
    WHERE re_release < '1995'
    ;

-- Find all titles that have "" included in the cast.
-- Insert all movies directed by "" into like list
INSERT INTO LikeList (m_name)
SELECT m_name
FROM Netflix
WHERE n_director = ""
;
-- Update Dislike with all movie titles from the Action genre

-- Delete movies releaced after 2019 from dislike list 
DELETE FROM Dislike
WHERE m_title IN(
    SELECT m_title 
    FROM Release
    WHERE re_release < '2019')
;



