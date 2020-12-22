import os, shutil
from nltk.stem import PorterStemmer
from pathlib import Path
import pandas as pd
import csv
import matplotlib as plt


def count_files(train_dir):
    list = os.listdir(train_dir)  # dir is your directory path
    number_files = len(list)
    return number_files

def get_method_invs(src,dst):

    for f in os.listdir(src):
        list_invs=[]
        with open(src+f,'r',encoding='utf-8',errors='ignore') as focus:

            for line in focus:
                method= str(line).strip().split('#')
                list_invs.append(method[1])


        print(len(list_invs))
        with open(dst+f,'w',encoding='utf-8',errors='ignore') as res:
            for i in list_invs:
                res.write(i+'\n')


def delete_less_support(train_dir,dst,limit):

    for folder in os.listdir(train_dir):
        #print(folder)
        support=count_files(train_dir+folder)
        if support >= limit:
            shutil.move(train_dir+folder,dst+folder)
            print(folder)


def delete_empty_files(rootdir):
    for root, dirs, files in os.walk(rootdir):
        # for d in ['RECYCLER', 'RECYCLED']:
        #     if d in dirs:
        #         dirs.remove(d)

        for f in files:
            fullname = os.path.join(root, f)
            try:
                if os.path.getsize(fullname) == 0:
                    print(fullname)
                    os.remove(fullname)
            except WindowsError:
                continue


def ten_folder(root_folder, temp):
    tags=os.listdir(root_folder)
    for t in tags:
        print(t)
        #for file in os.listdir(root_folder+t.strip()):

        os.mkdir(temp+t.strip())


def move_files(t, root, train_path, test_path):

    i=0
    tot = len(os.listdir("C:/Users/Claudio/Desktop/ten_folder_100/root/"+t+"/"))
    test = 1
    train = tot - test
    print(test, train)
    flag = True

    for file in sorted(os.listdir(root), key=lambda v: v.upper()):
        print(file)
        if flag:
            shutil.move(root + file, test_path + file) #1

            i = i + 1
            if i == test:
                break

            print(file)

        else:
            #shutil.copy(root + file, train_path + file) #2
            shutil.copy(test_path+file, train_path + file) #3 cambia in test


def remove_test(test_path, train_path,temp_path):
    for tr in os.listdir(train_path):
        for ts in os.listdir(test_path):
            if tr == ts:
                print('moved')
                shutil.move(train_path+tr,temp_path+tr)




def compute_metrics(act_topics, pred_topics, out_results, repo):

    out_results.write(repo + ",")
    if act_topics:
        #act_topics = remove_not_featured("topics_134.txt", act_topics)

        ##add language
        # pred_topics=pred_topics[:len(act_topics)]
        # out_results.write("actual topics [" + ','.join([str(elem) for elem in act_topics]) + "]" + "\n")
        # out_results.write("predicted topics [" + ','.join([str(elem) for elem in pred_topics]) + "]" + "\n")
        pred_topics = remove_dashes(pred_topics)
        act_topics = remove_dashes(act_topics)
        pred_topics, act_topics = stemming_topics(pred_topics, act_topics)

        for x in range(1, 11):
            ##act_topics = composed_word_h(act_topics)
            out_results.write(str(success_rate(pred_topics, act_topics, x)) + ",")
        out_results.write(str(precision(pred_topics, act_topics)) + ",")
        out_results.write(str(recall(pred_topics, act_topics)) + ",")
        out_results.write(str(top_rank(pred_topics, act_topics)) + "\n")


def calculate_metrics(test_dataset, out_results0,out_results1, out_results2, out_results3, out_results4, actual, predicted):

    for f in os.listdir(test_dataset):
        #print(f)

        ##get user topics

        act_topics, six_topics, seven_topics, eight_topics, nine_topics,ten_topics= get_n_tags(actual, key_actual=str(f).strip().replace('.txt', ''), dict_predicted=predicted,
                                             key_predicted= str(f).strip() )
        compute_metrics(act_topics, six_topics,out_results0,f)
        compute_metrics(act_topics, seven_topics, out_results1, f)
        compute_metrics(act_topics, eight_topics, out_results2, f)
        compute_metrics(act_topics, nine_topics, out_results3, f)
        compute_metrics(act_topics, ten_topics, out_results4, f)




