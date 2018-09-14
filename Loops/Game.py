#!/usr/bin/env python
# -*- coding: utf-8 -*-


def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
    return input(question) - 1


items = [u"корзинка" , u"картина" , u"ваза" ,  u"абажур" ,  u"туфля" , u"двери"]


keylocation = 2


keyfound = 0


loop = 1


print "Останньої ночі ви пішли спати у своєму комфортному ліжечку у "
print "власному домі."
print ""
print "Але тепер, пробудившись, опинився у закритій кімнаті. Ти не знаєш "
print "як ти попав туди, і навіть яка зараз година. В кімнаті ти бачиш"
print len(items), "речей:"

for x in items:
    print x
print ""
print "Двері зачинені! Можливо ключ десь всередині кімнати?"

while loop == 1:
    choice = menu(items, "Что именно ты хочешь сейчас проверить? ")
    if choice == 0:
        if choice == keylocation:
            print u"    Ты нашел маленький ключ в корзинке!"
            print ""
            keyfound = 1
        else:
            print u"    Ты ничего не нашел в корзинке!"
            print ""
    elif choice == 1:
        if choice == keylocation:
            print u"    Ты нашел маленький ключ за картиной!"
            print ""
            keyfound = 1
        else:
            print u"    Ты ничего не нашел за картиной!"
            print ""
    elif choice == 2:
        if choice == keylocation:
            print u"    Ты нашел маленький ключ в вазе!"
            print ""
            keyfound = 1
        else:
            print u"    Ты ничего не нашел в вазе!"
            print ""
    elif choice == 3:
        if choice == keylocation:
            print u"    Ты нашел маленький ключ над абажуром!"
            print ""
            keyfound = 1
        else:
            print u"    Ты ничего не нашел над абажуром!"
            print ""
    elif choice == 4:
        if choice == keylocation:
            print u"    Ты нашел маленький ключ в туфле!"
            print ""
            keyfound = 1
        else:
            print u"    Ты ничего не нашел в туфле!"
            print ""
    elif choice == 5:
        if keyfound == 1:
            loop = 0
            print u"    Ти вставив ключик у замкову щілину, провернув його, " \
                  u"і... почув клік!"
            print ""
        else:
            print u"    Двері зачинені, спочатку треба знайти ключ."
            print ""
print u"Світло пробивається у відкриту кімнату крізь відчинені тобою двері. " \
      u"Двері до твоєї свободи! :-)"


def check(choice, location):
    if choice == location:
        print u"Ты нашел ключ!"
        return 1
    else:
        print u"Здесь ничего нет :("
        return 0


while loop == 1:
    keyfound = check(menu(items, u"Куда еще заглянем? "), keylocation)
    if keyfound == 1:
        print u"    Ти вставив ключик у замкову щілину, провернув його, " \
              u"і... почув клік!"
        loop = 0

print u"Світло пробивається у відкриту кімнату крізь відчинені тобою двері. " \
      u"Двері до твоєї свободи! :-)"