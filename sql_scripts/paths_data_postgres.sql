/*Aggregate data from Postgres Database for examining path stretch*/

SELECT game_click.id as click_id,
       game_click.created as click_created,
       game_click.article_id as article_id,
       game_game.id as game_id,
       game_game.created as game_created,
       game_game.player_id as player_id,
       game_game.total_time as total_time,
       game_roundchallange.start_article_id as start_article_id,
       game_roundchallange.end_article_id as end_article_id
FROM game_click
INNER JOIN game_game ON game_click.game_id = game_game.id
INNER JOIN game_round ON game_game.round_id = game_round.id
INNER JOIN game_roundchallange ON game_round.challange_id = game_roundchallange.id
WHERE player_id IN (
    SELECT player_id
    FROM game_game
    WHERE won IS TRUE
    GROUP BY player_id
    HAVING COUNT(id) > 29
)
AND game_game.won IS TRUE;