def get_actual_tags(file_tags):

    with open(file_tags, mode='r',encoding='utf-8',errors='ignore') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: rows[2:] for rows in reader}


    return mydict



def get_n_tags(dict_actual,key_actual,dict_predicted,key_predicted):
    list_actual=dict_actual.get(key_actual)
    list_predicted=dict_predicted.get(key_predicted)
    return list_actual,list_predicted[0:1],list_predicted[0:2], list_predicted[0:3], list_predicted[0:4], list_predicted[0:5]



def stemming_topics(predicted,actual):
    stemmer = PorterStemmer()
    stemmed_pred=[]
    stemmed_act=[]
    for p in predicted:
        stemmed_pred.append(stemmer.stem(p))
    for a in actual:
        stemmed_act.append(stemmer.stem(a))
    return stemmed_pred , stemmed_act


def success_rate(predicted, actual, n):
    if actual:
        match = [value for value in predicted if value in actual]
        if len(match) >= n:
            return 1
        else:
            return 0
    else:
        return -1


def precision(predicted,actual):
    if actual:
        true_p = len([value for value in predicted if value in actual])
        false_p = len([value for value in predicted if value not in actual])
        return (true_p / (true_p + false_p))*100
    else:
        return -1


def recall(predicted,actual):
    if actual:
        true_p = len([value for value in predicted if value in actual])
        false_n = len([value for value in actual if value not in predicted])
        return (true_p/(true_p + false_n))*100
    else:
        return -1


def top_rank(predicted,actual):
    top = predicted.pop(0)
    if top in actual:
        predicted.insert(0, top)
        return 1
    else:
        return 0





def remove_dashes(actual):
    result=[]
    for topic in actual:
        if topic.find("-")!=-1:
            result.append(topic.replace("-",""))
        else:
            result.append(topic)
    return result


def compute_avg_metrics(file_path):

    #for file in os.listdir(file_path):
    df_cut_n=pd.read_csv(file_path,sep=',',encoding='utf-8',error_bad_lines=False)
    df_cut_n.columns=['name','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','precision','recall','top_rank']

    df_mean=df_cut_n.describe().iloc[1,:]
    print(df_mean)

    return df_mean
    #print(df_cut_n.describe().to_csv('avg_'+file_path))




def  map_MNB_to_path(t,file_lib):
    #df_training = pd.read_csv(file_training,encoding='utf-8',error_bad_lines=False)
    #df_training.columns=['name','tag1','tag2','tag3','tag4','tag5']
    #print(df_training)
    df_lib=pd.read_csv(file_lib,error_bad_lines=False, encoding='utf-8')
    #print(df_lib)
    #dict_lib={}

    for lib,path in zip(df_lib['name'],df_lib['path']):
        if str(t).replace('.txt','') == str(lib):
            #dict_lib.update({t:path})
            return path


def get_stats(lib_csv, predicted_csv):
    dict_actual={}
    dict_predicted={}

    with open(lib_csv, mode='r', encoding='utf-8', errors='ignore') as infile:
        r = csv.reader(infile)
        dict_actual.update( {rows[1]: rows[2:] for rows in r})


    with open('dataset_stats.csv','w', errors='ignore', encoding='utf-8') as stat:
        with open(predicted_csv, mode='r', encoding='utf-8', errors='ignore') as infile:
            reader = csv.reader(infile, delimiter=';')
            for rows in reader:
                for key, value in dict_actual.items():
                    if rows[0] == str(key).strip():
                        stat.write(str(rows[0])+','+','.join([str(elem) for elem in dict_actual.get(key)])+'\n')


def evaluate_results(out_file):
    with open(out_file,'w',encoding='utf-8',errors='ignore') as m:
        m.write('N_tags'+','+'s1'+','+'s2'+','+'s3'+','+'s4'+','+'s5'+','+'s6'+','+'s7'+','+'s8'+','+'s9'+','+'s10'+','+'precision'+','+'recall'+','+','+'top_rank \n')
        for i in range(1,6):
            avg=compute_avg_metrics('results_'+str(i)+'_topics.csv')
            list_results=avg.values.tolist()
            m.write(str(i)+','+','.join([str(elem) for elem in list_results])+'\n')


