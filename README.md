# AI Simple Agent Task
Python implementation for building AI-powered chat applications using the OpenAI API with advanced tool integration.

## 🎯 Task Overview

Implement simple Agent from scratch that will work we User Service. In this task you need to practice to add custom tools and make requests to OpenAI API.

## 🏗️ Architecture

### <img src="flow.png">
```
task/
├── models/
│   ├── conversation.py    ✅ Complete
│   ├── message.py         ✅ Complete
│   └── role.py            ✅ Complete
├── tools/                
│   ├── base.py            ✅ Abstract base tool interface
│   ├── web_search.py               🚧 TODO: implement all points described in TODO seactions
│   └── user/                       
│       ├── base.py                 ✅ Abstraction for user service related tools
│       ├── create_user_tool.py     🚧 TODO: implement all points described in TODO seactions
│       ├── update_user_tool.py     🚧 TODO: implement all points described in TODO seactions
│       ├── delete_user_tool.py     🚧 TODO: implement all points described in TODO seactions
│       ├── get_user_by_id_tool.py  🚧 TODO: implement all points described in TODO seactions
│       ├── search_users_tool.py    🚧 TODO: implement all points described in TODO seactions
│       └── models/           
│           └── user_info.py  ✅ Complete  
├── client.py   🚧 TODO: implement all points described in TODO seactions
├── prompts.py  🚧 TODO: provide system prompt
└── app.py      🚧 Add tool configs and play with different models
```

## 📋 Requirements

- **Python**: 3.11 or higher
- **Dependencies**: Listed in `requirements.txt`
- **Docker**

## 🔧 Setup Instructions

### 1. Environment Setup

```bash
python -m venv .venv
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. API Configuration

**Run user service** (run `docker-compose.yml`)

### If the task in the main branch is hard for you, then switch to the `with-detailed-description` branch

## 🔍 API Reference

### Request Format
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Who is Andrej Karpathy?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "web_search_tool",
        "description": "Tool for WEB searching.",
        "parameters": {
          "type": "object",
          "properties": {
            "request": {
              "type": "string",
              "description": "The search query or question to search for on the web"
            }
          },
          "required": [
            "request"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "get_user_by_id",
        "description": "Provides full user information",
        "parameters": {
          "type": "object",
          "properties": {
            "id": {
              "type": "number",
              "description": "User ID"
            }
          },
          "required": [
            "id"
          ]
        }
      }
    },
    ...
  ]
}
```

### Response Format
With tool calls
```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "",
        "tool_calls": [
          {
            "id": "call_6JriK7u5DL2heJ1lkw08WUFd",
            "function": {
              "arguments": "{\"request\":\"Andrej Karpathy profile\"}",
              "name": "web_search_tool"
            },
            "type": "function"
          }
        ]
      },
      "finish_reason": "tool_calls"
    }
  ]
}
```

Final response:
```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Andrej Karpathy is..."
      },
      "finish_reason": "stop"
    }
  ]
}
```