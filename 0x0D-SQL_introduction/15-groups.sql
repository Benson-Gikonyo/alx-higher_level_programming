-- lists the number of records with the same score in the table second_table
SELECT `score`, COUNT(*) as `number` FROM `second_table`
GROUP BY `score` HAVING `number` > 1
ORDER BY `number` DESC;