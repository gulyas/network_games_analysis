/*Aggregates data from the MySQL Database for examining scaffold theory*/

SELECT game_click.id as click_id,
       game_click.click_time as click_created,
       game_click.userid as user_id,
       game_click.clicked_page as article,
       game_game.uuid as uuid
FROM game_game
INNER JOIN game_click
ON game_game.uuid = game_click.game_uuid
WHERE game_click.userid IN (
    SELECT userid
    FROM game_gamewon
    WHERE game_gamewon.count > 499
);