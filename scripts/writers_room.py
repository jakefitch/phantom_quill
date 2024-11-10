import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from writers_room.plot_architect import develop_plot_outline
from openai import OpenAI
import os
from dotenv import load_dotenv
#from ..writers_room.plot_architect import develop_plot_outline




# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Function to brainstorm a new story concept
def brainstorm_concept(author_name):
    prompts = {
        "jack o'malley": (
            "You are a sci-fi thriller writer named Jack O'Malley. "
            "Your job is to come up with high-concept story ideas that are fast-paced and tech-heavy. "
            "Provide a one-liner pitch for a new novel idea."
        ),
        "cassandra graves": (
            "You are a horror writer named Cassandra Graves. "
            "Your job is to create unsettling and psychological horror story ideas. "
            "Provide a one-liner pitch for a new horror novel."
        ),
    }

    prompt = prompts.get(author_name.lower())
    if not prompt:
        return "Unknown author. Please choose either 'Jack O'Malley' or 'Cassandra Graves'."

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a creative writing assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        message = completion.choices[0].message.content.strip()
        return message
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("🔍 Welcome to the Writers' Room of Phantom Quill Press!")
    author = input("Choose an author persona (Jack O'Malley or Cassandra Graves): ")
    concept = brainstorm_concept(author)
    print(f"💡 New Story Idea from {author}: {concept}")

    # Generate the plot outline
    outline = develop_plot_outline(concept, author)
    print("\n📝 Plot Outline:")
    print(outline)




