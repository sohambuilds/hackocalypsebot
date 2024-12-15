# Tactical Survival RAG Chatbot

The **Tactical Survival RAG Chatbot** is an interactive system designed to provide survival tactics, information, and guidance based on real-time data about monsters, survivors, and resources. The chatbot integrates with multiple APIs, fetches data, formats it for a tactical survival context, and uses advanced machine learning models (BERT for embeddings and Groq for text generation) to answer user queries effectively.

The system leverages **Retrieval-Augmented Generation (RAG)**, utilizing FAISS for similarity search and Groq's API for response generation. It is ideal for survival scenarios where users may need to retrieve information about their surroundings, resources, and potential threats.
## Features

- **Tactical Survival Context**: Fetches real-time data about monsters, survivors, and resources.
- **Data Formatting**: Converts raw data into actionable survival advice.
- **RAG System**: Retrieves relevant context and generates meaningful responses based on user queries.
- **FAISS Integration**: Searches the most relevant context based on query similarity.
- **Groq API**: Generates context-aware, intelligent responses.

## Technologies Used

- **BERT (TensorFlow)**: For generating contextual embeddings from input text.
- **FAISS**: For efficient similarity search and clustering of embeddings.
- **Groq API**: For generating answers based on context and user queries.
- **Requests**: To fetch data from external APIs.
- **TensorFlow & PyTorch**: For deep learning model usage and embedding generation.

## API Integration

The chatbot interacts with the following APIs to retrieve necessary data:

- **Monster API** (`MONSTER_API_URL`): Provides information about nearby monsters, including their IDs and locations.
- **Survivor API** (`SURVIVORS_API_URL`): Retrieves information about survivors, their needs, and locations.
- **Resource API** (`RESOURCES_API_URL`): Fetches details about available resources (food, water, etc.).


## Setup Instructions

To run the Tactical Survival RAG Chatbot locally, follow these steps:

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repository-url/tactical-survival-chatbot.git
cd tactical-survival-chatbot
```

### Step 2: Set Up Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```
**Note:** Ensure you have the required versions of libraries like `tensorflow`, `transformers`, `faiss`, and `requests`.

### Step 4: Set API Keys
You need to set up the API keys for the Groq API. Create a .env file or set the environment variable directly:

```bash
GROQ_API_KEY=your_groq_api_key_here
```
Alternatively, export it directly in the terminal:

```bash
export GROQ_API_KEY=your_groq_api_key_here
```

### Step 5: Run the Chatbot
To start the chatbot, run the following command:

```bash
python chatbot.py
```
This will initialize the chatbot and allow you to interact with it via the command line.
## How it Works?

- **Data Fetching:** The chatbot fetches monster, survivor, and resource data from their respective APIs.
- **Data Formatting:** The data is formatted into actionable, tactical survival context (e.g., "Monster at location (x, y), avoid at night").
- **Query Handling:** The chatbot continuously listens for user queries.
- **Similarity Search (FAISS):** It uses FAISS to find the most relevant context by comparing the query with the available data.
- **Response Generation:** The Groq API generates a context-aware response based on the user's query and the relevant data.
- **Interactive Loop:** The chatbot remains active in a loop, answering user queries until "exit" is typed.

### Example Interaction

```plaintext
Welcome to the Tactical Survival Assistant! Ask me anything about survival.
Your question (type 'exit' to quit): Where are the survivors located?

Tactical Survival Response: Survivor 1 located in District A (40.7128, -74.0060). Key needs: food, water.
```
## Project Structure

```plaintext
/tactical-survival-chatbot
    ├── chatbot.py                # Main chatbot logic
    ├── requirements.txt          # List of dependencies
    ├── data_fetchers.py          # API data fetching functions
    ├── data_formatters.py        # Functions to format data into tactical context
    ├── similarity_search.py      # FAISS search for relevant context
    ├── response_generator.py    # Generate responses using Groq API
    ├── README.md                # Project documentation
    └── .env                      # API key configuration (optional)
```
## Key Functions

- **fetch_monster_data:** Fetches monster data from the external Monster API.
- **fetch_survivor_data:** Fetches survivor data from the Survivor API.
- **fetch_resource_data:** Fetches resource data from the Resource API.
- **format_monster_data:** Converts monster data into survival context.
- **format_survivor_data:** Converts survivor data into survival context.
- **format_resource_data:** Converts resource data into survival context.
- **get_embeddings:** Uses BERT to generate text embeddings.
- **generate_response:** Generates a response based on the query and context using the Groq API.
- **search_relevant_context:** Uses FAISS to search for the most relevant context based on a user's query.
## Troubleshooting

- **No response or error from Groq:** Make sure the Groq API key is correctly set and valid.
- **Error while fetching data from APIs:** Check the API status and verify the endpoint URLs.
- **Embedding issues:** Ensure the transformers and tensorflow libraries are correctly installed.

