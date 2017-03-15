SELECT
    show_name
FROM
    (SELECT
        MAX(num_of_reservations) AS number_of_reservation,
            s2.show_id
    FROM
        (SELECT
        reservation.show_id, COUNT(*) AS num_of_reservations
    FROM
        reservation
    GROUP BY reservation.show_id) AS s2) AS s1
        JOIN
    shows ON s1.show_id = shows.show_id
