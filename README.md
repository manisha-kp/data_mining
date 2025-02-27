# Comparison of Machine learning and deep learning algorithms for text classification

**Objective**: The goal of this study is to analyze and compare the performance of various machine learning (ML) and deep learning (DL) algorithms for text classification.

**Methodology**:

1.  Split training and testing data:

    First we split the data into training, validation and test data and save the test data in a csv file. We do this step before any preprocessing to prevent data leakage.

2.  Preprocessing: Preprocessing plays a crucial role in determining model performance. The following steps are applied to clean and prepare the text data:

    -   Convert text to **lowercase**

    -   Remove **special characters, numbers, and punctuation**

    -   **Tokenize** the text

    -   Remove **stop words**

    -   Apply **lemmatization**

    -   **Vectorization**: Convert text into numerical features using **TF-IDF**

3.  Model training: Both ML and DL models are trained and evaluated. The models tested include:

    -   **Machine Learning:** Linear Support Vector Machine (SVM), Naïve Bayes, Random Forest

    -   **Deep Learning:** BERT, LSTM

    Among these, **Linear SVM and BERT achieved the highest accuracy of 81%**.

4.  **Evaluation Metrics**\
    Model performance is assessed using the **classification report**, which includes:

    -   **Accuracy**

    -   **Precision**

    -   **Recall**

    -   **F1-score**

5.  **Conclusion**: The comparison highlights that while traditional ML models like **Linear SVM** perform well for text classification, deep learning models such as **BERT** provide competitive or superior results. The choice between ML and DL depends on factors such as dataset size, computational resources, and interpretability requirements.
