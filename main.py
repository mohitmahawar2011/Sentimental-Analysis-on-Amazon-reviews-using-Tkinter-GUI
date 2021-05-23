# This is a sample Python script.
from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import Font
import tkinter
import pickle
from PIL.ImageTk import PhotoImage
import pandas as pd
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
class Amazon():
    def __init__(self,root):
        self.master = root
        self.img = ImageTk.PhotoImage(Image.open("amazon_3.png"))
        self.f = Frame(self.master, height=self.master.winfo_screenwidth(), width=self.master.winfo_screenwidth())
        self.f.place(x=0, y=0)
        self.l = Label(self.f, image=self.img)
        self.l.place(x=0, y=0)
        self.myfont = Font(family='Ink Free', size=15, weight='bold')
        self.button2 = Button(self.f, text="Enter Text", height=3, width=40, bg='#f39c12', command=self.text).place(x=600, y=600)

    def text(self):
        self.w = Text(self.f, height=7, width=70, bg='#b3b6b7', font=self.myfont, fg='#273746')
        self.w.place(x=350, y=200)
        print('text')
        self.button1 = Button(self.f, text="Get Result", height=3, width=40, bg='#f39c12', command=self.retrieve_input)
        self.button1.place(x=600, y=600)
        print('bottun 1st')

    def retrieve_input(self):
        self.input = self.w.get("1.0", END)
        self.w.destroy()
        self.button1.destroy()
        self.result_frame = Frame(self.f, height=500, width=500, bg='#fdfefe')
        self.result_frame.place(x=500, y=180)
        print('result frame')
        self.button3 = Button(self.result_frame, text="Back", height=1, width=5, bg='#fdfefe',fg='grey', command=self.back)
        self.button3.place(x=450, y=5)
        print('button 3rd')

        self.result = self.generate_result()
        x=0

        if self.result[0]=='positive':
            print('1st')
            x += 5
            print(x)
            space = 70
            file = '4_1.png'
            text = 'This Review is Positive'

        elif self.result[0]=='neutral':
            x+=3
            file = '4_1.png'
            text = 'This Review is Neutral'
            space =  150
        else:
            x+=1
            file = '4_1.png'
            text = 'This Review is Negative'
            space = 200

        self.lst = [PhotoImage(file=file),PhotoImage(file=file),PhotoImage(file=file),PhotoImage(file=file),PhotoImage(file=file)]
        for i in range(x):
            print('loop')


            logolbl = Label(self.result_frame,image = self.lst[i],bg = 'white')
            logolbl.place(x=(i*70)+space, y=10)

        Label(self.result_frame,text = f"         Status   : {text}\nModel Used :  RandomForest Classification\n\tAccuracy   :  83.70%",font = self.myfont,bg = '#fdfefe',fg = '#273746').place(x = 10,y = 300)

    def generate_result(self):
        self.input = self.preprocessed_reviews(self.input)
        print(self.input)
        df = pd.read_csv(r'final_reviews__.csv')
        print('ok')

        #y_train = df.sentiment

        vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)
        print('reviews')
        X_train = vectorizer.fit_transform(df['Text'].values)
        print(X_train.get_shape())
        print('fitted')
        X_test = vectorizer.transform([self.input])
        print('input fit')
        filename = 'final_last_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(X_test)
        print('result ',result)
        return result
    def back(self):
        self.result_frame.destroy()
        self.__init__(self.master)

    def preprocessed_reviews(self,input):
        sentence = re.sub(r"http\S+", "",input)
        sentence = BeautifulSoup(sentence, 'lxml').get_text()
        sentence = self.decontracted(sentence)
        sentence = re.sub("\S*\d\S*", "", sentence).strip()
        sentence = re.sub('[^A-Za-z]+', ' ', sentence)
        ps = PorterStemmer()
        sentence = ' '.join([ps.stem(word) for word in sentence.split()])
        all_stopwords = stopwords.words('english')
        all_stopwords = set([all_stopwords.remove('not')])
        sentence = ' '.join(e.lower() for e in sentence.split() if e.lower() not in all_stopwords)
        print('sentence :',sentence)
        return sentence

    def decontracted(self,phrase):
        # specific
        phrase = re.sub(r"won't", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)
        # genrel
        phrase = re.sub(r"n\'t'", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        print('phrase is : ',phrase)
        return phrase
root = tkinter.Tk()
root.title("Application")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenwidth()))
root.resizable(False, False)
app = Amazon(root)
root.mainloop()
