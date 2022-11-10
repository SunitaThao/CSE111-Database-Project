--What Champion has the highest banrate? Print the champion name along with its banrate.

SELECT st_champ_name, max(st_banrate)
FROM stats;
