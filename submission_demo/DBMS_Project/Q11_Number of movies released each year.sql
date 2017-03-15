SELECT 
    release_date, COUNT(shows.show_id) AS Total_movie
FROM
    shows
        JOIN
    movie ON movie.show_id = shows.show_id
GROUP BY release_date
