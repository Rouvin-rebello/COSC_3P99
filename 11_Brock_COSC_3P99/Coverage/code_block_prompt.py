import openai
import os

# Set your API key
openai.api_key = "#add key"

# Function to generate text using the OpenAI API interface
def generate_text(prompt):
    try:
        response = openai.ChatCompletion.create(
            #model="gpt-4",  # Specify the correct model
            model="gpt-3.5-turbo",  # Specify the correct model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500  # Adjust based on your desired length of generated text
        )
        
        # Extract the generated text from the API response
        generated_text = response['choices'][0]['message']['content']
        
        return generated_text
    
    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        print(f"OpenAI API error: {e}")
        return None

# Function to load the source file content and create a prompt
def prepare_prompt(file_path):
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
        
        prompt = (
            f"Please analyze the following Python source code (all lines, methods) and divide it into multiple small code block categories"
            f"according to these categories. Format the output as follows:\n"
            f"1. Code Category Name: particular lines of code from the source code copied for the code block 2. Second category ...\n\n"
            f"Categories:\n"
            f"- Core Functionality\n"
            f"- Boundary Conditions and Edge Cases\n"
            f"- Error Handling\n"
            f"- Integration Points\n"
            f"- User Interface (UI) Interactions\n"
            f"- Security Features\n"
            f"- Performance and Scalability\n"
            f"- Configuration and Environment\n"
            f"- Output Consistency and more possible categories\n\n"
            f"Here is the source code (make sure to categorise all methods e.g.calculate_total, Item methods, order methods, priceditems, etc ):\n\n"
            f"{source_code}"
        )
        
        return prompt
    
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Function to extract code for a specific category and remove code markers
def extract_category_code(output, category):
    # Find the category section
    start_index = output.find(f"{category}:")
    if start_index == -1:
        return None
    
    # Extract the section of the output related to this category
    section = output[start_index:]
    end_index = section.find('\n\n')
    if end_index != -1:
        section = section[:end_index]
    
    # Remove the category header
    lines = section.split('\n')
    category_code = '\n'.join(lines[1:]).strip()
    
    # Remove Python code markers
    category_code = category_code.replace('```python', '').replace('```', '').strip()
    
    return category_code

# Function to save code to files
def save_code_categories(output):
    # Define category names and file suffixes
    categories = [
        "Core Functionality",
        "Boundary Conditions and Edge Cases",
        "Error Handling",
        "Integration Points",
        "User Interface (UI) Interactions",
        "Security Features",
        "Performance and Scalability",
        "Configuration and Environment",
        "Output Consistency"
    ]
    
    for category in categories:
        # Create a safe filename
        safe_category_name = category.replace(" ", "_").replace("(", "").replace(")", "")
        file_name = f"{safe_category_name}.py"
        
        # Extract code for this category
        category_code = extract_category_code(output, category)
        
        # Only write the file if it contains code other than "N/A"
        if category_code and category_code.upper() != "N/A":
            with open(file_name, 'w') as file:
                file.write(category_code)
            print(f"Saved {category} to {file_name}")
        elif category_code:
            print(f"No valid code found for {category}, skipping file creation.")

# Example usage
file_path = 'Shpping_cart_project.py'
prompt = prepare_prompt(file_path)
if prompt:
    result = generate_text(prompt)
    if result:
        save_code_categories(result)
