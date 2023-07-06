# Made in Mu
# May take some time to load on first launch
# Best run in command prompt with the packages installed

# Internal Packages
import time
from datetime import datetime
import os
import gc

# Third party Packages
import pytz
import ephem
import wmi
import geocoder
import timezonefinder
from geopy.point import Point
from backports.zoneinfo import ZoneInfo
import tzdata

def clear(): # Checks if Mu is running
    find = wmi.WMI()
    for process in find.Win32_Process():
        if not "pythonw.exe" == process.Name:
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(" \n" * 49)

def underline(text): # Underlines text
    print("\u0332".join(text))

def prompt(): # The exit prompt
    exita = input("Are you sure you want to quit? ")
    if exita == "yes" or exita == "Yes" or exita == "YES" or exita == "y" or exita == "Y":
        try:
            print()
            exit("User quit from menu")
        except SystemExit:
            pass
    elif exita == "no" or exita == "No" or exita == "NO" or exita == "n" or exita == "N":
        menu()
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        prompt()

def srise(): # sun rise
    global mystr
    global psrise
    global nsrise
    my_loc.horizon = '0'
    psrise = str(ephem.to_timezone(my_loc.previous_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "psrise"
    dtime(psrise)
    psrise = ("The Last Sunrise was on: " + psrise + " in " + timezone + " Timezone")
    print(psrise)
    nsrise = str(ephem.to_timezone(my_loc.next_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nsrise"
    dtime(nsrise)
    nsrise = ("The Next Sunrise is on: " + nsrise + " in " + timezone + " Timezone")
    print(nsrise)
    print()
    del mystr
    return

def srisec(): # sun rise civil
    global mystr
    global psrisec
    global nsrisec
    my_loc.horizon = '-6'
    psrisec = str(ephem.to_timezone(my_loc.previous_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "psrisec"
    dtime(psrisec)
    psrisec = ("The Last Civil Sunrise was on: " + psrisec + " in " + timezone + " Timezone")
    print(psrisec)
    nsrisec = str(ephem.to_timezone(my_loc.next_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nsrisec"
    dtime(nsrisec)
    nsrisec = ("The Next Civil Sunrise is on: " + nsrisec + " in " + timezone + " Timezone")
    print(nsrisec)
    print()
    del mystr
    return

def srisen(): # sun rise nutical
    global mystr
    global psrisen
    global nsrisen
    my_loc.horizon = '-12'
    psrisen = str(ephem.to_timezone(my_loc.previous_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "psrisen"
    dtime(psrisen)
    psrisen = ("The Last Nutical Sunrise was on: " + psrisen + " in " + timezone + " Timezone")
    print(psrisen)
    nsrisen = str(ephem.to_timezone(my_loc.next_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nsrisen"
    dtime(nsrisen)
    nsrisen = ("The Next Nutical Sunrise is on: " + nsrisen + " in " + timezone + " Timezone")
    print(nsrisen)
    print()
    del mystr
    return

def srisea(): # sun rise Astronomical
    global mystr
    global psrisea
    global nsrisea
    my_loc.horizon = '-18'
    psrisea = str(ephem.to_timezone(my_loc.previous_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "psrisea"
    dtime(psrisea)
    psrisea = ("The Last Astronomical Sunrise was on: " + psrisea + " in " + timezone + " Timezone")
    print(psrisea)
    nsrisea = str(ephem.to_timezone(my_loc.next_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nsrisea"
    dtime(nsrisea)
    nsrisea = ("The Next Astronomical Sunrise is on: " + nsrisea + " in " + timezone + " Timezone")
    print(nsrisea)
    print()
    del mystr
    return

def sset(): # sun set
    global mystr
    global psset
    global nsset
    my_loc.horizon = '0'
    psset = str(ephem.to_timezone(my_loc.previous_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "psset"
    dtime(psset)
    psset = ("The Last Sunset was on: " + psset + " in " + timezone + " Timezone")
    print(psset)
    nsset = str(ephem.to_timezone(my_loc.next_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nsset"
    dtime(nsset)
    nsset = ("The Next Sunset is on: " + nsset + " in " + timezone + " Timezone")
    print(nsset)
    print()
    del mystr
    return

def ssetc(): # sun set cival
    global mystr
    global pssetc
    global nssetc
    my_loc.horizon = '-6'
    pssetc = str(ephem.to_timezone(my_loc.previous_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "pssetc"
    dtime(pssetc)
    pssetc = ("The Last Civil Sunset was on: " + pssetc + " in " + timezone + " Timezone")
    print(pssetc)
    nssetc = str(ephem.to_timezone(my_loc.next_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nssetc"
    dtime(nssetc)
    nssetc = ("The Next Civil Sunset is on: " + nssetc + " in " + timezone + " Timezone")
    print(nssetc)
    print()
    del mystr
    return

def ssetn(): # sun set nutical
    global mystr
    global pssetn
    global nssetn
    my_loc.horizon = '-12'
    pssetn = str(ephem.to_timezone(my_loc.previous_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "pssetn"
    dtime(pssetn)
    pssetn = ("The Last Nutical Sunset was on: " + pssetn + " in " + timezone + " Timezone")
    print(pssetn)
    nssetn = str(ephem.to_timezone(my_loc.next_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nssetn"
    dtime(nssetn)
    nssetn = ("The Next Nutical Sunset is on: " + nssetn + " in " + timezone + " Timezone")
    print(nssetn)
    print()
    del mystr
    return

def sseta(): # sun set Astronomical
    global mystr
    global psseta
    global nsseta
    my_loc.horizon = '-18'
    psseta = str(ephem.to_timezone(my_loc.previous_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "psseta"
    dtime(psseta)
    psseta = ("The Last Astronomical Sunset was on: " + psseta + " in " + timezone + " Timezone")
    print(psseta)
    nsseta = str(ephem.to_timezone(my_loc.next_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nsseta"
    dtime(nsseta)
    nsseta = ("The Next Astronomical Sunset is on: " + nsseta + " in " + timezone + " Timezone")
    print(nsseta)
    print()
    del mystr
    return

def mphfq(): # First quarter moon
    global pmphfq
    global nmphfq
    global phack
    global mystr
    my_loc.horizon = '0'
    pmphfq = str(ephem.to_timezone(ephem.previous_first_quarter_moon(my_loc.date), tz))
    mystr = "pmphfq"
    dtime(pmphfq)
    pmphfq = ("The Last first quarter moon was on: " + pmphfq + " in " + timezone + " Timezone")
    print(pmphfq)
    nmphfq = str(ephem.to_timezone(ephem.next_first_quarter_moon(my_loc.date), tz))
    mystr = "nmphfq"
    phack = 1
    dtime(nmphfq)
    nmphfq = ("The Next first quarter moon is on: " + nmphfq + " in " + timezone + " Timezone")
    print(nmphfq)
    print()
    del phack
    del mystr
    return

def mphlq(): # last quarter moon
    global pmphlq
    global nmphlq
    global phack
    global mystr
    my_loc.horizon = '0'
    pmphlq = str(ephem.to_timezone(ephem.previous_last_quarter_moon(my_loc.date), tz))
    mystr = "pmphlq"
    dtime(pmphlq)
    pmphlq = ("The Last last quarter moon was on: " + pmphlq + " in " + timezone + " Timezone")
    print(pmphlq)
    nmphlq = str(ephem.to_timezone(ephem.next_last_quarter_moon(my_loc.date), tz))
    mystr = "nmphlq"
    phack = 1
    dtime(nmphlq)
    nmphlq = ("The Next last quarter moon is on: " + nmphlq + " in " + timezone + " Timezone")
    print(nmphlq)
    print()
    del mystr
    del phack
    return

def mphf(): # full moon
    global pmphf
    global nmphf
    global phack
    global mystr
    my_loc.horizon = '0'
    pmphf = str(ephem.to_timezone(ephem.previous_full_moon(my_loc.date), tz))
    mystr = "pmphf"
    dtime(pmphf)
    pmphf = ("The Last full moon was on: " + pmphf + " in " + timezone + " Timezone")
    print(pmphf)
    nmphf = str(ephem.to_timezone(ephem.next_full_moon(my_loc.date), tz))
    mystr = "nmphf"
    phack = 1
    dtime(nmphf)
    nmphf = ("The Next full moon is on: " + nmphf + " in " + timezone + " Timezone")
    print(nmphf)
    print()
    del mystr
    del phack
    return

def mphn(): # new moon
    global pmphn
    global nmphn
    global mystr
    my_loc.horizon = '0'
    pmphn = str(ephem.to_timezone(ephem.previous_new_moon(my_loc.date), tz))
    mystr = "pmphn"
    dtime(pmphn)
    pmphn = ("The Last new moon was on: " + pmphn + " in " + timezone + " Timezone")
    print(pmphn)
    nmphn = str(ephem.to_timezone(ephem.next_new_moon(my_loc.date), tz))
    mystr = "nmphn"
    dtime(nmphn)
    nmphn = ("The Next new moon is on: " + nmphn + " in " + timezone + " Timezone")
    print(nmphn)
    print()
    del mystr
    return

def mst(): #  moonset and rise
    global pmst
    global nmst
    global pmrt
    global nmrt
    global mstph
    global mystr
    my_loc.horizon = '0'
    pmst = str(ephem.to_timezone(my_loc.previous_setting(ephem.Moon(my_loc), use_center=True), tz))
    mystr = "pmst"
    dtime(pmst)
    mystr = "mstph"
    mphase()
    pmst = ("The Last Moonset was on: " + pmst + " and its a " + mstph + " in " + timezone  + " Timezone")
    print(pmst)
    nmst = str(ephem.to_timezone(my_loc.next_setting(ephem.Moon(my_loc), use_center=True), tz))
    mystr = "nmst"
    dtime(nmst)
    nmst = ("The Next Moonset is on: " + nmst + " and its a " + mstph + " in " + timezone  + " Timezone")
    print(nmst)
    print()
    pmrt = str(ephem.to_timezone(my_loc.previous_rising(ephem.Moon(my_loc), use_center=True), tz))
    mystr = "pmrt"
    dtime(pmrt)
    pmrt = ("The Last Moonrise was on: " + pmrt + " and its a " + mstph + " in " + timezone  + " Timezone")
    print(pmrt)
    nmrt = str(ephem.to_timezone(my_loc.next_rising(ephem.Moon(my_loc), use_center=True), tz))
    mystr = "nmrt"
    dtime(nmrt)
    nmrt = ("The Next Moonrise is on: " + nmrt + " and its a " + mstph + " in " + timezone  + " Timezone")
    print(nmrt)
    print()
    del mstph
    del mystr
    return

def merc():  # Mercury
    global mystr
    global pmercr
    global nmercr
    global pmercs
    global nmercs
    my_loc.horizon = '0'
    pmercr = str(ephem.to_timezone(my_loc.previous_rising(ephem.Mercury(my_loc), use_center=True), tz))
    mystr = "pmercr"
    dtime(pmercr)
    pmercr = ("The Last Mercury set was on: " + pmercr + " in " + timezone + " Timezone")
    print(pmercr)
    nmercr = str(ephem.to_timezone(my_loc.next_rising(ephem.Mercury(my_loc), use_center=True), tz))
    mystr = "nmercr"
    dtime(nmercr)
    nmercr = ("The Next Mercury set is on: " + nmercr + " in " + timezone + " Timezone")
    print(nmercr)
    print()
    pmercs = str(ephem.to_timezone(my_loc.previous_setting(ephem.Mercury(my_loc), use_center=True), tz))
    mystr = "pmercs"
    dtime(pmercs)
    pmercs = ("The Last Mercury rise was on: " + pmercs + " in " + timezone + " Timezone")
    print(pmercs)
    nmercs = str(ephem.to_timezone(my_loc.next_setting(ephem.Mercury(my_loc), use_center=True), tz))
    mystr = "nmercs"
    dtime(nmercs)
    nmercs = ("The Next Mercury rise is on: " + nmercs + " in " + timezone + " Timezone")
    print(nmercs)
    print()
    del mystr
    return

def ven(): # Venus
    global mystr
    global pvenr
    global nvenr
    global pvens
    global nvens
    my_loc.horizon = '0'
    pvenr = str(ephem.to_timezone(my_loc.previous_rising(ephem.Venus(my_loc), use_center=True), tz))
    mystr = "pvenr"
    dtime(pvenr)
    pvenr = ("The Last Venus set was on: " + pvenr + " in " + timezone + " Timezone")
    print(pvenr)
    nvenr = str(ephem.to_timezone(my_loc.next_rising(ephem.Venus(my_loc), use_center=True), tz))
    mystr = "nvenr"
    dtime(nvenr)
    nvenr = ("The Next Venus set is on: " + nvenr + " in " + timezone + " Timezone")
    print(nvenr)
    print()
    pvens = str(ephem.to_timezone(my_loc.previous_setting(ephem.Venus(my_loc), use_center=True), tz))
    mystr = "pvens"
    dtime(pvens)
    pvens = ("The Last Venus rise was on: " + pvens + " in " + timezone + " Timezone")
    print(pvens)
    nvens = str(ephem.to_timezone(my_loc.next_setting(ephem.Venus(my_loc), use_center=True), tz))
    mystr = "nvens"
    dtime(nvens)
    nvens = ("The Next Venus rise is on: " + nvens + " in " + timezone + " Timezone")
    print(nvens)
    print()
    del mystr
    return

def mars(): #mars
    global mystr
    global pmarsr
    global nmarsr
    global pmarss
    global nmarss
    my_loc.horizon = '0'
    pmarsr = str(ephem.to_timezone(my_loc.previous_rising(ephem.Mars(my_loc), use_center=True), tz))
    mystr = "pmarsr"
    dtime(pmarsr)
    pmarsr = ("The Last Mars set was on: " + pmarsr + " in " + timezone + " Timezone")
    print(pmarsr)
    nmarsr = str(ephem.to_timezone(my_loc.next_rising(ephem.Mars(my_loc), use_center=True), tz))
    mystr = "nmarsr"
    dtime(nmarsr)
    nmarsr = ("The Next Mars set is on: " + nmarsr + " in " + timezone + " Timezone")
    print(nmarsr)
    print()
    pmarss = str(ephem.to_timezone(my_loc.previous_setting(ephem.Mars(my_loc), use_center=True), tz))
    mystr = "pmarss"
    dtime(pmarss)
    pmarss = ("The Last Mars rise was on: " + pmarss + " in " + timezone + " Timezone")
    print(pmarss)
    nmarss = str(ephem.to_timezone(my_loc.next_setting(ephem.Mars(my_loc), use_center=True), tz))
    mystr = "nmarss"
    dtime(nmarss)
    nmarss = ("The Next Mars rise is on: " + nmarss + " in " + timezone + " Timezone")
    print(nmarss)
    print()
    del mystr
    return

def jup(): # Jupiter
    global mystr
    global pjupr
    global njupr
    global pjups
    global njups
    my_loc.horizon = '0'
    pjupr = str(ephem.to_timezone(my_loc.previous_rising(ephem.Jupiter(my_loc), use_center=True), tz))
    mystr = "pjupr"
    dtime(pjupr)
    pjupr = ("The Last Mars set was on: " + pjupr + " in " + timezone + " Timezone")
    print(pjupr)
    njupr = str(ephem.to_timezone(my_loc.next_rising(ephem.Jupiter(my_loc), use_center=True), tz))
    mystr = "njupr"
    dtime(njupr)
    njupr = ("The Next Mars set is on: " + njupr + " in " + timezone + " Timezone")
    print(njupr)
    print()
    pjups = str(ephem.to_timezone(my_loc.previous_setting(ephem.Jupiter(my_loc), use_center=True), tz))
    mystr = "pjups"
    dtime(pjups)
    pjups = ("The Last Mars rise was on: " + pjups + " in " + timezone + " Timezone")
    print(pjups)
    njups = str(ephem.to_timezone(my_loc.next_setting(ephem.Jupiter(my_loc), use_center=True), tz))
    mystr = "njups"
    dtime(njups)
    njups = ("The Next Mars rise is on: " + njups + " in " + timezone + " Timezone")
    print(njups)
    print()
    del mystr
    return

def sat(): # Saturn
    global mystr
    global psatr
    global nsatr
    global psats
    global nsats
    my_loc.horizon = '0'
    psatr = str(ephem.to_timezone(my_loc.previous_rising(ephem.Saturn(my_loc), use_center=True), tz))
    mystr = "psatr"
    dtime(psatr)
    psatr = ("The Last Mars set was on: " + psatr + " in " + timezone + " Timezone")
    print(psatr)
    nsatr = str(ephem.to_timezone(my_loc.next_rising(ephem.Saturn(my_loc), use_center=True), tz))
    mystr = "nsatr"
    dtime(nsatr)
    nsatr = ("The Next Mars set is on: " + nsatr + " in " + timezone + " Timezone")
    print(nsatr)
    print()
    psats = str(ephem.to_timezone(my_loc.previous_setting(ephem.Saturn(my_loc), use_center=True), tz))
    mystr = "psats"
    dtime(psats)
    psats = ("The Last Mars rise was on: " + psats + " in " + timezone + " Timezone")
    print(psats)
    nsats = str(ephem.to_timezone(my_loc.next_setting(ephem.Saturn(my_loc), use_center=True), tz))
    mystr = "nsats"
    dtime(nsats)
    nsats = ("The Next Mars rise is on: " + nsats + " in " + timezone + " Timezone")
    print(nsats)
    print()
    del mystr
    return

def ura(): # Uranus
    global mystr
    global purar
    global nurar
    global puras
    global nuras
    my_loc.horizon = '0'
    purar = str(ephem.to_timezone(my_loc.previous_rising(ephem.Uranus(my_loc), use_center=True), tz))
    mystr = "purar"
    dtime(purar)
    purar = ("The Last Uranus set was on: " + purar + " in " + timezone + " Timezone")
    print(purar)
    nurar = str(ephem.to_timezone(my_loc.next_rising(ephem.Uranus(my_loc), use_center=True), tz))
    mystr = "nurar"
    dtime(nurar)
    nurar = ("The Next Uranus set is on: " + nurar + " in " + timezone + " Timezone")
    print(nurar)
    print()
    puras = str(ephem.to_timezone(my_loc.previous_setting(ephem.Uranus(my_loc), use_center=True), tz))
    mystr = "puras"
    dtime(puras)
    puras = ("The Last Uranus rise was on: " + puras + " in " + timezone + " Timezone")
    print(puras)
    nuras = str(ephem.to_timezone(my_loc.next_setting(ephem.Uranus(my_loc), use_center=True), tz))
    mystr = "nuras"
    dtime(nuras)
    nuras = ("The Next Uranus rise is on: " + nuras + " in " + timezone + " Timezone")
    print(nuras)
    print()
    del mystr
    return

def nep(): # Neptune
    global mystr
    global pnepr
    global nnepr
    global pneps
    global nneps
    my_loc.horizon = '0'
    pnepr = str(ephem.to_timezone(my_loc.previous_rising(ephem.Neptune(my_loc), use_center=True), tz))
    mystr = "pnepr"
    dtime(pnepr)
    pnepr = ("The Last Neptune set was on: " + pnepr + " in " + timezone + " Timezone")
    print(pnepr)
    nnepr = str(ephem.to_timezone(my_loc.next_rising(ephem.Neptune(my_loc), use_center=True), tz))
    mystr = "nnepr"
    dtime(nnepr)
    nnepr = ("The Next Neptune set is on: " + nnepr + " in " + timezone + " Timezone")
    print(nnepr)
    print()
    pneps = str(ephem.to_timezone(my_loc.previous_setting(ephem.Neptune(my_loc), use_center=True), tz))
    mystr = "pneps"
    dtime(pneps)
    pneps = ("The Last Neptune rise was on: " + pneps + " in " + timezone + " Timezone")
    print(pneps)
    nneps = str(ephem.to_timezone(my_loc.next_setting(ephem.Neptune(my_loc), use_center=True), tz))
    mystr = "nneps"
    dtime(nneps)
    nneps = ("The Next Neptune rise is on: " + nneps + " in " + timezone + " Timezone")
    print(nneps)
    print()
    del mystr
    return

def mphase(): # Moon phase
    moon_my_loc = ephem.Moon(my_loc)
    moon_phase = moon_my_loc.moon_phase
    moon_phase_word = 0
    if moon_phase < .06:
        moon_phase_word = "New Moon"
    elif moon_phase >.06 <= .19:
        moon_phase_word = "Waxing Crescent Moon"
    elif moon_phase >.19 <= .31:
        moon_phase_word = "Third Quarter Moon"
    elif moon_phase >.31 <= .44:
        moon_phase_word = "Waxing Gibbous Moon"
    elif moon_phase >.44 <= .56:
        moon_phase_word = "Full Moon"
    elif moon_phase >.56 <= .69:
        moon_phase_word = "Waning Gibbous Moon"
    elif moon_phase >.69 <= .81:
        moon_phase_word = "First Quarter Moon"
    elif moon_phase >.81 <= .94:
        moon_phase_word = "Waning Crescent Moon"
    elif moon_phase >.94:
        moon_phase_word = "New Moon"
    globals()[mystr] = moon_phase_word

def dtime(n): # converts time to words
    full = str(n[-32]+n[-31]+n[-30]+n[-29]+n[-28]+n[-27]+n[-26]+n[-25]+n[-24]+n[-23]+n[-22]+n[-21]+n[-20]+n[-19]+n[-18]+n[-17])
    day = int(full[-8]+full[-7])
    if day == 1:
        day = str(day)
        day = (day+"st")
    elif day == 2:
        day = str(day)
        day = (day+"nd")
    elif day == 3:
        day = str(day)
        day = (day+"rd")
    elif day == 21:
        day = str(day)
        day = (day+"st")
    elif day == 22:
        day = str(day)
        day = (day+"nd")
    elif day == 23:
        day = str(day)
        day = (day+"rd")
    elif day == 31:
        day = str(day)
        day = (day+"st")
    else:
        day = str(day)
        day = (day+"th")
    month = int(full[-11]+full[-10])
    if month == 1:
        month = str("January")
    elif month == 2:
        month = str("Febuary")
    elif month == 3:
        month = str("March")
    elif month == 4:
        month = str("April")
    elif month == 5:
        month = str("May")
    elif month == 6:
        month = str("June")
    elif month == 7:
        month = str("July")
    elif month == 8:
        month = str("August")
    elif month == 9:
        month = str("September")
    elif month == 10:
        month = str("October")
    elif month == 11:
        month = str("November")
    elif month == 12:
        month = str("December")
    hour = int(full[-5]+full[-4])
    minute = str(full[-2]+full[-1])
    try:
        if phack == 1:
            hour = (hour)
    except NameError:
        pass
        hour = (hour + 1)
    if hour < 12:
        hour = str(hour)
        minute = str(minute+"AM")
    elif hour == 12:
        hour = str(hour)
        minute = str(minute+"PM")
    else:
        hour = str(hour-12)
        minute = str(minute+"PM")
    year = str(full[-16]+full[-15]+full[-14]+full[-13])
    globals()[mystr] = (day+" "+month+" "+year+" at "+hour+":"+minute)

def menu(): # The main menu
    global select
    delete()
    clear()
    select = "0"
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│       Select an option below:       │")
    print("│                                     │")
    print("│  1: Sun             6: Jupiter      │")
    print("│  2: Moon            7: Saturn       │")
    print("│  3: Mercury         8: Uranus       │")
    print("│  4: Venus           9: Neptune      │")
    print("│  5: Mars           10: All          │")
    print("│ 11: Exit                            │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    print()
    select = input("Select an option: ")
    if select == "1" or select == "sun" or select == "Sun" or select == "SUN":
        select = "1"
        twilight()
    elif select == "2" or select == "moon" or select == "Moon" or select == "MOON":
        select = "2"
        moon()
    elif select == "3" or select == "mercury" or select == "Mercury" or select == "MERCURY":
        select = "3"
        mode()
    elif select == "4" or select == "venus" or select == "Venus" or select == "VENUS":
        select = "4"
        mode()
    elif select == "5" or select == "mars" or select == "Mars" or select == "MARS":
        select = "5"
        mode()
    elif select == "6" or select == "jupiter" or select == "Jupiter" or select == "JUPITER":
        select = "6"
        mode()
    elif select == "7" or select == "saturn" or select == "Venus" or select == "VENUS":
        select = "7"
        mode()
    elif select == "8" or select == "uranus" or select == "Uranus" or select == "URANUS":
        select = "8"
        mode()
    elif select == "9" or select == "neptune" or select == "Neptune" or select == "NEPTUNE":
        select = "9"
        mode()
    elif select == "10" or select == "all" or select == "All" or select == "ALL":
        select = "10"
        mode()
    elif select == "11" or select == "exit" or select == "Exit" or select == "EXIT":
        prompt()
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        menu()

def twilight(): # Twilight select
    global twili
    clear()
    twili = ("0")
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│         Pick twilight Type:         │")
    print("│                                     │")
    print("│                                     │")
    print("│  1: None            4: Astronomical │")
    print("│  2: Civil           5: All          │")
    print("│  3: Nutical         6: Back         │")
    print("│                                     │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    twili = input("Select an option: ")
    if twili == "1" or twili == "none" or twili == "None" or twili == "NONE":
        twili = "1"
        mode()
    elif twili == "2" or twili == "cival" or twili == "Cival" or twili == "CIVAL":
        twili = "2"
        mode()
    elif twili == "3" or twili == "nutical" or twili == "Nutical" or twili == "NUTICAL":
        twili = "3"
        mode()
    elif twili == "4" or twili == "astronomical" or twili == "Astronomical" or twili == "ASTRONOMICAL":
        twili = "4"
        mode()
    elif twili == "5" or twili == "all" or twili == "All" or twili == "ALL":
        twili = "5"
        mode()
    elif twili == "6" or twili == "back" or twili == "Back" or twili == "BACK":
        menu()
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        twilight()

# moon options
def moon(): # moon mode select
    global smoon
    clear()
    smoon = ("0")
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│           Pick Moon Mode:           │")
    print("│                                     │")
    print("│                                     │")
    print("│                                     │")
    print("│    1: Normal           2. Phases    │")
    print("│                                     │")
    print("│    3: Both             4. Back      │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    smoon = input("Select an option: ")
    if smoon == "1" or smoon == "normal" or smoon == "Normal" or smoon == "NORMAL":
        smoon = "1"
        mode()
    elif smoon == "2" or smoon == "phases" or smoon == "Phases" or smoon == "PHASES":
        smoon = "2"
        phases()
    elif smoon == "3" or smoon == "both" or smoon == "Both" or smoon == "BOTH":
        smoon = "3"
        mode()
    elif smoon == "4" or smoon == "back" or smoon == "Back" or smoon == "BACK":
        menu()
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        moon()

def phases(): # moon phases
    global phase
    clear()
    twili = ("0")
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│           Pick Moon Phase:          │")
    print("│                                     │")
    print("│                                     │")
    print("│  1: First Quarter Moon              │")
    print("│  2: Last Quarter Moon    5: All     │")
    print("│  3: Full Moon            6: Back    │")
    print("│  4: New Moon                        │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    phase = input("Select an option: ")
    if phase == "1" or phase == "first quarter moon" or phase == "First Quarter Moon":
        phase = "1"
        mode()
    elif phase == "2" or phase == "last quarter moon" or phase == "Last Quarter Moon":
        phase = "2"
        mode()
    elif phase == "3" or phase == "full moon" or phase == "Full moon" or phase == "Full Moon" or phase == "FULL MOON":
        phase = "3"
        mode()
    elif phase == "4" or phase == "new moon" or phase == "New moon" or phase == "New Moon" or phase == "NEW MOON":
        phase = "4"
        mode()
    elif phase == "5" or phase == "all" or phase == "All" or phase == "ALL":
        phase = "5"
        mode()
    elif phase == "6" or phase == "back" or phase == "Back" or phase == "BACK":
        menu()
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        phases()


def mode(): # pick an option for how to find location
    global longitude
    global latitude
    global altitude
    global timezone
    clear()
    locms = ("0")
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│         Pick Location Mode:         │")
    print("│                                     │")
    print("│                                     │")
    print("│                                     │")
    print("│    1: Manual            2. Auto     │")
    print("│                                     │")
    print("│               3.Back                │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    locms = input("Select an option: ")
    if locms == "1" or locms == "manual" or locms == "Manual" or locms == "MANUAL":
        print()
        try:
            longitude = float(input("What is your longitude? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
        if -90 < longitude and longitude < 90:
            longitude = str(longitude)
            print()
        else:
            print()
            print("INVALID NUMBER")
            time.sleep(0.5)
            mode()
        try:
            latitude = float(input("What is your latitude? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
        if -180 < latitude and latitude < 180:
            latitude = str(latitude)
            print()
        else:
            print()
            print("INVALID NUMBER")
            time.sleep(0.5)
            mode()
        try:
            altitude = int(input("What is your elevation? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
        if 1.8 < altitude and altitude < 8848:
            print()
        else:
            print("INVALID NUMBER")
            time.sleep(0.5)
            mode()
        timezone = input("What is your timezone? ")
        try:
            tz = pytz.timezone(timezone)
            date()
        except pytz.exceptions.UnknownTimeZoneError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
    elif locms == "2" or locms == "auto" or locms == "Auto" or locms == "AUTO":
        location = geocoder.ip('me')
        latitude = location.geojson['features'][0]['properties']['lat']
        longitude = location.geojson['features'][0]['properties']['lng']
        cord = Point(latitude, longitude)
        lat, lon, altitude = cord
        tf = timezonefinder.TimezoneFinder()
        timezone_str = tf.certain_timezone_at(lat=latitude, lng=longitude)
        if timezone_str is None:
            print()
            print("Could not determine the time zone")
            time.sleep(0.5)
            mode()
        else:
            try:
                dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo(timezone_str))
                timezone = str(dt.tzname())
                longitude = str(longitude)
                latitude = str(latitude)
                altitude = int(altitude)
            except pytz.exceptions.UnknownTimeZoneError:
                pass
                print()
                print("Could not determine the time zone")
                time.sleep(0.5)
                mode()
            date()
    elif locms == "3" or locms == "back" or locms == "Back" or locms == "BACK":
        menu()
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        mode()

def date(): # imput your own date or do it automaticly
    global mytime
    clear()
    timedate = ("0")
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│           Pick Date Mode:           │")
    print("│                                     │")
    print("│                                     │")
    print("│                                     │")
    print("│    1: Manual            2. Auto     │")
    print("│                                     │")
    print("│               3.Back                │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    timedate = input("Select an option: ")
    if timedate == "1" or timedate == "manual" or timedate == "Manual" or timedate == "MANUAL":
        print()
        try:
            year = int(input("What is your year? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            date()
        if 999 < year and year < 10000:
            year = str(year)
            print()
        else:
            print()
            print("INVALID YEAR")
            time.sleep(0.5)
            date()
        try:
            month = int(input("What is your month as a number? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            date()
        if 0 < month and month < 13:
            month = str(month)
            print()
        else:
            print()
            print("INVALID MONTH")
            time.sleep(0.5)
            date()
        try:
            day = int(input("What is your day? "))
        except ValueError:
            pass
            print()
            print("INVALID DAY")
            time.sleep(0.5)
            date()
        if month == "1":
            if 0 < day and day < 32:
                day = str(day)
                print()
        elif month == "2":
            if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
                if 0 < day and day < 30:
                    day = str(day)
                    print()
            else:
                if 0 < day and day < 29:
                    day = str(day)
                    print()
        elif month == "3":
            if 0 < day and day < 32:
                day = str(day)
                print()
        elif month == "4":
            if 0 < day and day < 31:
                day = str(day)
                print()
        elif month == "5":
            if 0 < day and day < 32:
                day = str(day)
                print()
        elif month == "6":
            if 0 < day and day < 31:
                day = str(day)
                print()
        elif month == "7":
            if 0 < day and day < 32:
                day = str(day)
                print()
        elif month == "8":
            if 0 < day and day < 32:
                day = str(day)
                print()
        elif month == "9":
            if 0 < day and day < 31:
                day = str(day)
                print()
        elif month == "10":
            if 0 < day and day < 32:
                day = str(day)
                print()
        elif month == "11":
            if 0 < day and day < 31:
                day = str(day)
                print()
        elif month == "12":
            if 0 < day and day < 32:
                day = str(day)
                print()
        else:
            print("INVALID DAY")
            time.sleep(0.5)
            date()
        mytime = (year + "-" + month + "-" + day + " 12:00:00.000000")
        calc()
    elif timedate == "2" or timedate == "auto" or timedate == "Auto" or timedate == "AUTO":
        mytime = datetime.now()
        calc()
    elif timedate == "3" or timedate == "back" or timedate == "Back" or timedate == "BACK":
        mode()
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        date()

def calc(): # Runs all the calculations and the option to save to file
    global my_loc
    global tz
    clear()
    my_loc = ephem.Observer()
    my_loc.lat = latitude
    my_loc.lon = longitude
    my_loc.elevation = altitude
    my_loc.date = mytime
    tz = pytz.timezone(timezone)
    if select == "1":
        if twili == "1":
            underline(' Sunrise and Sunset')
            print()
            srise()
            sset()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Sunrise and Sunset'+ '\n' + '\n' + psrise + '\n' + nsrise + '\n' + '\n')
                f.write(psset + '\n' + nsset + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter")
                delete()
                menu()
            else:
                delete()
                menu()
        elif twili == "2":
            underline(' Civil Sunrise and Sunset')
            print()
            srisec()
            ssetc()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Civil Sunrise and Sunset'+ '\n' + '\n' + psrisec + '\n' + nsrisec + '\n' + '\n')
                f.write(pssetc + '\n' + nssetc + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter")
                delete()
                menu()
            else:
                delete()
                menu()
        elif twili == "3":
            underline(' Nutical Sunrise and Sunset')
            print()
            srisen()
            ssetn()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Nutical Sunrise and Sunset'+ '\n' + '\n' + psrisen + '\n' + nsrisen + '\n' + '\n')
                f.write(pssetn + '\n' + nssetn + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter")
                delete()
                menu()
            else:
                delete()
                menu()
        elif twili == "4":
            underline(' Astronomical Sunrise and Sunset')
            print()
            srisea()
            sseta()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Astronomical Sunrise and Sunset'+ '\n' + '\n' + psrisea + '\n' + nsrisea + '\n' + '\n')
                f.write(psseta + '\n' + nsseta + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter")
                menu()
            else:
                menu()
        elif twili == "5":
            underline(' Sunrise in all twilights')
            print()
            srise()
            srisec()
            srisen()
            srisea()
            print()
            underline(' Sunset in all twilights')
            print()
            sset()
            ssetc()
            ssetn()
            sseta()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Sunrise in all twilights'+ '\n' + '\n' + psrise + '\n' + nsrise + '\n' + '\n' + psrisec + '\n' + nsrisec + '\n' + '\n' + psrisen + '\n' + nsrisen + '\n' + '\n' + psrisea + '\n' + nsrisea + '\n' + '\n')
                f.write('\n' + 'Sunset in all twilights'+ '\n' + '\n' + psset + '\n' + nsset + '\n' + '\n' + pssetc + '\n' + nssetc + '\n' + '\n' + pssetn + '\n' + nssetn + '\n' + '\n' + psseta + '\n' + nsseta + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter")
                menu()
            else:
                menu()
        else:
            print()
            print("A UNKNOWN ERROR HAS OCCURRED")
            time.sleep(0.5)
            menu()
    elif select == "2":
        if smoon == "1":
            underline(' Moonrise and Moonset')
            print()
            mst()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Moonrise and Moonset'+ '\n' + '\n' + pmst + '\n' + nmst + '\n' + '\n' + '\n' + pmrt + '\n' + nmrt + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter")
                delete()
                menu()
            else:
                delete()
                menu()
        elif smoon == "2":
            if phase == "1":
                underline(' First Quarter Moon Phase')
                print()
                mphfq()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'First Quarter Phase'+ '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter")
                    delete()
                    menu()
                else:
                    delete()
                    menu()
            elif phase == "2":
                underline(' Last Quarter Moon Phase')
                print()
                mphlq()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Last Quarter Phase'+ '\n' + '\n' + pmphlq + '\n' + nmphlq + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter")
                    delete()
                    menu()
                else:
                    delete()
                    menu()
            elif phase == "3":
                underline(' Full Moon Phase')
                print()
                mphf()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Full Moon Phase'+ '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter")
                    delete()
                    menu()
                else:
                    delete()
                    menu()
            elif phase == "4":
                underline(' New Moon Phase')
                print()
                mphn()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'New Moon Phase'+ '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter")
                    delete()
                    menu()
                else:
                    delete()
                    menu()
            elif phase == "5":
                underline(' All Moon Phases')
                print()
                mphfq()
                mphlq()
                mphf()
                mphn()
                print()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'All Moon Phases'+ '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n'  + pmphlq + '\n' + nmphlq + '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter")
                    delete()
                    menu()
                else:
                    delete()
                    menu()
            else:
                print()
                print("A UNKNOWN ERROR HAS OCCURRED")
                time.sleep(0.5)
                menu()
        elif smoon == "3":
            underline(' All Moon Options')
            print()
            mst()
            mphfq()
            mphlq()
            mphf()
            mphn()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Moonrise and Moonset'+ '\n' + '\n' + pmst + '\n' + nmst + '\n' + '\n' + '\n' + pmrt + '\n' + nmrt + '\n' + '\n' + '\n')
                f.write('All Moon Phases'+ '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n'  + pmphlq + '\n' + nmphlq + '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter")
                delete()
                menu()
            else:
                delete()
                menu()
        else:
            print()
            print("A UNKNOWN ERROR HAS OCCURRED")
            time.sleep(0.5)
            menu()
    elif select == "3":
        underline(' Mercury rise and set')
        print()
        merc()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Mercury rise and set'+ '\n' + '\n' + pmercr + '\n' + nmercr + '\n' + '\n' + '\n' + pmercs + '\n' + nmercs + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            delete()
            menu()
        else:
            delete()
            menu()
    elif select == "4":
        underline(' Venus rise and set')
        print()
        ven()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Venus rise and set'+ '\n' + '\n' + pvenr + '\n' + nvenr + '\n' + '\n' + '\n' + pvens + '\n' + nvens + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            delete()
            menu()
        else:
            delete()
            menu()
    elif select == "5":
        underline(' Mars rise and set')
        print()
        mars()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Mars rise and set'+ '\n' + '\n' + pmarsr + '\n' + nmarsr + '\n' + '\n' + '\n' + pmarss + '\n' + nmarss + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            delete()
            menu()
        else:
            delete()
            menu()
    elif select == "6":
        underline(' Jupiter rise and set')
        print()
        jup()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Jupiter rise and set'+ '\n' + '\n' + pjupr + '\n' + njupr + '\n' + '\n' + '\n' + pjups + '\n' + njups + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            delete()
            menu()
        else:
            delete()
            menu()
    elif select == "7":
        underline(' Saturn rise and set')
        print()
        sat()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Saturn rise and set'+ '\n' + '\n' + psatr + '\n' + nsatr + '\n' + '\n' + '\n' + psats + '\n' + nsats + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            delete()
            menu()
        else:
            delete()
            menu()
    elif select == "8":
        underline(' Uranus rise and set')
        print()
        ura()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Uranus rise and set'+ '\n' + '\n' + purar + '\n' + nurar + '\n' + '\n' + '\n' + puras + '\n' + nuras + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            delete()
            menu()
        else:
            delete()
            menu()
    elif select == "9":
        underline(' Neptune rise and set')
        print()
        nep()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Neptune rise and set'+ '\n' + '\n' + pnepr + '\n' + nnepr + '\n' + '\n' + '\n' + pneps + '\n' + nneps + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            delete()
            menu()
        else:
            delete()
            menu()
    elif select == "10":
        underline(' All options')
        print()
        print()
        underline(' Sunrise in all twilights')
        print()
        srise()
        srisec()
        srisen()
        srisea()
        print()
        underline(' Sunset in all twilights')
        print()
        sset()
        ssetc()
        ssetn()
        sseta()
        print()
        underline(' All Moon Options')
        print()
        mst()
        mphfq()
        mphlq()
        mphf()
        mphn()
        print()
        underline(' Mercury rise and set')
        print()
        merc()
        print()
        underline(' Venus rise and set')
        print()
        ven()
        print()
        underline(' Mars rise and set')
        print()
        mars()
        print()
        underline(' Jupiter rise and set')
        print()
        jup()
        print()
        underline(' Saturn rise and set')
        print()
        sat()
        print()
        underline(' Uranus rise and set')
        print()
        ura()
        print()
        underline(' Neptune rise and set')
        print()
        nep()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Sunrise in all twilights'+ '\n' + '\n' + psrise + '\n' + nsrise + '\n' + '\n' + psrisec + '\n' + nsrisec + '\n' + '\n' + psrisen + '\n' + nsrisen + '\n' + '\n' + psrisea + '\n' + nsrisea + '\n' + '\n')
            f.write('\n' + 'Sunset in all twilights'+ '\n' + '\n' + psset + '\n' + nsset + '\n' + '\n' + pssetc + '\n' + nssetc + '\n' + '\n' + pssetn + '\n' + nssetn + '\n' + '\n' + psseta + '\n' + nsseta + '\n' + '\n' + '\n')
            f.write('Moonrise and Moonset'+ '\n' + '\n' + pmst + '\n' + nmst + '\n' + '\n' + '\n' + pmrt + '\n' + nmrt + '\n' + '\n' + '\n')
            f.write('All Moon Phases'+ '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n'  + pmphlq + '\n' + nmphlq + '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
            f.write('Mercury rise and set'+ '\n' + '\n' + pmercr + '\n' + nmercr + '\n' + '\n' + '\n' + pmercs + '\n' + nmercs + '\n' + '\n' + '\n')
            f.write('Venus rise and set'+ '\n' + '\n' + pvenr + '\n' + nvenr + '\n' + '\n' + '\n' + pvens + '\n' + nvens + '\n' + '\n' + '\n')
            f.write('Mars rise and set'+ '\n' + '\n' + pmarsr + '\n' + nmarsr + '\n' + '\n' + '\n' + pmarss + '\n' + nmarss + '\n' + '\n' + '\n')
            f.write('Jupiter rise and set'+ '\n' + '\n' + pjupr + '\n' + njupr + '\n' + '\n' + '\n' + pjups + '\n' + njups + '\n' + '\n' + '\n')
            f.write('Saturn rise and set'+ '\n' + '\n' + psatr + '\n' + nsatr + '\n' + '\n' + '\n' + psats + '\n' + nsats + '\n' + '\n' + '\n')
            f.write('Uranus rise and set'+ '\n' + '\n' + purar + '\n' + nurar + '\n' + '\n' + '\n' + puras + '\n' + nuras + '\n' + '\n' + '\n')
            f.write('Neptune rise and set'+ '\n' + '\n' + pnepr + '\n' + nnepr + '\n' + '\n' + '\n' + pneps + '\n' + nneps + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: '+ os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter")
            menu()
        else:
            menu()
    else:
        print()
        print("A UNKNOWN ERROR HAS OCCURRED")
        time.sleep(0.5)
        menu()

def delete(): # Deletes all varibles
    gc.collect()

menu() # starts main menu
