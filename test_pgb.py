from PGB import Band, Musician, Drummer, Guitarist, Singer, Bassist
import pytest

def test_create_musician():
  ringo = Musician("Ringo", "drums","We all live on a yellow submarine", "I'm everyone's least favorite beatle")

  assert ringo.name == "Ringo"
  assert ringo.instrument == 'drums'
  assert ringo.introduction == "I'm everyone's least favorite beatle"
  assert ringo.solo == "We all live on a yellow submarine"


def test_create_drummer():
  ringo = Drummer("Ringo","We all live on a yellow submarine", "I'm everyone's least favorite beatle")

  assert ringo.name == "Ringo"
  assert ringo.instrument == 'drums'
  assert ringo.introduction == "I'm everyone's least favorite beatle"
  assert ringo.solo == "We all live on a yellow submarine"

def test_create_band():
  John_n_Yoko = Band.create_from_data("Yoko Ono Band, We're better than the Beatles, John, guitarist, Yesterday, all my troubles se... BANG! SPLAT! , I <3 Yoko, Yoko, singer, Walking on thin ice, I'm paying the price , It's being the center of the universe")

  assert John_n_Yoko.band_slogan == "We're better than the Beatles"


def test_band_solo():
  John_n_Yoko = Band.create_from_data("Yoko Ono Band, We're better than the Beatles, John, guitarist, Yesterday all my troubles se... BANG! SPLAT! , I <3 Yoko, Yoko, singer, Walking on thin ice I'm paying the price , It's being the center of the universe")

  assert John_n_Yoko.play_solos() == "Yesterday all my troubles se... BANG! SPLAT! Walking on thin ice I'm paying the price "

def test_bands_to_list():
  Band.create_from_data("Yoko Ono Band, We're better than the Beatles, John, guitarist, Yesterday all my troubles se... BANG! SPLAT! , I <3 Yoko, Yoko, singer, Walking on thin ice I'm paying the price , It's being the center of the universe")
  Band.create_from_data("The Zombies, Braaaaains, Kurt, guitarist, I swear I don't have a gun , come as you are, Amy, singer, They tried to make me go to reahab , rehab is for quitters, Mama Cass, singer, I'm californa dreamin' , mmmm ham 'n' cheese")

  assert Band.all_bands[0].band_slogan=="We're better than the Beatles"
  assert Band.all_bands[1].name=="The Zombies"

@pytest.fixture(autouse=True)
def clean():
    Band.all_bands = []