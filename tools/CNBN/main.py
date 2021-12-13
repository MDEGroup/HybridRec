from github_crawling.MNB import load_data, predict_topics
import time
import os

model = 'CNB'
for i in range(1,11):
    print('*'*40)
    print('round'+str(i))
    train_dir = "./D1/train"+str(i)+'/'
    test_dir = "./D1/test"+str(i)+'/'

    dirs = os.listdir(test_dir)

    train_data, train_labels = load_data(train_dir)
    predict_topics(dirs, test_dir, train_data, train_labels, 20, "test_"+str(i)+".txt", model)



