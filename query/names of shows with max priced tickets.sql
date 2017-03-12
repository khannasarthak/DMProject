SELECT 
    show_name
FROM
    (SELECT 
        s1.show_id
    FROM
        (SELECT 
        e_id, show_id
    FROM
        eventtable
    WHERE
        ticket_price = (SELECT 
                MAX(ticket_price)
            FROM
                eventtable)) AS s1, shows
    WHERE
        s1.show_id = shows.show_id) AS s2,
    shows
WHERE
    s2.show_id = shows.show_id