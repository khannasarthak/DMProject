SELECT 
    performance_type, COUNT(*)
FROM
    shows
        JOIN
    performance ON performance.show_id = shows.show_id
GROUP BY performance_type