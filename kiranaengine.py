import csv
from email.mime import base
import os
import pandas as pd
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics.pairwise import cosine_similarity

from tfidfvectorgenerator import TfidfVectorGenerator

class KiranaEngine:
    def __init__(self,faq,type='tfidf') -> None:
        print("setup kirana engine")
        nltk_data_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"tmp/nltk")
        nltk.data.path.append(nltk_data_path)
        if not (os.path.exists(nltk_data_path)):
            os.makedirs(nltk_data_path)
            nltk.download('punkt', download_dir=nltk_data_path)
        self.faq=faq
        self.stemmer = StemmerFactory().create_stemmer()
        self.le = LE()
        self.classifier = None
        self.build_model(type)
        
    
    def cleanup(self, sentence):
        word_tokenized = nltk.word_tokenize(sentence)
        stemmed_words = [self.stemmer.stem(w) for w in word_tokenized]
        return ' '.join(stemmed_words)
    
    def build_model(self,type):
        model_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"models")
        self.vectorizer = TfidfVectorGenerator(model_dir_path)
        dataframelist = [pd.read_csv(csvfile, sep='\t').dropna() for csvfile in self.faq]
        self.data = pd.concat(dataframelist,ignore_index=True)
        self.questions = self.data['question'].values

        questions_cleaned = []
        for question in self.questions:
            questions_cleaned.append(self.cleanup(question))

        X = self.vectorizer.vectorize(questions_cleaned)

        print("data - "+self.data)

        if 'Class' not in list(self.data.columns):
            return
        
        y = self.data['Class'].values.tolist()
        if len(set(y)) < 2:
            return
        
        y = self.le.fit_transform(y)

        trainx,testx,trainy,testy = tts(X,y,test_size=.25,random_state=42)
        self.classifier = SVC(kernel='linier')
        self.classifier.fit(trainx,trainy)
    
    def query(self,user_message):
        try:
            cleaned_user=self.cleanup(user_message)
            t_usr_array = self.vectorizer.query(cleaned_user)
            if self.classifier:
                prediction = self.classifier.predict(t_usr_array)[0]
                class_ = self.le.inverse_transform([prediction])[0]
                questionset = self.data[self.data['class']==class_]
            else:
                questionset = self.data
            
            cos_sims=[]
            for question in questionset['question']:
                cleaned_question = self.cleanup(question)
                question_arr = self.vectorizer.query(cleaned_question)
                sims = cosine_similarity(question_arr,t_usr_array)
                cos_sims.append(sims)
            
            if len(cos_sims)>0:
                ind = cos_sims.index(max(cos_sims))
                return self.data['answer'][questionset.index[ind]]            
        except Exception as e:
            print(e)
            return "Maaf, saya belum memahami maksud pertanyaan Anda. Coba lagi dengan kalimat sederhana😊"




if __name__=="__main__":
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")
    faqlist = [os.path.join(base_path,"sapaan.tsv"),os.path.join(base_path,"faq.tsv")]

    # data = pd.read_csv(base_path+"/sapaan.tsv", sep='\t')
    