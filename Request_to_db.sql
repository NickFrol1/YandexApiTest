SELECT login, COUNT(*) AS confirm_orders
FROM "Couriers"
JOIN "Orders" ON "Couriers".id="Orders"."courierId"
WHERE "inDelivery" = 't'
GROUP BY "Couriers".login;

SELECT track,
	CASE
		WHEN "inDelivery"='t' AND cancelled = 'f' AND finished = 'f' THEN 1
		WHEN "inDelivery"='f' AND cancelled = 't' AND finished = 'f' THEN -1
		WHEN "inDelivery"='f' AND cancelled = 'f' AND finished = 'f' THEN 2
		ELSE 0
	END AS status
FROM "Orders";
