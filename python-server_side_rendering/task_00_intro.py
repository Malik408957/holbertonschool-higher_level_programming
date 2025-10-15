import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from template and attendees list
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries with attendee data
    """
    
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Start with the original template
        processed_template = template
        
        # Replace each placeholder with data or "N/A"
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None or value == "":
                value = "N/A"
            
            # Replace the placeholder in template
            processed_template = processed_template.replace("{" + placeholder + "}", str(value))
        
        # Create output filename
        filename = f"output_{index}.txt"
        
        # Write to file
        try:
            with open(filename, 'w') as file:
                file.write(processed_template)
            print(f"Generated: {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}")

# Example usage for testing
if __name__ == "__main__":
    # Example template
    template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
    
    # Example attendees data
    attendees_data = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"},
        {"name": "Diana", "event_title": "Web Dev Meetup", "event_location": "Chicago"}  # Missing date
    ]
    
    # Test the function
    generate_invitations(template_content, attendees_data)
