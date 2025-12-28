from src.core.rag.docs_processor import Processor
from src.utils.logging import Logger

logger = Logger()
def test_processor_load(file_path: str):
    processor = Processor()
    documents = processor.load(file_path)
    logger.log(f"Loaded {len(documents)} documents.","Info")
    

test_processor_load("/home/schaffen/Workspace/VDC/data/benh-tre-em.pdf")