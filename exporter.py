import csv
import os
from datetime import datetime

#export keyword list to a CSV in the output folder
def export_to_csv(keywords, filename=None):

    #first make sure the output folder exists
    os.makedirs("output", exist_ok=True)

    #create automatic filename with timestamp as noname
    if filename is None:
        timestamp = datetime.now().strftime('%d%m%Y_%H%M')
        filename = f'keywords_{timestamp}.csv'
    
    filepath = os.path.join('output', filename)

    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['keyword', 'word_count', 'type', 'length']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(keywords)
        print(f'Exported to {filepath}')
        return filepath
    except Exception as e:
        print(f'Export failed: {e}')
        return None
    
#test if it works:
# if __name__ == '__main__':
#     test_keywords = [
#         {
#             'keyword': 'python developer',
#             'word_count': 2,
#             'type': 'original',
#             'length': 16
#         },
#         {
#             'keyword': 'junior python developer',
#             'word_count': 3,
#             'type': 'suggestion',
#             'length': 25
#         }
#     ]

#     export_to_csv(test_keywords)