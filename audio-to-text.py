import whisper # Biblioteca de transcrição do áudio. Use pip install whisper para instalar no seu computador.
import openai # Biblioteca de GPT-3, a mesma do ChatGPT. Use pip install openai para instalar no seu computador.

openai.api_key = "YOUR_API_KEY"

# Função que recebe um áudio e retorna a transcrição dele.
def obterTranscricao(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio)
    transcricao = result["text"]
    return transcricao

# Função que recebe um texto e retorna a resposta do GPT-3.
def gerarRespostaGPT3(texto):
    completions = openai.Completion.create(
        engine='text-davinci-003',
        temperature=0.2,
        prompt=texto,
        max_tokens=1500,
        n=1,
        stop=None,
    )
    resposta = completions.choices[0].text
    return resposta

# Função que recebe um áudio e retorna o áudio legível.
def gerarAudioLimpo(audio):
    transcricao = obterTranscricao(audio)
    # Prompt para o GPT-3, específico para a transcrição do áudio.
    prompt = 'Torne a transcrição a seguir legível:\n\n' + transcricao + '\n\n'
    # Geração da resposta do GPT-3.
    audioLimpo = gerarRespostaGPT3(prompt)
    print (audioLimpo)

# Exemplo de chamada de uso da função.
gerarAudioLimpo("audio.ogg") # Substitua "audio.ogg" pelo nome do seu arquivo de áudio.