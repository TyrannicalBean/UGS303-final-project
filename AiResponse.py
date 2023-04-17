from Ai import Ai

class AiResponse:  
    
    def __init__(self, prompt:str, response:int):
        self.prompt = prompt
        self.response = response

    @staticmethod
    def generateResponses(prompt:str, num:int, promptExtension:str, ai: Ai) -> list['AiResponse']:
        fullPrompt = prompt +" "+ promptExtension
        return [AiResponse(prompt, response) for response in ai.generate_responses(fullPrompt, num)]

    def __str__(self):
        return str(self.response["message"]["content"])