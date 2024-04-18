from pytube import YouTube

try:
    #ask user for url
    url = input ("Enter the Youtube URL:")
    yt= YouTube(url)

    print("Title:",yt.title)
    print("Views:",yt.views)

    #Get the highest stream resolution

    yd=yt.streams.get_highest_resolution()

    #download the video to the current directory
    yd.download()

    print("Download complete...")
except Exception as e:
    print("An Error occured:",str(e))