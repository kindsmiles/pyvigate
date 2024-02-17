from ..ai.prompt_engineering import PromptEngineering


class ScrapePrompts(PromptEngineering):
    def extraction_prompt(self, webpage_content, query):
        template = "Given the following webpage content: \n{content}\n Extract information related to: {query}."
        return self.generate_prompt(template, content=webpage_content, query=query)

    def summary_prompt(self, webpage_content):
        template = "Summarize the following webpage content in a concise manner: \n{content}"
        return self.generate_prompt(template, content=webpage_content)

    def question_answer_prompt(self, webpage_content, question):
        template = "Given the content of this webpage: \n{content}\n Answer the following question: {question}"
        return self.generate_prompt(template, content=webpage_content, question=question)

    def data_validation_prompt(self, extracted_data, source_content):
        template = "Validate the following extracted data: {data} against this webpage content: \n{content}"
        return self.generate_prompt(template, data=extracted_data, content=source_content)

    def custom_prompt(self, custom_instructions):
        template = "{instructions}"
        return self.generate_prompt(template, instructions=custom_instructions)
