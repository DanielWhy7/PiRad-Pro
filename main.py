from random import randint
# Current version
VERSION='1.0.0'

running=True
lrunning=True

m_procedural=['p','proced','procedural']
m_random=['r','ran','rand','random','rng']
m_reverse=['e','rev','reverse']
m_remember=['qr','remem','remember']

m_sin=['sin','synapse','s']
m_cos=['cos','c']
m_tan=['tan','tg','t']
m_ctg=['ctan','ctg']

m_menu=['m','menu']
m_true=['t','true','1','y','yes','yeah']
m_exit=['exit','break','ctrl+c','escape','ctrlc','c','q','quit']

dline='_______________________________'

#TODO: mistake=0

# Data
deg=[0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360]
a=['0','π/6','π/4','π/3','π/2','2π/3','3π/4','5π/6','π','7π/6','5π/4','4π/3','3π/2','5π/3','7π/4','11π/6','2π']
sin=['0','1/2','√2/2','√3/2','1','√3/2','√2/2','1/2','0','-1/2','-√2/2','-√3/2','-1','-√3/2','-√2/2','-1/2','0']
cos=['1','√3/2','√2/2','1/2','0','-1/2','-√2/2','-√3/2','-1','-√3/2','-√2/2','-1/2','0','1/2','√2/2','√3/2','1']
tan=['0','√3/3','1','√3','','-√3','-1','-√3/3','0','√3/3','1','√3','','-√3','-1','-√3/3','0']
ctg=['','√3','1','√3/3','0','-√3/3','-1','-√3','','√3','1','√3/3','0','-√3/3','-1','-√3','']

def chin(s, array):
    return s in array

def echeck(text):
    if chin(text,m_exit):exit()
    if chin(text,m_menu):global lrunning;lrunning=False
    return text

print(f'\nπRad-Pro | Version: {VERSION}\n{dline}')

while running:
    mode=echeck(input('\nProcedural | Random | Reverse | Remember\nMode: ')).lower()

    func=echeck(input('\nSIN | COS | TAN | CTG\nFunc: ')).lower()
    sfunc='sin'
    if chin(func,m_cos):
        func=cos
        sfunc='cos'
    elif chin(func,m_tan):
        func=tan
        sfunc='tan'
    elif chin(func,m_ctg):
        func=ctg
        sfunc='ctg'
    else:
        func=sin
    print(dline+'\n')

    lrunning=True

    if chin(mode,m_remember):
        for i in range(17):
            print(sfunc+'('+str(deg[i])+'°): '+func[i])
    elif chin(mode,m_random):
        while lrunning:
            if not lrunning:break
            i=randint(0,17)
            ans=echeck(input(sfunc+'('+str(deg[i])+'°): '))

            if ans.replace('s','√')==func[i]:
                print('Right.')
            else:
                print('Wrong.Correct is '+func[i]+'.')
            print(dline)
    elif chin(mode,m_reverse):
        while lrunning:
            for i in range(16,-1,-1):
                if not lrunning:break
                ans=echeck(input('sin('+str(deg[i])+'°): '))
                if ans.replace('s','√')==func[i]:
                    print('Right.')
                else:
                    print('Wrong.Correct is '+func[i]+'.')
                print(dline)
    else:
        while lrunning:
            for i in range(17):
                if not lrunning:break
                ans=echeck(input('sin('+str(deg[i])+'°): '))
                if ans.replace('s','√')==func[i]:
                    print('Right.')
                else:
                    print('Wrong.Correct is '+func[i]+'.')
                print(dline)
