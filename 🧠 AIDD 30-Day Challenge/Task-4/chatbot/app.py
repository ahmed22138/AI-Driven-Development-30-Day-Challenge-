import chainlit as cl
from agent import agent # Assuming agent.py contains the agent instance
from agents import Runner

@cl.on_chat_start
async def start():
    cl.user_session.set("agent", agent)
    await cl.Message(content="Hello, how can I assist you today?").send()

@cl.on_message
async def main(message: cl.Message):
    current_agent = cl.user_session.get("agent")
    
    # Simple Flow (Non-Streaming): Await the full response from the Agent.
    # Debug: Print/Display tool outputs to verify the agent is actually invoking them.
    # The Runner will automatically handle tool calls made by the agent.
    result = await Runner.run(current_agent, message.content)

    # Send the final text response to the UI using cl.Message().send().
    await cl.Message(content=result.final_output).send()
