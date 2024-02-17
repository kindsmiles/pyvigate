class PromptEngineering:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.model_name = model_name

    def generate_extraction_prompt(self, webpage_content, query):
        """
        Creates a prompt for extracting specific information from a webpage.
        """
        prompt = f"Given the following webpage content: \n{webpage_content}\n Extract information related to: {query}."
        return prompt

    def generate_summary_prompt(self, webpage_content):
        """
        Generates a prompt to summarize the webpage content.
        """
        prompt = f"Summarize the following webpage content in a concise manner: \n{webpage_content}"
        return prompt

    def generate_question_answer_prompt(self, webpage_content, question):
        """
        Creates a prompt for answering a question based on the webpage content.
        """
        prompt = f"Given the content of this webpage: \n{webpage_content}\n Answer the following question: {question}"
        return prompt

    def generate_data_validation_prompt(self, extracted_data, source_content):
        """
        Generates a prompt to validate the accuracy of extracted data against the webpage content.
        """
        prompt = f"Validate the following extracted data: {extracted_data} against this webpage content: \n{source_content}"
        return prompt

    def custom_prompt(self, custom_instructions):
        """
        Allows for the creation of custom prompts based on specific instructions.
        """
        prompt = f"{custom_instructions}"
        return prompt
