# Profanity analysis of Twitter tweets using Python library profanity-check


**How profanity-check Works**

profanity-check uses a linear SVM model trained on 200k human-labeled samples of clean and profane text strings. Its model is simple but surprisingly effective, meaning profanity-check is both robust and extremely performant.

**Why Use profanity-check?**

Many profanity detection libraries use a hard-coded list of bad words to detect and filter profanity. For example, profanity uses this wordlist, and even better-profanity still uses a wordlist. There are obviously glaring issues with this approach, and, while they might be performant, these libraries are not accurate at all.

A simple example for which profanity-check is better is the phrase "You cocksucker" - profanity thinks this is clean because it doesn't have "cocksucker" in its wordlist.

**Installation**

$ pip install profanity-check

**Description**

Given a file of tweets and a list of abuses/racial slurs, identify the probability of profanity of Twitter tweets.

The file containg tweets will be called as the "tweet file".  A single column containing the tweets preceeded by the users' Twitter handle. Can be with/without a header. For example,

1. "@User1 tweet"
2. "@user2 tweet"
3. "@user3 tweet"

Python program identifies the probability of profanity per tweet using profanity-check. 

**Inputs Description**


A file containing Twitter handles and their tweets such that each line contains one Twitter handle and tweets. Check any of the example files called "tweets" with extensions "txt" for the correct format.

**Output Description**


A CSV file with 4 columns: "lines", "Probability_of_Profanity", "In_Percentage", - Check "output.csv".

**Program Requirements**

Install "profanity-check" 

**TO DO**


Test with a txt file which is similar to "tweets.txt". The file name should be same because "tweets.txt" is used in the code.If you are changing the input file name please rename it in the code as well.



