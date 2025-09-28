from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserUpdate


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "update_user"

    @property
    def description(self) -> str:
        return "Updates user info"

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "User ID that should be updated."
                },
                "new_info": UserUpdate.model_json_schema()
            },
            "required": ["id"]
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        try:
            user_id = arguments["id"]
            user = UserUpdate.model_validate(arguments["new_info"])
            return self._user_client.update_user(user_id, user)
        except Exception as e:
            return f"Error while updating a user: {str(e)}"
