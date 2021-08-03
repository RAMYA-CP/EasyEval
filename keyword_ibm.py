import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
import pandas as pd
from docx import Document
import re
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey='api-key'

authenticator = IAMAuthenticator(apikey)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://gateway-syd.watsonplatform.net/natural-language-understanding/api')

def create_keywords(sub_name,answer_key):
            # sub_name=sub_name.lower()
            # sub_name=sub_name[0].upper()+sub_name[1:]
            f=Document(answer_key)
            list_key=[]
            for i in f.paragraphs:
                print(i.text)
                response = natural_language_understanding.analyze(
                text=i.text,
                features=Features(keywords=KeywordsOptions(limit=3))).get_result()

                results=json.dumps(response, indent=2)

                text=''
                start=results.find('keywords')
                end=results.rfind(']')
                for i in range(start,end):
                    text+=results[i]

                cor_text=text
                keywords=[]
                for i in range(0,3):
                    result = re.search('text":(.*)",', cor_text)
                    cor_text=cor_text[cor_text.find(result.group(1)):]
                    keywords.append(result.group(1)[2:])
                print(keywords)
                list_key.append(keywords)
                df = pd.DataFrame(list_key)
                print(df)
                df.to_csv(sub_name+'_keywords.csv',header=False,index=False)
create_keywords('Answerkey.docx')
