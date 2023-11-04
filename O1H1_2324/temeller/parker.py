pi=3.14
hiz=150 #km/sn
ekvator_yaricap=6378 #km

# parker bu hız ile ekvatoru kaç dakika saniyede dolaşır

cevre= 2*pi*ekvator_yaricap
zaman=cevre/hiz

dk= zaman//60
sn=zaman%60

