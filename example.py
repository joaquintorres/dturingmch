from dturingmch.turingmachine import TuringMachine

simple_turing_machine = TuringMachine()
iset = [
['M','N','P'],
['A','N','A'],
['M','N','P'],
['Á','N','Á'],
[' ',8,' '],
['','',''],
['','',''],
['','','',],
['A','N','O'],
['M','N','D'],
['O','N','I'],
[' ','H','O']
]
tape = "MAMÁ TE AMO" #Lo turbio de este ejemplo es cortesía de VS
simple_turing_machine.load_instruction_set(iset)
simple_turing_machine.load_tape(tape)
simple_turing_machine.run_tape()
new_tape = simple_turing_machine.get_tape()
print(new_tape)
