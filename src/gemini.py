import os
from typing import NamedTuple

from dotenv import load_dotenv
from google.genai import Client
from google.genai.chats import Chat
from google.genai.types import Model

load_dotenv()

MODEL = "gemini-2.0-flash-lite"


class Message(NamedTuple):
    role: str
    text: str

    def message(self):
        if self.role == "user":
            return f"User: {self.text}"
        return self.text


class AIClient:
    def __init__(self):
        self.client = Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat: Chat | None = None

    def new_chat(self):
        """Create a new chat session."""
        self.chat = self.client.chats.create(model=MODEL)

    def get_messages(self):
        """Get the messages from the current chat session."""
        if self.chat is None:
            raise ValueError("Chat session not initialized. Call new_chat() first.")
        messages: list[Message] = []
        for msg in self.chat.get_history():
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
        if self.chat is None:
            raise ValueError("Chat session not initialized. Call new_chat() first.")
        self.chat.send_message(message=message)

    @staticmethod
    def _is_model_suitable(model: Model) -> bool:
        """Check if the model supports content generation."""
        if not model.supported_actions:
            return False
        return "generateContent" in model.supported_actions

    def fetch_all_models(self) -> list[Model]:
        return list(filter(self._is_model_suitable, self.client.models.list()))
