-- List shows with genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id;
