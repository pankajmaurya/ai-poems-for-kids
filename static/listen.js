const convertButton = document.getElementById('convertButton');
const audioPlayer = document.getElementById('audioPlayer');

convertButton.addEventListener('click', () => convertTextToSpeech());


async function convertTextToSpeech() {
  const apiKey = 'ADD-ME';
  const url = 'https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL?optimize_streaming_latency=0';
  var mytext = document.getElementById("hintsDiv").innerHTML.replace(/<br\s*\/?>/gi,' ')
  const requestBody = {
    text: mytext,
    model_id: 'eleven_monolingual_v1',
    voice_settings: {
      stability: 0,
      similarity_boost: 0,
      style: 0.5,
      use_speaker_boost: false
    }
  };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'accept': 'audio/mpeg',
        'xi-api-key': apiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    });

    if (!response.ok) {
      throw new Error('Text to speech conversion failed.');
    }

    const audioBlob = await response.blob();
    const audioURL = URL.createObjectURL(audioBlob);

    audioPlayer.src = audioURL;
    audioPlayer.play();
  } catch (error) {
    console.error(error);
    alert('An error occurred during text to speech conversion.');
  }
}
