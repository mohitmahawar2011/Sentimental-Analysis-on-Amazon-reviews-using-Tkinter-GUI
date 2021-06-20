# Sentimental-Analysis-on-Amazon-reviews-using-Tkinter-GUI
this project is sentimental Analysis on Amazon food reviews using Tkinter GUI Interface.

<h1 align="center">Amazon Food Reviews - NLP</h1>

## :file_folder: Dataset
The dataset used can be downloaded here (Kaggle) - [Click to Download](https://www.kaggle.com/snap/amazon-fine-food-reviews)

<ol>
Machine-Learning Objective

NLP is a field in machine learning with the ability of a computer to understand, analyze, manipulate, and potentially generate human language.

This project mainly focuses on Sentiment Analysis of Amazon Food Reviews. Various methods ranging from wordvectors to complex deep learning methods are used in this project.

</ol>

## Preprocessing
- Data Cleaning - Deduplications
- Removing html tags , punctuations and set of special characters like , or . or # etc .
- Checking if the word is made up of english letters and not alpha numeric characters .
- Converting to lowercase .
- Removal of stopwords .
- Stemming of words .

## Featurization
<ol>It is necessary to convert the words in vector format for NLP tasks . So used following methods to convert words in vector format .
</ol>

- Bag of Words (BoW)
- Bi-Grams and N-Grams
- TF-IDF (Term Frequency–Inverse Document Frequency)
- Average Word2Vec
- TF-IDF weighted Word2vec

- Word2Vec is the most popular technique to learn word embeddings . Embeddings are the vector representation of words and it is capable of capturing context of a word in a document , semantic and syntatic similarity , relation with other words , etc .

## Implementations

- Dimensionality Reduction using t-SNE , PCA
- Logistic Regression
- SGD for linear Regression
- Support Vector Machines
- Random Forests and GBDT
- KMeans , Agglomerative and Hierarchical Clustering methods (Unsupervised)
- Create Confusion matrix

### type of Sentiment :
---
![Screenshot (39)](https://user-images.githubusercontent.com/75325526/122684789-45b45080-d225-11eb-815f-7348093c1c82.png)

### Confusion matrix :
---
![Screenshot (35)](https://user-images.githubusercontent.com/75325526/122684770-2289a100-d225-11eb-9fa5-fcf684e49a80.png)


## deployment
 Using Tkinter GUI interface

![Screenshot (33)](https://user-images.githubusercontent.com/75325526/122684736-d5a5ca80-d224-11eb-94e6-05a128719990.png)

### Predicted Sentiment :
![Screenshot (34)](https://user-images.githubusercontent.com/75325526/122684758-0be34a00-d225-11eb-8875-08bfec771b5d.png)

---
#### prediction Accuracy Score - 83.70%  (great)
