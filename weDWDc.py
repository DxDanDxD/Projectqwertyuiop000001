from dataclasses import dataclass

@dataclass
class Player:
 name:
 role: str
 playerid:
 status: bool
 def setstatus(self, newstatus: bool):
  self.status=newstastus
  def heal(self):
   self.setstatus(True)
  def kill(self, victimname):

   self.setstatus(False)
  def nightaction(self):
   if self.role=='mf':
    kill()


