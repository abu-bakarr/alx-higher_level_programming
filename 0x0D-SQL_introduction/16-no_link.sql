-- display scroe and name in second_table where name is not null
SELECT score, name
FROM second_table
WHERE LENGTH(name) > 0
ORDER BY score DESC;