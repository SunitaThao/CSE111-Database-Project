--Print out the champion name of those who has a winrate higher than 50,
-- over 20,000 matches, is a Fighter, has a SKT T1 skin, 
--and is moderate difficulty

SELECT distinct c_name
FROM champion, stats, type, skins
WHERE c_name = sk_champ_name
    AND sk_champ_name = t_champ_name
    AND t_champ_name = st_champ_name
    AND st_winrate > '50'
    AND st_matches > '20000'
    AND t_name = 'Fighter'
    AND substr(sk_name, 1, 6) = 'SKT T1'
    AND c_difficulty = 'moderate';