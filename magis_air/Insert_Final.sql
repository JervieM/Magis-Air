

---------------------------------------------- CREW ASSIGNMENTS ----------------------------------------------
-- Insert data into CrewMember table
INSERT INTO "crew_assignments_crewmember" ("crew_id", "role", "first_name", "last_name", "middle_name")
VALUES
    ('000001', 'Captain', 'John', 'Doe', 'A'),
    ('000002', 'First Officer', 'Jane', 'Smith', 'B'),
    ('000003', 'Flight Attendant', 'Emily', 'Johnson', 'C'),
    ('000004', 'Flight Attendant', 'Michael', 'Brown', 'D');

------------------------------------ FLIGHT ROUTES APP ----------------------------------------
-- Insert data into Flight table
INSERT INTO "flight_routes_flight" ("flight_id", "origin", "destination", "departure_time", "travel_duration_hours", "travel_duration_minutes")
VALUES
    ('PL9328', 'Manila, Philippines', 'Tokyo, Japan', '10:00:00', 7, 30),
    ('AW0923', 'London, UK', 'New York, USA', '15:00:00', 11, 45),
    ('IF8362', 'Tokyo, Japan', 'London, UK', '08:30:00', 1, 45);

------------------------------------ FLIGHT SCHEDULES -------------------------------------------
-- Insert data into CrewSchedule table
INSERT INTO "crew_assignments_flightschedule" ("schedule_id", "date")
VALUES
    ('SCH-241201-000001', '2024-12-01'),
    ('SCH-241202-000001', '2024-12-02'),
    ('SCH-241203-000001', '2024-12-03');

-- Insert data into FlightSchedule table
INSERT INTO "flight_schedules_flightschedule" ("schedule_id", "date", "flight_id")
VALUES
    ('SCH-241201-000001', '2024-12-01', 'PL9328'),
    ('SCH-241202-000001', '2024-12-02', 'AW0923'),
    ('SCH-241203-000001', '2024-12-03', 'IF8362');

-- Insert data into CrewMember and FlightSchedule relationship table
INSERT INTO "crew_assignments_flightschedule_crew_members" ("flightschedule_id", "crewmember_id")
VALUES
    ('SCH-241201-000001', '000001'),
    ('SCH-241202-000001', '000002'),
    ('SCH-241203-000001', '000003'),
    ('SCH-241201-000001', '000004');


------------------------------------ FLIGHT BOOKING ----------------------------------------------

-- Insert data into BookingAdditionalItems table
INSERT INTO "flight_booking_additionalitem" ("item_id", "description")
VALUES
    ('I00001', 'Banana'),
    ('I00002', 'Baggage'),
    ('I00003', 'Shoes');


-- Insert data into Passenger table
INSERT INTO "flight_booking_passenger" ("passenger_id", "name", "first_name", "middle_name", "last_name", "birth_date", "gender")
VALUES
    ('PAS-241202-000001', 'Alice Williams', 'Alice', '', 'Williams', '1990-05-14', 'F'),
    ('PAS-241202-000002', 'Bob Brown', 'Bob', '', 'Brown', '1985-11-22', 'M'),
    ('PAS-241202-000003', 'Charlie Davis', 'Charlie', '', 'Davis', '1992-08-19', 'M');

-- Insert data into Booking table with a placeholder for additional_items
INSERT INTO "flight_booking_booking" ("booking_id", "total_cost", "booking_date", "flight_id", "passenger_id", "additional_items")
VALUES
    ('KSIFNQ-241101', 500.00, '2024-11-01', 'PL9328', 'PAS-241202-000001', 'Banana'),
    ('OAMQPD-241023', 300.00, '2024-10-23', 'AW0923', 'PAS-241202-000002', 'Baggage'),
    ('JDUQBZ-241128', 450.00, '2024-11-28', 'IF8362', 'PAS-241202-000003', 'Shoes');


------------------------------------ Flight Schedules -------------------------------------------
-- Insert data into FlightScheduleCrewMembers table
INSERT INTO "flight_schedules_flightschedule_crew_members" ("flightschedule_id", "crewmember_id")
VALUES
    ('SCH-241201-000001', '000001'),
    ('SCH-241201-000001', '000002'),
    ('SCH-241202-000001', '000003'),
    ('SCH-241203-000001', '000004');
