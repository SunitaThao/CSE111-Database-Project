--Print out the w ability of all champions whose names start with 'B'

SELECT a_wability
FROM abilities
WHERE substr(a_champ_name, 1, 1) = 'B';