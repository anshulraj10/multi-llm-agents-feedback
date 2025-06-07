from duckduckgo_search import DDGS

def search_web(query, num_results=3):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        return [r['body'] for r in results][:num_results]