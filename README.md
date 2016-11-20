# China_Cup
For China Cup<br />
The missing value is following:<br />

# Train
- overdue:<br />
original shape: (55596, 2)<br />
transform shape: (55596, 2)<br />
unique user number: 55596<br />
0.0 % users are missing

--------------------------------

- user_info:<br />
original shape: (55596, 6)<br />
transform shape: (55596, 6)<br />
unique user number: 55596<br />
0.0 % users are missing

--------------------------------

- loan_time:<br />
original shape: (55596, 2)<br />
transform shape: (55596, 2)<br />
unique user number: 55596<br />
0.0 % users are missing

--------------------------------

- browse_history:<br />
original shape: (22919547, 4)<br />
transform shape: (22919547, 4)<br />
unique user number: 47330<br />
14.87 % users are missing

--------------------------------

- bill_detail:<br />
original shape: (2338118, 15)<br />
transform shape: (2338118, 15)<br />
unique user number: 53174<br />
4.36 % users are missing

--------------------------------

- bank_detail:<br />
original shape: (6070197, 5)<br />
transform shape: (6070197, 5)<br />
unique user number: 9294<br />
83.28 % users are missing

--------------------------------


# Test
- usersID:<br />
original shape: (13899, 1)<br />
transform shape: (13899, 1)<br />
unique user number: 13899<br />
0.0 % users are missing

--------------------------------

- user_info:<br />
original shape: (13899, 6)<br />
transform shape: (13899, 6)<br />
unique user number: 13899<br />
0.0 % users are missing

--------------------------------

- loan_time:<br />
original shape: (13899, 2)<br />
transform shape: (13899, 2)<br />
unique user number: 13899<br />
0.0 % users are missing

--------------------------------

- browse_history:<br />
original shape: (5476055, 4)<br />
transform shape: (5476055, 4)<br />
unique user number: 11997<br />
13.68 % users are missing

--------------------------------

- bill_detail:<br />
original shape: (414895, 15)<br />
transform shape: (414895, 15)<br />
unique user number: 13643<br />
1.84 % users are missing

--------------------------------

- bank_detail:<br />
original shape: (376409, 5)<br />
transform shape: (376409, 5)<br />
unique user number: 709<br />
94.9 % users are missing

--------------------------------

# Features of the data
    - sample imbalance 
        can adjust the sample rate for different type, try to get close to the online sample balance
    - browse_history
        user can do multi activities at a time and the file record users' activity at different time. Many activity can come out from this file, like how many times the user operate, how many times the user take this activity or activity label.
    - the number of the activities has no pysical meaning, assumption base on the total number an activity taken.
    - the number of the activities' label has no pysical meaning, assumption base on the total number an activity label taken.

# Extract Features
## Basic information: education, gender ...
## Browse activity (1050):
    - the total times the costumer browse (1)
    - the time difference between the first and last browses of the costumer (1)
    - the frequency of the costumer browse (1)
    - total_times/frequency/average/min/max of a costumer take for a single activity label (11 different types * 5 = 55)
    - total_times/frequency of a costumer take for a single activity (216 different types * 2 = 432)
    - the average/min/max/count of activities number does the costumer take in one browse (4 )
    - the average/min/max/count of activities number label does the costumer take in one browse (4)
    - total_times/frequency of a costumer take for a single activity+label (276 different types * 2 = 552)
    
## Bill information

## Bank detail