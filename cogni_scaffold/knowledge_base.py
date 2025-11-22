# cogni_scaffold/knowledge_base.py

"""
This module contains the structured knowledge base for analytical frameworks.
Each entry in the dictionary provides metadata and a template for a specific framework.
"""

FRAMEWORK_KNOWLEDGE_BASE = {
    "swot": {
        "name": "SWOT Analysis",
        "aliases": ["swot"],
        "description": "A strategic planning technique used to help a person or organization identify Strengths, Weaknesses, Opportunities, and Threats related to business competition or project planning.",
        "use_case": "Quickly assessing a situation, strategic planning, competitor analysis, personal development.",
        "keywords": ["strengths", "weaknesses", "opportunities", "threats", "strategic", "competition"],
        "template": [
            {"type": "heading", "level": 3, "content": "SWOT Analysis"},
            {"type": "heading", "level": 4, "content": "Strengths (Internal, Positive)"},
            {"type": "list", "items": ["- ", "- ", "- "]},
            {"type": "heading", "level": 4, "content": "Weaknesses (Internal, Negative)"},
            {"type": "list", "items": ["- ", "- ", "- "]},
            {"type": "heading", "level": 4, "content": "Opportunities (External, Positive)"},
            {"type": "list", "items": ["- ", "- ", "- "]},
            {"type": "heading", "level": 4, "content": "Threats (External, Negative)"},
            {"type": "list", "items": ["- ", "- ", "- "]}
        ]
    },
    "porters_five_forces": {
        "name": "Porter's Five Forces",
        "aliases": ["porter", "five forces"],
        "description": "An analysis framework that uses five forces to determine the competitive intensity and therefore attractiveness of an industry in terms of its profitability.",
        "use_case": "Analyzing industry structure, understanding competitive landscape, informing strategic decisions.",
        "keywords": ["competition", "industry", "rivalry", "threat", "bargaining power", "profitability"],
        "template": [
            {"type": "heading", "level": 3, "content": "Porter's Five Forces Analysis"},
            {"type": "heading", "level": 4, "content": "Threat of New Entrants"},
            {"type": "paragraph", "content": "Analysis of barriers to entry..."},
            {"type": "heading", "level": 4, "content": "Bargaining Power of Buyers"},
            {"type": "paragraph", "content": "Analysis of buyer power..."},
            {"type": "heading", "level": 4, "content": "Bargaining Power of Suppliers"},
            {"type": "paragraph", "content": "Analysis of supplier power..."},
            {"type": "heading", "level": 4, "content": "Threat of Substitute Products or Services"},
            {"type": "paragraph", "content": "Analysis of substitutes..."},
            {"type": "heading", "level": 4, "content": "Rivalry Among Existing Competitors"},
            {"type": "paragraph", "content": "Analysis of industry rivalry..."}
        ]
    },
    "pestle": {
        "name": "PESTLE Analysis",
        "aliases": ["pestle", "pest"],
        "description": "A framework used to scan the external macro-environmental factors that can have an impact on an organization.",
        "use_case": "Environmental scanning, strategic planning, market research, risk analysis.",
        "keywords": ["macro-environment", "political", "economic", "social", "technological", "legal", "environmental"],
        "template": [
            {"type": "heading", "level": 3, "content": "PESTLE Analysis"},
            {"type": "heading", "level": 4, "content": "Political Factors"},
            {"type": "list", "items": ["- ", "- "]},
            {"type": "heading", "level": 4, "content": "Economic Factors"},
            {"type": "list", "items": ["- ", "- "]},
            {"type": "heading", "level": 4, "content": "Socio-Cultural Factors"},
            {"type": "list", "items": ["- ", "- "]},
            {"type": "heading", "level": 4, "content": "Technological Factors"},
            {"type": "list", "items": ["- ", "- "]},
            {"type": "heading", "level": 4, "content": "Legal Factors"},
            {"type": "list", "items": ["- ", "- "]},
            {"type": "heading", "level": 4, "content": "Environmental Factors"},
            {"type": "list", "items": ["- ", "- "]}
        ]
    },
    "bcg_matrix": {
        "name": "BCG Matrix",
        "aliases": ["bcg", "growth-share matrix"],
        "description": "A portfolio management framework that helps companies decide how to prioritize their different businesses or products.",
        "use_case": "Portfolio management, resource allocation, strategic planning for multi-product businesses.",
        "keywords": ["portfolio", "market growth", "market share", "stars", "cash cows", "question marks", "dogs"],
        "template": [
            {"type": "heading", "level": 3, "content": "BCG Matrix Analysis"},
            {"type": "heading", "level": 4, "content": "Stars (High Growth, High Share)"},
            {"type": "list", "items": ["- Product/Business Unit A: "]},
            {"type": "heading", "level": 4, "content": "Cash Cows (Low Growth, High Share)"},
            {"type": "list", "items": ["- Product/Business Unit B: "]},
            {"type": "heading", "level": 4, "content": "Question Marks (High Growth, Low Share)"},
            {"type": "list", "items": ["- Product/Business Unit C: "]},
            {"type": "heading", "level": 4, "content": "Dogs (Low Growth, Low Share)"},
            {"type": "list", "items": ["- Product/Business Unit D: "]}
        ]
    },
    "pyramid_principle": {
        "name": "Pyramid Principle",
        "aliases": ["minto pyramid", "pyramid"],
        "description": "A method for structuring communication to start with the main conclusion, and then provide supporting arguments in a logical, hierarchical manner.",
        "use_case": "Report writing, presentations, executive communication, structuring any form of argument.",
        "keywords": ["communication", "structure", "writing", "presentation", "conclusion", "argument"],
        "template": [
            {"type": "heading", "level": 3, "content": "Pyramid Principle Structure"},
            {"type": "heading", "level": 4, "content": "The Governing Thought (The main conclusion/answer)"},
            {"type": "paragraph", "content": "State the single most important conclusion here."},
            {"type": "heading", "level": 4, "content": "Key Supporting Arguments"},
            {"type": "list", "items": [
                "1. **Argument A:** ",
                "   - Supporting Data/Fact A1: ",
                "   - Supporting Data/Fact A2: ",
                "2. **Argument B:** ",
                "   - Supporting Data/Fact B1: ",
                "   - Supporting Data/Fact B2: ",
                "3. **Argument C:** ",
                "   - Supporting Data/Fact C1: ",
                "   - Supporting Data/Fact C2: "
            ]}
        ]
    },
    "first_principles": {
        "name": "First Principles Thinking",
        "aliases": ["first principles"],
        "description": "A problem-solving technique that involves breaking down a complex problem into its most basic, foundational elements and reasoning up from there.",
        "use_case": "Innovation, complex problem-solving, challenging assumptions, engineering.",
        "keywords": ["problem-solving", "innovation", "assumptions", "foundational", "reasoning", "elon musk"],
        "template": [
            {"type": "heading", "level": 3, "content": "First Principles Analysis"},
            {"type": "heading", "level": 4, "content": "1. Identify and Deconstruct the Problem/Goal"},
            {"type": "paragraph", "content": "What is the problem we are trying to solve? What are the current assumptions?"},
            {"type": "heading", "level": 4, "content": "2. Break Down to Fundamental Truths"},
            {"type": "paragraph", "content": "What are the absolute, undeniable, physics-level truths about this situation?"},
            {"type": "list", "items": ["- Truth 1: ", "- Truth 2: "]},
            {"type": "heading", "level": 4, "content": "3. Re-reason a Solution from the Ground Up"},
            {"type": "paragraph", "content": "Forgetting how it's currently done, what is the best way to build a solution based only on these truths?"}
        ]
    },
    "dcf_analysis": {
        "name": "DCF Analysis",
        "aliases": ["dcf", "discounted cash flow"],
        "description": "A valuation method used to estimate the value of an investment based on its expected future cash flows.",
        "use_case": "Fundamental analysis, stock valuation, corporate finance projects (M&A, capital budgeting).",
        "keywords": ["valuation", "cash flow", "discount rate", "wacc", "terminal value", "intrinsic value"],
        "template": [
            {"type": "heading", "level": 3, "content": "Discounted Cash Flow (DCF) Analysis"},
            {"type": "heading", "level": 4, "content": "1. Forecast Future Free Cash Flows (FCF)"},
            {"type": "list", "items": ["- Year 1 FCF: ", "- Year 2 FCF: ", "- Year N FCF: "]},
            {"type": "heading", "level": 4, "content": "2. Determine Discount Rate (WACC)"},
            {"type": "paragraph", "content": "Calculate the Weighted Average Cost of Capital (WACC)..."},
            {"type": "heading", "level": 4, "content": "3. Calculate Terminal Value"},
            {"type": "paragraph", "content": "Using either the Gordon Growth Model or an exit multiple..."},
            {"type": "heading", "level": 4, "content": "4. Discount Cash Flows and Terminal Value to Present"},
            {"type": "paragraph", "content": "Sum the present values of all FCFs and the terminal value..."},
            {"type": "heading", "level": 4, "content": "5. Calculate Intrinsic Value"},
            {"type": "paragraph", "content": "Intrinsic Value per Share = (Total Enterprise Value - Debt + Cash) / Shares Outstanding"}
        ]
    },
    "value_investing": {
        "name": "Value Investing",
        "aliases": ["value"],
        "description": "An investment paradigm that involves buying securities for less than their calculated intrinsic value, incorporating a margin of safety.",
        "use_case": "Long-term stock market investing, portfolio strategy, finding undervalued assets.",
        "keywords": ["value investing", "intrinsic value", "margin of safety", "benjamin graham", "warren buffett", "mr. market"],
        "template": [
            {"type": "heading", "level": 3, "content": "Value Investing Checklist"},
            {"type": "heading", "level": 4, "content": "1. Understand the Business"},
            {"type": "paragraph", "content": "Is the business simple and understandable? Does it have a consistent operating history?"},
            {"type": "heading", "level": 4, "content": "2. Calculate Intrinsic Value"},
            {"type": "paragraph", "content": "Using methods like DCF, what is the conservative estimate of the business's worth?"},
            {"type": "heading", "level": 4, "content": "3. Apply a Margin of Safety"},
            {"type": "paragraph", "content": "Is the current market price significantly below the calculated intrinsic value (e.g., 30-50% discount)?"},
            {"type": "heading", "level": 4, "content": "4. Assess Management Quality"},
            {"type": "paragraph", "content": "Is the management team rational, candid, and acting in the shareholders' interest?"},
            {"type": "heading", "level": 4, "content": "5. View the Stock as a Business"},
            {"type": "paragraph", "content": "Ignore short-term market fluctuations ('Mr. Market') and focus on the long-term business performance."}
        ]
    },
    "circle_of_competence": {
        "name": "Circle of Competence",
        "aliases": ["competence circle"],
        "description": "A mental model advising investors to only operate within the boundaries of what they know and understand deeply.",
        "use_case": "Defining investment criteria, risk management, personal investment philosophy, decision making.",
        "keywords": ["circle of competence", "buffett", "munger", "risk management", "know what you know"],
        "template": [
            {"type": "heading", "level": 3, "content": "Defining Your Circle of Competence"},
            {"type": "heading", "level": 4, "content": "1. Identify Your Areas of Genuine Expertise"},
            {"type": "paragraph", "content": "What industries, technologies, or business models do I understand better than the average intelligent investor?"},
            {"type": "list", "items": ["- Area 1: ", "- Area 2: "]},
            {"type": "heading", "level": 4, "content": "2. Define the Boundaries"},
            {"type": "paragraph", "content": "Be honest about what you *don't* know. What is clearly outside your circle?"},
            {"type": "heading", "level": 4, "content": "3. Operate Strictly Within the Circle"},
            {"type": "paragraph", "content": "Focus research and investment activities exclusively on opportunities within the defined boundaries."},
            {"type": "heading", "level": 4, "content": "4. Cautiously Expand the Circle Over Time"},
            {"type": "paragraph", "content": "Learning about new areas is encouraged, but do not invest until they are firmly within your circle of competence."}
        ]
    }
}
