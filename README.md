# Project-2-CPSC-335
Repo for CPSC 335 Project 2

## Group Members
Kshitij Pingle (kpingle@csu.fullerton.edu)  
Timothy Tran (timmyster413@csu.fullerton.edu)  
Tyler Nguyen (destiny1235321@csu.fullerton.edu)  
Elton Tran (eltontran00@csu.fullerton.edu)  

## JSON Input File
A JSON array with all test cases. Length of JSON array represents number of tests. Each subarray is one test case.  
The JSON input file is maintained in the following manner:-  
\[test1, test2, ... \]  
test = \[person1, person2, ..., duration_of_meeting\]  
person =  {"Schedule" : \[...\], "DailyAct" : \[...\]}  

### How to run our Program
First install every file within GitHub (files needed):

main.py  
schedule.py  
input.json  
output.txt  

##### Once installed, 
Open up input.json on any editing application. (VS code, Atom, Notepad)  
Inputs must follow this format :
#### [{"Schedule" : ["time", "time"], "DailyAct" : ["time", "time"]}, (duration_of_meetings)]
Each {input} is considered a 'person' or a member within a group, you can have multiple members within an input as long as it respects the format.  
The input "time" must be within ["0:00", "23:59"] to be a valid time.  
The input (duration_of_meetings) must be in minutes, (i.e. 2 hours = '120' minutes)  

Once changes are made to 'input.json'
Open up a terminal within this directory and run "python main.py" to run the program
Changes will be made in 'output.txt'


## Output.txt
Prints number of test cases performed and output for each test case  

### Edge Cases
Test case 4, 5, 10 are our edge cases

Test case 4 is testing for a case where NONE of the members within a group have a common time slot for a meeting to be arranged.  
Test case 5 is testing for a case where two members within a group have the same exact Schedule and Daily Activity.  
Test case 10 is testing for a case where three memebers of a group do not have anything on their Schedules.  

### Example Output
Number of Tests: 2  

Test Case 1 Output:  
[['10:30', '12:00'], ['13:30', '14:00'], ['15:00', '16:00'], ['18:00', '18:30']]  

Test Case 2 Output:  
[['15:00', '16:00'], ['17:00', '18:00']]  
