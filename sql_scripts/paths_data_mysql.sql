/*Aggregate data from MySQL Database for examining path stretch*/

SELECT game_click.click_time as click_time,
       game_click.userid as user_id,
       game_click.clicked_page as article,
       game_game.uuid as uuid,
       game_game.start_page as start_page,
       game_game.end_page as end_page,
       game_game.start_time as start_time,
       game_game.end_time as end_time
FROM game_game
INNER JOIN game_click
ON game_game.uuid = game_click.game_uuid
WHERE user_id IN (
    SELECT userid
    FROM game_gamewon
    WHERE game_gamewon.count > 29
)
AND game_game.end_time IS NOT NULL;
