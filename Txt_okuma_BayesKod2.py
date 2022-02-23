
# -*- coding: utf-8 -*-

#Bu kısımda 1.dosya kodunda Txt dosyasına yazılan maze okunma işlemi yapıldı
#buradan alınan verilere göre bir bayes işlemi uygulanacaktır.
import numpy as np
import emresonkod.py
#------------------ Txt'den Okuma ------------------------- #    
def TxtToMaze():
    
    f = open("maze.txt","r")
    
    txt = f.read()
    txt = txt[1:-1]
    
    while True:
        i = txt.find("[")+1
        s = txt.find("]")
        
        listeX = []
        txtList = txt[i:s]
        for k in txtList:
            if k == "1" or k == "0":
                num = int(k)
                listeX.append(num)
        txt = txt[s+1:]
        satir = np.array([listeX])
        try:
            maze = np.append(maze,satir,axis = 0)
        except:
            maze = np.array(satir)
        
        if txt == "":
            break
        
    return(maze)
maze = TxtToMaze()
print(maze)
#Bu kısımda Graph adlı bir sözlük oluşturuldu. Buradaki amaç boş olan
#yolların bağlantılı olduğu yolları sözlük şeklinde etiketlemek.
def MakeGraph():
    graph = {}
    x=0
    y=0
    
    for x in range(maze.shape[0]):
        for y in range(maze.shape[1]):
        
            if maze[x,y] == 0:
                graph[(x,y)] = []
                
                try:
                    if maze[x+1,y]==0:
                        graph[(x,y)].append((x+1,y))
                        
                except:
                    pass
                try:
                    if maze[x,y+1]== 0:
                        graph[(x,y)].append((x,y+1))
                except:
                    pass
                try:
                    if maze[x-1,y]==0:
                        graph[(x,y)].append((x-1,y))
                except:
                    pass
                try:
                    if maze[x,y-1]==0:
                        graph[(x,y)].append((x,y-1))
                except:
                    pass
    
              
    for i in graph:
        graph[i] = set(graph[i]) 
    return(graph)

graph = MakeGraph()
print(MakeGraph())
#---------------------------------------------------------------------#
#Bayes kısmı başlıyor. Bu kısımda aracın bulunduğu konum ve 
#bağlantılı yollara göre olma olasılığı bulunacak ve araç tahmini bir 
#olasılık listesi oluşturacak arac tahmini bir noktası olacak ve buna
#göre oluşturduğu olasılığı bir listeye atacak %50 veya %100 sonuçları 
#bizim için aracın konumunu bulmak için yeterli olacak.
#--------------------------------------------------------------------#
def MakeBayes():
    durum = True
    konum_isimleri =  [] #etiketleme işlemi etiketler bir listeye atıldı.
    
    for i in graph:
        konum_isimleri.append(i)
        
    node = []
    
    for i in graph:
        node.append(len(graph[i]))
        
    #print(node)
    w_pass = []
    for l in range(len(node)):
        w_pass.append(1/len(node))
    while durum:
        
        w = []
        for i in range(len(node)):   
            w.append(0)
        yol = 0
        if emresonkod.sol_sensor() >= 30:  # DEĞİŞECEK!!!!!!!!!!!!!
            yol +=1           # DEĞİŞECEK!!!!!!!!!!!!!
        if emresonkod.on_sensor >= 30 :  # DEĞİŞECEK!!!!!!!!!!!!!
            yol += 1          # DEĞİŞECEK!!!!!!!!!!!!!
        if emresonkod.sag_sensor >= 30:  # DEĞİŞECEK!!!!!!!!!!!!!
            yol += 1          # DEĞİŞECEK!!!!!!!!!!!!!
        if emresonkod.arka_sensor >=30:  # DEĞİŞECEK!!!!!!!!!!!!!
            yol += 1          # DEĞİŞECEK!!!!!!!!!!!!!
            
        
        sayac = 0
        p1=[] # p(a|b)
        
        for t in w_pass:
            if t!=0:
                m = konum_isimleri[sayac] #Bir adim önceki olabileceğim konum
                for i in graph[m]: #Bir önceki olabileceğim konumun bağlantı noktaları
                    kar = konum_isimleri.index(i)
                    if node[kar] == yol: 
                        hafiza=m
                        p1.append(i)      
            sayac += 1
        print(p1)
        p_ab=[]                
        for u in p1:
            p_ab.append(1/p1.count(u))
        tekrarsiz_p1 = []
        for i in p1:
            if i not in tekrarsiz_p1:
                tekrarsiz_p1.append(i)
        for z in range(len(p1)):
            w[konum_isimleri.index(p1[z])]+=p_ab[z]/len(tekrarsiz_p1)
        for i in range(len(node)):
            w_pass[i]=w[i]
        print(konum_isimleri)
        print(w)   
        if max(w)>0.5:
            start= konum_isimleri[w.index(max(w))]
            durum = False
