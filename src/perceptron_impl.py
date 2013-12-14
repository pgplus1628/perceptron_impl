import numpy as np
import pprint
import time


class Perceptron:

  def __init__(self, _dt, _y, alpha=0.25, nit=500, eps=0.1):
    self.D, self.V = _dt.shape
    self.dt = _dt
    self.y = _y
    self.alpha = alpha
    self.nit = nit
    self.w = np.zeros((self.V,), dtype=float)
    self.eps = eps

  def train(self):
    w = np.copy(self.w)
    for it in range(self.nit):
      old_w = np.copy(w)
      for itd in range(self.D):
        x = self.dt[itd]
        p = sum(x * w)
        if self.y[itd] * p <= 0.0:
          w += self.alpha * self.y[itd] * x

      self.w = np.copy(w)

      # Calculate eps
      _eps = 0.0
      for i in range(len(self.w)):
        _eps += abs(w[i] - old_w[i])

      print ' >>> Perceptron >>>  iteration %d  >>  %f' % (it, _eps)
      if _eps < self.eps:
        return self.w
    return self.w

  def test(self, _dt, y):
    d, v = _dt.shape
    p = 0.0
    #test_res = np.zeros((d,), dtype=float)
    test_res = []
    for itd in range(d):
      p += sum(self.w * _dt[itd])
      test_res.append(p)

    tp, tn, fp, fn = 0.0, 0.0, 0.0, 0.0

    for it in range(d):
      y1 = test_res[it]
      y2 = y[it]
      if y1 > 0.0 and y2 > 0.0:
        tp += 1
      elif y1 > 0.0 > y2:
        fp += 1
      elif y1 < 0.0 < y2:
          fn += 1
      elif y1 < 0.0 and y2 < 0.0:
        tn += 1

    pre = tp / (tp + fp)
    rec = tp / (tp + fn)
    f1 = 2 * (pre * rec) / (pre + rec)
    return pre, rec, f1



