# System Design Prep Template

Design a reservation and payment system for a parking garage.

## General Requirements

- Who are the users?
- How are they going to use it?
- What use cases are there?
- What are the inputs and outputs?
- How much data do we expect to handle?
- How many requests do we expect?
- Need to able to reserve a parking spot and receive some kind of ticket or receipt.
- Need to be able to pay for a parking spot.
- System needs to have a high consistency (no two people should be able to reserve the same spot at the same time)
- 3 types of vehicles (compact, regular, and large)
- Flat rate, but different based on vehicle.

## Public Endpoints (To give to backend)

/reserve
Params: garage_id, start_time, end_time
Returns: (spot_id, reservation_id)

/payment
Params: reservation_id
Note: Likely to use existing API (Stripe, Square)

/cancel
Params: reservation_id

/create_account
Params: username, password, first_name, last_name
Note: Likely to use existing API (Sign in with Google, Facebook)

## Internal Endpoints (To give to frontend)

/calculate_payment
Params: reservation_id

/freespots
Params: garage_id, vehicle_type, time
Note: Smaller vehicles can fit into larger spots if necessary

/allocate_spot
Params: garage_id, vehicle_type, time

## Data Entities

id => primary key, serial

Reservation

- garage_id => foreign_key, int
- spot_id => foreign_key, int
- start => timestamp
- end => timestamp
- paid => boolean

Garage

- zipcode => varchar
- rate_compact => decimal
- rate_regular => decimal
- rate_large => decimal

Spots

- garage_id => foreign_key, int
- vehicle_type => enum
- status => enum

Users

- username => varchar
- email => varchar
- first_name => varchar
- last_name => varchar

Vehicles

- user_id => foreign_key, int
- license => varchar
- vehicle_type => enum

## High Level Architecture

WebApp => Backend => MongoDB (Writing)
Load Balancer => MongoDB Replica, MongoDB Replica (Reading)
