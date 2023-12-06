import math

count = 0
x_sd_break = 3
cleary = ''
    
zoloto_c = 130 
svinec_c = 140
olovo_c = 230
serebro_c = 250
med_c = 400
cink_c = 400
latun_c = 400
jelezo_c = 460
stal_c = 500
chugun_c = 540
grafit_c = 750
steklo_lab_c = 840
kirpich_c = 880
alluminium_c = 920
maslo_podsoln_c = 1700
lyod_c = 2100
kerosine_c = 2100
efir_c = 2350
derevo_dub_c = 2400
spirt_c = 2500
water_c = 4200
vodorod_c = 14.304

a = str(input('Введите тему, которая нужна вам. - '))

if a == 'узнать температуру по абсолютной шкале' or a == 'Узнать температуру по абсолютной шкале' or a == 'УЗНАТЬ ТЕМПЕРАТУРУ ПО АБСОЛЮТНОЙ ШКАЛЕ':
    t = float(input('Введите текущую температуру тела, t.'))
    absolute_t_number = 273

    if t == math.isinf(t):
        x_sd_break -= 3
        exit()
    
    T = t + absolute_t_number
    if t >= 0:
        if t > 4 or t == 0:
            print(f'{t} градусов цельсия равны {T} градусам по абсолютной шкале.')
        elif t <= 4 and t > 1:
            print(f'{t} градуса цельсия равны {T} градусам по абсолютной шкале.') #(2) = градусам, тк > 4 (+273)
        elif t == 1:
            print(f'{t} градус цельсия равен {T} градусам по абсолютной шкале.') #(2) = градусам, тк > 4 (+273)

    if t < 0:
        if t == -1:
            print(f'{t} градус цельсия равен {T} градусам по абсолютной шкале.') #(2) = градусам, тк > 4 (+273)
        elif t == t >= -4 and t > 1 and t < 0:
            print(f'{t} градуса цельсия равны {T} градусам по абсолютной шкале.') #(2) = градусам, тк > 4 (+273)e
        if t < 4:
            print(f'{t} градусов цельсия равны {T} градусам по абсолютной шкале.')

