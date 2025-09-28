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
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

def main():
    user_client = UserClient()

    openai_client = OpenAIClient(
        model="gpt-4o",
        api_key=OPENAI_API_KEY,
        tools=[
            WebSearchTool(open_ai_api_key=OPENAI_API_KEY),
            GetUserByIdTool(user_client),
            SearchUsersTool(user_client),
            CreateUserTool(user_client),
            UpdateUserTool(user_client),
            DeleteUserTool(user_client),
        ]
    )

    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, SYSTEM_PROMPT))

    print("Type your question or 'exit' to quit.")
    print("Sample:")
    print("Add Andrej Karpathy as a new user")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break

        conversation.add_message(Message(Role.USER, user_input))

        ai_message = openai_client.get_completion(conversation.get_messages(), print_request=True)
        conversation.add_message(ai_message)
        print("🤖:", ai_message.content)
        print("=" * 100)
        print()


main()
