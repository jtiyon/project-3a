# Analyzing Corpora with Spacy (Two)

# Project 3a

## Name
Joshua Iyonsi
## Class year
2026
## Extension(s) - Describe your extension(s) here

## Resources - Who or what did you use to finish this project deliverable?
ChatGPT
Michael Ofori Tenkorang Jr 

-----------------------------------------------------------------------------------------------------------------------------------------------
*Please do not edit below this line!*
-----------------------------------------------------------------------------------------------------------------------------------------------

## Project Description

The goals of this assignment are:
* To analyze corpora with metadata.
* To make some basic corpus-level visualizations.

Here are the steps you should do to successfully complete this project:
1. From moodle, accept the assignment. Open and set up a code space (install a python kernel and select it).
2. Complete the notebook and commit it to Github. Make sure to answer all questions, and to commit the notebook in a "run" state!
3. I wrote the comments; you write the code! Complete and run `spacy_on_corpus.py` following the instructions in this notebook.
4. Edit the README.md file. Provide your name, your class year, links to/descriptions of any extensions and a list of resources. 
5. Commit your code often. We will take the last commit before the deadline as your submission of the project.

Possible extensions (from least points to most points; if you do an extension, it should be different from any extension you did for project 2d):
* Make word counts plots for the top 100 words and entities. Look at the labels on the y axis of each plot. Where do you think spaCy is making mistakes?
* Augment the `wordcount` functionality so that it displays relative frequencies of entity label pairs and token part of speech pairs.
* Augment the `wordcloud' functionality so that it also makes an entity cloud.
* Make the bar plots and/or word clouds more beautiful.
* Learn about the useful python collections package, especially the [Counter data type](https://docs.python.org/3/library/collections.html#collections.Counter). Copy spacy_on_corpus.py and name the copy spacy_on_corpus_counter.py. Change `get_token_counts` and `get_entity_counts` to use counters. 
* Add in the analyses from project 2c as functions `make_doc_markdown`, `make_doc_tables` and `make_doc_stats`; make sure to ask the user for a document before running any of these!
* Your other ideas are welcome! If you'd like to discuss one with Dr Stent, feel free.

## Project Rubric

- [] Notebook is code-complete. (3 points)
- [] All ten questions in notebook are completely and correctly answered. (10 points)
- [] File spacy_on_corpus.py is complete, runs and is commented. (10 points)
- [] Readme has student's name, class year and resources student used. (2 points)
- [] Extension (1-2 points for a start; 3-4 points for a complete extension; 5 points for a surprising and creative extension)

### Comments from grader
