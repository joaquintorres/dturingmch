# dturingmch
A very ~~dumb~~ simpleminded and limited implementation of a Turing machine as a Python class, meant only for refreshing some of Python's OOP syntax. The curious example used came from an anecdote I heard about a Computational Linguistics student's asignment.
As of yet, it uses a simple character list (fed as a string) as the "infinite tape", and a properly formatted list of lists as the instruction set, which should be of the same length as the tape. Each instruction has three elements: 
1. A character against which to compare the tape-read value.
1. A hardcoded string that indicates whether the machine should move forwards (```'N'```), backwards (```'P'```), to a particular instruction (an ```int``` value), or halt operations (```'H'```).
1. A character to replace the current one if it's the same as the one read on the first step.

Methods for the ```TuringMachine``` class are straightforward: getters and setters for the instruction set and the tape that use lists and strings respectively. When a tape has been run, the machine keeps only the modified version of the tape, so it's probably a good idea to store it in a variable first before feeding it.

No particular effort was put into error handling or testing since I don't intend this to serve any practical purpose, although I'll probably add a to-do list for the class stuff I wanted to mess around with and didn't get to test (and to fix some nasty things that look ugly even in something useless).
