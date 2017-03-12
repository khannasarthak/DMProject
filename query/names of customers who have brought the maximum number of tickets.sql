SELECT 
    COUNT(customer.customer_name)
FROM
    customer
        JOIN
    booking ON booking.customer_id = customer.customer_id
WHERE
    num_tickets = (SELECT 
            MAX(num_tickets)
        FROM
            booking
        ORDER BY customer_id)
