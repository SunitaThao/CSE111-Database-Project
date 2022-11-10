--Print the champion and it's r ability if it has a a legendary or ultimate skin

SELECT distinct a_champ_name, a_rability
FROM abilities, skins
WHERE a_champ_name = sk_champ_name
    AND sk_skin_kind = 'legendary' or sk_skin_kind = 'ultimate';