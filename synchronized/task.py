import multiprocessing

IDLE = "IDLE"
RUNNING = "RUNNING"

class Task:
	def __init__(self, function, args):
		self.function = self.targetFunction = function
		self.args = self.arguments = args
		self.parentConnection, self.childConnection = multiprocessing.Pipe()
		self.returnValue = None
		self.process = multiprocessing.Process(target=self.targetFunction, args=args)
		self.status = IDLE
		
	def start(self):
		self.process.start()
		self.status = RUNNING
		
	def stop(self):
		self.process.terminate()
		self.process = multiprocessing.Process(target=self.targetFunction, args=args)
		self.status = IDLE
