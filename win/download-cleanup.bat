REM Remove files older than 30 days. Replace [folder path] with your folder
forfiles /p "[folder path]" /s /m *.* /c "cmd /c Del @path" /d -30