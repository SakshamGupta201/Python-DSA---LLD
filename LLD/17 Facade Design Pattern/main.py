class CPU:
    def initialize(self):
        print("CPU initialized.")
        
class Memory:
    def load(self):
        print("Memory loaded.")
        
class HardDrive:
    def read(self):
        print("Hard drive read.")
        
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        print("Starting computer...")
        self.cpu.initialize()
        self.memory.load()
        self.hard_drive.read()
        print("Computer started successfully.")
        
class Client:
    def __init__(self):
        self.computer = ComputerFacade()

    def start_computer(self):
        self.computer.start()
        
c = Client()
c.start_computer()