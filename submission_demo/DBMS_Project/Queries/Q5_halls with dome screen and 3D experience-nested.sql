SELECT 
    s2.name_hall, s2.location
FROM
    (SELECT 
        hall.name_hall, hall.location, hall.hall_id
    FROM
        hall
    JOIN screen ON hall.hall_id = screen.hall_id
    WHERE
        screen.experience LIKE '%3D%') AS S2,
    screen
WHERE
    screen.screen_type LIKE '%Dome%'
        AND s2.hall_id = screen.hall_id