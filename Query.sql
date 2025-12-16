-- Query Name: SubsidiaryRestaurantAboveTheAvgStaff
-- Find all the restaurants where their combined # staff member of their subsidiary is larger than the average 
-- staff number per subsidiary.
SELECT
   r.restaurantName,r.restaurantLocation,
   r.restaurantType,s.subsidiaryName,
   s.subsidiaryLocation
FROM Restaurant r
JOIN Subsidiary s ON r.subsidiaryID = s.subsidiaryID
WHERE s.subsidiaryID IN (SELECT
       r2.subsidiaryID
   FROM Restaurant r2
   JOIN Staff s2 ON r2.restaurantID = s2.restaurantID
   GROUP BY r2.subsidiaryID
   HAVING COUNT(s2.staffID) >(
           SELECT AVG(staff_per_sub)
           FROM (SELECT
                   COUNT(s3.staffID) AS staff_per_sub
               FROM Restaurant r3
               JOIN Staff s3 ON r3.restaurantID = s3.restaurantID
               GROUP BY r3.subsidiaryID) AS sub_avg))
ORDER BY s.subsidiaryName;