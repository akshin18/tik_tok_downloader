from aiogram import Bot, Dispatcher,executor, types
import os
import random
import requests
from bs4 import BeautifulSoup as bs
bot = Bot(token = '1472087560:AAEBHI2CCbROQ5MBI1yQipM6b_-_jBK_xEg')

dp = Dispatcher(bot)







@dp.channel_post_handler(chat_id=[-1001159850794,-1001260436616])
async def da(post: types.Message):
    if post.text:
        if "https://vm.tiktok.com" in post.text or ( "tiktok.com" in post.text and 'video' in post.text) :
            await post.delete()

            ran = 'qwertyuiopasdfgh_-jklzxcvbnm1234567890'
            a = ''.join([random.choice(ran) for i in range(20)])
            s = requests.Session()

            r = s.get('https://ttdownloader.com/download_ajax/')

            soup = bs(r.content, 'html.parser')
            a = soup.find('input', id='token')['value']

            data = {
                'url': str(post.text),
                'format': '',
                'token': str(a)
            }

            r = s.post('https://ttdownloader.com/download_ajax/', data=data)
            soup = bs(r.content, 'html.parser')

            find = soup.find('a', attrs={'class': 'download-link'})['href']

            r = s.get(find)

            with open(f'{a}.mp4', 'wb')as f:
                f.write(r.content)
            s.close()


            with open(f'{a}.mp4','rb')as video:
                await post.answer_video(video)
            os.remove(f'{a}.mp4')




executor.start_polling(dp, skip_updates=True)

