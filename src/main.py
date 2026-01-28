from __future__ import annotations

import asyncio

from dotenv import load_dotenv

from src.llm import LLMClient
from src.memory import ChatMemory


HELP = """Commandes:
  /help            afficher l'aide
  /reset           reset la conversation (garde system)
  /exit            quitter
"""


async def run() -> None:
    load_dotenv()

    llm = LLMClient()
    mem = ChatMemory()
    mem.seed()

    print("LLM Chat CLI")
    print(HELP)

    while True:
        user = input("toi> ").strip()

        if not user:
            continue
        if user in {"/exit", "exit", "quit"}:
            break
        if user == "/help":
            print(HELP)
            continue
        if user == "/reset":
            mem.clear_to_system()
            print("Conversation réinitialisée.\n")
            continue

        mem.add_user(user)

        try:
            answer = await llm.chat(mem.messages)
        except Exception as e:
            print(f"\n[Erreur API] {e}\n")
            continue

        mem.add_assistant(answer)
        print(f"\nIA> {answer}\n")


if __name__ == "__main__":
    asyncio.run(run())
