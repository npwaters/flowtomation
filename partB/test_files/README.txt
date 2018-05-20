

Note:
the test below are primarily related to part 2

the numbers below correspond to ocnfiguration files in the 'test_files' directory



1. an empty json program configuration file (no text at all)
	Expected result: abort
2. an invalid json program configuration file (just bad json)
	Expected result: abort
3. an invalid configuration (correct json, but bad key/values for this problem)
	Expected result: abort
4. a flow with only a single service
	Expected result: continually re-run service?
5. a flow calling on a service that always returns an exit status of 1 (call the service "fail.py" if you like)
	Expected result: 
		flow will exit.
		Program will run next flow or re-run flow if only one flow
6. a flow that runs successfully
	Expected result: Program will run next flow or re-run flow if only one flow
7. a flow that calls services that take longer than one minute (have a service that does a time.sleep(60))
	Expected result: 
		program waits until service has finished
		Runs the next services in the flow straight away
		Program runs next flow on the next available minute
8. a file that includes multiple flows.
	Expected result:
		Runs one flow after another on each program run
9. Service that outputs invalid JSON
	Expected result: 
		log error
		Exit flow
10. Service that outputs JSON missing 'data' field
	Expected result:
		log error
		Exit flow
11. Error running service
	i.e.
		Permission issue
		File not found
		Stderr produced by service
	Expected result:
		Log error
		Exit flow
12. Input/Ouput data type verification failure
	Expected result:
		Log error
		Exit flow
		
