SELECT DISTINCT(CITY) FROM STATION
WHERE CITY REGEXP '[aeiouAEIOU]$' AND CITY REGEXP '^[aeiouAEIOU]';