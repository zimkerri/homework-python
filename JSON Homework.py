import json
from xml.etree.ElementTree import indent

data = {'Model':'Malibu', 'Rangi':'Qora', 'Yili':'2020','Narhi':'40000'}

data_json = json.dumps(data, indent=2)
print(data_json)

with open('data.json', 'w') as f:
    json.dump(data_json, f)

talaba = {'ism':'Hasan', 'familiya':'Husanov', 'tyil':'2000'}
talaba_json = json.dumps(talaba)
print(talaba_json)
print('-----------------------------------')
with open('talaba.json', 'w') as g:
    json.dump(talaba_json, g)

with open('students (2).json', 'r') as x:
    students = json.load(x)
print(students)
print('-------------------------------------')

pretty = {"batchcomplete":"","query":{"pages":{"13801":{"pageid":13801,"ns":0,"title":"Python","extract":"Python ([\u02c8p\u028c\u026a\u03b8 (\u0259)n] \u2014 payton, piton) \u2014 turli sohalar uchun yuqori darajadagi umumiy maqsadli dasturlash tili. Uning dizayn falsafasi muhim chekinishdan foydalangan holda kodning o\u02bbqilishiga urg\u02bbu beradi. Uning til konstruksiyalari va obyektga yo\u02bbnaltirilgan yondashuvi dasturchilarga kichik va yirik loyihalar uchun aniq, mantiqiy kod yozishda yordam berishga qaratilgan. Shuningdek Python sun\u02bciy intellekt hamda ma\u02bclumotlar muhandisiligi sohalarining tili hisoblanadi.\nPython deyarli barcha platformalarda ishlay oladi, xususan Windows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar shular jumlasidandir. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud bo\u02bblib, uning nomi \u2014 IronPython dasturlash muhitidir.\nGuido van Rossum 1980-yillarning oxirida ABC dasturlash tilining davomchisi sifatida Python ustida ishlay boshladi va birinchi marta 1991-yilda Python 0.9.0 versiyasini ommaga e\u02bclon qildi.\nPython dasturlash tiliga bo\u02bblgan talab yildan yilga oshib bormoqda. CodingDojo portalining tadqiqotlariga ko\u02bbra, 2020\u20142021-yillarda aynan Python tilida dasturlovchi mutaxassislarga eng ko\u02bbp talab bo\u02bblgan."}}}}
pretty_json = json.dumps(pretty, indent=2)
print(pretty_json)