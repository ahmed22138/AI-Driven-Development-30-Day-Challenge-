import os
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from tools import read_user_profile, update_user_profile

# 1. Initialize the Gemini client using the Base URL
# 2. Load GEMINI_API_KEY from environment variables.
# 3. Initialize the OpenAIChatCompletionsModel with gemini-2.0-flash.
openai_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY"),
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=openai_client,
)

# 4. Import tools from tools.py and register them to the agent instance.
# 5. Set the system prompt
agent = Agent(
    name="Personal Chatbot",
    instructions="Greet users by name if known. Detect when users share personal info and save it using tools.",
    model=gemini_model,
    tools=[read_user_profile, update_user_profile],
)
