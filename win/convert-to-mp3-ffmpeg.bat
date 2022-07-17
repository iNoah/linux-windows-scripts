REM Convert media files to MP3.
for %%a in ("*.*") do ffmpeg -i "%%a" "%%~na.mp3"