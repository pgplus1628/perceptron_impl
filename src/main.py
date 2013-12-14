from perceptron_impl import Perceptron
from environment import Env
import numpy as np
import pprint


def main():
  # Config
  data_dir = '../data/data 1'
  test_set_ids = ['s5']

  # Parameters
  alpha = 0.25
  nit = 500

  # Initialize
  print '[ Initialize ] start'
  Env.set_data_set(data_dir)
  Env.load_sw_set()
  Env.load_all_doc()
  Env.init_idf()
  print '[ Initialize ] initialize ok'

  # Construct DT matrix and Y vector
  print '[ Construct DT matrix and Y vector ] start'
  train_docs = []
  test_docs = []

  for doc in Env.all_docs:
    if doc.set_id in test_set_ids:
      test_docs.append(doc)
    else:
      train_docs.append(doc)

  V = Env.w_size
  DT = np.zeros((len(train_docs), V), dtype=float)
  Y = np.zeros(len(train_docs), dtype=float)
  print '[ Construct DT matrix and Y vector ] ok'

  # Load Train DT and Y
  print '[ Load Train DT and Y ] start'
  for itd in range(len(train_docs)):
    doc = train_docs[itd]
    tfidf_dic = doc.get_tfidf()
    vec = np.zeros(V, dtype=float)
    for _k, _v in tfidf_dic.items():
      vec[int(_k)] = _v
    #TODO
    pprint.pprint(vec.nonzero())

    DT[itd] = vec
    Y[itd] = doc.label
  print '[ Load Train DT and Y ] ok'

  # Train
  print '[ Train ] start'
  mod = Perceptron(DT, Y, alpha, nit)

  #TODO
  pprint.pprint(DT.nonzero())

  mod.train()
  print '[ Train ] ok'

  # Load test DT and Y
  print '[ Load Test DT and Y ] start'
  DT_test = np.zeros((len(test_docs), V), dtype=float)
  Y_test = np.zeros((len(test_docs)))

  for itd in range(len(test_docs)):
    doc = test_docs[itd]
    tfidf_dic = doc.get_tfidf()
    vec = np.zeros(V, dtype=float)
    for _k, _v in tfidf_dic.items():
      vec[int(_k)] = _v
    DT_test[itd] = vec
    Y_test[itd] = doc.label
  print '[ Load Test DT and Y ] ok'

  # Test 
  print '[ Test ] start'
  pre, rec, f1 = mod.test(DT_test, Y_test)
  print '[ Test ] ok'
  print '[ Test ] pre = %f rec = %f f1 = %f' % (pre, rec, f1)


if __name__ == '__main__':
  main()
