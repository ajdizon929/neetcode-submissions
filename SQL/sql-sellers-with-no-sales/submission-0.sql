-- Write your query below
SELECT seller.seller_name
FROM seller
WHERE seller.seller_id NOT IN (
    SELECT seller_id
    FROM orders
    WHERE sale_date >= '2020-01-01' and sale_date <= '2020-12-31'
)
ORDER BY seller.seller_name ASC;