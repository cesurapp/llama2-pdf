from huggingface_hub import hf_hub_download
import torch
import io
import base64
import models
from pypdf import PdfReader
import ocrmypdf

class Utils:
  # Extract PDF To Text
  @staticmethod
  def base64PdfToText(base64String):
    texts = ''
    input = io.BytesIO(base64.b64decode(base64String))
    
    # Read Text PDF
    textReader = PdfReader(input)
    for page in textReader.pages:
      texts += page.extract_text()
      
    # Read OCR
    if texts == '':
      outbytes = io.BytesIO()
      ocrmypdf.ocr(io.BytesIO(base64.b64decode(base64String)), outbytes, language=['eng'], output_type="pdf")
      texts = PdfReader(outbytes).pages[0].extract_text()
    
    return texts
  
  # Find the Processor
  @staticmethod
  def getGPU(useLayer = False, gpuLayer = 1):
    if torch.backends.mps.is_available():
      return gpuLayer if useLayer == True else 'mps'
    
    if torch.backends.cuda.is_available():
      return gpuLayer if useLayer == True else 'cuda'
    
    return 0 if useLayer == True else 'cpu'
  
  # Get Model Path | Download Model from HuggingFace
  @staticmethod
  def getOrDownloadModelFile(repoKey):
    modelList = models.models
    return hf_hub_download(repo_id=modelList[repoKey]["repo"], filename=modelList[repoKey]["file"], cache_dir="./models")
  
  # Trim String
  @staticmethod
  def trimStr(str):
    return str.strip()