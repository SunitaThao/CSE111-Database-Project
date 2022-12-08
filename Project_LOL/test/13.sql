--Print the nickname of the champions who have a tier S and a good match up with Miss Fortune

SELECT c_nickname
FROM champion, stats, matchups
WHERE c_key = st_key
    AND c_key = mu_key
    AND st_tier = 'S'
    AND good_mu_name = 'Miss Fortune';