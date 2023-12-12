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
    for doc_id in corpus.keys():
        # if there's a 'doc' key in that entry in the corpus dictionary
        if 'doc' in corpus[doc_id]:
            # for each token in that document
            for token in corpus[doc_id]['doc']:
                
                #if maintags wanted
                if 'leaveMainTags' in tags_to_exclude:
                    #check if tag is one of specified
                    if token.pos_ not in ['NOUN', 'VERB','ADJ', 'ADV','PROPN']:
                        #add to tags to exclude
                        tags_to_exclude.append(token.pos_)

                # if the token's coarse-grained part of speech is not in tags_to_exclude
                if token.pos_ not in tags_to_exclude:
                    # increment the value in token_counts for the key token.text; don't forget to check if token.text is in token_counts first! (3 lines of code)
                    if token.text not in token_counts:
                        token_counts[token.text] = 1
                    else:
                        token_counts[token.text] += 1
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
    for doc_id in corpus.keys():
        # if there's a 'doc' key in that entry in the corpus dictionary
         if 'doc' in corpus[doc_id]:
            # for each entity in that document
            for ent in corpus[doc_id]['doc'].ents:
                
                #check if maintags wanted
                if 'leaveMainTags' in tags_to_exclude:
                    #check if the entity's label is  one of the specified
                    if ent.label_ not in ['ORG', 'LOC', 'PERSON','GPE']:
                        #if so add the label in tags_to_exclude
                        tags_to_exclude.append(ent.label_)
                    
                # if the entity's label is not in tags_to_exclude
                if ent.label_ not in tags_to_exclude:
                    # increment the value in entity_counts for the key entity.text (3 lines of code)
                    if ent.text not in entity_counts:
                        entity_counts[ent.text] = 1
                    else:
                        entity_counts[ent.text]+=1
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
    end_index = (len(frequencies))
    start_index = end_index - top_k
    return frequencies[start_index : end_index]

def load_textfile(file_name, corpus, nlp):
    """Loads a textfile into a corpus. Doesn't need to return corpus since a corpus once made can be modified as it moves around.

    :param file_name: the path to a text file
    :type file_name: string
    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    :param nlp: a spaCy engine
    :type nlp: spaCy engine
     """
    # open file_name as f
    with open(file_name, 'r') as f:
        # make a dictionary containing the key 'doc' mapped to the spacy document for the text in file_name; then in the 'corpus' dictionary add the key file_name and map it to this dictionary
        corpus[file_name] = {'doc': nlp(' '.join(f.readlines()))}

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
        ##account for jsonl file in zip
        if file_name2.endswith('.jsonl'):
            ## then call load_jsonl
                load_jsonl(file_name2, corpus, nlp)
        else:
            #build the corpus using the contents of file_name2
            load_textfile(file_name2, corpus, nlp)
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
            js = json.loads(line)
            # if there are keys 'id' and 'fullText' in 'js'
            if 'id' in js.keys() and 'fullText' in js.keys():
                corpus[js["id"]] = {'metadata': js, 'doc': nlp(' '.join(js["fullText"]))}
            
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
        ## Set the max_length attribute for the spaCy engine
        nlp.max_length = 1500000
        # for each file_name matching pattern
        for file_name in glob.glob(pattern):
            # if file_name ends with '.zip', '.tar' or '.tgz'
            if file_name.endswith(('.zip', '.tar', '.tgz')):
                # then call load_compressed
                load_compressed(file_name, corpus, nlp)
            # if file_name ends with '.jsonl'
            elif file_name.endswith('.jsonl'):
                # then call load_jsonl
                load_jsonl(file_name, corpus, nlp)
            # otherwise (we assume the files are just text)
            else:
                # then call load_textfile
                load_textfile(file_name, corpus, nlp)

    except Exception as e: # if it doesn't work, say why
        print(f"Couldn't load % s due to error %s" % (pattern, str(e)))

    finally:
        ## Reset max_length to its default value to avoid affecting other parts of your code
        nlp.max_length = 1000000

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
    metadata_counts = {}
    # for each key (named doc_id) in the corpus dictionary
    for doc_id in corpus.keys():
        # if there's a metadata_key key in the metadata for that entry in the corpus dictionary
        if metadata_key in corpus[doc_id]['metadata'].keys():
            # add or increment the value of that dictionary in metadata_counts (3 lines of code!)
            if corpus[doc_id]['metadata'][metadata_key] not in metadata_counts:
                metadata_counts[corpus[doc_id]['metadata'][metadata_key]] = 1
            else:
                metadata_counts[corpus[doc_id]['metadata'][metadata_key]] += 1
    # return the metadata counts as a list of pairs
    return list(metadata_counts.items())


