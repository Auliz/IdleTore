from classes.inventory import Inventory as inv


class Player(inv):
  """
  Overall Player class inherits from inventory
  """

  def __init__(self, username) -> None:
    super().__init__(copper=0, tin=0, iron=0, coal=0, bronzeBar=0, ironBar=0, steelBar=0)
    self.miningLvl = 1
    self.smithingLvl = 1
    self.username = username

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
