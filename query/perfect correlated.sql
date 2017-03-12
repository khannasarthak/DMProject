SELECT 
    booking.e_id
FROM
    booking
WHERE
    price > (SELECT 
            AVG(booking.price)
        FROM
            booking)