import os
import openai
from dotenv import load_dotenv
from writers_room.plot_architect import develop_plot_outline
from writers_room.scene_writer import generate_scene

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Function to write and save each chapter based on plot outline
def write_and_save_chapters(plot_outline, author_name):
    chapter_count = 1
    max_chapters = min(24, len(plot_outline))  # Cap the maximum chapters at 24

    for chapter_summary in plot_outline[:max_chapters]:
        print(f"🖋️ Generating Chapter {chapter_count} of {max_chapters}...")

        # Generate the scene using scene_writer
        scene = generate_scene(chapter_summary, author_name)

        # Format the chapter text
        chapter_title = f"### Chapter {chapter_count}\n\n"
        chapter_text = chapter_title + scene + "\n\n"

        # Zero-padded filename for proper sorting
        filename = f"./output/{author_name.replace(' ', '_').lower()}_chapter_{str(chapter_count).zfill(2)}.md"
        save_chapter(chapter_text, filename)

        print(f"✅ Chapter {chapter_count} saved as {filename}")
        chapter_count += 1

# Function to save the chapter to a markdown file
def save_chapter(text, filename):
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(filename, 'w') as file:
        file.write(text)

# Main execution flow
if __name__ == "__main__":
    author = input("Choose an author persona (Jack O'Malley or Cassandra Graves): ")
    plot_summary = input("Enter a brief plot outline or use 'default' for auto-generated: ")

    # Auto-generate plot outline if not provided
    if plot_summary.lower() == "default":
        plot_outline = develop_plot_outline("The story follows a haunted artist in a coastal town.", author)
    else:
        plot_outline = develop_plot_outline(plot_summary, author)

    # Generate and save each chapter
    write_and_save_chapters(plot_outline, author)

    print("\n🚀 Chapter generation complete!")


