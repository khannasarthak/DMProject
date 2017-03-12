SELECT 
    shows.show_name
FROM
    shows
WHERE
    show_id IN (SELECT 
            eventtable.show_id
        FROM
            eventtable
        WHERE
            eventtable.ticket_price IN (SELECT 
                    MAX(eventtable.ticket_price)
                FROM
                    eventtable))