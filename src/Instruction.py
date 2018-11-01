class Instruction:
  'This is the instruction class which holds info on weight,opcode,sources,destinations and instruction type'
  def __init__(self, opcode):
    self.opcode = opcode

  def set_weight(self, weight):
    self.weight = weight
  
  def set_curr_weight(self, weight):
    self.currWeight = weight

  def reset_curr_weight(self):
    self.currWeight = self.weight

  def set_sources(self,sources):
    self.sources = sources
    self.currSources = []

  def set_destinations(self, destinations):
    self.destinations = destinations
    self.currDestinations = []
  
  def set_isa_extension(self, isa_extension):
    self.isaExtension = isa_extension

  def set_instruction_type(self, instruction_type):
    self.instructionType = instruction_type

  def set_instruction_size(self, instruction_size):
    self.instructionSize = instruction_size

  def return_string(self):
    InstructionString = "Instruction:"
    if hasattr(self,"opcode"):
      InstructionString = InstructionString + " opcode: " + self.opcode
    if hasattr(self,"sources"):
      InstructionString = InstructionString + " sources: "
      for i in self.sources: InstructionString = InstructionString + i + ","
    if hasattr(self,"destinations"):
      InstructionString = InstructionString + " destinations: "
      for i in self.destinations: InstructionString = InstructionString + i + ","
    if hasattr(self,"isaExtension"):
      InstructionString = InstructionString + " isa_extension: "
      for i in self.isaExtension: InstructionString = InstructionString + i + ","
    if hasattr(self,"weight"):
      InstructionString = InstructionString + " weight: " + str(self.weight)
    return InstructionString

  def instruction_asm_string(self):
    asmString = self.opcode
    asmString = asmString + " "
    for i in self.currDestinations: asmString = asmString + i + ","
    for i in range(len(self.sources)): 
      if i < (len(self.sources)-1):
        asmString = asmString + str(self.currSources[i]) + ","
      else:
        asmString = asmString + str(self.currSources[i]) + "\n"
    return asmString

  def reset_fields(self):
    self.currSources = []
    self.currDestinations = []
