# Project-2-CPSC-335
Repo for CPSC 335 Project 2

## Group Members
PLEASE ADD YOUR NAMES HERE  
Kshitij Pingle  
Timothy Tran  
Tyler Nguyen  
Elton Tran  

## JSON Input File
A JSON array with all test cases. Length of JSON array represents number of tests. Each subarray is one test case.  
The JSON input file is maintained in the following manner:-  
\[test1, test2, ... \]  
test = \[person1, person2, ..., duration_of_meeting\]  
person =  {"Schedule" : \[...\], "DailyAct" : \[...\]}  

## Edge Cases
Test case 4, 5, 10 are our edge cases

Test case 4 is testing for a case where NONE of the members within a group have a common time slot for a meeting to be arranges.
Test case 5 is testing for a case where two members within a group have the exact same Schedule and Daily Activity testing.
Test case 10 is testing for a case where three memebers of a group do not have anything on their schedule.

## Output.txt
Prints number of test cases performed and output for each test case  

### Example Output
Number of Tests: 2  

Test Case 1 Output:  
[['10:30', '12:00'], ['13:30', '14:00'], ['15:00', '16:00'], ['18:00', '18:30']]  

Test Case 2 Output:  
[['15:00', '16:00'], ['17:00', '18:00']]  

