from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from utils import Utils
import models
import hashlib
import os

class AI:
    def __init__(self) -> None:
        self.llModel = LlamaCpp(
            model_path=Utils.getOrDownloadModelFile(os.getenv('MODEL')), 
            n_gpu_layers=Utils.getGPU(True, 1), 
            temperature=0, 
            top_p=0.9, 
            f16_kv=True,
            n_ctx=4096,
            n_batch=512, 
            verbose=True,
            embedding=False,
        )
        self.stModel = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', cache_folder='./models', model_kwargs={'device': Utils.getGPU()})
        
        print("-----------------------------------------------------------")
        print("-----------------------------------------------------------")
        print("Working Processor:: {process}".format(process = Utils.getGPU().upper()))
        print("-----------------------------------------------------------")
        print("-----------------------------------------------------------")
        return
    
    # Ask Chat
    def askAi(self, prompts):
        results = []
        for prompt in prompts:
            results.append(Utils.trimStr(self.llModel(prompt)['result']))
        
        return results

    # Ask Embedings Store
    def askEmbedings(self, vectorStore, prompts):
        llmChain = RetrievalQA.from_chain_type(
            llm=self.llModel, 
            retriever=vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":1}), 
            chain_type='stuff', 
            chain_type_kwargs={'prompt': models.models[os.getenv('MODEL')]['template']}
        )

        results = {} if isinstance(prompts, dict) else []
        for key, prompt in prompts.items() if isinstance(prompts, dict) else enumerate(prompts):
            if isinstance(prompts, dict):
                results[key]=Utils.trimStr(llmChain({'query': prompt})['result'])
            else:
                results.append(Utils.trimStr(llmChain({'query': prompt})['result']))
        
        return results

    def askText(self, context, prompts):
        # Split Text
        textChunks = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100).split_text(context)
        
        # Create Vector Store
        docId = hashlib.md5(context.encode()).hexdigest()
        vectorStore = Chroma.from_texts(textChunks, self.stModel, collection_name=docId)
        result = self.askEmbedings(vectorStore, prompts)
        vectorStore.delete_collection()
        
        return result