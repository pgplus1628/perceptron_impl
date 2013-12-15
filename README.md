perceptron_impl
===============
## Directory Explain
src/ 程序的位置
doc/ 课程ppt
data/ 数据集

## Implementation
Perceptorn.py : perceptron的具体实现
main.py : 
environment.py : 做一些预处理的工作，读取数据，计算tf * idf

### Feature
为了减少运行的时间，在特征提取的时候做了一些过滤的工作
1. 通过正则表达式获取一个doc中所有的word `re.compile('\w+')`
2. 过滤stoword
3. 过滤len(word) < 3 的word

特征为tf * idf


### Run
在main.py中
分用s1,s2,s3,s4,s5作为测试的数据集，对模型进行训练和测试，计算 precision, recall, f1 和平均 f1

## How to run
cd src/
python main.py

## Result
运行时间 : 4:08
平均F1   : 0.938317


  zork% time python main.py
  [ Initialize ] start
   >>> init_idf Document = 1989 Term = 19722
   >>> init_idf ok
  [ Initialize ] initialize ok
  [ GLOBAL ] test_set ["s1"]
  [ Construct DT matrix and Y vector ] start
  [ Construct DT matrix and Y vector ] ok
  [ Load Train DT and Y ] start
  [ Load Train DT and Y ] ok
  [ Train ] start
   >>> Perceptron >>>  iteration 0  >>  40.899775
   >>> Perceptron >>>  iteration 1  >>  12.946972
   >>> Perceptron >>>  iteration 2  >>  5.007185
  [ Train ] ok
  [ Load Test DT and Y ] start
  [ Load Test DT and Y ] ok
  [ Test ] start
  [ Test ] ok
  [ Test ] pre = 0.951087 rec = 0.879397 f1 = 0.913838
  [ GLOBAL ] test_set ["s2"]
  [ Construct DT matrix and Y vector ] start
  [ Construct DT matrix and Y vector ] ok
  [ Load Train DT and Y ] start
  [ Load Train DT and Y ] ok
  [ Train ] start
   >>> Perceptron >>>  iteration 0  >>  41.799309
   >>> Perceptron >>>  iteration 1  >>  20.444892
   >>> Perceptron >>>  iteration 2  >>  11.452164
   >>> Perceptron >>>  iteration 3  >>  2.111887
  [ Train ] ok
  [ Load Test DT and Y ] start
  [ Load Test DT and Y ] ok
  [ Test ] start
  [ Test ] ok
  [ Test ] pre = 0.950249 rec = 0.959799 f1 = 0.955000
  [ GLOBAL ] test_set ["s3"]
  [ Construct DT matrix and Y vector ] start
  [ Construct DT matrix and Y vector ] ok
  [ Load Train DT and Y ] start
  [ Load Train DT and Y ] ok
  [ Train ] start
   >>> Perceptron >>>  iteration 0  >>  47.791042
   >>> Perceptron >>>  iteration 1  >>  16.627511
   >>> Perceptron >>>  iteration 2  >>  6.221138
   >>> Perceptron >>>  iteration 3  >>  1.933865
  [ Train ] ok
  [ Load Test DT and Y ] start
  [ Load Test DT and Y ] ok
  [ Test ] start
  [ Test ] ok
  [ Test ] pre = 0.963918 rec = 0.939698 f1 = 0.951654
  [ GLOBAL ] test_set ["s4"]
  [ Construct DT matrix and Y vector ] start
  [ Construct DT matrix and Y vector ] ok
  [ Load Train DT and Y ] start
  [ Load Train DT and Y ] ok
  [ Train ] start
   >>> Perceptron >>>  iteration 0  >>  44.016033
   >>> Perceptron >>>  iteration 1  >>  20.266837
   >>> Perceptron >>>  iteration 2  >>  3.971557
  [ Train ] ok
  [ Load Test DT and Y ] start
  [ Load Test DT and Y ] ok
  [ Test ] start
  [ Test ] ok
  [ Test ] pre = 0.923858 rec = 0.914573 f1 = 0.919192
  [ GLOBAL ] test_set ["s5"]
  [ Construct DT matrix and Y vector ] start
  [ Construct DT matrix and Y vector ] ok
  [ Load Train DT and Y ] start
  [ Load Train DT and Y ] ok
  [ Train ] start
   >>> Perceptron >>>  iteration 0  >>  46.562782
   >>> Perceptron >>>  iteration 1  >>  18.808117
   >>> Perceptron >>>  iteration 2  >>  4.345077
  [ Train ] ok
  [ Load Test DT and Y ] start
  [ Load Test DT and Y ] ok
  [ Test ] start
  [ Test ] ok
  [ Test ] pre = 0.954315 rec = 0.949495 f1 = 0.951899
  [ Average ]  average_f1 = 0.938317
  python main.py  247.77s user 0.85s system 99% cpu 4:08.66 total
  
    
