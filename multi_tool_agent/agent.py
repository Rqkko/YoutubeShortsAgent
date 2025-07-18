from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from .utils import load_instruction_from_file

scriptwriter_agent = LlmAgent(
    name="ShortsScriptwriter",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("scriptwriter_instruction.txt"),
    tools=[],
    output_key="generated_script",  # Save result to state
)

visualizer_agent = LlmAgent(
    name="ShortsVisualizer",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("visualizer_instruction.txt"),
    description="Generates visual concepts based on a provided script.",
    output_key="visual_concepts",  # Save result to state
)

# Read both state keys and combine into the final Markdown
formatter_agent = LlmAgent(
    name="ConceptFormatter",
    model="gemini-2.0-flash-001",
    instruction="""Combine the script from state['generated_script'] and the visual concepts from state['visual_concepts'] into the final Markdown format requested previously (Hook, Script & Visuals table, Visual Notes, CTA).""",
    description="Formats the final Short concept.",
    output_key="final_short_concept",
)

youtube_shorts_agent = LlmAgent(
    name="youtube_shorts_agent",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("shorts_agent_instruction.txt"),
    description="You are an agent that can write scripts, visuals and format youtube short videos. You have subagents that can do this",
    sub_agents=[scriptwriter_agent, visualizer_agent, formatter_agent],
)

root_agent = youtube_shorts_agent