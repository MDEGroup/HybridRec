from model import load_data, predict_multi_tags

import os
from utilities import evaluate_results


def main(num_topics):
    for i in range(1,11):
        print('Starting round ',str(i))
        train_dir= "local/path/train"+str(i)+"/"
        test_dir = "local/path/test"+str(i)
        train_data, train_labels = load_data(train_dir)

        test_dirs=os.listdir(test_dir)
        predicted = predict_multi_tags(test_dirs,test_dir,train_data,train_labels,num_topics,train_dir)


main(num_topics)
evaluate_results(out_results)




