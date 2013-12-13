from document import Document as Doc
import os


ALL_SETS = ['s1', 's2', 's3', 's4', 's5']
BASEBALL = 'baseball'
HOCKEY = 'hockey'

BLABEL = 1
HLABEL = -1

STOP_WORDS_NAME = 'stopwords.txt'

class Env:
  sw_set = set()
  data_dir = ''
  train_set = []
  test_set = []
  w2id_dic = {}
  id2w_dic = {}
  w_size = 0
  
  train_docs = []
  test_docs = []

  def __init__(self, stopwords_dir):
    with open(stopwords_dir,'r') as f :
      for line in f :
        Env.sw_set.add(line.strip('\r\n'))

  def init_train_docs(self) :
    for train_id in Env.train_set :
      dir1 = Env.data_dir + '/' + train_id 
      # Init baseball train set
      bas_dir = dir1 + '/' + BASEBALL
      bas_sets = os.listdir(bas_dir)
      for doc_name in bas_sets : 
        if not doc_name.isdigit() :
          continue
        doc_dir = bas_dir + '/' + doc_name
        doc = Doc(doc_name, train_id, BLABEL)
        doc.read_doc()
        Env.train_docs.append(doc)

      # Init hockey train set
      hoc_dir = dir1 + '/' + HOCKEY
      hoc_sets = os.listdir(hoc_dir)
      for doc_name in hoc_sets : 
        if not doc_name.isdigit():
          continue
        doc_dir = hoc_dir + '/' + doc_name
        doc = Doc(doc_name, train_id, HLABEL)
        doc.read_doc()
        Env.train_docs.append(doc)
    
  def init_test_docs(self):
    for test_id in Env.test_sets : 
      dir1 = Env.data_dir + '/' + test_id
      
      # Init baseball test set
      bas_dir = dir1 + '/' + BASEBALL
      bas_sets = os.listdir(bas_dir)
      for doc_name in bas_sets : 
        if not doc_name.isdigit():
          continue
        doc_dir = bas_dir + '/' + doc_name 
        doc = Doc(doc_name, test_id, BLABLE)
        doc.read_doc()
        Env.test_docs.append(doc)
  
      # Init hockey test set
      hoc_dir = dir1 + '/' + HOCKEY
      hoc_sets = os.listdir(hoc_dir)
      for doc_name in hoc_sets : 
        if not doc_name.isdigit():
          continue
        doc_dir = hoc_dir + '/' + doc_name
        doc = Doc(doc_name, train_id, HLABEL)
        doc.read_doc()
        Env.test_docs.append(doc)



  def set_data_set(self, data_dir, test_set_ids):
    Env.data_dir = data_dir
    Env.test_set = test_set_ids
    for x in test_set_ids :
      if x not in ALL_SETS :
        Env.train_set.append(x)

    # Init stop_words list 
    stop_words_dir = Env.data_dir + '/' + STOP_WORDS_NAME
    with open(,'r') as f :
      for line in f :
        Env.sw_set.add(line.strip('\r\n'))



  @staticmethod
  def w2id(word):
    if word in Env.w2idset :
      return Env.w2id_dic[word]
    else :
      Env.w2id_dic[word] = w_size
      Env.id2w_dic[w_size] = word
      w_size += 1
      return w_size - 1

  @staticmethod
  def id2w(id):
    return Env.id2w_dic[id]


  @staticmathod
  def label2str(label):
    if label == BLABEL : 
      return BASEBALL
    else : 
      return HOCKEY

def main():





if __name__ == '__main__' :
  main()







