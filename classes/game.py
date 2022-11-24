class Game():
  """
  This is the overall game class.
  """
  def __init__(self) -> None:
    self.currentZone = 0
    self.gameStatus = False

  def setZone(self, zone):
    """
    This method changes the current zone
    """
    self.currentZone = zone

  def setGameStatus(self, status):
    """
    This method changes the current game status
    """
    self.gameStatus = status

  def getZone(self):
    """
    returns current zone
    """
    return self.currentZone

  def getStatus(self):
    """
    returns current game status
    """
    return self.gameStatus