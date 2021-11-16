-- SQLite
-- Database Systems Project 
-- SQL Quieries and Data Modification Statements
-- Sabrina Gonzalez & Jude Orsua 


-- Find shows that were released after the year 2019.
SELECT s_title
FROM (SELECT n_name, COUNT(DISTINCT c_custkey) AS cus
      FROM nation, customer
      WHERE n_nationkey = c_nationkey
      GROUP BY n_name) AS C
WHERE cus IN (SELECT MIN(cus)
              FROM (SELECT n_name, COUNT(DISTINCT c_custkey) AS cus
                  FROM customer, nation
                  WHERE n_nationkey = c_nationkey
                  GROUP BY n_name) AS N)

-- Find all moves in the Comedy genre from India 
-- Find all tv shows in the 
-- Find the 5 movies that have been releaces the most recently. (Kinda goes go but whatever)
-- Find the country that has the most tv shows. 
-- Find the title of tv shows that were frfom Germeny, America and Canada.
-- Find the title of movies released in between the year 2020 and 2021.
-- Find all titles released before 1995. 
-- Find all titles that have "" included in the cast.
