SELECT 
    shows.show_name, s1.show_id
FROM
    shows,
    (SELECT 
        MAX(num_of_reservations) AS number_of_reservation,
            s2.show_id
    FROM
        (SELECT 
        reservation.show_id,
            COUNT(reservation.hall_id) AS num_of_reservations
    FROM
        shows
    JOIN reservation ON reservation.show_id = shows.show_id
    GROUP BY reservation.show_id) AS s2) AS s1
WHERE
    s1.show_id = shows.show_id

    
    
