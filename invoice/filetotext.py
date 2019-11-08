# coding:utf-8
from . import record
import sys
import io
import csv
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './invoice/VoiceToInvoice.json'

def transcribe_file(speech_file):
    """Transcribe the given audio file."""

    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    datalist = []
    with io.open('./invoice/data.csv') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            datalist.append(row[0])


    audio = types.RecognitionAudio(content=content)
    print('Recognizing...')
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ja-JP',
        speech_contexts=[types.SpeechContext(
            phrases=datalist
        )])

    response = client.recognize(config, audio)
    print('Finished Recognizing')
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    results = {}
    n = 0
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        #------result.alternatives[0].transcript------
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        number = 'k'+str(n)
        results[number]=(u'認識結果: {}'.format(result.alternatives[0].transcript))
        n += 1

    return(results)


def main():
    filename = makeWave()
    transcribe_file(filename)

if __name__=='__main__':
    main()
