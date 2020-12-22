from model import load_data, predict_multi_tags

import os
from utilities import evaluate_results


def main():
    for i in range(1,11):
        print('Starting round ',str(i))
        train_dir= "C:/Users/claudio/Desktop/ten_folder_100/train"+str(i)+"/"
        test_dir = "C:/Users/claudio/Desktop/ten_folder_100/test"+str(i)
        train_data, train_labels = load_data(train_dir)

        test_dirs=os.listdir(test_dir)
        predicted = predict_multi_tags(test_dirs,test_dir,train_data,train_labels,10,train_dir)


main()
evaluate_results('results.csv')




