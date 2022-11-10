--Print the champion name, its role, its q ability, its bad match up, and its pickrate if it's over 3.0
--in desc order of pickrate

SELECT distinct t_champ_name, t_role, a_qability, bad_mu_name, st_pickrate
FROM type, abilities, matchups, stats
WHERE t_champ_name = a_champ_name
    AND a_champ_name = mu_champ_name
    AND mu_champ_name = st_champ_name
    AND st_pickrate > '3.0'
Order by st_pickrate DESC;