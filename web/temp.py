# def mapping(category, color, icon):
#     globals()[str(category) + '_detail'] = db.session.query(category).all()
#     temp_detail = globals()[str(category) + '_detail']
#
#     for i in range(len(temp_detail)):
#         folium.Marker(
#             location=[temp_detail[i].lat, temp_detail[i].lng],
#             tooltip=temp_detail[i].name,  # 마커에 마우스를 올렸을 때 표시되는 툴팁으로 병원명 표시
#             popup=folium.Popup(temp_detail[i].addr, max_width=200),
#             icon=folium.Icon(color= color, icon= icon)
#         ).add_to(pension_map)
#
# mapping(Hospital, 'red', 'glyphicon-heart-empty')
# mapping(Parm, 'red', 'glyphicon-plus')
# mapping(Mart, 'purple', 'glyphicon-shopping-cart')
# mapping(Bank, 'red', 'glyphicon-usd')
# mapping(Police, 'blue', 'glyphicon-map-marker')

# hospital_distance = []
# for i in range(len(hospital_detail)):
#     start = (hospital_detail[i].lat, hospital_detail[i].lng)
#     name = hospital_detail[i].name
#     addr = hospital_detail[i].addr
#     sun = hospital_detail[i].sun
#     haver = haversine(start, goal)
#     hospital_distance.append([name, haver, addr, sun])
# hospital_distance = pd.DataFrame(hospital_distance)
# hospital_distance.columns = ['name', 'haver', 'addr', 'sun']
# hospital_distance_list = hospital_distance['haver'].sort_values(ascending=True)
#
# near_hospital_distance = hospital_distance_list.head(1).values[0]
# near_hospital = hospital_distance[hospital_distance['haver'] == near_hospital_distance]


def cal_distance(category):
    goal = (pension_lat, pension_lng)
    temp_distance = []
    temp_detail = globals()[str(category) + '_detail']
    for i in range(len(temp_detail)):
        start = (temp_detail[i].lat, temp_detail[i].lng)
        name = temp_detail[i].name
        addr = temp_detail[i].addr
        sun = temp_detail[i].sun
        haver = haversine(start, goal)
        temp_distance.append([name, haver, addr, sun])
    temp_distance = pd.DataFrame(temp_distance)
    temp_distance.columns = ['name', 'haver', 'addr', 'sun']
    temp_distance_list = temp_distance['haver'].sort_values(ascending=True)
    near_temp_distance = temp_distance_list.head(1).values[0]
    globals()['near' + str(category)] = temp_distance[temp_distance['haver'] == near_temp_distance]
