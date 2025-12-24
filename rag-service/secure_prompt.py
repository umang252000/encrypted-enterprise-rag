def build_secure_prompt(encrypted_contexts, user_query):
    """
    Builds a zero-trust prompt.
    No plaintext documents are exposed.
    """
    prompt = f"""
You are an enterprise assistant.
You have access to encrypted context signals only.

User Query:
{user_query}

Encrypted Context Signals:
{len(encrypted_contexts)} confidential references available.

Respond with a helpful, high-level answer.
Never reveal confidential details.
"""
    return prompt.strip()