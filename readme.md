# TaskAgent AI 🕵️
### An Autonomous LLM-Driven SQL Agent for Intelligent Task Management

## 📌 Overview

TaskAgent AI is an intelligent task management application powered by Large Language Models (LLMs), LangChain, and LangGraph.

It allows users to manage their tasks through natural language conversations instead of writing SQL queries manually.

The application uses an AI agent that understands user instructions, selects appropriate SQL tools, and performs database operations such as creating, reading, updating, and deleting tasks.

It uses **Groq LLM (GPT-OSS-20B)** for natural language understanding and **MySQL** for persistent task storage.

## ✨ Features

- **Natural Language Interaction:** Communicate with the task management system using a chatbot interface.
- **Create Tasks:** Add new tasks with titles and descriptions.
- **View Tasks:** Retrieve and display existing tasks.
- **Update Tasks:** Change task status between pending, in progress, and completed.
- **Delete Tasks:** Remove tasks from the database.
- **AI-Powered SQL Agent:** Automatically generates and executes SQL queries using LangChain SQL tools.
- **Conversation Memory:** Maintains conversation context using LangGraph's InMemorySaver.
- **Interactive UI:** Provides a simple chatbot interface using Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | User interface |
| LangChain | LLM integration and agent tools |
| LangGraph | Agent execution and conversation memory |
| Groq | LLM inference |
| GPT-OSS-20B | Language model |
| MySQL | Relational database |
| SQLAlchemy | Database connectivity |
| PyMySQL | MySQL database driver |
| Python-dotenv | Environment variable management |

## 🏗️ Architecture

The application follows an agent-based architecture.

```text
              User
               |
               v
         Streamlit UI
               |
               v
        LangGraph Agent
               |
       +-------+-------+
       |               |
       v               v
    Groq LLM       Memory
  (GPT-OSS-20B)  (InMemorySaver)
       |
       v
  SQLDatabaseToolkit
       |
       v
    SQLDatabase
       |
       v
   SQLAlchemy
       |
       v
   PyMySQL Driver
       |
       v
   MySQL Database
       |
       v
     Tasks Table
```

## 📂 Project Structure

```text
TaskAgent-AI/
│
├── SQL_Agent.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd TaskAgent-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

Activate the environment on Windows:

```bash
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install streamlit langchain langchain-groq langchain-community langgraph sqlalchemy pymysql python-dotenv
```
### 4. Run the Application

```bash
streamlit run SQL_Agent.py
```

The application will open in your browser.

## 💬 Example Interactions

Users can interact with the AI agent using natural language.

| User Prompt | Agent Operation |
|---|---|
| Add a task called Learn Python | CREATE |
| Show all my tasks | READ |
| Show my pending tasks | READ with filtering |
| Mark task 1 as completed | UPDATE |
| Delete task 2 | DELETE |

## 🗄️ Database Schema

The application uses a MySQL database named `taskagent_db` with a table called `tasks`.

| Column | Data Type | Description |
|---|---|---|
| id | INT | Primary key with auto-increment |
| title | VARCHAR(255) | Task title |
| description | TEXT | Task description |
| status | ENUM | pending, in_progress, completed |
| created_at | TIMESTAMP | Task creation timestamp |

## 🧠 How It Works

1. The user enters a task-related request through the Streamlit chatbot.
2. The LangGraph agent receives the user's message.
3. The Groq-hosted GPT-OSS-20B model understands the request.
4. The agent selects the appropriate SQL tool from SQLDatabaseToolkit.
5. The SQL query is executed against the MySQL database.
6. The agent processes the database result and generates a natural language response.
7. The conversation context is maintained using LangGraph's InMemorySaver.

## 🔮 Future Enhancements

- User authentication and personalized task management.
- Task deadlines and priority management.
- Task reminders and notifications.
- Improved conversation memory.
- Task filtering and analytics dashboard.
- Deployment to a cloud platform.

## 👩‍💻 Author

**Joshi Krishna Lahari**

B.Tech – Computer Science and Engineering (AI & ML)

## 📄 License

This project is intended for educational and learning purposes. 
