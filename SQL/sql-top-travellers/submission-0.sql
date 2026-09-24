-- Write your query below
SELECT users.name, COALESCE(r.travelled_distance,0) AS travelled_distance
FROM users
LEFT JOIN (
    SELECT rides.user_id, SUM(distance) AS travelled_distance
    FROM rides
    GROUP BY rides.user_id
) r ON users.id = r.user_id
ORDER BY travelled_distance DESC, users.name ASC;
