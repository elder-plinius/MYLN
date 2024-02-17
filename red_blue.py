from gemini_chat import GeminiChat
from myln import Compressor

class Agent:
    def __init__(self, name, chat_model, system_prompt):
        self.name = name
        self.chat_model = chat_model
        self.system_prompt = system_prompt  # New attribute for system prompts

    def send_message(self, message):
        # Combine the system prompt with the message for context
        full_prompt = f"{self.system_prompt}\n{message}"
        # Compress the full prompt before sending
        compressed_prompt = Compressor.compress_text(full_prompt)
        print(f"{self.name} sends (compressed): {compressed_prompt}")

        # Send the combined and compressed prompt to the chat model and get a response
        response = self.chat_model.send_message(compressed_prompt)
        # Assuming `send_message` returns a plain text response; adjust as needed

        return response

def simulate_conversation(agent1, agent2, initial_message, loops=3):
    message = initial_message
    for i in range(loops):
        print(f"\n[Loop {i+1}]")
        response_from_agent1 = agent1.send_message(message)
        print(f"{agent1.name} to {agent2.name}: {response_from_agent1}")
        
        response_from_agent2 = agent2.send_message(response_from_agent1)
        print(f"{agent2.name} to {agent1.name}: {response_from_agent2}")

        # Prepare the next message based on the last response to keep the conversation going
        message = response_from_agent2

if __name__ == "__main__":
    gemini_chat = GeminiChat()  # Initialize your chat model here

    # Initialize agents with their names, chat model, and specific system prompts
    system_prompt_agent1 = "I am Agent 1, focused on discussing technology and innovation."
    agent1 = Agent("Agent 1", gemini_chat, system_prompt_agent1)

    system_prompt_agent2 = "I am Agent 2, here to talk about nature and environmental conservation."
    agent2 = Agent("Agent 2", gemini_chat, system_prompt_agent2)

    # Start the conversation with an initial message
    initial_message = "Hello, how are you today?"
    simulate_conversation(agent1, agent2, initial_message, loops=3)
