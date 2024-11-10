import openai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Function to develop a plot outline based on the concept
def develop_plot_outline(concept, author_name):
    # Define the prompt to expand the concept into a full plot outline
    prompts = {
        "jack o'malley": (
            f"You are a sci-fi thriller writer named Jack O'Malley. "
            f"Based on the following concept: '{concept}', create a detailed plot outline for a novel. "
            "Include key plot points, twists, and a basic chapter breakdown."
        ),
        "cassandra graves": (
            f"You are a horror writer named Cassandra Graves. "
            f"Based on the following concept: '{concept}', create a detailed plot outline for a novel. "
            "Include key plot points, twists, and a basic chapter breakdown."
        ),
    }

    # Get the prompt for the chosen author
    prompt = prompts.get(author_name.lower())
    if not prompt:
        return "Unknown author. Please choose either 'Jack O'Malley' or 'Cassandra Graves'."

    try:
        # New API call format
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a skilled plot architect and story developer."},
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=500,
            temperature=0.7,
        )
        # Extract and return the content
        plot_outline = response.choices[0].message.content.strip()
        return plot_outline
    except Exception as e:
        return f"Error: {str(e)}"

# Test function (optional, for standalone testing)
if __name__ == "__main__":
    test_concept = "A reclusive artist discovers her favorite paint is mixed with a mysterious pigment that brings her nightmares to life."
    test_author = "Cassandra Graves"
    print(develop_plot_outline(test_concept, test_author))

