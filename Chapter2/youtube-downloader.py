import pytube

#다운 받을 동영상 URL지정
yt = pytube.YouTube("https://www.youtube.com/watch?v=_PFxNS8p6PI&t=3s")
videos = yt.streams.all()

# print('videos', videos)

# for i in  range(len(videos)) :  # range(1,6) 1,2,3,4,5
#     print(i, ',', videos[i])


down_dir = "/Users/yuri/Documents/crawling/section2/download/"

videos[0].download(down_dir)
