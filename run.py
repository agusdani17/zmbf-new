import os,sys
if len(sys.argv) == 2:
	if sys.argv[1] == "log":
		__import__("log").make()
	elif sys.argv[1] == "nolog":
		__import__("nolog").make()