def get_basic_statistics(corpus):
    """Prints summary statistics for the input corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # print the number of documents in the corpus
    print(f'Document: {len(corpus)}\n')
    # get the token frequency table (instead of None)
    token_counts = get_token_counts(corpus)
    # print the number of tokens in the corpus
    print(f'Tokens: %i\n' % sum([x[1] for x in token_counts]))
    # print the number of unique tokens in the corpus
    print(f'Unique tokens: %i\n' % len(token_counts))
    # get the entity frequency table (instead of None)
    entity_counts = get_entity_counts(corpus)
    # print the number of entities in the corpus
    print(f'Entities: %i\n' % sum([x[1] for x in entity_counts]))
    # print the number of unique entities in the corpus
    print(f'Unique entities: %i\n' % len(entity_counts))
    # get the publication year table
    publication_years = get_metadata_counts(corpus, 'publicationYear')
    ##sort pub years from smallest-largest
    sorted_pub_years = sorted(publication_years, key=lambda x:x[0])
    # print the publication year range of the corpus
    ##print(f'Publication year range: {sorted_pub_years[0][0]}-{sorted_pub_years[-1][0]}\n')
    # get the page count table
    pgCounts = get_metadata_counts(corpus, 'pageCount')
    ## sort pgcount table
    sorted_pgCounts = sorted(pgCounts, key=lambda x:x[0])
    # print the page count range of the corpus
    ##print(f'Page count range: {sorted_pgCounts[0][0]}-{sorted_pgCounts[-1][0]}\n')


def plot_word_entity_frequencies(corpus, k=25):
    """Makes bar charts for the top k most frequent tokens and entities in the corpus.

    :param corpus: a dictionary mapping document identifiers to document metadata and document NLP output
    :type corpus: dict
    """
    # get the token frequency table (instead of None)
    token_counts = get_token_counts(corpus, tags_to_exclude= ['leaveMainTags'])
    # get the top k most frequent tokens (instead of None)
    reduced_token_counts = reduce_to_top_k(token_counts, k)
    # make a bar chart for them
    plt.barh([x[0] for x in reduced_token_counts], [x[1] for x in reduced_token_counts])
    plt.xlabel('Frequency')
    plt.ylabel('Tokens')
    plt.title(f'Top {k} Most Frequent Tokens')
    plt.tight_layout()
    plt.savefig("token_counts.png")
    plt.clf()

    # get the entity frequency table (instead of None)
    entity_counts = get_entity_counts(corpus, tags_to_exclude=['leaveMainTags'])
    # get the top k most frequent entities (instead of None)
    reduced_entity_counts = reduce_to_top_k(entity_counts, k)
    # make a bar chart for them
    plt.barh([x[0] for x in reduced_entity_counts], [x[1] for x in reduced_entity_counts])
    plt.xlabel('Frequency')
    plt.ylabel('Entities')
    plt.title(f'Top {k} Most Frequent Entities')
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
    metadata_counts = get_metadata_counts(corpus, key)
    # make a bar chart for them
    plt.barh([x[0] for x in metadata_counts], [x[1] for x in metadata_counts])
    plt.xlabel('Frequency')
    plt.ylabel(f'{key}_Counts')
    plt.title(f"Top Most Frequent {key}_Counts")
    plt.tight_layout()
    plt.savefig(key + "_counts.png")
    plt.clf()  

def plot_word_cloud(corpus):
    # get the token frequency table (instead of None)
    token_counts = get_token_counts(corpus, tags_to_exclude=['leaveMainTags'])
    # make the word cloud
    wc = wordcloud.WordCloud(width=800, height=400, max_words=200).generate_from_frequencies(dict(token_counts))
    # plot the word cloud
    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('Top Word WordCloud')
    plt.savefig('token_wordcloud.png')
    plt.clf()

def main():
    """The main function. 
      First we ask the user for a pattern. 
      Then, we build a corpus. 
      Then, we let the user choose whether they want corpus statistics, plots of corpus wordcounts, or a wordcloud for the corpus.
    """
    # ask the user to input a zip file, jsonl file or pattern
    pattern = input('Input a zip file, jsonl file, or pattern: ')
    print(f'Loading %s, this may take awhile!' % pattern)
    # build the corpus from the pattern (instead of None)
    corpus = build_corpus(pattern)
    # keep going til the user quits with Ctrl-C
    while True:
            # set the goal to something that doesn't exist
        goal = ''
        # until the goal is 'statistics', 'wordcount' or 'wordcloud'
        while goal not in ('statistics', 'wordcount', 'wordcloud', 'metadatafreq'):
            # ask the user for a value for 'goal' from 'statistics', 'wordcount', 'metadatafreq' or 'wordcloud'
            goal = input("set your goal['statistics', 'wordcount', 'wordcloud', 'metadatafreq']").lower()
            print(f'You want to get: {goal}')
            # if the goal is 'statistics'
            if goal == 'statistics':
                # get basic corpus statistics
                get_basic_statistics(corpus)
            # else if the goal is 'wordcount'
            elif goal == 'wordcount':
                # plot word and entity counts
                plot_word_entity_frequencies(corpus)
            ##else if the goal is 'metadataFreq'
            elif goal == 'metadatafreq':
                #ask for meta_data_key
                key = input("Which metadata frequency do you seek?['publicationYear', 'pageCount']:")
                #plot metadatafreq
                plot_metadata_frequencies(corpus, key)
            ##
            # else if the goal is 'wordcloud'
            elif goal == 'wordcloud':
                # make a wordcloud
                plot_word_cloud(corpus)

# this says, if executing this on the command line like python spacy-on-corpus.py, run main()    
if __name__ == "__main__":
    main()