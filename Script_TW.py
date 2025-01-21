import os as _O
import yt_dlp as _Y

def _A(_B):
    if not _O.path.exists(_B): 
        _O.makedirs(_B)

def _C(_D, _E='Descargas Completas'):
    _A(_E)
    _F = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': _O.path.join(_E, '%(title)s [%(id)s].%(ext)s'),
        'noplaylist': True,
        'cachedir': False,
        'no_warnings': True,
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        },
    }
    with _Y.YoutubeDL(_F) as _G:
        try:
            _H = _G.extract_info(_D, download=True)
            _I = _G.prepare_filename(_H)
            print(f"Descargado: {_I}")
        except Exception as _J:
            print(f"Error: {_J}")

if __name__ == "__main__":
    _L = "".join([chr(x) for x in [66, 121, 83, 117, 112, 114, 101, 109, 45, 84, 88]])
    print(_L)
    _K = input("Añade la URL: ")
    _C(_K)
