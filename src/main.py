from perceptron_impl import Perceptron
from environment import Env
import numpy as np


def main():
  # Config
  data_dir = '../data/data 1'
  test_set_ids = ['s5']

  # Parameters
  alpha = 0.25
  nit = 500

  # Initialize
  Env.set_data_set(data_dir)
  Env.load_sw_set()
  Env.load_all_doc()
  Env.init_idf()

  # Construct DT matrix and Y vector
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

  # Load Train DT and Y
  for itd in len(train_docs):
    doc = train_docs[itd]
    tfidf_dic = doc.get_tfidf()
    vec = np.zeros(V, dtype=float)
    for _k, _v in tfidf_dic:
      vec[int(_k)] = _v
    DT[itd] = vec
    Y[itd] = doc.label

  # Train
  mod = Perceptron(DT, Y, alpha, nit)
  mod.train()

  # Load test DT and Y
  DT_test = np.zeros((len(test_docs), V), dtype=float)
  Y_test = np.zeros((len(test_docs)))

  for itd in len(test_docs):
    doc = test_docs[itd]
    tfidf_dic = doc.get_tfidf()
    vec = np.zeros(V, dtype=float)
    for _k, _v in tfidf_dic:
      vec[int(_k)] = _v
    DT_test[itd] = vec
    Y_test[itd] = doc.label

  pre, rec, f1 = mod.test(DT_test, Y_test)

  print pre, rec, f1


if __name__ == '__main__':
  main()