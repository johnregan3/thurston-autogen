from autogen.agentchat.contrib.teachable_agent import TeachableAgent

# InterviewAgent is a TeachableAgent customized for life-lesson interviews.
# from https://gist.github.com/langecrew/a5620c686790567442b6eb4060f0306d

try:
    from termcolor import colored
except ImportError:

    def colored(x, *args, **kwargs):
        return x

class InterviewAgent(TeachableAgent):

    goal = "creating a chatbot to simulate an interaction with this person"
    details = "names, dates, places, memories, anectodes, stories, skills, interests, values, beliefs, emotional responses, speech patterns, humor"

    def consider_memo_storage(self, comment):
        """Decides whether to store something from one user comment in the DB."""


        is_ai_generated = self.analyze(
            comment,
            "Was the TEXT likely an AI-generated explanation? Look for any AI statements about processing, capabilities, or instructions, distinguishing them from genuine user responses. Respond with yes or no. ONLY RESPOND WITH ONE WORD",
        )

        if "yes" in is_ai_generated.lower():
            return

        # Check for broad legacy-related information.
        is_relevant = self.analyze(
            comment,
            "Does the TEXT include any details that are important for " + self.goal + ", noting any " + self.details + ", etc.? Respond with yes or no. ONLY RESPOND WITH ONE WORD",
        )

        if "yes" in is_relevant.lower():

            # Extract all relevant CRM information.
            summary = self.analyze(
                comment,
                "Extract all details from the TEXT that are important for " + self.goal + " and provide a summary. Note any " + self.details + ", or anything else that may be useful.",
            )

            if summary.strip():
                # Formulate a question this information could answer.
                question = self.analyze(
                    comment,
                    "If someone asked for a summary of this persons's " + self.details + " based on the TEXT, what question would they be asking? Provide the question only. If there is no question, respond with 'none'.",
                )

                if "none" not in question.lower():
                    # Store the summary as a memo.
                    if self.verbosity >= 1:
                        print(colored("\nREMEMBER THIS INFORMATION", "light_yellow"))
                    self.memo_store.add_input_output_pair(question, summary)

    def consider_memo_retrieval(self, comment):
        """Decides whether to retrieve memos from the DB, and add them to the chat context."""
        # Directly use the user comment for memo retrieval.
        memo_list = self.retrieve_relevant_memos(comment)

        # Additional CRM-specific check.
        response = self.analyze(
            comment,
            "Does the TEXT request information related to this persons's " + self.details + ", etc? Answer with yes or no.",
        )
        if "yes" in response.lower():
            # Retrieve relevant CRM memos.
            life_query = "What are this person's " + self.details + ", etc. based on previous interactions?"
            memo_list.extend(self.retrieve_relevant_memos(life_query))

        # De-duplicate the memo list.
        memo_list = list(set(memo_list))

        # Append the memos to the last user message.
        return comment + self.concatenate_memo_texts(memo_list)
