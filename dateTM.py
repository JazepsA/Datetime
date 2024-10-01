import datetime


#Iegūt pašreizējo datumu un laiku
current_datetime=datetime.datetime.now()
print("Pašreizējais datums un laiks: ",current_datetime)

#Izgūst tikai pašreizējo datumu
current_date= current_datetime.date()
print("Pašreizējais datums: ",current_date)

#Izgūst tikai pašreizējo laiku bez milisekundēm
current_time= current_datetime.time()
print("Pašreizējais laiks: ",current_time.replace(microsecond=0))

#Izveido konkrētu datumu un laiku
custom_datetime= datetime.datetime(2024,9,30,15,45,30)
print("Konkrēts datums un laiks: ",custom_datetime)

#Aprēķina dienu starpību starp diviem datumiem

start_date=datetime.date(2024,8,1)
end_date=datetime.date(2025,7,12)
date_difference =end_date - start_date
print("Dienu starpība starp datumiem: ",date_difference.days)
