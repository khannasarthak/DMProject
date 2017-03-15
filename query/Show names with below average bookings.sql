SELECT 
    shows.show_name
FROM
    shows
WHERE
    shows.show_id IN (SELECT 
            eventtable.show_id
        FROM
            eventtable
        WHERE
            e_id IN (SELECT 
                    booking.e_id
                FROM
                    booking
                WHERE
                    num_tickets < (SELECT 
                            AVG(num_tickets)
                        FROM
                            booking)
                GROUP BY e_id))
