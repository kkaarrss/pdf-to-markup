from pdf2image import convert_from_path
import os
import base64

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="sk-****************************",
    # base_url="...",
    # organization="...",
    # other params...
)

def create(file_path):
     # remove any folder and extension from the file name
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    pages = convert_from_path(file_path)
    for i, page in enumerate(pages):
        success = False
        max_retries = 3
        retry_count = 0

        while not success and retry_count < max_retries:
            try:
                page.save(f'image_converted_file_name_{i + 1}.png', 'PNG')

                image_converted = open(f'image_converted_file_name_{i + 1}.png', 'rb')

                # Step 3: Convert the image to base64
                image_data = base64.b64encode(image_converted.read()).decode("utf-8")

                message = HumanMessage(
                    content=[
                        {"type": "text", "text": """Convert this pdf into markdown following these rules:
                                                    - IGNORE HEADERS AND FOOTERS.
                                                    - Convert any table to JSON format.
                                                    """},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                        }
                    ]
                )
                ai_msg = llm.invoke([(
                    "system",
                    "You are a powerful AI system that can convert PDFs to markdown.",
                ), message])

                text = ai_msg.content
                print(text, flush=True)

                with open(f"{file_name}.txt", "a") as file:
                    file.write(f"{text}\n")

                success = True
            except Exception as e:
                print(f"Error: {e}")
                retry_count += 1


if __name__ == "__main__":
    # for each file in the folder pdf call create(filename)
    for file in os.listdir("pdf"):
        if file.endswith(".pdf"):
            print(f"Processing file: {file}")
            create(f"pdf/{file}")
