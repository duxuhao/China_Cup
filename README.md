# China_Cup
For China Cup
The missing value is following:

# Train
- overdue:
original shape: (55596, 2)
transform shape: (55596, 2)
unique user number: 55596
0.0 % users are missing
--------------------------------
- user_info:
original shape: (55596, 6)
transform shape: (55596, 6)
unique user number: 55596
0.0 % users are missing
--------------------------------
- loan_time:
original shape: (55596, 2)
transform shape: (55596, 2)
unique user number: 55596
0.0 % users are missing
--------------------------------
- browse_history:
original shape: (22919547, 4)
transform shape: (22919547, 4)
unique user number: 47330
14.87 % users are missing
--------------------------------
- bill_detail:
original shape: (2338118, 15)
transform shape: (2338118, 15)
unique user number: 53174
4.36 % users are missing
--------------------------------
- bank_detail:
original shape: (6070197, 5)
transform shape: (6070197, 5)
unique user number: 9294
83.28 % users are missing
--------------------------------

# Test
- usersID:
original shape: (13899, 1)
transform shape: (13899, 1)
unique user number: 13899
0.0 % users are missing
--------------------------------
- user_info:
original shape: (13899, 6)
transform shape: (13899, 6)
unique user number: 13899
0.0 % users are missing
--------------------------------
- loan_time:
original shape: (13899, 2)
transform shape: (13899, 2)
unique user number: 13899
0.0 % users are missing
--------------------------------
- browse_history:
original shape: (5476055, 4)
transform shape: (5476055, 4)
unique user number: 11997
13.68 % users are missing
--------------------------------
- bill_detail:
original shape: (414895, 15)
transform shape: (414895, 15)
unique user number: 13643
1.84 % users are missing
--------------------------------
- bank_detail:
original shape: (376409, 5)
transform shape: (376409, 5)
unique user number: 709
94.9 % users are missing
--------------------------------

# Features of the data
- sample imbalance
- browse_history: user can do multi activities at a time and the file record users' activity at different time. Many activity can come out from this file, like how many times the user operate, how many times the user take this activity or activity label.