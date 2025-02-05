import os
import yt_dlp

def download_youtube_video(urls, output_path=r"C:\Users\lucas\Desktop\ESTUDOS\DataExpert_Boot_Camp", audio_only=False, quality="best"):
    """
    Baixa vídeos do YouTube e os nomeia corretamente com prefixos numéricos baseados na ordem invertida da lista.
    
    :param urls: Lista de URLs dos vídeos do YouTube.
    :param output_path: Diretório onde os arquivos serão salvos.
    :param audio_only: Se True, baixa apenas os áudios.
    :param quality: Qualidade do vídeo ('best', 'worst', etc.).
    """
    os.makedirs(output_path, exist_ok=True)

    # *Inverte a lista para que o primeiro vídeo seja o mais antigo*
    urls = urls[::-1]

    for i, url in enumerate(urls, start=1):
        prefixo = f"{i:02d} - "  # Define o prefixo numérico para manter a ordem correta
        ydl_opts = {
            'outtmpl': os.path.join(output_path, f"{prefixo}%(title)s.%(ext)s"),
            'format': 'bestvideo+bestaudio/best',  # Aqui, estamos pegando o melhor vídeo e áudio
            'postprocessors': []  # Não é necessário nenhum pós-processamento se você não for converter para MP3
        }

        print(f"📥 Baixando vídeo {i}/{len(urls)}: {url}")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"⚠️ Erro ao baixar {url}: {e}")

if __name__ == "__main__":
    video_urls = [
              "https://www.youtube.com/watch?v=5U-BbZ9G_xU&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=dWj8VeBEQCc&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=emQM9gYh0Io&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=nyu-8Si21ec&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=XWaJFretFec&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=8J1uOJI2HFE&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=DQefW9sNmw0&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=3R-SLYK-P_0&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=JriG4d9o2Mk&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=QH1339Fy40Y&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=JiedBnTFCeg&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=ja7VOqDVkuo",
        "https://www.youtube.com/watch?v=dzB0HMtMIfI&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=EIOZY3tMIVg",
        "https://www.youtube.com/watch?v=7O7DH0ux0x4",
        "https://www.youtube.com/watch?v=XD2b8V_RfFc&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=ZRmBIktFyDI&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=nt38LZhk7jQ&ab_channel=DatawithZach",
        "https://www.youtube.com/watch?v=lvR0uDQb3s0&t=1s&ab_channel=DatawithZach"
    ]

    download_type = input("Baixar apenas áudio? (s/n): ").strip().lower() == 's'
    
    print("\n📥 Baixando os vídeos...")
    download_youtube_video(video_urls, audio_only=download_type)

    print("\n✅ Download concluído!")
