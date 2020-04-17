#First draft with adequate dictionary used as an instruction set
DEFAULT_TAPE = [' ']
DEFAULT_MV = 0
DEFAULT_DICT = [['A','N','X'],['B','H','P']]
DEFAULT_CHAR = ' '

class TuringMachine:
	def __init__(self):
		self._tape = DEFAULT_TAPE
		self._dict = DEFAULT_DICT
		self._mv_ptr = DEFAULT_MV
		self._rd_buf = DEFAULT_CHAR
		self._tapelen = 1
	
	def load_tape(self,new_tape):
		self._tape = list(new_tape)
		self._tapelen = len(self._tape)
	
	def get_tape(self):
		aux = "".join(self._tape)
		return aux
	
	def append_tape(self,extra_tape):
		self._tape.append(list(extra_tape))
	
	def load_instruction_set(self,instr_set):
		self._dict = instr_set
	
	def get_instruction_set(self):
		return self._dict
	
	def append_instruction(self,rd,mv,wr):
		self._dict.append([rd,mv,wr])
	# 'do all' function, could be more modular
	def run_tape(self):
		while(True):
			self._rd_buf = self._tape[self._mv_ptr] 
			self._tape[self._mv_ptr] = self._dict[self._mv_ptr][2] 
			if (self._rd_buf == self._dict[self._mv_ptr][0]): #hardcoded
				if (self._dict[self._mv_ptr][1] == 'N'):
					self._mv_ptr+=1
				elif (self._dict[self._mv_ptr][1] == 'P'):
					self._mv_ptr-=1
				elif (self._dict[self._mv_ptr][1] == 'H'):
					return self._tape
				else:
					self._mv_ptr = self._dict[self._mv_ptr][1]
			if(self._mv_ptr == self._tapelen):
				self._tape.append(' ')
