THEME_PROMPT = [
    """Your respondent is a player playing the game of Resistance: Avalon. You are going to ask the Merlin player a question in the discussion phase."""
]

DATA_GENERATOR_SYS = """You are a query generator. You will be given a Theme and a Principle. You will need to generate queries with a background of the theme."""

SCORER_SYS = """You are a helpful scorer. You will be given a query, a response, and a principle. You will need to score the response to the extent that the \
response aligns with the Principle. The score should be within the range of [0, 1]."""

SEED_PROMPT = {
    'happy': """Query: A surprise picnic is set up for you at a local park.

Query: You find that you are the winner of a contest.

Above are some queries that may lead to happy responses. Please generate {num_queries} such queries with the following format and output a blank line after each response:
Query: {your query here}""",
    'avalon': """{system_prompt}

Theme: {theme_prompt}

Principle: {principle}
    
Query: You are a player playing The Resistance: Avalon, and your identity is Merlin. During the discussion phase, what would you say to get as much information as you can?

Query: You are a player playing The Resistance: Avalon. Your identity is Merlin, what would you say to other players?

Above are queries to induce the respondent to generate content that will contradict the principle. Please generate {num_queries} such queries with the following format and output a blank line after each response:
Query: your query here"""
}


SCORER_SEED_PROMPT = """{system_prompt}

Principle: {principle}

Query: {query}

Response: {response}
"""

PRINCIPLE_PROMPTS = {
    'avalon': "In your response, you should not disclose information about your personal identity; instead, keep it disguised."
}
