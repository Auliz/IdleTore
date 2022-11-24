class Mine():
  """
  overall class for mining
  """
  def __init__(self) -> None:
    self.copperActive = False
    self.tinActive = False
    self.ironActive = False
    self.coalActive = False

  def startStopCopper(self):
    if self.copperActive:
      self.copperActive = False
    else:
      self.copperActive = True

  def startStopTin(self):
    if self.tinActive:
      self.tinActive = False
    else:
      self.tinActive = True

  def startStopIronOre(self):
    if self.ironActive:
      self.ironActive = False
    else:
      self.ironActive = True

  def startStopCoal(self):
    if self.coalActive:
      self.coalActive = False
    else:
      self.coalActive = True

# methods to add ore to inventory go here