import os
import re
import pprint
import json
import numpy as np

ALL_SET = ['s1', 's2', 's3', 's4', 's5']

BASEBALL = 'baseball'
HOCKEY = 'hockey'

BLABEL = 1
HLABEL = -1
STOP_WORDS_NAME = 'stopwords.all'


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
  idf = {}

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
    if word not in Env.w2id_dic:
      Env.w2id_dic[word] = Env.w_size
      Env.id2w_dic[Env.w_size] = word
      Env.w_size += 1

    return Env.w2id_dic[word]

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

  @staticmethod
  def init_idf():
    D = len(Env.all_docs)
    T = Env.w_size

    print ' >>> init_idf Document = %d Term = %d' % (D, T)

    for t in range(T):
      nt = 0
      for d in Env.all_docs:
        if t in d.tf:
          nt += 1

      Env.idf[t] = np.log(D * 1.0 / nt)

    print ' >>> init_idf ok '


class Doc:

  def __init__(self, dname, set_id, label):
    self.dname = dname
    self.set_id = set_id
    self.label = label
    self.ddir = Env.data_dir + '/' + set_id + '/' + label2str(label) + '/' + dname
    self.tfidf_bool = False
    self.tf = {}
    self.tfidf = {}
    self.word_num = 0

  def __extract_raw_words(self):
    with open(self.ddir) as f:
      ss = f.read()
      all_w = re.findall(re.compile('\w+'), ss.lower())
      self.word_num = len(all_w)
      return all_w

  def __extract_valid_ids(self, wlist):
    for w in wlist:
      if w in Env.sw_set:
        continue
      if len(w) <= 3:
        continue

      wid = Env.w2id(w)
      if wid not in self.tf:
        self.tf[wid] = 0
      self.tf[wid] += 1

  def read_doc(self):
    all_words = self.__extract_raw_words()
    self.__extract_valid_ids(all_words)

  def __cal_tfidf(self):
    for _t in self.tf.keys():
      self.tfidf[_t] = (1.0 * self.tf[_t] / self.word_num) * Env.idf[_t]

  def get_tfidf(self):
    if not self.tfidf_bool:
      self.__cal_tfidf()
      self.tfidf_bool = True

    return self.tfidf

  def __repr__(self):
    return json.dumps(self.tf)


def main():
  data_dir = '../data/data 1'
  Env.set_data_set(data_dir)
  Env.load_sw_set()
  Env.load_all_doc()
  #pprint.pprint(Env.all_docs)
  #pprint.pprint(Env.w_size)
  with open('words_list', 'w') as fout:
    pprint.pprint(Env.w2id_dic, fout)

if __name__ == '__main__':
  main()

