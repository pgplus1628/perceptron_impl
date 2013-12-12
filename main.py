
from environment import Environment as Env
import pprint


STOP_WORDS_DIR = '../data/stopwords.txt'


def main():

  env = Env(STOP_WORDS_DIR)
  pprint.pprint(env.sw_set)






if __name__ == '__main__' :
  main()

