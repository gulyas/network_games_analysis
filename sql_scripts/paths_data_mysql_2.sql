/*Aggregate data from MySQL Database for examining path stretch
  Using the game_gamewinner table instead of counting clicks separately*/

SELECT game_gamewinner.userid as user_id,
       game_gamewinner.clicks as clicks,
       game_game.start_page as start_page,
       game_game.end_page as end_page,
       game_game.id as game_id,
       game_game.start_time as start_time,
       game_game.end_time as end_time
FROM game_gamewinner
INNER JOIN game_game
ON game_gamewinner.game_id = game_game.id
WHERE user_id IN (
    SELECT COUNT(userid)
    FROM game_gamewon
    WHERE game_gamewon.count > 29
);