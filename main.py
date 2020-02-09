from publisher import ChannelPublisher
from storage import BOT_TOKEN, CHANNEL


publisher = ChannelPublisher(BOT_TOKEN, CHANNEL)


link1= "https://vc.ru/future/104863-vse-govoryat-a-oni-delayut-umnye-goroda-kotorye-my-vse-zasluzhili"
link2= 'https://international.stockholm.se/globalassets/ovriga-bilder-och-filer/smart-city/welcome-to-the-smartest-city-in-the-world-english-designfiction-sthlm-stad.pdf'
text_with_link = '[«оскар»]({})'.format(link1)
text_with_link2 = '[планируют]({})'.format(link2)


text = '#умныйСтокгольм \n \n' \
       'В конце 2019 года прошел {} в сфере городских инноваций World Smart City Awards. \n' \
       'Победитель - Стокгольм, в котором {} запускать летающих роботов-светлячков, точечно освещающих город, автономную ферму мидий, очищающих воду, общественные сады на крышах и канатные трамваи. \n' \
       'Может быть у вас есть идеи, как сделать, чтобы в списке номинантов оказался Челябинск, или Краснодар, или Самара? Плагиат хорошего опыта приветствуется.'.format(text_with_link, text_with_link2)

publisher.send_text(text)