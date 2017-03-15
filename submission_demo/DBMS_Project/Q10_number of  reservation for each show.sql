SELECT 
    show_name,
    shows.show_id,
    COUNT(reservation.show_id) AS num_of_reservations
FROM
    shows
        JOIN
    reservation ON reservation.show_id = shows.show_id
GROUP BY reservation.show_id