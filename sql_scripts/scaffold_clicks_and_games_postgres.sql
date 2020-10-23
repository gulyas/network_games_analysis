/*Aggregates data from the Postgres Database for examining scaffold theory*/

SELECT game_click.id as click_id,
       game_click.created as click_created,
       game_click.article_id as article_id,
       game_game.id as game_id,
       game_game.created as game_created,
       game_game.player_id as player_id
FROM game_game
INNER JOIN game_click
ON game_game.id = game_click.game_id
WHERE player_id IN (
    SELECT player_id
    FROM game_game
    WHERE won IS TRUE
    GROUP BY player_id
    HAVING COUNT(id) > 499
);
