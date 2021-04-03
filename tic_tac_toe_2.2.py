import sys
import random
import time
global keys
keys={'7':' ','8':' ','9':' ',
      '4':' ','5':' ','6':' ',
      '1':' ','2':' ','3':' ',
      }
class Computer:#电脑出棋
    def __init__(self,action):
        self.action='O'
        return None
    
    def last(self,cp,remain):#优先考虑能不能赢
        if '7' in cp and '8' in cp and '9' in remain:
            self.position='9'
        elif '7' in cp and '8' in remain and '9' in cp:
            self.position='8'
        elif '7' in remain and '8' in cp and '9' in cp:
            self.position='7'
        elif '4' in cp and '5' in cp and '6' in remain:
            self.position='6'
        elif '4' in cp and '5' in remain and '6' in cp:
            self.position='5'
        elif '4' in remain and '5' in cp and '6' in cp:
            self.position='4'
        elif '1' in cp and '2' in cp and '3' in remain:
            self.position='3'
        elif '1' in cp and '2' in remain and '3' in cp:
            self.position='2'
        elif '1' in remain and '2' in cp and '3' in cp:
            self.position='1'
        elif '1' in cp and '4' in cp and '7' in remain:
            self.position='7'
        elif '1' in cp and '4' in remain and '7' in cp:
            self.position='4'
        elif '1' in remain and '4' in cp and '7' in cp:
            self.position='1'
        elif '2' in cp and '5' in cp and '8' in remain:
            self.position='8'
        elif '2' in cp and '5' in remain and '8' in cp:
            self.position='5'
        elif '2' in remain and '5' in cp and '8' in cp:
            self.position='2'
        elif '3' in cp and '6' in cp and '9' in remain:
            self.position='9'
        elif '3' in cp and '6' in remain and '9' in cp:
            self.position='6'
        elif '3' in remain and '6' in cp and '9' in cp:
            self.position='3'
        elif '1' in cp and '5' in cp and '9' in remain:
            self.position='9'
        elif '1' in cp and '5' in remain and '9' in cp:
            self.position='5'
        elif '1' in remain and '5' in cp and '9' in cp:
            self.position='1'
        elif '3' in cp and '5' in cp and '7' in remain:
            self.position='7'
        elif '3' in cp and '5' in remain and '7' in cp:
            self.position='5'
        elif '3' in remain and '5' in cp and '7' in cp:
            self.position='3'
        else:
            self.position='.'

    def defence(self,hp,cp,remain):#防御
        if '7' in hp and '8' in hp and '9' in remain:
            self.position='9'
        elif '7' in hp and '8' in remain and '9' in hp:
            self.position='8'
        elif '7' in remain and '8' in hp and '9' in hp:
            self.position='7'
        elif '4' in hp and '5' in hp and '6' in remain:
            self.position='6'
        elif '4' in hp and '5' in remain and '6' in hp:
            self.position='5'
        elif '4' in remain and '5' in hp and '6' in hp:
            self.position='4'
        elif '1' in hp and '2' in hp and '3' in remain:
            self.position='3'
        elif '1' in hp and '2' in remain and '3' in hp:
            self.position='2'
        elif '1' in remain and '2' in hp and '3' in hp:
            self.position='1'
        elif '1' in hp and '4' in hp and '7' in remain:
            self.position='7'
        elif '1' in hp and '4' in remain and '7' in hp:
            self.position='4'
        elif '1' in remain and '4' in hp and '7' in hp:
            self.position='1'
        elif '2' in hp and '5' in hp and '8' in remain:
            self.position='8'
        elif '2' in hp and '5' in remain and '8' in hp:
            self.position='5'
        elif '2' in remain and '5' in hp and '8' in hp:
            self.position='2'
        elif '3' in hp and '6' in hp and '9' in remain:
            self.position='9'
        elif '3' in hp and '6' in remain and '9' in hp:
            self.position='6'
        elif '3' in remain and '6' in hp and '9' in hp:
            self.position='3'
        elif '1' in hp and '5' in hp and '9' in remain:
            self.position='9'
        elif '1' in hp and '5' in remain and '9' in hp:
            self.position='5'
        elif '1' in remain and '5' in hp and '9' in hp:
            self.position='1'
        elif '3' in hp and '5' in hp and '7' in remain:
            self.position='7'
        elif '3' in hp and '5' in remain and '7' in hp:
            self.position='5'
        elif '3' in remain and '5' in hp and '7' in hp:
            self.position='3'
        else:
            self.position='0'
    
    def auto(self,cp,remain,occupy):#自主就近出棋
        while True:#无需防御，自行出棋
            if len(remain)==1:#最后一格无法用随机数
                self.position=remain[0]
                break
            
            possibility=[]
            i=random.randint(0,len(cp)-1)
            cp_1=cp[i]
            if cp_1=='1':
                possibility.append(str(int(cp_1)+1))
                possibility.append(str(int(cp_1)+3))
            elif cp_1=='2':
                possibility.append(str(int(cp_1)+1))
                possibility.append(str(int(cp_1)+3))
                possibility.append(str(int(cp_1)-1))
            elif cp_1=='3':
                possibility.append(str(int(cp_1)+3))
                possibility.append(str(int(cp_1)-1))
            elif cp_1=='4':
                possibility.append(str(int(cp_1)+1))
                possibility.append(str(int(cp_1)+3))
                possibility.append(str(int(cp_1)-3))
            elif cp_1=='5':
                possibility.append(str(int(cp_1)+1))
                possibility.append(str(int(cp_1)+3))
                possibility.append(str(int(cp_1)-1))
                possibility.append(str(int(cp_1)-3))
            elif cp_1=='6':
                possibility.append(str(int(cp_1)-1))
                possibility.append(str(int(cp_1)+3))
                possibility.append(str(int(cp_1)-3))
            elif cp_1=='7':
                possibility.append(str(int(cp_1)+1))
                possibility.append(str(int(cp_1)-3))
            elif cp_1=='8':
                possibility.append(str(int(cp_1)+1))
                possibility.append(str(int(cp_1)-1))
                possibility.append(str(int(cp_1)-3))
            elif cp_1=='9':
                possibility.append(str(int(cp_1)-1))
                possibility.append(str(int(cp_1)-3))
            
            for i in occupy:#把possibility变为can
                while i in possibility:
                    possibility.remove(i)
            if possibility==[]:
                continue
            else:
                i=random.randint(0,len(possibility)-1)
                self.position=possibility[i]
                break
    
    def c_position(self,position):
        cp=[]
        hp=[]
        for k in keys.keys():#获取各个位置状态
            if keys[k]=='O':
                cp.append(str(k))
            elif keys[k]=='X':
                hp.append(str(k))
        
        entire=['1','2','3','4','5','6','7','8','9']
        remain=['1','2','3','4','5','6','7','8','9']
        
        for c in cp:
            if c in remain:
                remain.remove(c)
        for h in hp:
            if h in remain:
                remain.remove(h)
        occupy=[i for i in entire if i not in set(remain)]
        
        if len(remain)==9 or len(cp)==0:#未完成一轮，随机出棋
            while True:
                n=random.randint(1,9)
                if str(n) in remain:
                    break
            self.position=str(n)
        else:
            self.last(cp,remain)
            if self.position=='.':
                self.defence(hp,cp,remain)
                if self.position=='0':
                    self.auto(cp, remain, occupy)
                        
        return self.position
    
    def demon(self,position):
        cp=[]
        hp=[]
        for k in keys.keys():#获取各个位置状态
            if keys[k]=='O':
                cp.append(str(k))
            elif keys[k]=='X':
                hp.append(str(k))
        
        entire=['1','2','3','4','5','6','7','8','9']
        remain=['1','2','3','4','5','6','7','8','9']
        
        for c in cp:
            if c in remain:
                remain.remove(c)
        for h in hp:
            if h in remain:
                remain.remove(h)
        occupy=[i for i in entire if i not in set(remain)]
        
        order=0
        if len(remain)==9:#电脑先手
            order=1
            a=random.randint(0,7)
            if a>=4:#五成概率先手下中间
                self.position='5'
            else:#五成概率下四个角
                if a==0:
                    self.position='1'
                elif a==1:
                    self.position='3'
                elif a==2:
                    self.position='7'
                elif a==3:
                    self.position='9'
        elif len(cp)==0:#人类先手
            order=2
            a=random.randint(0,3)
            if occupy==['5']:
                if a==0:
                    self.position='1'
                elif a==1:
                    self.position='3'
                elif a==2:
                    self.position='7'
                elif a==3:
                    self.position='9'
            else:
                self.position='5'
        if len(cp)>=len(hp):
            order=1
        else:
            order=2

        if len(remain)<9 and len(cp)!=0 and len(hp)!=0:
            self.last(cp,remain)#优先考虑能不能赢
            if self.position=='.':
                #电脑先手
                if order==1 and '5'in cp and len(cp)==1:#O2,O1在5
                    i=random.randint(1,2)
                    if '8'in hp:
                        if i==1:
                            self.position='3'
                        else:
                            self.position='1'
                    elif '2'in hp:
                        if i==1:
                            self.position='7'
                        else:
                            self.position='9'
                    elif '4'in hp:
                        if i==1:
                            self.position='3'
                        else:
                            self.position='9'
                    elif '6'in hp:
                        if i==1:
                            self.position='7'
                        else:
                            self.position='1'
                    elif '1'in hp:
                        self.position='9'
                    elif '3'in hp:
                        self.position='7'
                    elif '9'in hp:
                        self.position='1'
                    elif '7'in hp:
                        self.position='3'
                elif order==1 and '1'in cp and len(cp)==1:#O2，O1在角
                    if '3'in hp or '8'in hp:
                        self.position='7'
                    elif '7'in hp or '6'in hp or '9'in hp:
                        self.position='3'
                    elif '5'in hp:
                        self.position='9'
                    elif '2'in hp:
                        self.position='4'
                    elif '4'in hp:
                        self.position='2'
                elif order==1 and '3'in cp and len(cp)==1:
                    if '1'in hp or '8'in hp:
                        self.position='9'
                    elif '9'in hp or '4'in hp or '7'in hp:
                        self.position='1'
                    elif '5'in hp:
                        self.position='7'
                    elif '2'in hp:
                        self.position='6'
                    elif '6'in hp:
                        self.position='2'
                elif order==1 and '7'in cp and len(cp)==1:
                    if '2'in hp or '9'in hp:
                        self.position='1'
                    elif '1'in hp or '6'in hp or '3'in hp:
                        self.position='9'
                    elif '5'in hp:
                        self.position='3'
                    elif '4'in hp:
                        self.position='8'
                    elif '8'in hp:
                        self.position='4'
                elif order==1 and '9'in cp and len(cp)==1:
                    if '2'in hp or '7'in hp:
                        self.position='3'
                    elif '4'in hp or '1'in hp or '3'in hp:
                        self.position='7'
                    elif '5'in hp:
                        self.position='1'
                    elif '6'in hp:
                        self.position='8'
                    elif '8'in hp:
                        self.position='6'
                elif order==1 and len(occupy)>=4:#O2已出，此时需防则防，无需则选择性占角
                    self.defence(hp,cp,remain)
                    if self.position=='0':
                        if '1'in remain:
                            self.position='1'
                        elif '3'in remain:
                            self.position='3'
                        elif '7'in remain:
                            self.position='7'
                        elif '9'in remain:
                            self.position='9'
                        elif '2'in hp and '4'in hp and '1'in remain:
                            self.position='1'
                        elif '2'in hp and '6'in hp and '3'in remain:
                            self.position='3'
                        elif '6'in hp and '8'in hp and '9'in remain:
                            self.position='9'
                        elif '4'in hp and '8'in hp and '7'in remain:
                            self.position='7'
                        else:
                            self.auto(cp,remain,occupy)
                            
                #电脑后手
                if order==2 and len(cp)==1 and len(hp)==2:#出O2
                    self.defence(hp,cp,remain)#先防一下
                    if self.position=='0':#考虑无需防守的特殊情况
                        i=random.randint(1,4)
                        if '1'in occupy and '5'in hp and '9'in occupy:
                            if i<=2:
                                self.position='7'
                            else:
                                self.position='3'
                        elif '3'in occupy and '5'in hp and '7'in occupy:
                            if i<=2:
                                self.position='1'
                            else:
                                self.position='9'
                        elif '1'in occupy and '5'in cp and '9'in occupy:
                            if i==1:
                                self.position='2'
                            elif i==2:
                                self.position='6'
                            elif i==3:
                                self.position='8'
                            elif i==4:
                                self.position='4'
                        elif '3'in occupy and '5'in cp and '7'in occupy:
                            if i==1:
                                self.position='2'
                            elif i==2:
                                self.position='6'
                            elif i==3:
                                self.position='8'
                            elif i==4:
                                self.position='4'
                        elif '2'in hp and '4'in hp:
                            self.position='1'
                        elif '2'in hp and '6'in hp:
                            self.position='3'
                        elif '8'in hp and '4'in hp:
                            self.position='7'
                        elif '8'in hp and '6'in hp:
                            self.position='9'
                        elif '1'in hp and ('6'in hp or '8'in hp):
                            if i==1:
                                self.position='7'
                            elif i==2:
                                self.position='3'
                            else:
                                self.position='9'
                        elif '3'in hp and ('4'in hp or '8'in hp):
                            if i==1:
                                self.position='7'
                            elif i==2:
                                self.position='1'
                            else:
                                self.position='9'
                        elif '9'in hp and ('2'in hp or '4'in hp):
                            if i==1:
                                self.position='7'
                            elif i==2:
                                self.position='3'
                            else:
                                self.position='1'
                        elif '7'in hp and ('6'in hp or '2'in hp):
                            if i==1:
                                self.position='1'
                            elif i==2:
                                self.position='3'
                            else:
                                self.position='9'
                        elif '4'in hp and '3'in hp:
                            if i<=2:
                                self.position='1'
                            else:
                                self.position='2'
                        elif '4'in hp and '9'in hp:
                            if i<=2:
                                self.position='7'
                            else:
                                self.position='8'
                        elif '6'in hp and '1'in hp:
                            if i<=2:
                                self.position='3'
                            else:
                                self.position='2'
                        elif '6'in hp and '7'in hp:
                            if i<=2:
                                self.position='8'
                            else:
                                self.position='9'
                        elif '8'in hp and '1'in hp:
                            if i<=2:
                                self.position='4'
                            else:
                                self.position='7'
                        elif '8'in hp and '3'in hp:
                            if i<=2:
                                self.position='9'
                            else:
                                self.position='6'
                        elif '2'in hp and '7'in hp:
                            if i<=2:
                                self.position='1'
                            else:
                                self.position='4'
                        elif '2'in hp and '9'in hp:
                            if i<=2:
                                self.position='3'
                            else:
                                self.position='6'
                elif order==2 and len(cp)>1 and len(hp)>2:
                    self.defence(hp,cp,remain)
                if self.position=='0':
                    self.auto(cp,remain,occupy)
            
        return self.position
