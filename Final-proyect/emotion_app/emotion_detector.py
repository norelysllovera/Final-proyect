import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Configuración del autenticador y el servicio
authenticator = IAMAuthenticator('TU_API_KEY')
service = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
service.set_service_url('TU_URL_DEL_SERVICIO')

def emotion_predictor(text):
    if not text:
        return {'error': 'No text provided'}, 400
    response = service.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    emotions = response['emotion']['document']['emotion']
    formatted_response = json.dumps(emotions, indent=2)
    return formatted_response
