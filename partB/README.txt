The program logs all activity to log file 'a2.log' in the CWD.

The program supports two levels of logging:
	'INFO' - this is the default level
	'DEBUG' - can be activated by adding the 'debug' parameter
	
	E.g.
	'./ifttt.py debug'
	'./ifttt.py ifttt_test_1.json debug'
	
	Note: when specifying a configuration file, the debug option must be the second parameter


A service that fails to load or fails mandatory field verification is not added to the running configuration
Any flow that is configured to use the service will be skipped
The running-configuration of a service whose configuration file is changed since the program first run and fails mandatory field verification will not be changed
When the issue is rectified the updated configuration will be loaded into running-config

The program supports cleaning up of the running-configuration when a service is un-installed




