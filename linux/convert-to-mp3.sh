# convert media files to MP3
for i in *.* ; do 
    ffmpeg -i "$i" "$(basename "${i/.mp3}").aac" 
    
done
