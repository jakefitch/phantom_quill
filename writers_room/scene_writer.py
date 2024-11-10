import openai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Function to generate a scene based on chapter details
def generate_scene(chapter_summary, author_name):
    prompts = {
        "jack o'malley": (
            f"You are a sci-fi thriller writer named Jack O'Malley. "
            f"Using the chapter summary: '{chapter_summary}', write a vivid and action-packed scene. "
            "Include detailed descriptions, high-tech elements, and intense dialogue."
        ),
        "cassandra graves": (
            f"You are a horror writer named Cassandra Graves. "
            f"Using the chapter summary: '{chapter_summary}', write a tense, atmospheric scene. "
            "Focus on eerie descriptions, unsettling details, and realistic dialogue that builds suspense."
        ),
    }

    # Get the appropriate prompt
    prompt = prompts.get(author_name.lower())
    if not prompt:
        return "Unknown author. Please choose either 'Jack O'Malley' or 'Cassandra Graves'."

    try:
        # Make the API call to generate the scene
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a creative and detailed scene writer."},
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=700,
            temperature=0.8,
        )
        # Extract the generated scene content
        scene_text = response.choices[0].message.content.strip()
        return scene_text
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function (optional, for standalone testing)
if __name__ == "__main__":
    test_chapter = (
        "Eliot paints his first portrait in Merrow's End, a haunting image of the coastline. "
        "At midnight, the painting comes to life, the waves crashing violently, revealing a shadowy figure lurking in the water."
    )
    test_author = "Cassandra Graves"
    generated_scene = generate_scene(test_chapter, test_author)
    print("\n🎬 Generated Scene:\n")
    print(generated_scene)
