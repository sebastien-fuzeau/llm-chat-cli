from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

import httpx


class LLMClient:
    """
    Minimal client for OpenAI-compatible Chat Completions endpoint.
    Uses env:
      - OPENAI_API_KEY (required)
      - MODEL (default: gpt-4.1-mini)
      - OPENAI_BASE_URL (default: https://api.openai.com/v1)
    """

    def __init__(
            self,
            api_key: Optional[str] = None,
            model: Optional[str] = None,
            base_url: Optional[str] = None,
    ) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model or os.getenv("MODEL", "gpt-4.1-mini")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY manquant (mets-le dans .env)")

    async def chat(self, messages: List[Dict[str, Any]]) -> str:
        url = f"{self.base_url.rstrip('/')}/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"model": self.model, "messages": messages}

        async with httpx.AsyncClient(timeout=30) as client:
            res = await client.post(url, headers=headers, json=payload)
            res.raise_for_status()
            data = res.json()

        return data["choices"][0]["message"]["content"]
