SELECT 
    hall.name_hall,
    hall.hall_id,
    COUNT(reservation.hall_id) AS num_of_reservations
FROM
    hall
        JOIN
    reservation ON reservation.hall_id = hall.hall_id
GROUP BY reservation.hall_id