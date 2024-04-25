import os
import openai
from lyzr import QABot
from pprint import pprint

"""### Required environment variables"""

os.environ['OPENAI_API_KEY'] = ""

"""### Download PDF from a URL

### File Path for PDF
"""

my_qabot = QABot.pdf_qa(input_files=["/content/President of the United States - Wikipedia.pdf"])

"""### Bot creation

### Let's Play
"""

# Ask a question
answer = my_qabot.query("What is the eligibility to become the president of united states")

pprint(answer.response)
