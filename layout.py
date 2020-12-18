import PySimpleGUI as sg
import schedule, time, motor
from datetime import datetime as dt


hours = ["06", "08", "10", "12", "14", "16", "18", "20", "21", "23"]
minutes = ["00", "15", "30", "45"]


layout = [[sg.Text("Beidi Motore laufet immer am:", font=("Helvetica 15"))],
          [sg.Combo(values = hours, key = "h24Hours",font=("Helvetica 15")),sg.Combo(values = minutes, key = "h24Minutes",font=("Helvetica 15")), sg.Button("ON",font=("Helvetica 15"), key = "24HON"),sg.Button("OFF",font=("Helvetica 15"), key = "24HOFF"), sg.Text("no nüt festgleit", key = "h24selected",font=("Helvetica 15"))],
          [sg.Text("De wiss Becher istelle", font=("Helvetica 15"))],
          [sg.CalendarButton("Datum uswähle", key = "whiteDate",font=("Helvetica 15"), begin_at_sunday_plus=1,format=('%d.%m.%Y')),sg.Combo(values = hours, key = "whiteHours",font=("Helvetica 15")),sg.Combo(values = minutes, key = "whiteMinutes",font=("Helvetica 15")), sg.Button("festlegge",font=("Helvetica 15"), key = "setWhite"),sg.Text("Ziit", key = "whiteTimeSelected",font=("Helvetica 15"),size = (5,1)),sg.Text("Datum", key = "whiteDateSelected", enable_events = True,font=("Helvetica 15"),size = (25,1))],
          [sg.Text("De grüen Becher istelle", font=("Helvetica 15"))],
          [sg.CalendarButton("Datum uswähle", key = "greenDate",font=("Helvetica 15"), begin_at_sunday_plus=1,format=('%d.%m.%Y')),sg.Combo(values = hours, key = "greenHours",font=("Helvetica 15")),sg.Combo(values = minutes, key = "greenMinutes",font=("Helvetica 15")), sg.Button("festlegge",font=("Helvetica 15"), key = "setGreen"),sg.Text("Ziit", key = "greenTimeSelected",font=("Helvetica 15"),size = (5,1)),sg.Text("Datum", key = "greenDateSelected",font=("Helvetica 15"),size = (25,1))],
          [sg.Button("Jetzt de wiss Becher dreihe", font=("Helvetica 15"),key = "whiteNow"), sg.Button("Jetzt de grüen Becher dreihe", font=("Helvetica 15"),key = "greenNow")],
          [sg.Text("letschtmol gfüeteret: ",font=("Helvetica 15")),sg.Text("",font=("Helvetica 15"),key = "lastfed", size = (25,1))]]





window = sg.Window("Crowlomat", layout, size = (600,1000))


#set up pins for motors
white = motor.motor(11,12,13,15)
green = motor.motor(7,16,18,22)

def runEvery24Hours():
    white.turn()
    time.sleep(5)
    green.turn()
    window["lastfed"].update(dt.now())
    

def turnOnce(motor, checkDate):
    motor.turnOnDate(checkDate)
    window["lastfed"].update(dt.now().strftime("%d.%m.%Y - %H:%M"))

while True:
    schedule.run_pending()
    
    # get information form UI
    event, values = window.read(timeout=100)
    
    #setup
    
    
    
    #stop event loop if window is closed
    if event  == sg.WIN_CLOSED:
        break
    #set time for 24 hour mode
    if event == "24HON":
        timeH24set = (values["h24Hours"] + ":" + values["h24Minutes"])
        window["h24selected"].update(timeH24set)
        schedule.every().day.at(timeH24set).do(runEvery24Hours).tag("24h")
    #turn of 24 hour mode    
    if event == "24HOFF":
        window["h24selected"].update("nöd feschtgleit")
        schedule.clear("24h")
    #set date and time for white cup
    if event == "setWhite":
        timeSet = values["whiteHours"] + ":" + values["whiteMinutes"]
        dateSet = window["whiteDateSelected"].Get()
        window["whiteTimeSelected"].update(values["whiteHours"] + ":" + values["whiteMinutes"])
        schedule.every().day.at(timeSet).do(turnOnce,motor = white, checkDate = dateSet)  
    #set date and time for green cup    
    if event == "setGreen":
        window["greenTimeSelected"].update(values["greenHours"] + ":" + values["greenMinutes"])
        timeSet = values["greenHours"] + ":" + values["greenMinutes"]
        dateSet = window["greenDateSelected"].Get()
        
        schedule.every().day.at(timeSet).do(turnOnce,motor = green, checkDate = dateSet)
    #turn white cup now    
    if event == "whiteNow":
        white.turn()
        window["lastfed"].update(dt.now().strftime("%d.%m.%Y - %H:%M"))

    #turn green cup now
    if event == "greenNow":
        green.turn()
        window["lastfed"].update(dt.now().strftime("%d.%m.%Y - %H:%M"))
        
        
        
        
        
