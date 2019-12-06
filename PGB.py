import re

class Band:
  all_bands = []

  @classmethod
  def to_list(cls):
    return all_bands

  def __init__(self, name, band_slogan, members):
    self.name = name
    self.band_slogan=band_slogan
    self.members = members
    self.all_bands.append(self)
    
  def create_from_data(data):
    # data should take the form of:
    # band name, band slogan, Musician name, instrument, solo, intro, repeat

    data = re.split(", |\n",data)
    name = data [0]
    slogan = data [1]
    members = []
    for i in range(2,len(data),4):
      if data[i+1] == "drummer":
        members.append(Drummer(data[i],data[i+2],data[i+3]))
      if data[i+1] == "singer":
        members.append(Singer(data[i],data[i+2],data[i+3]))
      if data[i+1] == "guitarist":
        members.append(Guitarist(data[i],data[i+2],data[i+3]))
      if data[i+1] == "bassist":
        members.append(Bassist(data[i],data[i+2],data[i+3]))
    return Band(name,slogan,members)
  
  def play_solos(self):
    result = ""
    for member in self.members:
      result += member.play_solo()
    return result

  def __repr__(self):
    return self.band_slogan

  def __str__(self):
    return "We go to 11"



class Musician:
  def __repr__(self):
    return "We all just wanna be big rock stars"

  def __str__(self):
    return self.introduction

  def get_instrument(self):
    return self.instrument

  def play_solo(self):
    return self.solo


  def __init__(self, name, instrument, solo, introduction):
    self.name = name
    self.introduction = introduction
    self.instrument = instrument
    self.solo = solo
    
class Drummer (Musician):
  def __init__(self, name, solo, introduction):
    super().__init__(name, "drums", solo, introduction)
  

class Guitarist (Musician):
  def __init__(self, name, solo, introduction):
    super().__init__(name, "guitar", solo, introduction)

class Singer (Musician):
  def __init__(self, name, solo, introduction):
    super().__init__(name, "voice", solo, introduction)

class Bassist (Musician):
  def __init__(self, name, solo, introduction):
    super().__init__(name, "bass", solo, introduction)