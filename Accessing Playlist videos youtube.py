from pytube import Playlist

p = Playlist('https://youtube.com/playlist?list=PLFQ_kv5qlEJdC5kBEiEdpr5oLP2kzvI1W')

fhand = open('Tareekh ke Auraq.txt', 'w')
for i, url in enumerate(p.video_urls):
    line = str(i+1) + "\t" + str(url) + '\n\n'
    fhand.write(line)
    print(i+1, url)

fhand.close()

