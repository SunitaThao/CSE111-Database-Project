--Print the champion and it's r ability if it has a legendary or ultimate skin

SELECT distinct a_champ_name, a_rability
FROM abilities, skins
WHERE a_key = sk_key
    AND sk_skin_kind = 'legendary' or sk_skin_kind = 'ultimate';