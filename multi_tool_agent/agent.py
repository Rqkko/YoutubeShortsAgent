from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from .utils import load_instruction_from_file

scriptwriter_agent = LlmAgent(
    name="ShortsScriptwriter",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("scriptwriter_instruction.txt"),
    tools=[google_search],
    output_key="generated_script",  # Save result to state
)

root_agent = scriptwriter_agent