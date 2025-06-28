import os
from typing import NamedTuple

from dotenv import load_dotenv
from google.genai import Client
from google.genai.chats import Chat
from google.genai.types import Model

load_dotenv()

DEFAULT_MODEL = "gemini-2.0-flash-lite"


class Message(NamedTuple):
    role: str
    text: str

    def message(self):
        if self.role == "user":
            return f"User: {self.text}"
        return self.text


class AIClient:
    def __init__(self):
        self._client = Client(api_key=os.getenv("GEMINI_API_KEY"))
        self._chat: Chat | None = None
        self._model: str = DEFAULT_MODEL

    def new_chat(self):
        """Create a new chat session."""
        self._chat = self._client.chats.create(model=self._model)

    def get_messages(self):
        """Get the messages from the current chat session."""
        if self._chat is None:
            raise ValueError("Chat session not initialized. Call new_chat() first.")
        messages: list[Message] = []
        for msg in self._chat.get_history():
            role = getattr(msg, "role", None)
            # Try to get text from parts[0].text if available
            text = None
            if hasattr(msg, "parts") and msg.parts:
                part = msg.parts[0]
                # part may be a dict or object
                if isinstance(part, dict):
                    text = part.get("text", str(part))
                else:
                    text = getattr(part, "text", str(part))
            messages.append(Message(role=str(role), text=text or ""))
        return messages

    def send_message(self, message: str) -> None:
        """Send a message to the current chat session."""
        if self._chat is None:
            raise ValueError("Chat session not initialized. Call new_chat() first.")
        self._chat.send_message(message=message)

    @staticmethod
    def _is_model_suitable(model: Model) -> bool:
        """Check if the model supports content generation."""
        if not model.supported_actions:
            return False
        return "generateContent" in model.supported_actions

    def fetch_models(self) -> list[Model]:
        return list(filter(self._is_model_suitable, self._client.models.list()))
