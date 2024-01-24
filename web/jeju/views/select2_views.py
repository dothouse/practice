from flask import Blueprint, render_template, request, url_for, session, g, flash, redirect

from werkzeug.utils import redirect

from jeju import db

from jeju.models import selectData, Pension, Mart, Police, Parm, Hospital, Bank, Tour, Food, Gift

bp = Blueprint('select2', __name__, url_prefix='/select')


@bp.route('/select2', methods=('GET', 'POST'))
def show_select2():
    # 카테고리 옵션

    try:
        request.form['spot2']
    except:
        return redirect('/select1')

    # 유형1
    if request.form['month'] == 'monthType1':
        monthType_str = '일반'
        monthType = 1
    elif request.form['month'] == 'monthType2':
        monthType_str = '아이 동반'
        monthType = 2
    elif request.form['month'] == 'monthType3':
        monthType_str = '체험'
        monthType = 3
    elif request.form['month'] == 'monthType4':
        monthType_str = '맛집'
        monthType = 4
    elif request.form['month'] == 'monthType5':
        monthType_str = '자연 탐방'
        monthType = 5

    # 관광지
    if request.form['spot1'] == 'spot1Type1':
        spot1Type_str = '경관, 포토, 스팟'
        spot1Type = 1
    elif request.form['spot1'] == 'spot1Type2':
        spot1Type_str = '반려동물, 동반, 애견'
        spot1Type = 2
    elif request.form['spot1'] == 'spot1Type3':
        spot1Type_str = '체험, 레저'
        spot1Type = 3
    elif request.form['spot1'] == 'spot1Type4':
        spot1Type_str = '도보, 등산, 오름, 숲길'
        spot1Type = 4
    elif request.form['spot1'] == 'spot1Type5':
        spot1Type_str = '테마, 실내, 박물관, 미술, 유적지, 역사'
        spot1Type = 5
    elif request.form['spot1'] == '':
        return redirect(url_for('select1.open_select1'))

    # 여행지 소분류
    if request.form['spot2'] == '해변/드라이브':
        spot2Type_str = request.form['spot2']
        spot2Type = 11
    elif request.form['spot2'] == '힐링/휴식':
        spot2Type_str = request.form['spot2']
        spot2Type = 12
    elif request.form['spot2'] == '반려동물':
        spot2Type_str = request.form['spot2']
        spot2Type = 20
    elif request.form['spot2'] == '레저/수상/해수욕장':
        spot2Type_str = request.form['spot2']
        spot2Type = 31
    elif request.form['spot2'] == '승마/이색/마을/어린이':
        spot2Type_str = request.form['spot2']
        spot2Type = 32
    elif request.form['spot2'] == '하이킹':
        spot2Type_str = request.form['spot2']
        spot2Type = 40
    elif request.form['spot2'] == '유적/역사':
        spot2Type_str = request.form['spot2']
        spot2Type = 51
    elif request.form['spot2'] == '실내/미술/박물관/테마':
        spot2Type_str = request.form['spot2']
        spot2Type = 52
    elif request.form['spot2'] == '':
        return redirect(url_for('select1.open_select1'))

    # 식당
    if request.form['food'] == 'foodType1':
        foodType_str = '아시아음식(일식/중식/아시아)'
        foodType = 1
    elif request.form['food'] == 'foodType2':
        foodType_str = '양식'
        foodType = 2
    elif request.form['food'] == 'foodType3':
        foodType_str = '술집'
        foodType = 3
    elif request.form['food'] == 'foodType4':
        foodType_str = '간식'
        foodType = 4
    elif request.form['food'] == 'foodType5':
        foodType_str = '패스트푸드'
        foodType = 5
    elif request.form['food'] == 'foodType6':
        foodType_str = '한식'
        foodType = 6

    if request.form['pet'] == 'petType1':
        petType_str = '미동반'
        petType = 0
    elif request.form['pet'] == 'petType2':
        petType_str = '동반'
        petType = 1

    # 숙소 추가 옵션
    pension_opt_list = ['pool', 'garden', 'sea', 'nocost', 'bus']
    for pension_opt in pension_opt_list:
        try:
            request.form[pension_opt]
            globals()[str(pension_opt)] = 1
            globals()[str(pension_opt) + '_str'] = '선택'
        except:
            globals()[str(pension_opt)] = 0
            globals()[str(pension_opt) + '_str'] = '미선택'

    # 주변 추가 옵션
    add_opt_list = ['police', 'hospital', 'bank', 'mart', 'gift']
    for add_opt in add_opt_list:
        try:
            request.form[add_opt]
            globals()[str(add_opt)] = 1
            globals()[str(add_opt) + '_str'] = '선택'
        except:
            globals()[str(add_opt)] = 0
            globals()[str(add_opt) + '_str'] = '미선택'

    # data 추가
    new_data = selectData(month=monthType, month_str=monthType_str,
                          spot1=spot1Type, spot1_str=spot1Type_str,
                          spot2=spot2Type, spot2_str=spot2Type_str,
                          food=foodType, food_str=foodType_str,
                          pet=petType, pet_str=petType_str,
                          pool=pool, garden=garden, sea=sea, nocost=nocost, bus=bus,
                          police=police, hospital=hospital, bank=bank, mart=mart, gift=gift)
    db.session.add(new_data)
    db.session.commit()

    select_value = db.session.query(selectData).order_by(selectData.id.desc())[0]

    return render_template("select/select2.html",
                           select_value=select_value)
