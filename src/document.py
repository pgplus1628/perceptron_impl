from environment import Env
from environment import BASEBALL 
from environment import HOCKEY
from environment import BLABEL
from environment import HLABEL

import re

class Document:

  self.ddir = ''

  self.label = 0;
  self.w_count = {}
  self.dname = ''
  self.set_id = ''


  def __init__(self, dname, set_id, label):
    self.dname = dname
    self.set_id = set_id
    self.ddir = Env.data_dir + '/' + set_id + '/' + Env.label2str(label) + '/' + dname
    self.label = label
  

  def __extract_raw_words(self):
    with open(self.ddir, 'r') as f :
      ss = f.read()
      return set(re.findall(re.compile('\w+'), ss.lower()))

  def __extract_valid_ids(self, wlist):
    for w in wlist : 
      if w not in Env.sw_set : 
        wid = Env.w2id(w)
        self.w_count[wid] += 1


  def read_doc(self):
      all_words = self.__extract_raw_words()
      self.__extract_valid_ids(all_worlds)
      


