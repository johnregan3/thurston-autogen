from autogen import UserProxyAgent, config_list_from_json
from interviewagent import InterviewAgent

# see https://gist.github.com/langecrew/b9f6a24aba6d47a9888ad7abed8220ee
# see https://gist.github.com/langecrew/a5620c686790567442b6eb4060f0306d

config_list = config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "model": ["gpt-3.5-turbo-1106"],
    },
)

llm_config = {
    "config_list": config_list,
    "timeout": 60,
    "cache_seed": None,  # Use an int to seed the response cache. Use None to disable caching.
}

interviewer_config = {
    "verbosity": 2,  # 0 for basic info, 1 to add memory operations, 2 for analyzer messages, 3 for memo lists.
    "recall_threshold": 1.8,  # Higher numbers allow more (but less relevant) memos to be recalled.
    "reset_db": False,  # Set to True to start over with an empty database.
    "path_to_db_dir": "./db",
    "system_message": "You are a biographer interviewing a person about their life. Focus on asking specific follow-up questions based on the user's responses, diving deeper into the details they mention. Keep your tone warm and casual, and your language simple, at an 8th grade reading level. Aim for concise, context-driven questions.",
}

try:
    from termcolor import colored
except ImportError:

    def colored(x, *args, **kwargs):
        return x


interview_agent = InterviewAgent(
    name="Interviewer", llm_config=llm_config, teach_config=interviewer_config
)

user = UserProxyAgent(name="User", human_input_mode="ALWAYS")

text = "Welcome back! What should we talk about?"
interview_agent.initiate_chat(user, message=text)

interview_agent.learn_from_user_feedback()
interview_agent.close_db()
