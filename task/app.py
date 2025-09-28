import os

from task.openai_client import OpenAIClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role
from task.prompts import SYSTEM_PROMPT
from task.tools.users.create_user_tool import CreateUserTool
from task.tools.users.delete_user_tool import DeleteUserTool
from task.tools.users.get_user_by_id_tool import GetUserByIdTool
from task.tools.users.search_users_tool import SearchUsersTool
from task.tools.users.update_user_tool import UpdateUserTool
from task.tools.users.user_client import UserClient
from task.tools.web_search import WebSearchTool

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def main():
    #TODO:
    # 1. Create UserClient
    # 2. Create OpenAIClient with all tools (WebSearchTool, GetUserByIdTool, SearchUsersTool, CreateUserTool, UpdateUserTool, DeleteUserTool)
    # 3. Create Conversation and add there first System message with SYSTEM_PROMPT (you need to write it in task.prompts#SYSTEM_PROMPT)

    print("Type your question or 'exit' to quit.")
    print("Sample:")
    print("Add Andrej Karpathy as a new user")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break
        #TODO:
        # 1. Add User message to Conversation
        # 2. Call OpenAIClient with conversation history
        # 3. Add Assistant message to Conversation and print its content


        print("=" * 100)
        print()


main()
