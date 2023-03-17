Spam Email Classifier
This is a Python script that classifies emails as either spam or not spam (ham) using machine learning. The script uses a supervised learning algorithm to train a model on a dataset of emails that have been labeled as either spam or ham.

Prerequisites
To use this script, you need to have the following installed on your system:

Python 3.x
Pip
Scikit-learn
Installation
To install the required packages, run the following command in your terminal:

Copy code
pip install scikit-learn
Usage
To use the script, follow these steps:

Download or clone this repository to your local machine.
Open a terminal window and navigate to the directory where the repository is located.
Run the following command to train the model:
Copy code
python train.py
The script will train the model on the dataset and save the model to a file named spam_classifier.pkl.

The script will output either "SPAM" or "HAM" depending on whether the email is classified as spam or not.
Dataset
The dataset used to train the model is the SpamAssassin Public Corpus. The dataset consists of over 5,000 labeled emails, with approximately 40% of them being spam.

License
This script is released under the MIT License. See the LICENSE file for more details.