class Human:#人类出棋
    def __init__(self,action):
        self.action='X'
        return None
    
    def h_position(self,position):
        while True:
            cp=[]
            hp=[]
            for k in keys.keys():#获取各个位置状态
                if keys[k]=='O':
                    cp.append(str(k))
                elif keys[k]=='X':
                    hp.append(str(k))
                    
            remain=['1','2','3','4','5','6','7','8','9']
            for c in cp:
                if c in remain:
                    remain.remove(c)
            for h in hp:
                if h in remain:
                    remain.remove(h)
                        
            self.position=str(input('\n请输入位置'))
            if self.position in remain or self.position=='q' or self.position=='Q':
                break
            else:
                print('\t错误输入')
                continue
        return self.position
        return self.position
class Run:#程序运行
    def __init__(self):
        self.human=Human(self)
        self.computer=Computer(self)
    
    def result(self):
        if keys['7']=='O' and keys['8']=='O' and keys['9']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['4']=='O' and keys['5']=='O' and keys['6']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['1']=='O' and keys['2']=='O' and keys['3']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['7']=='O' and keys['4']=='O' and keys['1']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['8']=='O' and keys['5']=='O' and keys['2']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['9']=='O' and keys['6']=='O' and keys['3']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['7']=='O' and keys['5']=='O' and keys['3']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['9']=='O' and keys['5']=='O' and keys['1']=='O':
            print('\n电脑获胜,辣鸡人类')
            self.win=1
        elif keys['7']=='X' and keys['8']=='X' and keys['9']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        elif keys['4']=='X' and keys['5']=='X' and keys['6']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        elif keys['1']=='X' and keys['2']=='X' and keys['3']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        elif keys['7']=='X' and keys['4']=='X' and keys['1']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        elif keys['8']=='X' and keys['5']=='X' and keys['2']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        elif keys['9']=='X' and keys['6']=='X' and keys['3']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        elif keys['7']=='X' and keys['5']=='X' and keys['3']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        elif keys['9']=='X' and keys['5']=='X' and keys['1']=='X':
            print('\n人类获胜,这不有手就行？')
            self.win=1
        else:
            self.win=0
            
        if self.win==1:
            a=input('\t单击ENTER以结束')
            sys.exit()
            
    def human_run(self):
        self.human.h_position(self)
        self.position=str(self.human.position)
        if self.position=='q' or self.position=='Q':
            sys.exit()
        self.action=self.human.action
        keys[self.position]=self.action
        print(f'''\t-------------
                \r\t| {keys['7']} | {keys['8']} | {keys['9']} |
                \r\t-------------
                \r\t| {keys['4']} | {keys['5']} | {keys['6']} |
                \r\t-------------
                \r\t| {keys['1']} | {keys['2']} | {keys['3']} |
                \r\t-------------
                ''')
        print('等待电脑玩家')
        time.sleep(2)
            
    def computer_run(self):
        self.computer.c_position(self)
        self.action=self.computer.action
        self.position=str(self.computer.position)
        keys[self.position]=self.action
        print(f'''\t-------------
                \r\t| {keys['7']} | {keys['8']} | {keys['9']} |
                \r\t-------------
                \r\t| {keys['4']} | {keys['5']} | {keys['6']} |
                \r\t-------------
                \r\t| {keys['1']} | {keys['2']} | {keys['3']} |
                \r\t-------------
                ''')
                
    def demon_run(self):
        self.computer.demon(self)
        self.action=self.computer.action
        self.position=str(self.computer.position)
        keys[self.position]=self.action
        print(f'''\t-------------
                \r\t| {keys['7']} | {keys['8']} | {keys['9']} |
                \r\t-------------
                \r\t| {keys['4']} | {keys['5']} | {keys['6']} |
                \r\t-------------
                \r\t| {keys['1']} | {keys['2']} | {keys['3']} |
                \r\t-------------
                ''')
    
    def first_round(self):
        self.select=input('\n1.normal\t2.demon\n请选择，输入数字：')
        y=[]
        for x in range(100):
            y.append(int(random.randint(1,100))-50)
        z=[i for i in y if i>0]
        self.hc=len(z)
        if self.hc<=50:#随机决定人类先手
            print('\n人类先手')
            print(f'''\t-------------
                \r\t| {keys['7']} | {keys['8']} | {keys['9']} |
                \r\t-------------
                \r\t| {keys['4']} | {keys['5']} | {keys['6']} |
                \r\t-------------
                \r\t| {keys['1']} | {keys['2']} | {keys['3']} |
                \r\t-------------
                ''')
            self.human_run()
        else:
            print('\n电脑先手')
            time.sleep(2)
            if self.select==1 or self.select=='1':
                self.computer_run()
            elif self.select==2 or self.select=='2':
                self.demon_run()
            
    def other_rounds(self):
        if self.hc<=50:
            self.players=[self.computer,self.human]
        else:
            self.players=[self.human,self.computer]
        
        mark='true'
        while mark=='true':
            for player in self.players:
                if player==self.computer:
                    if self.select==1 or self.select=='1':
                        self.computer_run()
                    elif self.select==2 or self.select=='2':
                        self.demon_run()
                elif player==self.human:
                    self.human_run()
                self.result()
                
            value=[]
            for i in keys.values():
                value.append(i)
            if value.count(' ')>0:
                mark='true'
            else:
                mark='false'
        
        if self.win==0:
            print('恭喜你和人工智障打个平手')
            a=input('\t单击ENTER以结束')
            sys.exit()

if __name__=='__main__':
    print('\n小键盘中的1-9按键的实际位置对应棋盘坐标\n\teg:1代表左下角，5代表中间')
    print('\n在任意时刻单击q键可退出游戏')
    while True:
        game=Run()
        game.first_round()
        while True:
            game.other_rounds()