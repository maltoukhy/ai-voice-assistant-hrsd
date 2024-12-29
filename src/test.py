import os
from dotenv import load_dotenv

from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from pathlib import Path

import glob

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llamaparse_api_key = os.getenv("LLAMA_PARSE_API_KEY")


def parse_documents(directory_path):
    # set up parser
    parser = LlamaParse(
        api_key=llamaparse_api_key
        , result_type="markdown"  # "markdown" and "text" are available
    )

    directory_path = Path(directory_path).absolute()

    # use SimpleDirectoryReader to parse our file
    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(input_files=[file for file in glob.glob(f"{directory_path}/*.pdf")], file_extractor=file_extractor).load_data()
    with open("test_file.txt", "w", encoding="utf-8") as f:
        for document in documents:
            f.write(document.get_content())
            f.write("\n")

parse_documents(directory_path='knowledge_base')