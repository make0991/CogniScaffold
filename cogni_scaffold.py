# cogni_scaffold/cogni_scaffold.py

import re
from .knowledge_base import FRAMEWORK_KNOWLEDGE_BASE

class CogniScaffold:
    """
    A cognitive scaffolding tool to assist in structured thinking and analysis.
    It provides functionalities to search, get templates for, and suggest
    analytical frameworks.
    """
    def __init__(self):
        self._db = FRAMEWORK_KNOWLEDGE_BASE

    def _find_framework_key(self, name):
        """Finds the internal dictionary key for a framework by name or alias."""
        lower_name = name.lower()
        for key, framework in self._db.items():
            if lower_name == framework["name"].lower() or lower_name in framework["aliases"]:
                return key
        return None

    def search(self, keyword):
        """
        Searches the knowledge base for frameworks matching a keyword.
        
        Args:
            keyword (str): The keyword to search for in framework names,
                           descriptions, use cases, or keywords.
                           
        Returns:
            list: A list of dictionaries, each containing the name and
                  description of a matching framework.
        """
        results = []
        search_term = keyword.lower()
        for key, framework in self._db.items():
            # Create a searchable text block
            searchable_content = " ".join([
                framework["name"],
                framework["description"],
                framework["use_case"],
                " ".join(framework["keywords"])
            ]).lower()
            
            if re.search(r'\b' + re.escape(search_term) + r'\b', searchable_content):
                results.append({
                    "name": framework["name"],
                    "description": framework["description"]
                })
        return results

    def _format_template(self, template_data):
        """Formats a structured template into a Markdown string."""
        md_string = ""
        for item in template_data:
            if item["type"] == "heading":
                md_string += f"{'#' * item['level']} {item['content']}\n\n"
            elif item["type"] == "paragraph":
                md_string += f"{item['content']}\n\n"
            elif item["type"] == "list":
                for list_item in item["items"]:
                    md_string += f"{list_item}\n"
                md_string += "\n"
        return md_string.strip()

    def get_template(self, framework_name):
        """
        Gets a markdown template for a specified framework.
        
        Args:
            framework_name (str): The name or an alias of the framework.
            
        Returns:
            str: A formatted Markdown template, or an error message if not found.
        """
        key = self._find_framework_key(framework_name)
        if not key:
            return f"Error: Framework '{framework_name}' not found."
            
        template_data = self._db[key].get("template")
        if not template_data:
            return f"Error: No template available for '{framework_name}'."
            
        return self._format_template(template_data)

    def suggest(self, problem_description, top_n=3):
        """
        Suggests relevant frameworks based on a problem description.
        This is a basic keyword-matching recommender.
        
        Args:
            problem_description (str): A string describing the problem to be analyzed.
            top_n (int): The number of top suggestions to return.
            
        Returns:
            list: A ranked list of suggested framework dictionaries.
        """
        scores = {}
        problem_lower = problem_description.lower()
        
        for key, framework in self._db.items():
            score = 0
            # Higher weight for keywords
            for keyword in framework["keywords"]:
                if re.search(r'\b' + re.escape(keyword) + r'\b', problem_lower):
                    score += 2
            
            # Lower weight for general description matches
            if re.search(r'\b' + '|'.join(re.escape(w) for w in framework["name"].lower().split()) + r'\b', problem_lower):
                score += 1
            
            if score > 0:
                scores[framework["name"]] = {
                    "name": framework["name"],
                    "use_case": framework["use_case"],
                    "score": score
                }
        
        # Sort by score in descending order
        sorted_suggestions = sorted(scores.values(), key=lambda x: x["score"], reverse=True)
        
        return sorted_suggestions[:top_n]

if __name__ == '__main__':
    # Example Usage
    scaffold = CogniScaffold()

    print("--- 1. Searching for frameworks related to 'competition' ---")
    search_results = scaffold.search("competition")
    for res in search_results:
        print(f"- {res['name']}: {res['description']}")

    print("\n" + "="*50 + "\n")

    print("--- 2. Getting the template for 'SWOT Analysis' ---")
    swot_template = scaffold.get_template("swot")
    print(swot_template)
    
    print("\n" + "="*50 + "\n")

    print("--- 3. Suggesting frameworks for a problem ---")
    problem = "I need to analyze the competitive landscape of a new industry I want to enter and understand my company's strategic position."
    suggestions = scaffold.suggest(problem)
    print(f"Problem: \"{problem}\"")
    print("Suggestions:")
    for i, sug in enumerate(suggestions):
        print(f"{i+1}. {sug['name']} (Score: {sug['score']}) - Use for: {sug['use_case']}")
