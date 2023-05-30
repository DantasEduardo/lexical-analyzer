import re
import unicodedata


STOP_WORDS = ["de","a","o","que","e","do","da","em","um","para","com","nao","uma","os","no","se","na","por","mais","as","dos", 
              "como","mas","foi","ao","das","tem","seu","sua","ou","ser","quando","ha","nos","ja","esta","eu","tambem", 
              "so","pelo","pela","ate","isso","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse",
              "estao","voce","vc","tinha","foram","essa","num","nem","suas","meu","minha","tem","numa","pelos","havia","seja",
              "qual","sera","nos","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","voces","vcs",
              "vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta", 
              "estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","esta","estamos","estao","estive",
              "esteve","estivemos","estiveram","estava","estavamos","estavam","estivera","estiveramos","esteja","estejamos",
              "estejam","estivesse","estivessemos","estivessem","estiver","estivermos","estiverem","hei","ha","havemos","hao"
              "houve","houvemos","houveram","houvera","houveramos","haja","hajamos","hajam","houvesse","houvessemos","houvessem"
              "houver","houvermos","houverem","houverei","houvera","houveremos","houverao","houveria","houveriamos","houveriam"
              "sou","somos","sao","era","eramos","eram","fui","foi","fomos","foram","fora","foramos","seja","sejamos","sejam",
              "fosse","fossemos","fossem","for","formos","forem","serei","sera","seremos","serao","seria","seriamos","seriam",
              "tenho","tem","temos","tem","tinha","tinhamos","tinham","tive","teve","tivemos","tiveram","tivera","tiveramos",
              "tenha","tenhamos","tenham","tivesse","tivessemos","tivessem","tiver","tivermos","tiverem","terei","tera","teremos"
              "terao","teria","teriamos","teriam","pq"]

GOOD_WORDS = ["promissor","impressionante","exponencial","destacado","florescente","prospero","lucrativo","significativo","notavel","ascensao",
              "surpreendente","encorajador","empolgante","brilhante","solido","favoravel","promovendo","crescimento","estavel","relevante",
              "positivo","alta","oferta","crescente","aumento","forte","fortes","melhor","melhores","qualificado","qualificados","qualificada",
              "qualificadas"]


BAD_WORDS = ["volatil","instavel","declinante","desfavoravel","declinio","prejudicial","problematico","arriscado","desafiador","especulativo",
             "manipulado","controverso","desvalorizado","inconstante","sobrecarregado","descontrolado","fragilizado","desaquecido","desorganizado",
             "vulneravel","conflituoso","erro","queda","reducao","reducoes","recuam","pior","piorar","falta","faltava","negativa","negativar",
             "negativo","cancer","prejudica","prejudicar","prejudicou"]

INTENSE_WORDS = ["muito", "bastante", "absoluto", "absolutamente", "extremamente", "profundo", "profundamente", "esmagadoramente", "esmagador",
                 "deslumbrante", "formidavel","tao"]

# categorias
NORMAL = 0
BAD = 1 
GOOD = 2 
INTENSE = 3 


def prep(txt:str) -> list:
    txt = unicodedata.normalize('NFD', txt)
    txt = re.sub(r'[^\w\s]|[\u0301]','',txt.lower())
    txt = unicodedata.normalize('NFC', txt)
    return [i for i in txt.split(" ") if i not in STOP_WORDS]


def tokeniza_phrase(text:str) -> list:
    text = prep(text)
    tokens = []
    for i in text:
        if i in GOOD_WORDS:
            tokens.append((i,GOOD))
        elif i in INTENSE_WORDS:
            tokens.append((i,INTENSE))
        elif i in BAD_WORDS:
            tokens.append((i,BAD))
        else:
            tokens.append((i,NORMAL))
    return tokens 

def get_feling(text:str) -> int:
    tokens = tokeniza_phrase(text)
    tokens = [tk for word, tk in tokens]

    qtd_good = tokens.count(GOOD)
    qtd_bad = tokens.count(BAD)

    while INTENSE in tokens:
        index = tokens.index(INTENSE)
        if tokens[index+1] in GOOD_WORDS:
            qtd_good+=1
        elif tokens[index+1] in BAD_WORDS:
            qtd_bad+=1
        tokens.pop(index)

    if qtd_good == qtd_bad:
        return 0  
    elif qtd_good > qtd_bad:
        return 1
    elif qtd_bad > qtd_good:
        return -1


def get_felings(text:list) -> list:
    return [(prep(txt), get_feling(txt)) for txt in text]

