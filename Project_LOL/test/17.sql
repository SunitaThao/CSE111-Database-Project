--Print how many champions have a Dark Star skin and has a banrate lower than 2

SELECT count(sk_champ_name)
FROM skins, stats
WHERE sk_champ_name = st_champ_name
    AND sk_name = 'Dark Star'
    AND st_banrate < '2';