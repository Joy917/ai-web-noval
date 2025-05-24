def generate_outline(character_details):
    """
    Generates a structured character story outline based on predefined templates.

    Parameters:
    character_details (dict): A dictionary containing details about the character,
                              such as name, background, motivations, and relationships.

    Returns:
    str: A formatted outline string.
    """
    outline_template = """
    Character Outline:
    Name: {name}
    Background: {background}
    Motivations: {motivations}
    Relationships: {relationships}
    Key Events: {key_events}
    """

    # Extract character details
    name = character_details.get('name', 'Unknown Character')
    background = character_details.get('background', 'No background provided.')
    motivations = character_details.get('motivations', 'No motivations provided.')
    relationships = character_details.get('relationships', 'No relationships provided.')
    key_events = character_details.get('key_events', 'No key events provided.')

    # Generate the outline
    outline = outline_template.format(
        name=name,
        background=background,
        motivations=motivations,
        relationships=relationships,
        key_events=key_events
    )

    return outline.strip()