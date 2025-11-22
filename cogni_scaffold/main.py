# main.py
# This is an example script demonstrating how to use the CogniScaffold tool.

from . import CogniScaffold

def main():
    """
    Main function to showcase the features of CogniScaffold.
    """
    # 1. Initialize the tool
    # This loads the knowledge base into the scaffold instance.
    print("Initializing CogniScaffold...")
    scaffold = CogniScaffold()
    print("Initialization complete.")
    print("\n" + "="*70 + "\n")

    # 2. Use the .search() method
    # Let's find frameworks related to strategy and competition.
    keyword_to_search = "competition"
    print(f"--- Searching for frameworks related to '{keyword_to_search}' ---")
    search_results = scaffold.search(keyword_to_search)
    
    if search_results:
        for result in search_results:
            print(f"  - Found: {result['name']}")
            print(f"    Description: {result['description']}")
    else:
        print(f"No frameworks found for the keyword '{keyword_to_search}'.")
    
    print("\n" + "="*70 + "\n")

    # 3. Use the .get_template() method
    # Let's get a structured template for a PESTLE analysis.
    framework_to_template = "PESTLE"
    print(f"--- Generating template for '{framework_to_template}' Analysis ---")
    template = scaffold.get_template(framework_to_template)
    print(template)
    
    print("\n" + "="*70 + "\n")

    # 4. Use the .suggest() method
    # Let's imagine we are a startup and need to figure out our market position.
    problem_description = (
        "We are a new software startup trying to decide if we should enter the "
        "highly competitive food delivery market. We need to understand the macro "
        "environmental factors, the industry's competitive structure, and our "
        "own internal strengths and weaknesses to make a strategic decision."
    )
    print("--- Suggesting frameworks for a complex problem ---")
    print(f"Problem Description:\n\"{problem_description}\"\n")
    
    suggestions = scaffold.suggest(problem_description)
    
    if suggestions:
        print("Top suggestions for your problem:")
        for i, suggestion in enumerate(suggestions):
            print(f"  {i+1}. {suggestion['name']} (Relevance Score: {suggestion['score']})")
            print(f"     Use for: {suggestion['use_case']}")
    else:
        print("Could not find any relevant frameworks for the problem description.")

if __name__ == "__main__":
    main()
