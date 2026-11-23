from PIL import Image,ImageDraw,ImageFont
# Second-pass visual constants keep the plate stable across deterministic runs.
W=H=1024; BG=(9,18,35); INK=(235,242,244); MUTED=(157,177,188); LINE=(47,72,88); ACC=(246,177,61); RED=(227,91,75); CYAN=(78,190,187); GREEN=(120,188,130); PAPER=(18,34,51)
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img); fp='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bp='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(n,b=0): return ImageFont.truetype(bp if b else fp,n)
def t(x,y,s,n=14,c=INK,b=0): d.text((x,y),s,font=F(n,b),fill=c)
def p(box,fill=PAPER,ol=LINE): d.rounded_rectangle(box,10,fill=fill,outline=ol,width=2)
t(34,25,'THE MONDAY ATLAS',34,ACC,1); t(36,67,'23 NOVEMBER 2026  /  FIELD NOTES FROM A WORLD IN MOTION',13,MUTED,1); d.line((35,94,989,94),fill=ACC,width=3)
t(38,108,'COP31 COLLAPSES',31,INK,1); t(39,145,'NO DEAL IN ANTALYA',23,RED,1); t(39,179,'First UN climate summit without an agreement since Copenhagen 2009.',14,MUTED); t(39,201,'44 hours overtime  •  fossil fuels absent from draft  •  Addis Ababa 2027',12,MUTED)
p((35,231,505,465),(24,39,54),(110,139,146)); t(54,248,'LEAD / SUN 22 → MON REACTION',11,ACC,1); d.rectangle((54,286,481,445),fill=(31,51,63),outline=(90,120,126),width=2)
for x in (88,165,242,319,396):
 d.rectangle((x,337,x+40,375),fill=(171,184,178),outline=(224,226,210),width=2); d.rectangle((x+7,375,x+13,415),fill=(132,148,145)); d.rectangle((x+27,375,x+33,415),fill=(132,148,145)); d.arc((x+8,310,x+32,342),180,360,fill=(214,222,210),width=3)
d.line((270,289,270,433),fill=RED,width=4); d.line((253,303,287,418),fill=RED,width=3); t(57,424,'Guterres: “deeply disappointed”',12,INK,1)
p((530,108,989,465),(13,29,43),(65,101,111)); t(550,126,'WHERE THE DAY LANDED',12,CYAN,1); mx,my,mw,mh=550,153,420,275; d.rectangle((mx,my,mx+mw,my+mh),fill=(11,40,55),outline=(57,105,112),width=1)
for i in range(1,7): d.line((mx+i*mw/7,my,mx+i*mw/7,my+mh),fill=(28,71,78),width=1)
for i in range(1,5): d.line((mx,my+i*mh/5,mx+mw,my+i*mh/5),fill=(28,71,78),width=1)
coast=[(575,205),(600,190),(630,197),(653,183),(688,193),(720,178),(751,192),(775,182),(806,205),(840,210),(867,235),(900,250),(925,280),(908,302),(874,295),(850,315),(823,298),(790,315),(760,300),(731,321),(700,302),(675,316),(646,300),(620,315),(594,292),(570,280)]; d.polygon(coast,fill=(41,77,72),outline=(102,148,125))
for x,y,l in [(667,211,'Antalya'),(759,278,'Bahrain'),(610,248,'Dymer'),(705,265,'New Delhi'),(904,347,'Wellington'),(840,270,'Cikande'),(683,251,'Tonj'),(617,235,'Poland'),(870,235,'NYC')]: d.ellipse((x-5,y-5,x+5,y+5),fill=ACC,outline=INK,width=1); t(x+8,y-2,l,10)
t(552,438,'7 regions  •  one NYC cluster dot',11,MUTED)
p((35,482,505,627),(39,30,35),(161,87,75)); t(53,497,'CO-LEAD / SAT–SUN',11,ACC,1); t(53,520,'BAHRAIN / HORMUZ',22,INK,1); d.rectangle((58,557,130,591),fill=(174,96,57)); d.polygon([(70,557),(84,532),(98,557)],fill=(222,144,57)); d.ellipse((88,533,102,547),fill=(238,180,111)); d.arc((148,548,253,615),180,360,fill=CYAN,width=3); t(272,548,'2 injured; 1 critical',12,INK,1); t(272,568,'≥3 tankers attacked',12,INK); t(272,588,'14+ still at Kharg',12,INK)
p((530,482,989,627),(23,42,48),(74,146,135)); t(548,497,'BESOK / TUE 24 NOV',12,CYAN,1); events=['UNSC technology + conflict debate — New York','UEFA UCL MD5 — Madrid / Manchester / London','Falcon 9 USSF-266 — Vandenberg, 15:55 UTC','White House turkey pardon — Washington DC, 14:00 ET','FIFA U-17 MD2 groups I–L — Doha']
for i,e in enumerate(events): yy=522+i*19; d.ellipse((550,yy+3,556,yy+9),fill=ACC); t(565,yy,e,11)
cards=[('BTC','$60.6–61.2k',CYAN),('DYMER','2 dead / 15 missing',RED),('CIKANDE','29 safe / 32 missing',ACC),('INDIA–NZ','DAY 5 / IN PROGRESS',GREEN),('NEPAL–MODI','TALKS / $2bn REQUEST',ACC),('ASIA TAPE','KOSPI −3.74%',RED),('U17','DOHA / MATCHDAY',CYAN),('NATO','BRUSSELS / AGENDA',GREEN),('SOUTH SUDAN','24 CIVILIANS',RED),('POLAND','3 × KH-101',ACC),('GAZA AID','CORRIDOR / AID',GREEN),('COP31 REACTION','NO TALKS ANNOUNCED',CYAN)]
for i,(a,b,c) in enumerate(cards):
 x=35+(i%4)*244; y=647+(i//4)*105; p((x,y,x+228,y+94),(17,32,47)); t(x+10,y+8,a,11,c,1); t(x+10,y+25,b,10); d.rectangle((x+110,y+48,x+198,y+77),outline=c,width=3); d.ellipse((x+130,y+22,x+151,y+43),outline=c,width=2); d.line((x+141,y+43,x+141,y+78),fill=c,width=2); d.line((x+112,y+78,x+198,y+78),fill=c,width=2)
d.line((35,969,989,969),fill=ACC,width=2); t(38,978,'DATE CHECK  •  MONDAY 23 NOVEMBER 2026  •  36 DISTINCT THREADS  •  SOURCES LEDGER INCLUDED',11,INK,1); img.save('entry.png',optimize=True)