if a == 'Удельная теплоемкость' or a == 'удельная теплоемкость' or a == 'УДЕЛЬНАЯ ТЕПЛОЕМКОСТЬ':
#Q = cm(t2 - t1) ============ Q_ex = zxc * m_Q * zxc ; zxc = (t2 - t1)

    what_to_search_Q = str(input('Какую величину требуется найти? - ')) #Q; m; c; t2; t1;

    if what_to_search_Q == 'Q' or what_to_search_Q == 'Й' or what_to_search_Q == 'q':
        x_sd_break = 1

        q_Q = str(input('Вещество - '))
        m_Q = float(input('Масса = '))
        t2 = float(input('Итоговая температура = '))
        t1 = float(input('Начальная температура = '))
        zxc = t2 - t1 #(t2 - t1) - дельта t

        if q_Q == 'Золото':
            Q_ex = zoloto_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')
            
        if q_Q == 'Свинец':
            Q_ex = svinec_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Олово':
            Q_ex = olovo_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Серебро':
            Q_ex = serebro_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Медь':
            Q_ex = med_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Цинк':
            Q_ex = cink_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')
        
        if q_Q == 'Латунь':
            Q_ex = latun_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Железо':
            Q_ex = jelezo_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')
        
        if q_Q == 'Сталь':
            Q_ex = stal_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')
        
        if q_Q == 'Чугун':
            Q_ex = chugun_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Графит':
            Q_ex = grafit_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Лаболаторное стекло':
            Q_ex = steklo_lab_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Кирпич':
            Q_ex = chugun_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Аллюминий':
            Q_ex = alluminium_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Подсолнечное масло':
            Q_ex = maslo_podsoln_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Лед' or q_Q == 'Лёд':
            Q_ex = chugun_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Керосин':
            Q_ex = kerosine_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')
        
        if q_Q == 'Эфир':
            Q_ex = efir_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Дуб':
            Q_ex = derevo_dub_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Спирт':
            Q_ex = spirt_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')

        if q_Q == 'Вода':
            Q_ex = water_c * m_Q * zxc
            print(f'Удельная теплоемкость равна {Q_ex} джоулям (Дж).')
        
    if what_to_search_Q == 'm' or what_to_search_Q == 'ь' or what_to_search_Q == 'M':
        q_Q = str(input('Вещество - '))
        count += 0.001
        Q_xe = float(input('Количество теплоты (Q) = '))
        count += 0.001
        t2 = float(input('Итоговая температура = '))
        count += 0.001
        t1 = float(input('Начальная температура = '))
        count += 0.001

        zxc = t2 - t1

        if zxc == math.isinf(t2 - t1):
            exit()
        else:
            x_sd_break -= 1
            math.fabs(count) 

        #(Q_xe / zxc) / c_вещества

        if q_Q == 'Золото':
            m = (Q_xe / zxc) / zoloto_c
            print(f'Масса равна {m} килограммов')
            
        if q_Q == 'Свинец':
            m = (Q_xe / zxc) / svinec_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Олово':
            m = (Q_xe / zxc) / olovo_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Серебро':
            m = (Q_xe / zxc) / serebro_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Медь':
            m = (Q_xe / zxc) / med_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Цинк':
            m = (Q_xe / zxc) / cink_c
            print(f'Масса равна {m} килограммов')
        
        if q_Q == 'Латунь':
            m = (Q_xe / zxc) / latun_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Железо':
            m = (Q_xe / zxc) / jelezo_c
            print(f'Масса равна {m} килограммов')
        
        if q_Q == 'Сталь':
            m = (Q_xe / zxc) / stal_c
            print(f'Масса равна {m} килограммов')
        
        if q_Q == 'Чугун':
            m = (Q_xe / zxc) / chugun_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Графит':
            m = (Q_xe / zxc) / grafit_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Лаболаторное стекло':
            m = (Q_xe / zxc) / steklo_lab_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Кирпич':
            m = (Q_xe / zxc) / chugun_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Аллюминий':
            m = (Q_xe / zxc) / alluminium_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Подсолнечное масло':
            m = (Q_xe / zxc) / maslo_podsoln_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Лед' or q_Q == 'Лёд':
            m = (Q_xe / zxc) / chugun_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Керосин':
            m = (Q_xe / zxc) / kerosine_c
            print(f'Масса равна {m} килограммов')
        
        if q_Q == 'Эфир':
            m = (Q_xe / zxc) / efir_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Дуб':
            m = (Q_xe / zxc) / derevo_dub_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Спирт':
            m = (Q_xe / zxc) / spirt_c
            print(f'Масса равна {m} килограммов')

        if q_Q == 'Вода':
            m = (Q_xe / zxc) / water_c
            print(f'Масса равна {m} килограммов')

