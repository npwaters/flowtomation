import sys


parameters = "$$ input is $$"
if "$$" in parameters:
    parameters = parameters.replace("$$", "the_std_input")

sys.exit()
