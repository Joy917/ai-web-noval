def write_chapter(outline, title, summary):
    """
    Generates a chapter based on the provided outline and saves it to a file.

    Parameters:
    outline (str): The structured outline to base the chapter on.
    title (str): The title of the chapter.
    summary (str): A one-sentence summary of the chapter's main content.
    """
    from datetime import datetime
    import os

    # Generate the current date and time for the filename
    current_time = datetime.now().strftime("%Y.%m.%d-%H.%M")
    
    # Define the output directory
    output_dir = 'output/chapters'
    os.makedirs(output_dir, exist_ok=True)

    # Create the filename based on the specified format
    filename = f"[Chapter] {title} ({summary}) - {current_time}.txt"
    file_path = os.path.join(output_dir, filename)

    # Generate the chapter content (this is a placeholder for actual chapter generation logic)
    chapter_content = f"# Chapter: {title}\n\n{outline}\n\n## Summary\n{summary}"

    # Write the chapter content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(chapter_content)

    print(f"Chapter '{title}' has been written to '{file_path}'.")