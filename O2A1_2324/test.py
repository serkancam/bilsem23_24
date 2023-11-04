#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Turkce Vigenere Sifreleme
# Copyright 2013 Caner BASARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


HARFLER = u'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
HARFDONUSUM = [(u'i', u'İ'), (u'ğ', u'Ğ'), (u'ü', u'Ü'), (u'ş', u'Ş'), (u'ö', u'Ö'), (u'ç', u'Ç'), (u'ı', u'I')]


def buyult(s):
    for x, y in HARFDONUSUM:
        s = s.replace(x, y)
    return s.upper()


def kucult(s):
    for x, y in HARFDONUSUM:
        s = s.replace(y, x)
    return s.lower()


def iletiDonustur(anahtar, ileti, kip):    
    donusturulmus = []

    anahtarIndex = 0
    anahtar = buyult(anahtar)

    for harf in ileti:
        num = HARFLER.find(buyult(harf))
        if num != -1:
            if kip == 'sifrele':
                num += HARFLER.find(anahtar[anahtarIndex])
            elif kip == 'desifrele':
                num -= HARFLER.find(anahtar[anahtarIndex])

            num %= len(HARFLER)

            if harf.isupper():
                donusturulmus.append(HARFLER[num])
            elif harf.islower():
                donusturulmus.append(kucult(HARFLER[num]))

            anahtarIndex += 1
            if anahtarIndex == len(anahtar):
                anahtarIndex = 0
        else:
            donusturulmus.append(harf)

    return ''.join(donusturulmus)

mesaj=u"Gençler cesaretimizi takviye ve idame eden sizlersiniz. Siz, almakta olduğunuz terbiye ve irfan ile insanlık ve medeniyetin, vatan sevgisinin, fikir hürriyetinin en kıymetli timsali olacaksınız. Yükselen yeni nesil, istikbal sizsiniz. Cumhuriyeti biz kurduk, onu yükseltecek ve yaşatacak sizsiniz."

sifreli=u"Ğnbuprs kpkeffeügnlj elecvzn iv npbvp vhro çürprsçüğnl. Şşk, spbbuğs şaefşnsıa epjfvzn iv nfgib çpr jyfssaiu iv rrenbççruşb, öehby fvcşjçüğnc, gşyçü uvceççruşbçs ro uuprruüü mnbşizç şabklevüosk. Pbzşnzvs kfyü ğıgjü, ükzvljlf vvaçüğnl. Çfabafjhpmn njı ynüpüu, cğa kvufvphfkpe cr zigszmçiy knlşşbçd."
print (iletiDonustur(u'bilsem', sifreli, 'desifrele'))