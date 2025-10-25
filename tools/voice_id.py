# tools/voice_id.py
import torch
from speechbrain.pretrained import SpeakerRecognition

model = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb")

def verify_voice(known_voice_path, test_voice_path):
    """
    Compares two voice samples and returns True if they match (same speaker).
    """
    try:
        score, prediction = model.verify_files(known_voice_path, test_voice_path)
        return prediction.item(), score.item()
    except Exception as e:
        return False, str(e)

# Optional test script
if __name__ == "__main__":
    result, score = verify_voice("voice_samples/athul_dev.wav", "voice_samples/test.wav")
    print(f"Match: {result}, Score: {score}")
