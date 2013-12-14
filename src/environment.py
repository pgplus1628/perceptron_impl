import os
import re
import pprint
import json

ALL_SET = ['s1', 's2', 's3', 's4', 's5']

BASEBALL = 'baseball'
HOCKEY = 'hockey'

BLABEL = 1
HLABEL = -1
STOP_WORDS_NAME = 'stopwords.txt'


def label2str(label):
  if label == BLABEL:
    return BASEBALL
  else:
    return HOCKEY


class Env:
  sw_set = set()
  data_dir = ''
  train_set = []
  test_set = []
  w2id_dic = {}
  id2w_dic = {}
  w_size = 0

  all_docs = []

  def __init__(self):
    pass

  @staticmethod
  def load_sw_set():
    _dir = os.path.abspath(os.path.join(Env.data_dir, os.path.pardir)) + '/' + STOP_WORDS_NAME
    with open(_dir, 'r') as f:
      for line in f:
        Env.sw_set.add(line.strip('\r\n'))

  @staticmethod
  def w2id(word):
    if word in Env.w2id_dic:
      return Env.w2id_dic[word]
    else:
      Env.w2id_dic[word] = Env.w_size
      Env.id2w_dic[Env.w_size] = word
      Env.w_size += 1

  @staticmethod
  def id2w(wid):
    return Env.id2w_dic[wid]

  @staticmethod
  def load_all_doc():
    for set_id in ALL_SET:
      dir1 = Env.data_dir + '/' + set_id

      #Init baseball set
      bas_dir = dir1 + '/' + BASEBALL
      bas_set = os.listdir(bas_dir)
      for doc_name in bas_set:
        if not doc_name.isdigit():
          continue
        doc = Doc(doc_name, set_id, BLABEL)
        doc.read_doc()
        Env.all_docs.append(doc)

      #Init hockey set
      hoc_dir = dir1 + '/' + HOCKEY
      hoc_set = os.listdir(hoc_dir)
      for doc_name in hoc_set:
        if not doc_name.isdigit():
          continue
        doc = Doc(doc_name, set_id, HLABEL)
        doc.read_doc()
        Env.all_docs.append(doc)

  @staticmethod
  def set_data_set(data_dir):
    Env.data_dir = data_dir

  @staticmethod
  def set_test_set(test_set_ids):
    Env.test_set = test_set_ids
    for x in ALL_SET:
      if x not in Env.test_set:
        Env.train_set.append(x)


class Doc:

  ddir = ''

  dname = ''
  set_id = 0
  label = 0
  w_count = {}

  def __init__(self, dname, set_id, label):
    self.dname = dname
    self.set_id = set_id
    self.label = label
    self.ddir = Env.data_dir + '/' + set_id + '/' + label2str(label) + '/' + dname

  def __extract_raw_words(self):
    with open(self.ddir) as f:
      ss = f.read()
      return set(re.findall(re.compile('\w+'), ss.lower()))

  def __extract_valid_ids(self, wlist):
    for w in wlist:
      if w not in Env.sw_set:
        wid = Env.w2id(w)
        _v = self.w_count.get(wid, 0)
        self.w_count[wid] = int(_v) + 1

  def read_doc(self):
    all_words = self.__extract_raw_words()
    self.__extract_valid_ids(all_words)

  def __repr__(self):
    return json.dumps(self.w_count)


def main():
  data_dir = '../data/data 1'
  Env.set_data_set(data_dir)
  Env.load_sw_set()
  Env.load_all_doc()
  pprint.pprint(Env.all_docs)


if __name__ == '__main__':
  main()










