import requests
import json

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions, RelationsOptions, ConceptsOptions

api_key = "VQY5LwimKsA3o4O1UXgpe41PvXlRjDS8HCGKIfrFwoP2"

api_url = "https://gateway-syd.watsonplatform.net/natural-language-understanding/api"

summary_api_url = "https://api.deepai.org/api/summarization"

summary_api_key = "c75267bb-15f9-4831-a4bb-6477ef9ed214"

vi_api_key = "7c9ea5c2e8424799bb7f7fb4a16e22dd"

naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
version='2018-09-21',
iam_apikey=api_key,
url=api_url,)

class TE:

    """
        Class for text data extraction
    """

    def get_keywords(self, text=None, url=None, limit = 5):

        """
            returns a list of keywords
        """

        if text==None and url==None:
            return "Error"

        response = naturalLanguageUnderstanding.analyze(
        text=text,
        url = url,
        features=Features(
            keywords=KeywordsOptions(limit=limit)
        )).get_result()
        keywords = []
        for word in response['keywords']:
            keywords.append(word['text'])
        return keywords

    def get_concepts(self, text=None, url=None):

        """
            returns a list of dicts with text, relevance, reference url
        """

        if text==None and url==None:
            return "Error"
        
        response = naturalLanguageUnderstanding.analyze(
        text=text,
        url = url,
        features=Features(
            concepts=ConceptsOptions()
        )).get_result()
        return response['concepts']

    def get_entities(self, text=None, url=None):
        if text==None and url==None:
            return "Error"
        
        response = naturalLanguageUnderstanding.analyze(
        text=text,
        url = url,
        features=Features(
            entities=EntitiesOptions(limit=50)
        )).get_result()
        return response

    def get_relations(self, text=None, url=None):
        if text==None and url==None:
            return "Error"

        response = naturalLanguageUnderstanding.analyze(
        text=text,
        url = url,
        features=Features(
            relations=RelationsOptions()
        )).get_result()
        return response

    def get_summary(self, text):
        r = requests.post(summary_api_url,
        data={
        'text': text,
        },
        headers={'api-key': summary_api_key}
        )
        return r.json()

        


if __name__ == '__main__':
    te = TE()
    print(te.get_keywords(""" Microwaves are a type of electromagnetic radiation, as are radio waves, ultraviolet radiation, X-rays and gamma-rays. Microwaves have a range of applications, including communications, radar and, perhaps best known by most people, cooking. Electromagnetic radiation is transmitted in waves or particles at different wavelengths and frequencies. This broad range of wavelengths is known as the electromagnetic spectrum EM spectrum). The spectrum is generally divided into seven regions in order of decreasing wavelength and increasing energy and frequency. The common designations are radio waves, microwaves, infrared (IR), visible light, ultraviolet (UV), X-rays and gamma-rays. Microwaves fall in the range of the EM spectrum between radio and infrared light. Microwaves have frequencies ranging from about 1 billion cycles per second, or 1 gigahertz (GHz), up to about 300 gigahertz and wavelengths of about 30 centimeters (12 inches) to 1 millimeter (0.04 inches), according to the Encyclopedia Britannica. This region is further divided into a number of bands, with designations such as L, S, C, X and K, according to Ginger Butcher's book "Tour of the Electromagnetic Spectrum."
    """,limit = 3))
