




class Environment:
  sw_set = set()
  data_set_dir = ''
  train_set = []
  test_set = []

  def __init__(self, stopwords_dir):
    with open(stopwords_dir,'r') as f :
      for line in f :
        self.sw_set.add(line.strip('\r\n'))


  def init_data_set(self, data_dir, test_set_ids):
    





