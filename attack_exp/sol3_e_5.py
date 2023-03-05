from Crypto.Util.number import *
from gmpy2 import invert,iroot
from functools import reduce
nlist=[92270627783020341903769877272635163757611737252302329401876135487358785338853904185572496782685853218459404423868889360808646192858060332110830962463986164014331540336037718684606223893506327126112739408023014900003600028654929488487584130630596342720833061628867179840913592694993869009133576053124769728363, 102900163930497791064402577447949741195464555746599233552338455905339363524435647082637326033518083289523250670463907211548409422234391456982344516192210687545692054217151133151915216123275005464229534891629568864361154658107093228352829098251468904800809585061088484485542019575848774643260318502441084765867, 90267480939368160749458049207367083180407266027531212674879245323647502822038591438536367206422215464489854541063867946215243190345476874546091188408120551902573113507876754578290674792643018845798263156849027209440979746485414654160320058352559498237296080490768064578067282805498131582552189186085941328701, 90673177193017332602781813187879442725562909473411994052511479411887936365983777106776080722300002656952655125041151156684340743907349108729774157616323863062525593382279143395837261053976652138764279456528493914961780300269591722101449703932139132398288208673556967030162666354552157189525415838326249712949, 90916739755838083837461026375700330885001446224187511395518230504776419813625940046511904838818660297497622072999229706061698225191645268591198600955240116302461331913178712722096591257619538927050886521512453691902946234986556913039431677697816965623861908091178749411071673467596883926097177996147858865293]
clist=[83421434286602546493364204139182949897795123160498680670964040331447569764445309937195566103281638928183742488663157138572020817924561990979723444797045375101801354862472761507421896454904818874439231990567738173059815647539737800523632262742398190575822391771655932895657208471832891505814792263361394479317, 25585088950095290712328215701309273521406235982885781641137768116285362079062975527364909549362511146004390419156826709543326814581466248280564194951706937822088902607754944405407698735824315900942915322054614437632116732271787823814807624841386886185122143173564380877370643120953803688563589496390425159539, 44374979291120575503988741531987454898919254880086464254904878064332010355432423956182135846738023874326776872139229379943321321362822522900479438294291206287205647145759972233097276253408812699557305314344220807356024994977399840843758750494467535572805794732065369887057841293267499209427585419962565568495, 24086371701602948122317790211004032014326487279907486724991846810668564197542368948703436295770758262739732290677177527297040556666434577730354732397784651220918412407485171180732327730242552955646750279842251200227937257322414662213662054605527282812231172173474061845763736546747711105935349033514358348526, 23204039098754030513954332212496652705175644349879686639449689791620605370809827884267260830136516742466455588549253481016504796674014871020503543639681251834114159250986728840380777774144853925216884802529230212783759821262799845229436535491711201551797166082529740271577684082458494926929260818927584104158]
index=[3, 8, 12, 16, 20]
def CRT(mi, ai):
  M = reduce(lambda x, y: x * y, mi)
  ai_ti_Mi = [a * (M // m) * invert(M // m, m) for (m, a) in zip(mi, ai)]
  return reduce(lambda x, y: x + y, ai_ti_Mi) % M
def small_e_boardcast_attack(nlist , e , clist):
  m = CRT(nlist , clist)
  tmp = iroot(m , e)
  if tmp[1] == 1:
    return tmp[0]
  else:
    return 0

m = small_e_boardcast_attack(nlist,5,clist)
print(long_to_bytes(m).split(b'\x00')[-1])
'''
b't is a f'
'''