class Smithy():
  """
  overall class for smithing
  """
  def __init__(self) -> None:
    self.bronzeActive = False
    self.ironActive = False
    self.steelActive = False

  def startStopBronze(self):
    if self.bronzeActive:
      self.bronzeActive = False
    else:
      self.bronzeActive = True

  def startStopIronBar(self):
    if self.ironActive:
      self.ironActive = False
    else:
      self.ironActive = True

  def startStopSteel(self):
    if self.steelActive:
      self.steelActive = False
    else:
      self.steelActive = True

# methods to add smelted bars to inventory go here