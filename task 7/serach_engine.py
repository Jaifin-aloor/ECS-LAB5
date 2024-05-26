from googleapiclient.discovery import build

def google_search(query, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, **kwargs).execute()
    return res['items']

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    cse_id = "YOUR_SEARCH_ENGINE_ID"
    query = "memory leaks"

    results = google_search(query, api_key, cse_id)
    for result in results:
        print(result['title'])
        print(result['link'])
        print(result['snippet'])
        print()

