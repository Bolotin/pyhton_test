def polisys(user_group, device_location, device_type, device_vendor):
   
    #Правила для операторов ТБ (инженеры ТЗС и первая линия ЦУС)
    if device_type == 'VSP' and user_group == 'opeator_west' and device_location == 'west':
        return('Admin')
    elif device_type == 'VSP' and user_group == 'opeator_center' and device_location == 'center':
        return('Admin')
    elif device_type == 'VSP' and user_group == 'opeator_east' and device_location == 'east':
        return('Admin')
    elif device_type == 'TB' and user_group == 'opeator_west' and device_location == 'west':
        return('Operator')
    elif device_type == 'TB' and user_group == 'opeator_center' and device_location == 'center':
        return('Operator')
    elif device_type == 'TB' and user_group == 'opeator_east' and device_location == 'east':
        return('Operator')
    
    # Правила для администраторво ТБ(инженеры ТЗС на период выполнения работ)
    elif device_type == ('VSP' or 'TB') and user_group == 'admin_west' and device_location == 'west':
        return('Admin')
    elif device_type == ('VSP' or 'TB') and user_group == 'admin_center' and device_location == 'center':
        return('Admin')
    elif device_type == ('VSP' or 'TB') and user_group == 'admin_east' and device_location == 'east':
        return('Admin')            
    
    #Правила для инженеров второй линии поддержки ЦУС
    elif device_type == ('VSP' or 'TB' or 'BACKBONE') and user_group == 'second_line' and device_type == 'Juniper':
        return('Admin(2)')  #Специальный профиль с аттрибутами для Juniper
    elif device_type == ('VSP' or 'TB' or 'BACKBONE') and user_group == 'second_line' and not device_type  == 'Juniper':
        return('Admin')  #Общий профиль для Cisco, Huawei и остальных вендоров
    elif device_type == 'CA' and user_group == 'second_line' and device_type  == 'Juniper':
        return('Operator(2)')  #Специальный профиль с аттрибутами для Juniper
    elif device_type == 'CA' and user_group == 'second_line' and not device_type  == 'Juniper':
        return('Operator')  #Общий профиль для Cisco, Huawei и остальных вендоров
  
    #Правила для инженеров ЦА
    elif user_group == 'operator_CA' and device_type  == 'Juniper':
        return('Operator(2)')  #Специальный профиль с аттрибутами для Juniper
    elif user_group == 'operator_CA' and not device_type  == 'Juniper':
        return('Operator')  #Общий профиль для Cisco, Huawei и остальных вендоров
    elif user_group == 'admin_CA' and device_type  == 'Juniper':
        return('Admin(2)')  #Специальный профиль с аттрибутами для Juniper
    elif user_group == 'admin_CA' and not device_type  == 'Juniper':
        return('Admin')  #Общий профиль для Cisco, Huawei и остальных вендоров  
    else:
        return('Deny') 
 

profile = polisys('opeator_west','west','VSP','Juniper')
print(profile)
