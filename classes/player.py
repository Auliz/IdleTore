class Player():
  """
  Overall Player class
  """
  def __init__(self) -> None:
    self.miningLvl = 1
    self.smithingLvl = 1
    self.username = ''

  def setName(self, name):
    """
    sets player name
    """
    self.username = name

  def getName(self):
    """
    gets player name
    """
    return self.username

  # Player method for mining / smelting need to be added here
