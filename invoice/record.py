#coding:utf-8
import pyaudio  #録音機能を使うためのライブラリ
import wave     #wavファイルを扱うためのライブラリ
import datetime


def getTime():
    dt_now = datetime.datetime.now()
    #月日、時間を全て二桁にする
    if dt_now.month<10:
        month = '0'+str(dt_now.month)
    else:
        month = str(dt_now.month)
    if dt_now.day<10:
        day = '0'+str(dt_now.day)
    else:
        day = str(dt_now.day)
    if dt_now.hour<10:
        hour = '0'+str(dt_now.hour)
    else:
        hour = str(dt_now.hour)
    if dt_now.minute<10:
        minute = '0'+str(dt_now.minute)
    else:
        minute = str(dt_now.minute)
    if dt_now.second<10:
        second = '0'+str(dt_now.second)
    else:
        second = str(dt_now.second)

    time = str(dt_now.year)+month+day+hour+minute+second

    return(time)

def makeWave():
    RECORD_SECONDS = 5 #録音する時間の長さ（秒）
    WAVE_OUTPUT_FILENAME = "./invoice/data/"+getTime()+".wav" #音声を保存するファイル名
    iDeviceIndex = 1 #録音デバイスのインデックス番号

    #基本情報の設定
    FORMAT = pyaudio.paInt16 #音声のフォーマット
    CHANNELS = 1             #モノラル
    RATE = 16000             #サンプルレート
    CHUNK = 2**11            #データ点数
    audio = pyaudio.PyAudio() #pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
            rate=RATE, input=True,
            input_device_index = iDeviceIndex, #録音デバイスのインデックス番号
            frames_per_buffer=CHUNK)

    #--------------録音開始---------------

    print ("Recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


    print ("Finished Recording")

    #--------------録音終了---------------

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return(WAVE_OUTPUT_FILENAME)
