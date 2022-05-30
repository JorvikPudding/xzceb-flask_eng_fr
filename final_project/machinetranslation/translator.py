#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-05-30',
    authenticator=auth
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    trans_att = translation.get('translations')
    french_text = trans_att[0].get('translation')
    return french_text

def french_to_english(french_text):
    #write the code here
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    trans_att = translation.get('translations')
    english_text = trans_att[0].get('translation')
    return english_text
