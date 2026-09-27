Part 1 — Analysis & Design

1. Proposed system name

ParkEase Kenya – Modern Parking Management System

The system will automate parking operations by showing available parking slots, recording vehicles entering, calculating parking duration and fees when vehicles leave, and opening the exit barrier after payment. These are directly based on the requirements in the assignment. 

2. Main system modules

Module	Function

Parking Slot Module	Displays available and occupied parking slots
Vehicle Entry Module	Records vehicle details and arrival time
Parking Management Module	Tracks vehicles currently inside
Fee Calculation Module	Calculates parking duration and amount payable
Payment Module	Records/validates payment
Exit Module	Opens the barrier after successful payment
Database Module	Stores vehicles, slots, payments and parking records
Admin/Dashboard Module	Allows management to monitor the parking facility


The brief specifically requires visual availability before entry, vehicle recording on arrival, automatic calculation of time and payment on exit, and barrier opening after payment. 


---

3. Use-case flow

The basic process will be:

START
                │
                ▼
      Display Available Slots
                │
                ▼
       Driver Selects Slot
                │
                ▼
       Record Vehicle Details
                │
                ▼
       Record Arrival Time
                │
                ▼
          Vehicle Parks
                │
                ▼
       Vehicle Requests Exit
                │
                ▼
      Calculate Parking Time
                │
                ▼
       Calculate Parking Fee
                │
                ▼
          Make Payment
                │
          ┌─────┴─────┐
          │           │
       Failed      Successful
          │           │
          ▼           ▼
       Retry      Open Barrier
                      │
                      ▼
              Update Slot = FREE
                      │
                      ▼
                    END


---

4. Parking fee algorithm

According to the assignment:

Up to 30 minutes: Free

Up to 2 hours: Ksh 50

Up to 4 hours: Ksh 100

Up to 6 hours: Ksh 300

More than 6 hours: Ksh 500 


Pseudocode

START

Input arrivalTime
Input exitTime

Calculate duration = exitTime - arrivalTime

IF duration <= 30 minutes
    fee = 0

ELSE IF duration <= 2 hours
    fee = 50

ELSE IF duration <= 4 hours
    fee = 100

ELSE IF duration <= 6 hours
    fee = 300

ELSE
    fee = 500

Display duration
Display fee

END


---

5. Data structures

A. Array / List

Used to store parking slots.

Example:

Slot 1 → Available
Slot 2 → Occupied
Slot 3 → Available
Slot 4 → Occupied

Reason: We need to quickly display and update the status of parking slots.

B. Queue

A queue can be used for vehicles waiting when all parking slots are occupied.

Vehicle A → Vehicle B → Vehicle C
    ↑                    ↑
   Front                Rear

Reason: Vehicles are handled using First-In, First-Out (FIFO).

C. Hash Table / Dictionary

Can store active parking records using the vehicle registration number as the key.

KDA 123A → Vehicle record
KCB 456B → Vehicle record
KDC 789C → Vehicle record

Reason: It allows fast lookup of a vehicle when it exits.

D. Stack

A stack can be used for certain administrative/history operations where the most recent record is accessed first.

Reason: It follows Last-In, First-Out (LIFO).

E. Database tables

Persistent records should be stored in a relational database rather than relying only on in-memory data structures.


---

6. Dynamic database design

A possible database is:

parking_slots

Field	Type

slot_id	INT
slot_number	VARCHAR
status	VARCHAR
location	VARCHAR


Example:

1 | A01 | AVAILABLE | Ground Floor
2 | A02 | OCCUPIED  | Ground Floor
3 | A03 | AVAILABLE | Ground Floor

vehicles

Field	Type

vehicle_id	INT
registration_no	VARCHAR
vehicle_type	VARCHAR
owner_name	VARCHAR


parking_records

Field	Type

record_id	INT
vehicle_id	INT
slot_id	INT
entry_time	DATETIME
exit_time	DATETIME
duration	INT
fee	DECIMAL
status	VARCHAR


payments

Field	Type

payment_id	INT
record_id	INT
amount	DECIMAL
payment_time	DATETIME
payment_status	VARCHAR



---

7. Database relationship

VEHICLES
   │
   │ 1
   ▼
PARKING_RECORDS
   │
   ├──────────► PARKING_SLOTS
   │
   │ 1
   ▼
PAYMENTS

This lets the system maintain the complete journey:

Vehicle → Slot → Entry → Parking duration → Fee → Payment → Exit


---

8. Next: actual system 💻

We can build it as:

ParkEase-Kenya/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── entry.html
│   ├── exit.html
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md