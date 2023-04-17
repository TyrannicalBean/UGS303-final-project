import os
import json
from AiResponse import AiResponse
from Ai import Ai
from multiprocessing.pool import Pool

FILE_NAME = "data.json"
datafile = open(FILE_NAME)
data = json.load(datafile)
responses = dict()
ai = Ai(
        openai_api_key = data['OpenAiAPIKey'], 
        openai_org = data['OpenAiOrganization'],
        model = data['model'],
        temperature = data['temperature']
    )

def main():
    processes_pool = Pool()
    responseTupel = processes_pool.map(assignResponses, data['prompts'])
    responses = {response[0]: response[1] for response in responseTupel}
    outfiles = []
    promptNum = 0
    for prompt in responses.keys():
        outfileName = "outfile" + str(promptNum+1)+".txt"
        outfiles.append(open(outfileName, 'w', encoding="utf-8"))
        outfile = outfiles[promptNum]
        outfile.write("*************** prompt:"+str(promptNum+1)+" ****************\n")
        outfile.write(prompt+"\n\n")
        for response in responses[prompt]:
            outfile.write(str(response) + "\n")
        promptNum += 1
        outfile.close()
    datafile.close()

def assignResponses(prompt):
    responses = AiResponse.generateResponses(prompt, data['responsesPerPrompt'], data['prompt extension'], ai)
    return (prompt, responses)

if __name__ == '__main__':
    main()