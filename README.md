# Profanity analysis of Twitter tweets using Python library profanity-check


**How profanity-check Works**

profanity-check uses a linear SVM model trained on 200k human-labeled samples of clean and profane text strings. Its model is simple but surprisingly effective, meaning profanity-check is both robust and extremely performant.

**Why Use profanity-check?**

Many profanity detection libraries use a hard-coded list of bad words to detect and filter profanity. For example, profanity uses this wordlist, and even better-profanity still uses a wordlist. There are obviously glaring issues with this approach, and, while they might be performant, these libraries are not accurate at all.

A simple example for which profanity-check is better is the phrase "You cocksucker" - profanity thinks this is clean because it doesn't have "cocksucker" in its wordlist.

**Installation**

$ pip install profanity-check

**Short Description**

Given a file of tweets and a list of abuses/racial slurs, identify the probability of profanity of Twitter tweets.



