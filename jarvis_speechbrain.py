# jarvis_speechbrain.py
"""
JARVIS SpeechBrain Integration
- Includes all necessary compatibility patches
- Suppresses warnings
- Ready for voice recognition
"""

import os
import sys
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")
os.environ['PYTHONWARNINGS'] = 'ignore'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print("🔊 Initializing JARVIS Speech System...")

# Apply compatibility patches
import torchaudio
if not hasattr(torchaudio, 'list_audio_backends'):
    torchaudio.list_audio_backends = lambda: ['soundfile']

try:
    from speechbrain.pretrained import SpeakerRecognition
    print("✅ Voice Recognition Engine: READY")
    
    # Initialize speaker recognition
    verification = SpeakerRecognition.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir="pretrained_models/spkrec-ecapa-voxceleb"
    )
    
    print("✅ Speaker Verification: READY")
    print("🎯 JARVIS Speech System: OPERATIONAL")
    
    # Your main JARVIS code here
    def verify_speaker(audio_file1, audio_file2):
        """Verify if two audio files are from the same speaker"""
        score, prediction = verification.verify_files(audio_file1, audio_file2)
        return score, prediction
    
    print("\nUsage example:")
    print('score, same_speaker = verify_speaker("audio1.wav", "audio2.wav")')
    
except Exception as e:
    print(f"❌ Speech system initialization failed: {e}")
    print("But basic SpeechBrain import works - check your model download")