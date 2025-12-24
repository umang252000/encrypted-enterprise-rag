def run_llm(prompt: str):
    """
    Prototype-safe LLM response.
    Replaceable with OpenAI / local LLM.
    """
    return (
        "Based on the confidential documents, "
        "this agreement includes negotiated pricing terms "
        "with conditions tied to volume and duration."
    )