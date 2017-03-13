SELECT 
    show_name
FROM
    shows
        JOIN
    movie ON movie.show_id = shows.show_id
