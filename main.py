from api import get_keyword_suggestions
from analyzer import analyze_keywords, filter_long_tail, sort_by_length
from exporter import export_to_csv

def main():
    print('=' * 50)
    print('SEO Keyword Analyzer')
    print('=' * 50)

    #First let user enter a keyword and save it into a variable
    keyword = input('\nEnter a keyword to analyze: ').strip()
    if not keyword:
        print('No keyword entered. Exiting program.')
        return
    
    print(f'Fetching suggestions for: "{keyword}"')

    #Get the data for the keyword
    suggestions = get_keyword_suggestions(keyword)
    if not suggestions:
        print('No keyword suggestions found.')
        return
    
    #Analyze the suggestions
    all_keywords = analyze_keywords(keyword, suggestions)
    long_tail = filter_long_tail(all_keywords)

    #Show results
    print(f'Found {len(all_keywords)} keywords ({len(long_tail)} long-tail)\n')
    for kw in all_keywords:
        print(f'{kw["type"]:10} | {kw["word_count"]} words | {kw["keyword"]}')

    #export results to CSV
    print()
    export_choice = input('Export to CSV? (yes/no): ')
    if export_choice.lower() == 'yes':
        export_to_csv(all_keywords)

if __name__ == '__main__':
    main()