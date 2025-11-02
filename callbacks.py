from langchain.callbacks.base import BaseCallbackHandler
from typing import Dict, Any, List
from langchain.schema import LLMResult

class AgentCallbackHandler(BaseCallbackHandler):
    """Callback handler for agent execution events."""

    def on_llm_start(
        self,
        serialized: dict,
        prompts: List[str],
        **kwargs: Any,
    ) -> Any:
        """Run when LLM starts."""
        print(f"***Prompt to LLM was:***\n{prompts[0]}")
        print("*************")

    def on_llm_end(
        self,
        response: LLMResult,
        **kwargs: Any,
    ) -> None:
        """Run when LLM ends."""
        print(f"***Prompt to LLM was:***\n{response.generations[0][0].text}")
        print("*************")