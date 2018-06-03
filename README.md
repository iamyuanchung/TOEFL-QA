# TOEFL-QA: A question answering dataset for machine comprehension of spoken content

Authors: Bo-Hsiang Tseng & [Yu-An Chung](https://iamyuanchung.github.io)

The dataset was originally collected by [Tseng et al. (2016)](https://arxiv.org/abs/1608.06378), and later used in [Fang et al. (2016)](https://arxiv.org/abs/1608.07775) and [Chung et al. (2018)](https://arxiv.org/abs/1711.05345). We make the dataset publicly available to encourage more research on this challenging task. If you have any questions about this dataset, do not hesitate to shoot me an <a href="mailto:iamyuanchung@gmail.com">email</a>.

# Introduction
Multimedia or spoken content presents more attractive information than plain text content, but it's more difficult to display on a screen and be selected by a user. As a result, accessing large collections of the former is much more difficult and time-consuming than the latter for humans. It's highly attractive to develop a machine which can automatically understand spoken content and summarize the key information for humans to browse over. In this endeavor, we propose a new task of machine comprehension of spoken content. We define the initial goal as the listening comprehension test of [TOEFL](https://en.wikipedia.org/wiki/Test_of_English_as_a_Foreign_Language), a challenging academic English examination for English learners whose native language is not English.

In this test, the subjects would first listen to an audio story around five minutes and then answer several question according to that story. The story is related to the college life such as conversation between the student and the professor or a lecture in the class. Each question has four choices where only one is correct. A real example in the TOEFL examination is shown in the following figure. The questions in TOEFL are not simple even for a human with relatively good knowledge because the question cannot be answered by simply matching the words in the question and in the choices with those in the story, and key information is usually buried by many irrelevant utterances. To answer the questions like "Why does the professor mention Issac Newton?", the listeners have to understand the whole audio story and draw the inferences to answer the question correctly.

![](https://github.com/iamyuanchung/TOEFL-QA/blob/master/example.png)

# Data
The collected TOEFL dataset includes 963 examples in total (717 for training, 124 for validation, 122 for testing). Each example consists of a story, a question, and 4 choices.

# Existing Models
Evaluation metric: Accuracy on the test set

|                                                                |  Acc. on test set  |
|:--------------------------------------------------------------:|:------------------:|
|  [Sukhbaatar et al. (2015)](https://arxiv.org/abs/1503.08895)  |         45.2       |
|     [Tseng et al. (2016)](https://arxiv.org/abs/1608.06378)    |         42.5       |
|     [Fang et al. (2016)](https://arxiv.org/abs/1608.07775)     |         49.1[code (Torch)](https://github.com/sunprinceS/Hierarchical-Attention-Model)       |
|     [Chung et al. (2018)](https://arxiv.org/abs/1711.05345)    |         56.1[code (TensorFlow)](https://github.com/chun5212021202/QACNN)       |

# Citation
If you use the dataset in your work, please cite the following two papers as:
```
@inproceedings{tseng2016towards,
  title     = {Towards machine comprehension of spoken content: Initial TOEFL listening comprehension test by machine},
  author    = {Tseng, Bo-Hsiang and Shen, Sheng-Syun and Lee, Hung-Yi and Lee, Lin-Shan},
  booktitle = {INTERSPEECH},
  year      = {2016}
}
```
and
```
@inproceedings{chung2018supervised,
  title     = {Supervised and unsupervised transfer learning for question answering},
  author    = {Chung, Yu-An and Lee, Hung-Yi and Glass, James},
  booktitle = {NAACL HLT},
  year      = {2018}
}
```
