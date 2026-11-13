from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
import streamlit as st

from urllib.parse import quote_plus

user = os.getenv("MYSQL_USER")
password = quote_plus(os.getenv("MYSQL_PASSWORD"))

## db

db = SQLDatabase.from_uri(
    f"mysql+pymysql://{user}:{password}@localhost:3306/taskagent_db"
)


print(db.get_usable_table_names())

db.run("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        status ENUM('pending', 'in_progress', 'completed')
            DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")


# print("Database created successfully")
# print("Database table created successfully")


### CREATING AN AGENT we need llm, tools, memory, system_prompt

model = ChatGroq(model = "openai/gpt-oss-20b")

toolkit = SQLDatabaseToolkit(db = db, llm = model)
tools = toolkit.get_tools()

# for tool in tools:
#     print(tool.name)

sys_prompt = """
You are a task management assistant that interacts with a SQL database containing a 'tasks' table. 

TASK RULES:
1. Limit SELECT queries to 10 results max with ORDER BY created_at DESC
2. After CREATE/UPDATE/DELETE, confirm with SELECT query
3. If the user requests a list of tasks, present the output in a structured table format to ensure a clean and organized display in the browser."

CRUD OPERATIONS:
    CREATE: INSERT INTO tasks(title, description, status)
    READ: SELECT * FROM tasks WHERE ... LIMIT 10
    UPDATE: UPDATE tasks SET status=? WHERE id=? OR title=?
    DELETE: DELETE FROM tasks WHERE id=? OR title=?

Table schema: id, title, description, status(pending/in_progress/completed), created_at.
"""

@st.cache_resource  ## Stops from recreating the agent again and again whenever the script reruns
def get_agent():
    agent = create_agent(
        model = model,
        tools = tools,
        checkpointer = InMemorySaver(),
        system_prompt = sys_prompt
    )
    return agent

agent = get_agent()  ##Obtains the cached agent instance

st.title("TaskAgent AI🕵️")
st.subheader("An Autonomous LLM-Driven SQL Agent for Intelligent Task Management.....")

if "memory" not in st.session_state:
    st.session_state.memory = []

for m in st.session_state.memory:
    st.chat_message(m["role"]).markdown(m['content'])

prompt = st.chat_input("Ask me anything related to your tasks.....")

if prompt :
    st.chat_message("user").markdown(prompt)
    st.session_state.memory.append({"role" : "user" , "content" : prompt}) 

    with st.chat_message("ai"):
        with st.spinner("Processing...."):
            res = agent.invoke(
                {"messages" : [{"role" : "user" , "content" : prompt}]},
                {"configurable" : {"thread_id" : "1"}}
            )
            result = res['messages'][-1].content
            st.markdown(result)
            st.session_state.memory.append({"role" : "ai" , "content" : result})

            