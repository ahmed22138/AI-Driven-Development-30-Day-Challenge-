Role: Senior Python AI Engineer
Objective: Build a "Personal Chatbot with Memory" using Chainlit and the openai-agents SDK.

1. Project Overview
The goal is to develop an intelligent web-based chatbot that persists user data (name, preferences, history) across sessions.

UI: Chainlit (Modern, responsive web interface).
Model: Google Gemini model named gemini-2.0-flash (via OpenAI Agents SDK).
Memory: Local JSON file storage (accessed via function calling).
2. Critical Technical Constraints
You must adhere to the following strict configuration rules:

Zero-Bloat Protocol (CRITICAL):
Do NOT write extra code. Do not add bells, whistles, advanced error handling (unless specified), or unnecessary comments.
Focus strictly on the integration: Connect the agent to chainlit. Nothing else.
No "Hallucinated" Features: If it's not in the SDK docs, do not invent it.
API Configuration:
Use the OpenAI Agents SDK Python Library configured for Gemini.
Base URL: https://generativelanguage.googleapis.com/v1beta/openai/
API Key: Load GEMINI_API_KEY from environment variables.
Model: Use OpenaiChatCompletionModel adapted for Gemini.
SDK Specificity: You are using openai-agents SDK. This is NOT the standard openai library. You must use the specific syntax provided by the openai-agents SDK.
Error Recovery Protocol:
If you encounter a SyntaxError, ImportError, or AttributeError related to openai-agents during development, STOP.
Do not guess the fix. You MUST call the get-library-docs tool again to re-read the documentation and verify the correct syntax before rewriting the code.
Dependency Management: Use uv for package management.
3. Architecture & File Structure
Note: The current directory is the root. Do not create a subfolder named chatbot.

.
├── .env                  # Environment variables
├── tools.py              # Memory management functions (SDK Specific Format)
├── agent.py              # Agent configuration & tool binding
├── app.py                # Chainlit UI & Event Handlers
├── user_profile.json     # JSON Storage (Auto-created if missing)
└── pyproject.toml        # UV Config
4. Implementation Steps
Follow this exact logical flow. Do not skip steps.

Step 1: Documentation & Pattern Analysis
Before writing any code, you must verify the SDK syntax.

Action: Use the MCP tool get-library-docs (or resolve-library-id) to fetch the official documentation for the openai-agents SDK.
Analysis: Deeply analyze the returned documentation. Look specifically for:
How to define tools (decorators vs classes).
How to initialize the Agent.
How to pass the OpenaiChatCompletionModel to the agent.
Check: If you are unsure, query the docs again.
Step 2: Tool Implementation (tools.py)
Create the memory functions using the strict format found in Step 1.

Functions:
read_user_profile(): Returns dict from user_profile.json. Handle FileNotFoundError (return empty dict).
update_user_profile(key: str, value: str): Updates a specific key in JSON and saves.
Format: Ensure these are defined as tools recognizable by the openai-agents SDK (e.g., using the correct @tool decorator or FunctionTool wrapper).
Step 3: Agent Configuration (agent.py)
Configure the LLM and Agent using the patterns found in Step 1.

Initialize the Gemini client using the Base URL.
Initialize the OpenaiChatCompletionModel with gemini-2.0-flash.
Bind Tools: Import tools from tools.py and register them to the agent instance exactly as the docs prescribe.
System Prompt: Set instructions to: "Greet users by name if known. Detect when users share personal info and save it using tools."
Step 4: UI & Application Logic (app.py)
Integrate with Chainlit.

@cl.on_chat_start:
Initialize the agent.
Display Welcome Message: Send the static message: "Hello, how can I assist you today?"
Constraint: Do NOT inject the username or read the profile for this specific greeting.
@cl.on_message:
Pass the user message to the Agent.
Simple Flow (Non-Streaming): Await the full response from the Agent. Do NOT use streaming mode.
Send the final text response to the UI using cl.Message().send().
Debug: Print/Display tool outputs to verify the agent is actually invoking them.
Step 5: Environment & Dependencies
Create a .env template.
List necessary packages in pyproject.toml (ensure openai-agents is included).
Smart Install: Check pyproject.toml and the current environment. If the dependencies are already installed, DO NOT run the installation commands again.
5. Testing Scenarios
New User: User says "I'm John" -> Bot saves name -> Bot replies "Nice to meet you, John."
Persistence: Restart server -> User returns -> Bot sends static greeting ("Hello, how can I assist you today?") -> User asks "Do you know my name?" -> Bot retrieves "John."
Context Update: User says "I love Python" -> Bot updates profile -> User asks "What do I like?" -> Bot retrieves "Python."