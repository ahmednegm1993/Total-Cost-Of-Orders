SELECT 
o.id,
    c.id, 
    c.first_name, 
    SUM(o.total_order_cost) AS total_order_cost
FROM 
   [dbo].[customer]  c
JOIN 
    [dbo].[orders] o
ON 
    c.id = o.cust_id
GROUP BY 
    c.id, c.first_name,o.id
ORDER BY 
    o.id asc;
