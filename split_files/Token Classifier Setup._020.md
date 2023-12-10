---
file: /home/pedro/Documents/chatgpt_export/Markdown/Token Classifier Setup..md
heading_stack: <root> -> 7049cac4-1b3f-4580-87a8-9fe55086d69e -> System -> e179ded9-9f60-4738-93be-a4499fba828c -> System -> aaa20480-f877-4b91-a126-0ab43c876e05 -> User -> 0b1a1818-bf5a-4512-93fb-4cc2141fc1a9 -> Assistant -> 14f7dbc1-340f-4816-a087-bd1bfba100a7 -> Tool -> b64baf9f-de05-4932-bb5c-856dd7f3412b -> Assistant -> 016f628a-e89c-4676-84aa-b656bffb2a93 -> Tool -> 5348c801-dcbe-40bb-a64c-84c302f23f38 -> Assistant -> edfbcbe6-5256-4144-844d-f39a1140e39d -> Assistant -> ba54d961-50a4-413a-92a8-094e86e2361b -> Tool
---
# Tool

==== Cell ID: 6f95f711-69a8-42f4-862c-3cf645ae6e5b
Cell Type: code
Cell State: finished_with_no_error
== Source ==
!pip install -q scikit-learn
!pip install -q nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import nltk
nltk.download('punkt')
== Output ==
[nltk_data] Downloading package punkt to /home/noteable/nltk_data...                                                    
                                                                    [nltk_data]   Unzipping tokenizers/punkt.zip.
True



[child ⬇️](#28fdfc2e-cb1f-4050-8cc0-63e71098fd88)

---

(main branch ⎇)
###### 28fdfc2e-cb1f-4050-8cc0-63e71098fd88
[parent ⬆️](#ba54d961-50a4-413a-92a8-094e86e2361b)
