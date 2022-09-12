import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfVectorGenerator:
    def __init__(self,model_dir,size=100):
        filename = 'tfidf.pkl'

        self.model_dir=model_dir
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)
        self.model_file_path = os.path.join(self.model_dir,filename)
        self.vec_size=size
        self.vectorizer = None

    def vectorize(self, cleaned_questions):
        if os.path.exists(self.model_file_path):
            with open(self.model_file_path,"rb") as input_file:
                self.vectorizer = pickle.load(input_file)
        else:
            self.vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
            self.vectorizer.fit(cleaned_questions)
            with open(self.model_file_path,"wb") as output_file:
                pickle.dump(self.vectorizer,output_file)
        
        transformed_X=[]
        if self.vectorizer:
            transformed_X_csr = self.vectorizer.transform(cleaned_questions)
            transformed_X = transformed_X_csr.A
        return transformed_X

    def query(self,user_message):
        transformed_user_array = None
        try:
            transformed_user = self.vectorizer.transform([user_message])
            transformed_user_array = transformed_user.toarray()
        except Exception as e:
            print(e)
            return "Maaf, saya belum memahami maksud pertanyaan Anda. Coba lagi dengan kalimat sederhana"
        
        return transformed_user_array




