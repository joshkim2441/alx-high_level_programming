-- List number of records with same score in table 'second_table'
-- of database 'hbtn_0c_0' in my MySQL server
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
