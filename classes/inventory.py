from time import time, sleep

class Inventory():
  """
  overall inventory class
  """
  def __init__(self, copper, tin, iron, coal, bronzeBar, ironBar, steelBar) -> None:
    self.copperOreAmnt = copper
    self.tinOreAmnt = tin
    self.ironOreAmnt = iron
    self.coalOreAmnt = coal
    self.bronzeBarAmnt = bronzeBar
    self.ironBarAmnt = ironBar
    self.steelBarAmnt = steelBar

  def addCopper(self):
    sleep(1)
    # print(self.addCopperToInventory())?
    self.copperOreAmnt += 1
    print(self.copperOreAmnt)