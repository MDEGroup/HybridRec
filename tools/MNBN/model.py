from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
import glob, os
import operator
from sklearn.feature_extraction.text import TfidfVectorizer

from utilities import get_actual_tags, map_MNB_to_path, calculate_metrics



def load_multi_data(src_path):
    #Loading the dataset
    print('Loading the dataset')
    X = []
    y = []
    formats=['*.atl', '*.asm','*.ocl', '.*ecore']
    for category in os.listdir(src_path):
        model_path=src_path+category+'/'
        for f in formats:
            file_list = glob.glob(os.path.join(model_path,f ))

            for file_path in file_list:
                f=open(file_path,'r', encoding="utf-8", errors="ignore")
                data=f.read()

            X.append(data)
            y.append(category)
    print(len(X))
    print(len(y))
    return X, y


def load_data(src_path):
    #Loading the dataset
    print('Loading the dataset')
    X = []
    y = []
    for category in os.listdir(src_path):
        model_path=src_path+category+'/'
        file_list = glob.glob(os.path.join(model_path, '*.txt'))
        for file_path in file_list:
            f=open(file_path,'r', encoding="utf-8", errors="ignore")
            data=f.read()

            X.append(data)
            y.append(category)


    print(len(X))
    print(len(y))
    return X, y




def predict_multi_tags(dirs, test_dir, train_data, labels, num_topics,train_dir):
    ###Extracting features
    time_testing = 0
    print('Extracting features from dataset')
    count_vect = TfidfVectorizer(input='train', stop_words={'english'}, lowercase=True, analyzer='word')
    train_vectors = count_vect.fit_transform(train_data)
    train_vectors.shape
    tfidf_transformer = TfidfTransformer()
    train_tfidf = tfidf_transformer.fit_transform(train_vectors)
    train_tfidf.shape
    print('Training a Multinomial Naive Bayes (MNB)')
    out_dict = {}
    clf = MultinomialNB()

    predicted_topics = {}

    for d in dirs:

        for f in os.listdir(test_dir + "/" + d):

            #print(freq)
            test = open(test_dir + "/" + d + "/" + f, "r", encoding="utf-8", errors="ignore")
            i = 0
            list_topics = []
            # var = input("Please enter a code snippet: ")
            docs_new = [test.read()]

            X_new_counts = count_vect.transform(docs_new)
            X_new_tfidf = tfidf_transformer.transform(X_new_counts)
            predicted = clf.fit(train_tfidf, labels).predict(X_new_tfidf)
            # print(X_new_tfidf)
            # print(clf.predict_proba(X_new_tfidf))
            for prob in clf.predict_proba(X_new_tfidf):
                for cat, p in zip(clf.classes_, prob):
                    # print(cat+":"+str(p))
                    out_dict.update({cat: str(p)})
                    ranked_dict = sorted(out_dict.items(), key=operator.itemgetter(1), reverse=True)

            while i < num_topics:
                for tupla in ranked_dict:
                    # print(str(i)+" "+tupla[0])
                    list_topics.append(tupla[0])
                    #print(str(tupla))

                    i = i + 1
                    if i == num_topics:
                        predicted_topics.update({f: list_topics})

                        break

        out_results0 = open("results_1_topics.csv", "a+", encoding="utf-8",
                           errors="ignore")
        out_results1 = open("results_2_topics.csv", "a+", encoding="utf-8",
                           errors="ignore")
        out_results2 = open("results_3_topics.csv", "a+", encoding="utf-8",
                            errors="ignore")
        out_results3 = open("results_4_topics.csv", "a+", encoding="utf-8",
                            errors="ignore")
        out_results4 = open("results_5_topics.csv", "a+", encoding="utf-8",
                            errors="ignore")

        actual=get_actual_tags('lib_tags.csv')

        calculate_metrics(test_dir + "/" + d, out_results0,out_results1, out_results2, out_results3,out_results4, actual, predicted_topics)

        file_csv = open("training_data.csv", "a+", encoding="utf-8", errors="ignore")



    actual = get_actual_tags('lib_tags.csv')
    for key, value in predicted_topics.items():
        file_csv.write(str(map_MNB_to_path(key.strip(),'top_tag_lib_no_dups.csv'))+',' + ",".join([str(elem) for elem in value]) + "\n")


    return predicted_topics

def predict_topics(test, train_data, labels,recommended_list):
    ###Extracting features
    time_testing = 0
    print('Extracting features from dataset')
    count_vect = TfidfVectorizer(input='train', stop_words={'english'}, lowercase=True, analyzer='word')
    train_vectors = count_vect.fit_transform(train_data)
    train_vectors.shape
    tfidf_transformer = TfidfTransformer()
    train_tfidf = tfidf_transformer.fit_transform(train_vectors)
    train_tfidf.shape
    print('Training a Multinomial Naive Bayes (MNB)')
    ###train model
    clf = MultinomialNB()

    documents=[]
    i = 0
    list_topics = []
    # var = input("Please enter a code snippet: ")
    atl_input = [test.read()]

    X_new_counts = count_vect.transform(atl_input)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    cat=str(clf.fit(train_tfidf, labels).predict(X_new_tfidf)).replace("[","").replace("]","").replace("\'","")
    print(cat)
    folder_rec='C:/Users/claudio/Desktop/train_atl/'+ cat

    for file in os.listdir(folder_rec):
        doc= open(folder_rec+"/"+file, "r", encoding="utf-8", errors= "ignore")
        documents.append(doc.read())

    recommended_list.update({test.name: documents})

    return recommended_list





    # for fold in dirs:
    #     for f in os.listdir(test_dir + fold):
    #
    #         test = open(test_dir + "/" + fold + "/" + f, "r", encoding="utf-8", errors="ignore")
    #         i = 0
    #         list_topics = []
    #         # var = input("Please enter a code snippet: ")
    #         atl_input = [test.read()]
    #
    #         X_new_counts = count_vect.transform(atl_input)
    #         X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    #         cat=str(clf.fit(train_tfidf, labels).predict(X_new_tfidf)).replace("[","").replace("]","").replace("\'","")
    #         folder_rec='C:/Users/claudio/Desktop/train_atl/'+ cat
    #
    #         for file in os.listdir(folder_rec):
    #             doc= open(folder_rec+"/"+file, "r", encoding="utf-8", errors= "ignore")
    #             documents.append(doc.read())
    #
    #         for d in documents:
    #             print(d)
    #
    #         recommended_list.update({test.name: documents})

            #glove_sematic_sim(test.read(),documents,stopwords)

