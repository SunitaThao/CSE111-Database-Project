--Print the highest cost of each champion's skins

SELECT max(sk_cost)
FROM skins
GROUP by sk_champ_name;