#Hfizadaki konum ile başlangıç konumu aynı olması gerek.
    #print(start)
    if hafiza[0] == start[0]:
        if hafiza[1] > start[1]:
            yon = "-y"
        if hafiza[1] < start[1]:
            yon = "+y"
    if hafiza[1] == start[1]:
        if hafiza[0] > start[0]:
            yon = "-x"
        if hafiza[0] < start[0]:
            yon = "+x"
    return start, yon
start, yon = MakeBayes()


#dfs ve short_path kısmı başlıyor.Araç deep search yapacağı ve 
#en kısa yolu bulacağı kodlar aşağıda bulunmaktadır.
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(dfs_paths(graph, start, goal))
    except StopIteration:
        return None


goal = (8,8)  #hocaya bağlı olabilir.

cozum= shortest_path(graph, start, goal)        

#Bu kısımdan sonra motorlarla çıktıya gitme kısmı var:#
def MakeYonListesi():
    yon_listesi = []
    
    yon_listesi.append(yon)
    for i in range(len(cozum)-1):
        if cozum[i+1][0]-cozum[i][0] > 0:
            yon_listesi.append("+x")
        elif cozum[i+1][0]-cozum[i][0] < 0:
            yon_listesi.append("-x")
        elif cozum[i+1][1]-cozum[i][1] > 0:
            yon_listesi.append("+y")
        elif cozum[i+1][1]-cozum[i][1] < 0:
            yon_listesi.append("-y")
                   
    
    for j in range(len(yon_listesi)-1):
        if yon_listesi[j] == "+x":
            if yon_listesi[j+1] == "+x":
                print("duz git")
                emresonkod.forward()
                pass
            elif yon_listesi[j+1] == "-x":
                print("arkaya don")
                emresonkod.backward()
                pass
            elif yon_listesi[j+1] == "+y":
                print("sola don")
                emresonkod.left()
                pass
            elif yon_listesi[j+1] == "-y":
                print("saga don")
                emresonkod.right()
                pass
        elif yon_listesi[j] == "-x":
            if yon_listesi[j+1] == "+x":
                print("arkaya don")
                emresonkod.backward()
                pass
            elif yon_listesi[j+1] == "-x":
                print("duz git")
                emresonkod.forward()
                pass
            elif yon_listesi[j+1] == "+y":
                print("saga don")
                emresonkod.right()
                pass
            elif yon_listesi[j+1] == "-y":
                print("sola don")
                emresonkod.left()
                pass 
        elif yon_listesi[j] == "+y":
            if yon_listesi[j+1] == "+x":
                print("saga don")
                emresonkod.right()
                pass
            elif yon_listesi[j+1] == "-x":
                print("sola don")
                emresonkod.left()
                pass
            elif yon_listesi[j+1] == "+y":
                print("duz git")
                emresonkod.forward()
                pass
            elif yon_listesi[j+1] == "-y":
                print("arkaya don")
                emresonkod.backward()
                pass 
        elif yon_listesi[j] == "-y":
            if yon_listesi[j+1] == "+x":
                print("sola don")
                emresonkod.left()
                pass
            elif yon_listesi[j+1] == "-x":
                print("saga don")
                emresonkod.right()
                pass
            elif yon_listesi[j+1] == "+y":
                print("arkaya don")
                emresonkod.backward()
                pass
            elif yon_listesi[j+1] == "-y":
                print("duz git")
                emresonkod.forward()
                pass
    return yon, yon_listesi

print(MakeYonListesi())
        
            