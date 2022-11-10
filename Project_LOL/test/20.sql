--Print out easiest champions to play that are also junglers.

SELECT distinct c_name
FROM champion, type
WHERE c_name = t_champ_name
    AND c_difficulty = 'low'
    AND t_role = 'jungle';