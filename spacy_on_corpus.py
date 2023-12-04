# import spacy for nlp
import spacy
# import glob in case user enters a file pattern
import glob
# import shutil in case user enters a compressed archive (.zip, .tar, .tgz etc.); this is more general than zipfile
import shutil
# import matplotlib for making graphs
import matplotlib.pyplot as plt
# import wordcloud for making wordclouds
import wordcloud
# import json
import json

def get_token_counts(corpus, tags_to_exclude = ['PUNCT', 'SPACE']):
    """Builds a token frequency table.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param tags_to_exclude: (Coarse-grained) part of speech tags to exclude from the results
    :type tags_to_exclude: list[string]
    :returns: a list of pairs (item, frequency)
    :rtype: list
    """
    # make an empty dictionary called token_counts
    token_counts = {}
    # for each key (named doc_id) in the corpus dictionary

        # if there's a 'doc' key in that entry in the corpus dictionary

            # for each token in that document

                # if the token's coarse-grained part of speech is not in tags_to_exclude

                    # increment the value in token_counts for the key token.text; don't forget to check if token.text is in token_counts first! (3 lines of code)
 
    # return the token counts as a list of pairs
    return list(token_counts.items())

def get_entity_counts(corpus, min_freq = 50, tags_to_exclude = ['QUANTITY']):
    """Builds an entity frequency table.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param tags_to_exclude: named entity labels to exclude from the results
    :type tags_to_exclude: list[string]
    :returns: a list of pairs (item, frequency)
    :rtype: list
    """
    # make an empty dictionary called entity_counts
    entity_counts = {}
    # for each key (named doc_id) in the corpus dictionary

        # if there's a 'doc' key in that entry in the corpus dictionary

            # for each entity in that document

                # if the entity's label is not in tags_to_exclude

                    # increment the value in entity_counts for the key entity.text (3 lines of code)

    # return the entity counts as a list of pairs
    return list(entity_counts.items())

def reduce_to_top_k(frequencies, top_k=25):
    """Gets the top k most frequent items.

    :param frequencies: a list of pairs (item, frequency)
    :type frequencies: list
    :param top_k: the number you want to keep
    :type top_k: int
    :returns: a list of the top k most frequent items
    :rtype: list
    """
    # sort the frequency table by frequency (least to most frequent) 
    frequencies = sorted(frequencies, key=lambda x: x[1])
    # return the top k of them
    return 

def load_textfile(file_name, corpus, nlp):
    """Loads a textfile into a corpus. Doesn't need to return corpus since a corpus once made can be modified as it moves around.

    :param file_name: the path to a text file
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
     """
    pass # take this line out when you have filled in the code below
    # open file_name as f
    
        # make a dictionary containing the key 'doc' mapped to the spacy document for the text in file_name; then in the 'corpus' dictionary add the key file_name and map it to this dictionary
        # uncomment this line and indent appropriately: corpus[file_name] = {'doc': nlp(' '.join(f.readlines()))}

def load_compressed(file_name, corpus, nlp):
    """Loads a zipfile into a corpus. Doesn't need to return corpus since a corpus once made can be modified as it moves around.

    :param file_name: the path to a zipfile
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
   """
    # uncompress the compressed file
    shutil.unpack_archive(file_name, 'temp')
    # for each file_name in the compressed file
    for file_name2 in glob.glob('temp/*'):
        pass # take this line out when you have filled in the code below
        # build the corpus using the contents of file_name2 

    # clean up by removing the extracted files
    shutil.rmtree("temp")

def load_jsonl(file_name, corpus, nlp):
    """Loads a jsonl file into a corpus. Doesn't need to return corpus since a corpus once made can be modified as it moves around.

    :param file_name: the path to a jsonl file
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
     """
    # open file_name as f
    with open(file_name, encoding='utf-8') as f:
        # walk over all the lines in the file
        for line in f.readlines():
                # load the python dictionary from the line using the json package; assign the result to the variabe 'js'
                pass #take this line out when you have filled in the code below
                # if there are keys 'id' and 'fullText' in 'js'

                    # uncomment this line and indent appropriately: corpus[js["id"]] = {'metadata': js, 'doc': nlp(' '.join(js["fullText"]))}
            
