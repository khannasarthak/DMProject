SELECT 
    screen_type, COUNT(screen.hall_id)
FROM
    hall
        JOIN
    screen ON hall.hall_id = screen.hall_id
GROUP BY screen_type