#bimbimbambambambam
if a == 'удельная теплота сгорания некоторых видов топлива' or a == 'Удельная теплота сгорания некоторых видов топлива':
    q_stage_of_10 = math.pow(10, 7)
    q_stage_of_10 = int(q_stage_of_10)
    porox_q = 0.38 * q_stage_of_10 #1
    drova_syh_q = 1.0 * q_stage_of_10 #2
    torf_q = 1.4 * q_stage_of_10 #3
    antrawzit_q = 3.0 * q_stage_of_10 #4
    kam_ugol_q = 2.7 * q_stage_of_10 #5
    spirt_q0 = 2.7 * q_stage_of_10 #6
    drev_ugol_q = 3.4 * q_stage_of_10 #7
    prirod_gas_q = 4.4 * q_stage_of_10 #8
    neft_q = 4.4 * q_stage_of_10 #9
    benz_q = 4.6 * q_stage_of_10 #10
    kerosine_q0 = 4.6 * q_stage_of_10 #11
    vodorod_q = 12.0 * q_stage_of_10 #12

    what_to_search_Q = str(input('Какую величину требуется найти? - '))
    if what_to_search_Q == 'Q' or what_to_search_Q == 'й' or what_to_search_Q == 'q':
        q_Q = str(input('Вещество - '))
        m_Q = float(input('Масса = '))

        def Q_toplivo_q():
            print(f'Удельная теплота сгорания топлива равна {float(q_sgor * m_Q)} Дж')

        if q_Q == 'Порох' or q_Q == 'порох':
            q_sgor = porox_q
            Q_toplivo_q()

        if q_Q == 'Сухие дрова' or q_Q == 'сухие дрова' or q_Q == 'дрова сухие' or q_Q == 'Дрова сухие':
            q_sgor = drova_syh_q
            Q_toplivo_q()

        if q_Q == 'Торф' or q_Q == 'торф':
            q_sgor = torf_q
            Q_toplivo_q()

        if q_Q == 'Антрацит' or q_Q == 'антрацит':
            q_sgor = antrawzit_q
            Q_toplivo_q()

        if q_Q == 'Каменный уголь' or q_Q == 'каменный уголь' or q_Q == 'Уголь каменный' or q_Q == 'уголь каменный':
            q_sgor = kam_ugol_q
            Q_toplivo_q()

        if q_Q == 'Спирт' or q_Q == 'спирт':
            q_sgor = spirt_c
            Q_toplivo_q()

        if q_Q == 'Древесный уголь' or q_Q == 'древесный уголь' or q_Q == 'Уголь древесный' or q_Q == 'уголь древесный':
            q_sgor = drev_ugol_q
            Q_toplivo_q()

        if q_Q == 'Природный газ' or q_Q == 'природный газ':
            q_sgor = prirod_gas_q
            Q_toplivo_q()

        if q_Q == 'Нефть' or q_Q == 'нефть':
            q_sgor = neft_q
            Q_toplivo_q()

        if q_Q == 'Бензин' or q_Q == 'бензин':
            q_sgor = benz_q
            Q_toplivo_q()

        if q_Q == 'Керосин' or q_Q == 'керосин':
            q_sgor = kerosine_c
            Q_toplivo_q()

        if q_Q == 'Водород' or q_Q == 'водород':
            q_sgor = vodorod_q
            Q_toplivo_q()

    if what_to_search_Q == 'm' or what_to_search_Q == 'M' or what_to_search_Q == 'ь':
        q_Q = str(input('Вещество - '))
        Q_topl = float(input('Удельная теплота сгорания топлива = '))

        def Q_toplivo_m():
            print(f'Macca топлива равна {float(Q_topl / q_sgor)} кг')
        
        if q_Q == 'Порох' or q_Q == 'порох':
            q_sgor = porox_q
            Q_toplivo_m()

        if q_Q == 'Сухие дрова' or q_Q == 'сухие дрова' or q_Q == 'дрова сухие' or q_Q == 'Дрова сухие':
            q_sgor = drova_syh_q
            Q_toplivo_m()

        if q_Q == 'Торф' or q_Q == 'торф':
            q_sgor = torf_q
            Q_toplivo_m()

        if q_Q == 'Антрацит' or q_Q == 'антрацит':
            q_sgor = antrawzit_q
            Q_toplivo_m()

        if q_Q == 'Каменный уголь' or q_Q == 'каменный уголь' or q_Q == 'Уголь каменный' or q_Q == 'уголь каменный':
            q_sgor = kam_ugol_q
            Q_toplivo_m()

        if q_Q == 'Спирт' or q_Q == 'спирт':
            q_sgor = spirt_c
            Q_toplivo_m()

        if q_Q == 'Древесный уголь' or q_Q == 'древесный уголь' or q_Q == 'Уголь древесный' or q_Q == 'уголь древесный':
            q_sgor = drev_ugol_q
            Q_toplivo_m()

        if q_Q == 'Природный газ' or q_Q == 'природный газ':
            q_sgor = prirod_gas_q
            Q_toplivo_m()

        if q_Q == 'Нефть' or q_Q == 'нефть':
            q_sgor = neft_q
            Q_toplivo_m()

        if q_Q == 'Бензин' or q_Q == 'бензин':
            q_sgor = benz_q
            Q_toplivo_m()

        if q_Q == 'Керосин' or q_Q == 'керосин':
            q_sgor = kerosine_c
            Q_toplivo_m()

        if q_Q == 'Водород' or q_Q == 'водород':
            q_sgor = vodorod_q
            Q_toplivo_m()

