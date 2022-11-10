--Print out all the champions who are mages

SELECT distinct t_champ_name
FROM type
WHERE t_name = 'Mage';