--Statistics from the MySQL database

-- ----------------------------------
-- Counting articles
SELECT COUNT(DISTINCT clicked_page) FROM game_click;

-- ----------------------------------
-- Counting games
SELECT COUNT(id) FROM game_game;

-- Number of finished games
SELECT SUM(count) FROM game_gamewon;

-- Average total time of played games
SELECT AVG(timestampdiff(SECOND, start_time, end_time)) FROM game_game
WHERE end_time IS NOT NULL;

-- Average duration of won games
SELECT AVG(timestampdiff(SECOND, start_time, end_time)) FROM game_game
INNER JOIN game_gamewinner
ON game_game.id = game_gamewinner.game_id;

-- ----------------------------------
-- Average/min/max clicks per finished games
SELECT AVG(clicks) FROM ( --MIN, MAX
    SELECT COUNT(game_click.id) AS clicks FROM game_click
    INNER JOIN game_game
    ON game_click.game_id = game_game.id
    WHERE game_game.end_time IS NOT NULL
    GROUP BY game_id
) AS inner_query;

-- Min/max clicks per finished games, method II.
SELECT MIN(clicks) FROM game_gamewinner; -- MAX

-- ----------------------------------
-- Number of players
SELECT COUNT(DISTINCT userid) FROM game_gameplayed;

-- Number of players with at least 30 played games
SELECT COUNT(DISTINCT userid) FROM game_gameplayed
WHERE count > 29;

-- Number of players with at least 30 won games (and with at least 50, 100, 500)
SELECT COUNT(DISTINCT userid) game_gamewon
WHERE count > 29; -- 49, 99, 499