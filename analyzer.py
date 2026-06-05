def analyze_keywords(keyword, suggestions):
    """
    We're gonna transfer raw API data into a list of keyword dictionaries, with the first being the original keyword
    """
    results = [] #first is creating the empty variable where we will be saving the dictionaries in

    #first, we add the original keyword, always the first
    results.append({
        'keyword': keyword,
        'word_count': len(keyword.split()),
        'type': 'original',
        'length': len(keyword)
    })

    #second, adding suggestions
    for suggestion in suggestions:
        results.append({
            'keyword': suggestion,
            'word_count': len(suggestion.split()),
            'type': 'suggestion',
            'length': len(suggestion)
        })

    return results

#Only long tail keywords (of at least 3 words) will be filtered
def filter_long_tail(keywords, min_words=3):
    return [kw for kw in keywords if kw["word_count"] >= min_words]

#Sort keywords based on their length (shortest first)
def sort_by_length(keywords):
    return sorted(keywords, key=lambda x: x["length"])

#test if it works:
# if __name__ == '__main__':
#     test_keyword = 'python developer'
#     test_suggestions = ["python developer jobs", "junior python developer", "remote python developer jobs"]

#     analyzed = analyze_keywords(test_keyword, test_suggestions)

#     print(analyzed)
#     print(filter_long_tail(analyzed))
#     print(sort_by_length(analyzed))