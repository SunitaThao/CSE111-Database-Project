--Print the champion name, its role, its q ability, its bad match up, and its pickrate if it's over 3.0
--in desc order of pickrate

SELECT t_champ_name, t_role, a_qability, bad_mu_name, st_pickrate
FROM type, abilities, matchups, stats
WHERE t_key = a_key
    AND a_key = mu_key
    AND mu_key = st_key
    AND st_pickrate > '3.0'
Order by st_pickrate DESC;