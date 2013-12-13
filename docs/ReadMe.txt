Note:
----
1) "HW01 - Perceptron Implementation - V0.1.ppt" has just the basic explanation pseudocode for implementation.
2) Use folder "data 1" for this task


Time:
----
This task will take approximately 5 hours for good programmer(having knowledge of file read/write, collections like vector, hashtable etc
is good enough)


Submission:
-----------
And please submit your program (both binary and source code) before
October 5, 23:59pm(Beijing time).


============================================================================================
data 1
The data contains two newsgroups, each corresponding to a different topic. 
One is baseball and another is hockey. 
The data has been breaked into five groups of the same size for 5-fold Cross-validation.
Furthermore, each document contains 'From', 'Subject' headers and the main body. 
You can also use this information in your approach.

=============================================================================================
data 2
The data is after preprocessed.
In each data, each line describe an article:
[label] [keyword1]:[value1] [keyword2]:[value2]…
Label(+1, -1) is the classification of the article.
Value_i is how many times (or whether) particular keyword_i appeared in the
article.
You should notice that i is not successive.
This data is also breaked into five groups of the same size for 5-fold
Cross-validation.

==============================================================================================
You can choose either of these two data as your homework.
But we strongly recommend you to try "data 1" first and regard "data 2" as the plan B.

About your task
---------------
Your task is to detect which topic/classification one document belongs to.
The evaluation measures includes precision, recall, and f1 measure.
See the slides for more details.


Good luck!
