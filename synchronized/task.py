import multiprocessing

class Task:
	def __init__(self, function, args):
		self.targetFunction = function
		self.parentConnection, self.childConnection = multiprocessing.Pipe()
		
	def task(self, conn):
		conn.send(
		