def build_corpus(pattern, corpus={}, nlp=spacy.load("en_core_web_sm")):
    """Builds a corpus from a pattern that matches one or more compressed or text files.

    :param pattern: the pattern to match to find files to add to the corpus
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
    :returns: a dictionary mapping document identifiers to document metadata and document NLP output
    :rtype: dict
     """
    try:
        pass # take this line out when you have filled in the code below
        # for each file_name matching pattern

            # if file_name ends with '.zip', '.tar' or '.tgz'

                # then call load_compressed

            # if file_name ends with '.jsonl'

                # then call load_jsonl

            # otherwise (we assume the files are just text)
                # then call load_textfile

    except Exception as e: # if it doesn't work, say why
        print(f"Couldn't load % s due to error %s" % (pattern, str(e)))
    # return the corpus
    return corpus

def get_metadata_counts(corpus, metadata_key):
    """Gets frequency data for the values of a particular metadata key.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param metadata_key: a key in the metadata dictionary
    :type metadata_key: str
    :returns: a dictionary mapping values of the metadata key to their frequencies
    :rtype: dict
    """
    # make an empty dictionary called metadata_counts

    # for each key (named doc_id) in the corpus dictionary

        # if there's a metadata_key key in the metadata for that entry in the corpus dictionary

            # add or increment the value of that dictionary in metadata_counts (3 lines of code!)

  # return the metadata counts as a list of pairs


def get_basic_statistics(corpus):
    """Prints summary statistics for the input corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # print the number of documents in the corpus
 
    # get the token frequency table (instead of None)
    token_counts = None

    # print the number of tokens in the corpus
    print(f'Tokens: %i\n' % sum([x[1] for x in token_counts]))
    # print the number of unique tokens in the corpus

    # get the entity frequency table (instead of None)
    entity_counts = None
    # print the number of entities in the corpus

    # print the number of unique entities in the corpus

    # get the publication year table

    # print the publication year range of the corpus

    # get the page count table

    # print the page count range of the corpus


def plot_word_entity_frequencies(corpus):
    """Makes bar charts for the top k most frequent tokens and entities in the corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # get the token frequency table (instead of None)
    token_counts = None
    # get the top k most frequent tokens (instead of None)
    reduced_token_counts = None
    # make a bar chart for them
    plt.barh([x[0] for x in reduced_token_counts], [x[1] for x in reduced_token_counts])
    plt.tight_layout()
    plt.savefig("token_counts.png")
    plt.clf()
    # get the entity frequency table (instead of None)
    entity_counts = None
    # get the top k most frequent entities (instead of None)
    reduced_entity_counts = None
    # make a bar chart for them
    plt.barh([x[0] for x in reduced_entity_counts], [x[1] for x in reduced_entity_counts])
    plt.tight_layout()
    plt.savefig("entity_counts.png")
    plt.clf()   

def plot_metadata_frequencies(corpus, key):
    """Makes bar charts for the frequencies of values of a metadata key in a corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param key: a metadata key
    :type key: str
    """
    # get the metadata key table (instead of None)

    # make a bar chart for them
    plt.barh([x[0] for x in metadata_counts], [x[1] for x in metadata_counts])
    plt.tight_layout()
    plt.savefig(key + "_counts.png")
    plt.clf()  

def plot_word_cloud(corpus):
    # get the token frequency table (instead of None)
    token_counts = None
    # make the word cloud
    wc = wordcloud.WordCloud(width=800, height=400, max_words=200).generate_from_frequencies(dict(token_counts))
    # plot the word cloud
    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('token_wordcloud.png')
    plt.clf()

def main():
    """The main function. 
      First we ask the user for a pattern. 
      Then, we build a corpus. 
      Then, we let the user choose whether they want corpus statistics, plots of corpus wordcounts, or a wordcloud for the corpus.
    """
    # ask the user to input a zip file, jsonl file or pattern

    print(f'Loading %s, this may take awhile!' % pattern)
    # build the corpus from the pattern (instead of None)
    corpus = None
    # keep going til the user quits with Ctrl-C
    while True:
            # set the goal to something that doesn't exist
        goal = ''
        # until the goal is 'statistics', 'wordcount' or 'wordcloud'

            # ask the user for a value for 'goal' from 'statistics', 'wordcount' or 'wordcloud'

            # if the goal is 'statistics'
                # get basic corpus statistics
            # else if the goal is 'wordcount'
                # plot word and entity counts
            # else if the goal is 'wordcloud'
                # make a wordcloud


# this says, if executing this on the command line like python spacy-on-corpus.py, run main()    
if __name__ == "__main__":
    main()