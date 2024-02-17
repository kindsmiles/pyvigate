class PromptEngineering:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.model_name = model_name

    def generate_prompt(self, template, **kwargs):
        """
        Generates a prompt based on a template and keyword arguments.
        """
        return template.format(**kwargs)