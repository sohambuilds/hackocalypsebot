from RagAnswerGenerator import RagAnswerGenerator  # Import the RAG Answer Generator class

class RagChatPipeline:
    def __init__(self, directory):
        """
        Initializes the RAG Chat Pipeline.
        
        Args:
            directory (str): The directory containing text files for indexing.
        """
        self.rag_generator = RagAnswerGenerator(directory)

    def run_chat(self):
        """
        Runs an interactive chat loop to allow users to ask questions
        and receive responses generated using the RAG pipeline.
        """
        print("Hello! Welcome to the RAG Chat System.")
        print("Type 'exit' anytime to leave the session.")

        while True:
            try:
                # Get user input
                user_question = input("\nAsk your question: ").strip()

                if user_question.lower() == "exit":
                    print("Thank you for using the RAG Chat System. Goodbye!")
                    break

                if not user_question:
                    print("Please enter a valid question.")
                    continue

                # Generate and display the response
                answer = self.rag_generator.generate_answer(user_question)
                print("\nResponse:", answer)

            except KeyboardInterrupt:
                print("\nSession interrupted. Type 'exit' to leave.")
            except Exception as e:
                print(f"An error occurred: {e}")
