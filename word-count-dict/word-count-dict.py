def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    dict={}
    for i in sentences:
        for word in i:
            if word in dict:
                dict[word]+=1
            else:
                dict[word]=1
    return dict