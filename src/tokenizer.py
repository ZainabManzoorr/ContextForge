import tiktoken


class Tokenizer:
    def __init__(self, model: str = "gpt-4o-mini"):
        """
        Model-aware tokenizer for RAG system.
        Falls back to cl100k_base if model encoding is unavailable.
        """
        try:
            self.enc = tiktoken.encoding_for_model(model)
        except Exception:
            self.enc = tiktoken.get_encoding("cl100k_base")

    def encode(self, text: str):
        return self.enc.encode(text)

    def decode(self, tokens):
        return self.enc.decode(tokens)

    def token_len(self, text: str) -> int:
        return len(self.enc.encode(text))