--Print out the champions that have a good match up against Azir, 
--their nickname, and their e ability

SELECT mu_champ_name, c_nickname, a_eability
FROM matchups, champion, abilities, skins
WHERE mu_champ_name = c_name
    AND c_name = sk_champ_name 
    AND sk_champ_name = a_champ_name
    AND good_mu_name = 'Azir'
GRoup by mu_champ_name, c_nickname;