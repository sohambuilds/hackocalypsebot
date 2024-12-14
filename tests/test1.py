
import requests

# Define API URLs and headers
GROQ_API_KEY = ""
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MONSTER_API_URL = "https://api.mlsakiit.com/monsters"
SURVIVORS_API_URL = "https://api.mlsakiit.com/survivors"
RESOURCES_API_URL = "https://api.mlsakiit.com/resources"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# Function to fetch monster data from API
def fetch_monster_data():
    try:
        response = requests.get(MONSTER_API_URL, headers={"accept": "application/json"})
        response.raise_for_status()
        data = response.json()  # Parse JSON response
        return data.get("monsters", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching monster data: {e}")
        return []

# Function to format monster data into readable context
def format_monster_data(monsters):
    if not monsters:
        raise ValueError("No monster data available to process.")
    formatted = []
    for monster in monsters:
        formatted.append(
            f"Monster ID: {monster['monster_id']}, Location: ({monster['lat']}, {monster['lon']})"
        )
    return formatted

# Function to fetch resource data from API
def fetch_resource_data():
    try:
        response = requests.get(RESOURCES_API_URL, headers={"accept": "application/json"})
        response.raise_for_status()
        data = response.json()  # Parse JSON response
        return data.get("features", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resource data: {e}")
        return []

# Function to fetch survivor data from API
def fetch_survivor_data():
    try:
        response = requests.get(SURVIVORS_API_URL, headers={"accept": "application/json"})
        response.raise_for_status()
        data = response.json()  # Parse JSON response
        # Assuming data is a list of survivor dictionaries:
        return data  # Directly return the list 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching survivor data: {e}")
        return []

# Function to format survivor data into readable context
def format_survivor_data(survivors):
    if not survivors:
        raise ValueError("No survivor data available to process.")
    formatted = []
    for survivor in survivors:
        formatted.append(
            f"Survivor ID: {survivor['survivor_id']}, District: {survivor['district']}, "
            f"Location: ({survivor['lat']}, {survivor['lon']})"
        )
    return formatted



# Function to format resource data into readable context
def format_resource_data(resources):
    if not resources:
        raise ValueError("No resource data available to process.")
    formatted = []
    for resource in resources:
        props = resource.get("properties", {})
        geometry = resource.get("geometry", {})
        coords = geometry.get("coordinates", [])
        formatted.append(
            f"District: {props.get('dist_name', 'N/A')} "
            f"(Code: {props.get('dist_code', 'N/A')}), "
            f"Temp: {props.get('temp', 'N/A')}°C, Rainfall: {props.get('rainfall', 'N/A')}mm, "
            f"Wind Speed: {props.get('wind_speed', 'N/A')}m/s, "
            f"Water: {props.get('water', 'N/A')}L, Food Rations: {props.get('food_rations', 'N/A')}kg, "
            f"Medkits: {props.get('medkits', 'N/A')}, Ammo: {props.get('ammo', 'N/A')}, "
            f"Camp Exists: {props.get('camp_exists', 'N/A')}, "
            f"Coordinates: {coords}"
        )
    return formatted


#---------------------------------------------------------------------------------------

# Function to generate a response using Groq API
# from backend.chatbot import chat_with_bot

# if __name__ == "__main__":
#     user_query = input("Ask the chatbot: ")
#     bot_response = chat_with_bot(user_query)
#     print(f"Bot: {bot_response}")
import requests

# Define API URLs and headers
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MONSTER_API_URL = "https://api.mlsakiit.com/monsters"
SURVIVORS_API_URL = "https://api.mlsakiit.com/survivors"
RESOURCES_API_URL = "https://api.mlsakiit.com/resources"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# Function to fetch monster data from API
def fetch_monster_data():
    try:
        response = requests.get(MONSTER_API_URL, headers={"accept": "application/json"})
        response.raise_for_status()
        data = response.json()  # Parse JSON response
        return data.get("monsters", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching monster data: {e}")
        return []

# Function to format monster data into readable context
def format_monster_data(monsters):
    if not monsters:
        raise ValueError("No monster data available to process.")
    formatted = []
    for monster in monsters:
        formatted.append(
            f"Monster ID: {monster['monster_id']}, Location: ({monster['lat']}, {monster['lon']})"
        )
    return formatted

# Function to fetch resource data from API
def fetch_resource_data():
    try:
        response = requests.get(RESOURCES_API_URL, headers={"accept": "application/json"})
        response.raise_for_status()
        data = response.json()  # Parse JSON response
        return data.get("features", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resource data: {e}")
        return []

# Function to fetch survivor data from API
def fetch_survivor_data():
    try:
        response = requests.get(SURVIVORS_API_URL, headers={"accept": "application/json"})
        response.raise_for_status()
        data = response.json()  # Parse JSON response
        # Assuming data is a list of survivor dictionaries:
        return data  # Directly return the list 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching survivor data: {e}")
        return []

# Function to format survivor data into readable context
def format_survivor_data(survivors):
    if not survivors:
        raise ValueError("No survivor data available to process.")
    formatted = []
    for survivor in survivors:
        formatted.append(
            f"Survivor ID: {survivor['survivor_id']}, District: {survivor['district']}, "
            f"Location: ({survivor['lat']}, {survivor['lon']})"
        )
    return formatted
    


# Function to format resource data into readable context
def format_resource_data(resources):
    if not resources:
        raise ValueError("No resource data available to process.")
    formatted = []
    for resource in resources:
        props = resource.get("properties", {})
        geometry = resource.get("geometry", {})
        coords = geometry.get("coordinates", [])
        formatted.append(
            f"District: {props.get('dist_name', 'N/A')} "
            f"(Code: {props.get('dist_code', 'N/A')}), "
            f"Temp: {props.get('temp', 'N/A')}°C, Rainfall: {props.get('rainfall', 'N/A')}mm, "
            f"Wind Speed: {props.get('wind_speed', 'N/A')}m/s, "
            f"Water: {props.get('water', 'N/A')}L, Food Rations: {props.get('food_rations', 'N/A')}kg, "
            f"Medkits: {props.get('medkits', 'N/A')}, Ammo: {props.get('ammo', 'N/A')}, "
            f"Camp Exists: {props.get('camp_exists', 'N/A')}, "
            f"Coordinates: {coords}"
        )
    return formatted


#---------------------------------------------------------------------------------------

# Function to generate a response using Groq API
def generate_response(query, context):
    # Prepare the prompt for the model with the query and context
    messages = [{"role": "user", "content": query}]
    
    # Add the retrieved context to the message
    for doc in context:
        messages.append({"role": "system", "content": doc})

    try:
        response = requests.post(GROQ_API_URL, json={
            "model": "llama3-8b-8192",  # Example model ID, choose based on your API response
            "messages": messages
        }, headers=HEADERS)

        response_data = response.json()
        if "choices" not in response_data:
            raise ValueError(f"Unexpected response format: {response_data}")
        
        return response_data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating response: {e}"

#----------------------------------

def chunk_context(context, max_chunk_size=100):
    """
    Split the context into chunks to fit within token limits.
    """
    chunks = []
    current_chunk = []
    current_size = 0

    for doc in context:
        doc_size = len(doc.split())
        if current_size + doc_size > max_chunk_size:
            chunks.append(current_chunk)
            current_chunk = []
            current_size = 0
        current_chunk.append(doc)
        current_size += doc_size

    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def process_chunks(query, context_chunks):
    """
    Process each context chunk and combine responses.
    """
    combined_response = []
    for chunk in context_chunks:
        response = generate_response(query, chunk)
        combined_response.append(response)
    return "\n\n".join(combined_response)




def fetch_monster_data():
    try:
        response = requests.get(MONSTER_API_URL, headers={"accept": "application/json"})
        response.raise_for_status()
        return response.json().get("monsters", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching monster data: {e}")
        return [{"monster_id": "unknown", "lat": 0, "lon": 0}]  # Default fallback





def format_monster_data(monsters):
    return [f"Monster {monster['monster_id']} at ({monster['lat']}, {monster['lon']})" for monster in monsters]

def format_survivor_data(survivors):
    return [f"Survivor {survivor['survivor_id']} in {survivor['district']} ({survivor['lat']}, {survivor['lon']})" for survivor in survivors]

def format_resource_data(resources):
    return [
        f"{props.get('dist_name', 'Unknown')}: Temp {props.get('temp', 'N/A')}°C, Food {props.get('food_rations', 'N/A')}kg"
        for resource in resources if (props := resource.get("properties"))
    ]



#----------------------------------


# Main logic for the RAG chatbot
def rag_chatbot():
    # Step 1: Fetch monster, survivor, and resource data from APIs
    monsters = fetch_monster_data()
    survivors = fetch_survivor_data()
    resources = fetch_resource_data()
    
    # Step 2: Format the data into readable context
    try:
        context = format_monster_data(monsters)
        context += format_survivor_data(survivors)
        context += format_resource_data(resources)
    except ValueError as e:
        print(e)
        return
    
    # Step 3: Chat loop
    print("Welcome to the RAG Chatbot! Ask me anything about survival.")
    while True:
        query = input("\nYour question (type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        
        # Step 4: Generate a response based on the query and retrieved context
        response = generate_response(query, context)
        print("\nChatbot Response:", response)

# Example usage
if __name__ == "__main__":
    rag_chatbot()
