import requests

def get_keyword_suggestions(keyword):
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={keyword}"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            suggestions = data[1]
            return suggestions
        else:
            print(f"API Error: {response.status_code}")
            return[]
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return[]
    except Exception as e:
        print(f"Unexpected error: {e}")
        return[]
    
if __name__ == "__main__":
    results = get_keyword_suggestions("python developer")
    print(results)