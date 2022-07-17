REM Extract subtitle from media files
for %%a in ("*.*") do ffmpeg -i "%%a" "%%~na.srt"