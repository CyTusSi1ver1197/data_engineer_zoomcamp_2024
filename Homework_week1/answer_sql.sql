-- Question 3
-- SELECT count(*) 
-- FROM green_taxi_data_2019
-- WHERE CAST(lpep_pickup_datetime AS DATE) = '2019-09-18' AND CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18'
-- Ans: 15612


-- Question 4
-- SELECT lpep_pickup_datetime
-- FROM public.green_taxi_data_2019
-- WHERE trip_distance >= ANY(SELECT MAX(trip_distance) FROM public.green_taxi_data_2019)
-- Ans: 2019-09-26


-- Question 5
-- SELECT zo."Borough", SUM(taxi."total_amount") 
-- FROM green_taxi_data_2019 as taxi inner join zone_green_taxi_2019 as zo on taxi."PULocationID" = zo."LocationID" 
-- WHERE CAST(lpep_pickup_datetime AS DATE) = '2019-09-18' AND CAST(lpep_dropoff_datetime AS DATE) = '2019-09-18'
-- group by zo."Borough"
-- HAVING SUM(taxi."total_amount") > 50000
-- Ans:
-- "Brooklyn"
-- "Manhattan"
-- "Queens"


-- Question 6:
-- SELECT zone_green_taxi_2019."Zone" from zone_green_taxi_2019
--   Where zone_green_taxi_2019."LocationID" =(
-- 	   SELECT taxi."DOLocationID" 
-- 	   FROM green_taxi_data_2019 as taxi inner join zone_green_taxi_2019 as zo on taxi."PULocationID" = zo."LocationID" 
-- 	   WHERE zo."Zone" = 'Astoria' AND taxi."tip_amount" >= ANY(
--     SELECT MAX(tip_amount) FROM green_taxi_data_2019 as taxi inner join zone_green_taxi_2019 as zo on taxi."PULocationID" = zo."LocationID" 
-- 	   WHERE zo."Zone" = 'Astoria'))
--Ans : JFK Airport