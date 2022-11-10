--Print out all the champions that have a bad match up against Seraphine

SELECT mu_champ_name
FROM matchups
WHERE bad_mu_name = 'Seraphine';