if a == 'Удельная теплота плавления некоторых веществ' or a == 'удельная теплота плавления некоторых веществ':
    q_stage_of_10 = math.pow(10, 5)
    alluminium_lambda = 3.9 * q_stage_of_10
    led_lambda = 3.4 * q_stage_of_10
    jelezo_lambda = 2.7 * q_stage_of_10
    med_lambda = 2.1 * q_stage_of_10
    zink_lambda = 1.12 * q_stage_of_10
    spirt_lambda = 3.9 * q_stage_of_10
    serebro_lambda = 0.87 * q_stage_of_10
    stal_lambda = 0.84 * q_stage_of_10
    zoloto_lambda = 0.67 * q_stage_of_10
    vodorod_lambda, olovo_lambda = 0.59 * q_stage_of_10, 0.59 * q_stage_of_10
    svinec_lambda = 0.25 * q_stage_of_10
    kislorod_lambda = 0.14 * q_stage_of_10
    rtut_lambda = 0.12 * q_stage_of_10
    #Qобщ = Q2 + Q1
    #Q(лямбда) = лямбда * m
    #Qобщ = (cm(t2 - t1)) + (лямбда * m)

    #python -mpip install -U pip
    #python -mpip install -U matplotlib

    what_to_search_lambda = str(input('Какую величину требуется найти? - '))
    if what_to_search_lambda == 'Удельная теплота' or what_to_search_lambda == 'удельная теплота':
        vesh_lambda = str(input('Введите вещество '))
        #Q_lambda = lambda abc: L * m
        massa = int(input('Введите массу тела '))
        t1 = int(input('Введите начальную теплоту: '))
        t2 = int(input('Введите конечную теплоту: '))

        def func():
            print(f'Удельная теплота плавления равна {float(Lambda * massa) + float(c * massa * (t2 - t1))} Дж')

        if vesh_lambda == 'Алюминий' or vesh_lambda == 'алюминий':
            Lambda = alluminium_lambda
            c = alluminium_c
            func()
        if vesh_lambda == 'Лед' or vesh_lambda == 'Лёд' or vesh_lambda == 'лед' or 'лёд':
            Lambda = led_lambda
            c = lyod_c
            func()
        if vesh_lambda == 'Железо' or vesh_lambda == 'железо':
            Lambda = jelezo_lambda
            c = jelezo_c
            func()
        if vesh_lambda == 'медь' or vesh_lambda == 'Медь':
            Lambda = med_lambda
            c = med_c
            func()
        if vesh_lambda == 'Цинк' or vesh_lambda == 'цинк':
            Lambda = zink_lambda
            c = cink_c
            func()
        if vesh_lambda == 'Спирт' or vesh_lambda == 'спирт':
            Lambda = spirt_lambda
            c = spirt_c
            func()
        if vesh_lambda == 'Серебро' or vesh_lambda == 'серебро':
            Lambda = serebro_lambda
            c = serebro_c
            func()
        if vesh_lambda == 'Сталь' or vesh_lambda == 'сталь':
            Lambda = stal_lambda
            c = stal_c
            func()
        if vesh_lambda == 'Золото' or vesh_lambda == 'золото':
            Lambda = zoloto_lambda
            c = stal_c
            func()
        if vesh_lambda == 'Водород' or vesh_lambda == 'водород':
            Lambda = vodorod_lambda
            c = round(vodorod_c, 2)
            func()
        if vesh_lambda == 'Олово' or vesh_lambda == 'олово':
            Lambda = olovo_lambda
            func()
        if vesh_lambda == 'Свинец' or vesh_lambda == 'свинец':
            Lambda = svinec_lambda
            func()
        if vesh_lambda == 'Кислород' or vesh_lambda == 'кислород':
            Lambda = kislorod_lambda
            func()
        if vesh_lambda == 'Ртуть' or vesh_lambda == 'ртуть':
            Lambda = rtut_lambda
            func()