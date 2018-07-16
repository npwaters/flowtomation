# Flowtomation
 <br>
Flowtomation was originally developed for a University assignment. Flowtomation is developed using Python 3.5/3.6. The assignment was awarded a score of 99% which included marks for coding style as well as functionality. Flowtomation has been updated since submission.<br>
 <br>
Flowtomation implements functionality similar to cloud based tools IFTTT and Stringify -  a way to specify connections between data sources, behaviours and actions.<br>
 <br>
Flowtomation runs a series of command line programs (Flow) every minute. Output from a program (Service) is used as input to the next Service. Output/Input is encapsulated in a JSON formatted message. Services can be added (installed), and configuration changes made while Flowtomation is running.  Flowtomation validates Service configuration and input/output against pre-defined rules.<br>
 <br>
Flowtomation was developed in two parts (A and B).
<br>
Part A represented the initial specification, and as such was a simple implementation. There was no input/output format, or Service configuration verification. Part A purely performed the following:<br>

- Run the flows configured at run time per the schedule (every minute)<br>
- Facilitate communication among the Services
<br>

Part B represents a change in specifications, and as such is a more complex implementation.


For simplicity, the final version (part B) of Flowtomation is maintained in this repository only.
<br>
<br>
### Application features:<br>
- Run the flows configured at run time per the schedule (every minute)
- Data is passed between services using JSON messages instead of plain text<br>
- Flowtomation validates that messages are of a supported type and match the configured input/output type<br>
- Each Service lives in its own directory with its own configuration file <br>
- Flow configuration can be modified, and Services can be installed/uninstalled while Flowtomation is running<br>
- Service configuration is checked for mandatory fields<br>
- A service that fails to load or fails mandatory field verification is not added to the running configuration<br>
- Any flow that is configured to use the service will be skipped<br>
- The running-configuration of a service whose configuration file is changed since Flowtomation first run and fails mandatory field verification will not be changed<br>
- When the issue is rectified the updated configuration will be loaded into running-config<br>
- Supports cleaning up of the running-configuration when a service is un-installed<br>
 <br>
Flowtomation logs all activity to log file 'partB/flowtomation.log' in the CWD.<br>
 <br>
#### Flowtomation supports two levels of logging:<br>
- 'INFO' - this is the default level<br>
- 'DEBUG' - can be activated by adding the 'debug' parameter<br>
	 <br>
	E.g.<br>
	'partB/flowtomation.py debug'<br>
	'partB/flowtomation.py flowtomation_test_1.json debug'<br>
	 <br>
	Note: when specifying a configuration file, the debug option must be the second parameter<br>
	 <br>

# Requirements to run:<br>
 <br>
Python 3.5+ on Linux/WSL<br>
 <br>
 <br>
# Details and running instructions:<br>
 <br>
Flowtomation uses STDOUT from a Service as STDIN for the next Service in the Flow. STDOUT can be "injected" into the parameters for the next Service using the special character combination '$$' in the Service configuration.<br>
 <br>
### Sample of pre-installed services: <br>
 <br>
- 'time of day' - return the current time<br>
- 'is morning' - check if given time is before 12pm<br>
- 'is afternoon' - check if given time is between 12pm - 6pm<br>
- 'is evening' - check if given time is after 6pm<br>
- 'quit if false' - check if conditions for the flow to continue have been met based on a boolean output from the previous service<br>
- 'py echo' - return a new version of the input string by 'injecting' the input string into the service parameters<br>
- 'append to file' - append input string to a file<br>
 <br>
 <br>
### Sample flow 1:

Append the current time to a file if it is the morning.<br>
 <br>
#### Run the sample:<br>
'partB/flowtomation.py test_files/flowtomation_test_6.json'<br>
 <br>
#### Observe Flowtomation output:<br>
'partB/flowtomation.log'<br>
 <br>
#### Observe outcome:<br>
Current time appended to 'partB/times.txt' if flow execution time is before 12pm.<br>
 <br>
 <br>
### Sample flow 2:
Unpack all the zip files in a directory and append the unpacked file names to a file
<br>
<br>
#### Run the sample:
'partB/flowtomation.py flowtomation_unzip_files_sample.json'<br>
 <br>
 <br>
#### Observe Flowtomation output:<br>
Flowtomation logs to 'partB/flowtomation.log'<br>
 <br>
#### Observe the task outcome:<br>
The filenames of unpacked files from all 'zip' files appended to 'flowtomation_output_file.txt'<br>
 <br>
 <br>


#### Run the test cases:<br>
Test cases can be found in the 'partB/test_files' files with test outcome information listed in 'partB/test_files/README.txt'<br>
 <br>
e,g.<br>
'partB/flowtomation.py'<br>
'partB/flowtomation.py flowtomation_test_1.json debug'<br>
 <br>
 <br>
# Possible issues running Flowtomation samples:<br>
 <br>
#### Incorrect line endings:<br>
 <br>
Line endings should be Unix style.<br>
if not run:<br>
find -iname "*.py" -exec dos2unix {} \\;<br>
 <br>
#### Python script files not executable:<br>
 <br>
if python files are not executable run:<br>
find -iname "*.py" -exec chmod +x {} \\; <br>
<br>