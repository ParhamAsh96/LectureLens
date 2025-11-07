import pyaudio
import time
import wave


def record_voice():
    is_recorded = False
    while not is_recorded:
        try:
            p = pyaudio.PyAudio()

            FRAMES_PER_BUFFER = 3200
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            info = p.get_default_input_device_info()
            RATE = int(info["defaultSampleRate"])

            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=info["index"],
                frames_per_buffer=FRAMES_PER_BUFFER
                )
            
            start = time.time()
            print("Start recording...\n")

            second = 60
            frames = []
            for i in range(0, int(RATE/FRAMES_PER_BUFFER*second)):
                data = stream.read(FRAMES_PER_BUFFER)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            end = time.time()
            length = (end - start) / 60
            print(f"Recording duration: {length:.2f} minutes\n")

            obj = wave.open("src/notetaker/core/data/voice.wav", "wb")
            obj.setnchannels(CHANNELS)
            obj.setsampwidth(p.get_sample_size(FORMAT))
            obj.setframerate(RATE)
            obj.writeframes(b"".join(frames))
            obj.close()
            is_recorded = True
        
        except Exception as e:
            print(f"Something went wrong: {e}")
            print("The program will try again in 10 seconds.\n")
            if stream: 
                try: 
                    stream.close()
                except: 
                    pass
            p.terminate()
            time.sleep(10)