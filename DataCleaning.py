# Databricks notebook source
# Filter row by stop words
def not_in_stop_words(row):
  
  content = row.content.split(' ')
  final_content = []
  
  for word in content:
    if word not in stop_words and len(word) >= 2:
      final_content.append(word)
      
  return final_content



import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

# Dataset
# Load the files first in the Data section
news_df = sqlContext.read.load('/FileStore/tables/articles1.csv', 
                          format='com.databricks.spark.csv', 
                          header='true', 
                          inferSchema='true')

# Stopwords
stop_words = set(stopwords.words('english'))

filtered_news = news_df.rdd.map(not_in_stop_words)
