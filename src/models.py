from langchain.prompts import PromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

# Prompt Templates
templateChat=ChatPromptTemplate(input_variables=['context', 'question'], messages=[
    HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context', 'question'], 
      template="[INST]<<SYS>> Use the following pieces of retrieved context to answer the question. Write only answer, don't write anything else. Use short answers. Use commas instead of lists. Do not write the answer type. <</SYS>> \nQuestion: {question}\nContext: {context}\nAnswer:[/INST]"
    ))
])
template=PromptTemplate(input_variables=['context', 'question'], template="""Use the following pieces of retrieved context to answer the question. Write only answer, don't write anything else. Use short answers. Use commas instead of lists. Do not write the answer type.

Context: {context}
Question: {question}

Answer:"""
)

# Models
models = {
  "7b-Q4KM-CHAT": {
    "repo": "TheBloke/Llama-2-7B-Chat-GGUF",
    "file": "llama-2-7b-chat.Q4_K_M.gguf",
    "template": templateChat
  },
  "7b-Q5KM-CHAT": {
    "repo": "TheBloke/Llama-2-7B-Chat-GGUF",
    "file": "llama-2-7b-chat.Q5_K_M.gguf",
    "template": templateChat
  },
  "13b-Q4KM-CHAT": {
    "repo": "TheBloke/Llama-2-13B-chat-GGUF",
    "file": "llama-2-13b-chat.Q4_K_M.gguf",
    "template": template
  },
  "13b-Q5KM-CHAT": {
    "repo": "TheBloke/Llama-2-13B-chat-GGUF",
    "file": "llama-2-13b-chat.Q5_K_M.gguf",
    "template": templateChat
  },
  "70b-Q4KM-CHAT": {
    "repo": "TheBloke/Llama-2-70B-Chat-GGUF",
    "file": "llama-2-70b-chat.Q4_K_M.gguf",
    "template": templateChat
  },
  "70b-Q5KM-CHAT": {
    "repo": "TheBloke/Llama-2-70B-Chat-GGUF",
    "file": "llama-2-70b-chat.Q5_K_M.gguf",
    "template": templateChat
  },
  
  # Uncensored (LLama2 7B)
  "luna-7b-Q4KM-CHAT": {
    "repo": "TheBloke/Luna-AI-Llama2-Uncensored-GGUF",
    "file": "luna-ai-llama2-uncensored.Q4_K_M.gguf",
    "template": template
  },
   "luna-7b-Q5KM-CHAT": {
    "repo": "TheBloke/Luna-AI-Llama2-Uncensored-GGUF",
    "file": "luna-ai-llama2-uncensored.Q5_K_M.gguf",
    "template": template
  }
}