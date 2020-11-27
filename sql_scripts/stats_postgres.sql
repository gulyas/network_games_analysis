--Statistics from the PostgreSQL database

-- ----------------------------------
-- Counting articles
SELECT COUNT(id) FROM articles_article;

-- Counting articles with filled content_links field
SELECT COUNT(id) FROM articles_article
WHERE content_links IS NOT NULL;

-- Counting articles with filled inbound_links field
SELECT COUNT(id) FROM articles_article
WHERE inbound_links IS NOT NULL;

-- Counting articles with filled outbound_links field
SELECT COUNT(id) FROM articles_article
WHERE outbound_links IS NOT NULL;

-- Counting articles with filled content field
SELECT COUNT(id) FROM articles_article
WHERE content IS NOT NULL;

-- ----------------------------------
-- Counting games
SELECT COUNT(id) FROM game_game;

-- Counting finished/unfinished games
SELECT COUNT(id) FROM game_game
WHERE won IS TRUE; -- or FALSE

-- Average/Minimal/Maximal total time of a finished games
SELECT AVG(total_time) FROM game_game; --MIN, MAX

-- ----------------------------------
-- Counting average clicks per games
SELECT AVG(clicks) FROM (
    SELECT COUNT(id) AS clicks FROM game_click
    GROUP BY game_id
) AS inner_query;

-- Counting average clicks per finished/unfinished games
SELECT AVG(clicks) FROM (
    SELECT COUNT(game_click.id) AS clicks FROM game_click
    INNER JOIN game_game
    ON game_click.game_id = game_game.id
    WHERE game_game.won IS TRUE -- FALSE
    GROUP BY game_id
) AS inner_query;

-- Minimal/maximal count of clicks in finished games
SELECT MIN(clicks) FROM ( -- MAX
    SELECT COUNT(game_click.id) AS clicks FROM game_click
    INNER JOIN game_game
    ON game_click.game_id = game_game.id
    WHERE game_game.won IS TRUE
    GROUP BY game_id
) AS inner_query;

-- ----------------------------------
-- Counting players
SELECT COUNT(DISTINCT player_id) FROM game_game;

-- Number of players with at least 30 games
SELECT COUNT(player_id) FROM (
    SELECT COUNT(id) AS played_games, player_id FROM game_game
    GROUP BY player_id
) AS inner_query
WHERE played_games > 29;

--Number of players with at least 30 finished games (and with at least 50, 100, 500)
SELECT COUNT(player_id) FROM (
    SELECT COUNT(id) AS played_games, player_id FROM game_game
    WHERE won IS TRUE
    GROUP BY player_id
) AS inner_query
WHERE played_games > 29 -- 49, 99, 499