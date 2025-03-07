-- database
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
