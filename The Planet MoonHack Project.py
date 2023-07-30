# Made in Mu
# May take some time to load on first launch
# Best run in command prompt with the packages installed

# Internal Packages
import time
from datetime import datetime
import os
import winsound

# Third party Packages
import pytz
import ephem
import wmi
import geocoder
import timezonefinder
from geopy.point import Point
from backports.zoneinfo import ZoneInfo
from playsound import playsound
import wget

def clear():
    global mem
    try:
        if mem == 0:
            print(" \n" * 49)
            return
        elif mem == 1:
            os.system('cls' if os.name == 'nt' else 'clear')     # Checks if Mu is running
            return
        else:
            print(" \n" * 49)
            return
    except Exception:
        find = wmi.WMI()
        for process in find.Win32_Process():
            if "pythonw.exe" == process.Name:  # cmd.exe
                mem = 1
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                mem = 0
                print(" \n" * 49)
        return

def underline(text):  # Underlines text
    print("\u0332".join(text))

def delete(n):
    try:
        if n == 0:
            pass
        elif n == 1:
            print()
            print("Clearing Variables")
            time.sleep(0.5)
        elif n == 2:
            print()
            print("Clearing all Variables")
            time.sleep(0.8)
            for k, v in (globals().copy()).items():
                if not k.startswith('_') and k != 'tmp' and k != 'In' and k != 'Out' and not hasattr(v, '__call__'):
                    tv = str(type(v))
                    if not tv == "<class 'module'>":
                        del globals()[k]
            del tv
            prompt1()
            return
        for k, v in (globals().copy()).items():
            if not k.startswith('_') and k != 'tmp' and k != 'In' and k != 'Out' and not hasattr(v, '__call__'):
                tv = str(type(v))
                if not tv == "<class 'module'>" and not k == "mem" and not k == "sfxsounds":
                    del globals()[k]
        del tv
        menu()
        return
    except Exception:
        try:
            for k, v in (globals().copy()).items():
                if not k.startswith('_') and k != 'tmp' and k != 'In' and k != 'Out' and not hasattr(v, '__call__'):
                    tv = str(type(v))
                    if not tv == "<class 'module'>" and not k == "mem" and not k == "sfxsounds":
                        del globals()[k]
            del tv
            menu()
            return
        except Exception:
            print()
            print("A UNKNOWN ERROR HAS OCCURRED")
            time.sleep(0.5)
            menu()
            return

def prompt1():
    global sfxsounds
    sounds = 2
    clear()
    sounds = input("Do you want to enable the sound? ")
    if sounds == "yes" or sounds == "Yes" or sounds == "YES" or sounds == "y" or sounds == "Y":
        sfxsounds = 1
        time.sleep(1)
        sound()
        return
    elif sounds == "no" or sounds == "No" or sounds == "NO" or sounds == "n" or sounds == "N":
        sfxsounds = 0
        menu()
        return
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        print()
        prompt1()
        return

def download_bar1(current, total, width=80):
    print("Downloading " + file + ": " + "%d%% [%d / %d] bytes" % (current / total * 100, current, total))

def download_bar2(current, total, width=80):
    print("Downloading " + file + ": " + "%d%% [%d / %d] bytes" % (current / total * 100, current, total))
    os.system('cls' if os.name == 'nt' else 'clear')

def sound():
    global file
    global sfxsounds
    global soundchecks
    global oselected
    sfxsounds = 1
    temp = 0
    file = "none"
    print()
    if mem == 1:
        download_bar = download_bar2
    else:
        download_bar = download_bar1
    try:
        path = (os.getcwd() + "/Music/")
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        path = (os.getcwd() + "/Voice/")
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        if not os.path.exists(os.getcwd() + "/Music/Planets.wav") == True:
            try:
                if E == 1:
                    pass
            except Exception:
                E = 1
            URL = "https://github.com/slyfalco/The-MoonHack-Project/raw/main/Music/Planets.wav"
            file = "Planets.wav"
            wget.download(URL, os.getcwd() + "/Music/Planets.wav", bar=download_bar)
            if mem == 1:
                print("Downloaded " + file)
            else:
                print()
                print()
                print("Downloaded " + file)
                print()
            time.sleep(0.02)
        filestd = ["All", "Astronomical", "Auto", "Back", "Both", "Civil", "Disable", "ERROR", "First quarter moon", "Full moon", "INVALID", "Jupiter", "Last quarter moon", "Manual", "Mars", "Mercury", "Moon", "Nautical", "Neptune", "New moon", "None", "Normal", "Phases" , "Saturn", "Sun", "Uranus", "Venus", "All"]
        tempa2 = "/"
        for i in filestd:
            if not os.path.exists(os.getcwd() + "/Voice" + tempa2 + i + ".wav") == True:
                try:
                    if E == 1:
                        pass
                except Exception:
                    E = 1
                URL = ("https://github.com/slyfalco/The-MoonHack-Project/raw/main/Voice/" + i + ".wav")
                file = (i + ".wav")
                wget.download(URL, os.getcwd() + "/Voice" + tempa2 + i + ".wav", bar=download_bar)
                if mem == 1:
                    print("Downloaded " + file)
                else:
                    print()
                    print()
                    print("Downloaded " + file)
                    print()
                time.sleep(0.02)
        try:
            if E == 1:
                del E
                time.sleep(1)
        except Exception:
            pass
        del file
        temp = 1
    except Exception:
        file = 1
        del file
        print()
        print("Unable to download Sound files")
        time.sleep(0.5)
        print("Try checking your internet connection")
        time.sleep(2)
        print()
        print("Continuing without sound")
        time.sleep(2)
        sfxsounds = 0
        temp = 2
        print()
    try:
        if soundchecks == 1:
            print("Continuing at Selected Option")
            winsound.PlaySound(os.getcwd() + "/Music/Planets.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
            time.sleep(1)
            if oselected == "twilight":
                oselected = "twilight"
                del soundchecks
                del oselected
                twilight()
                return
            elif oselected == "moon":
                oselected = "moon"
                del soundchecks
                del oselected
                moon()
                return
            elif oselected == "mode":
                oselected = "mode"
                del soundchecks
                del oselected
                mode()
                return
            elif oselected == "mmode":
                oselected = "mmode"
                del soundchecks
                mode()
                return
            elif oselected == "amode":
                oselected = "amode"
                del soundchecks
                mode()
                return
            elif oselected == "mdate":
                oselected = "smode"
                del soundchecks
                date()
                return
            elif oselected == "adate":
                oselected = "amode"
                del soundchecks
                date()
                return
            elif oselected == "exit":
                oselected = "exit"
                del soundchecks
                oselected = "exit"
                menu()
                return
            elif oselected == "back1":
                oselected = "back1"
                del soundchecks
                del oselected
                delete()
                menu()
                return
    except Exception:
        if temp == 1:
            winsound.PlaySound(os.getcwd() + "/Music/Planets.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
            menu()
            return
        elif temp == 2:
            menu()
            return

def srise():  # sun rise
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

def srisec():  # sun rise civil
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

def srisen():  # sun rise nutical
    global mystr
    global psrisen
    global nsrisen
    my_loc.horizon = '-12'
    psrisen = str(ephem.to_timezone(my_loc.previous_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "psrisen"
    dtime(psrisen)
    psrisen = ("The Last Nautical Sunrise was on: " + psrisen + " in " + timezone + " Timezone")
    print(psrisen)
    nsrisen = str(ephem.to_timezone(my_loc.next_rising(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nsrisen"
    dtime(nsrisen)
    nsrisen = ("The Next Nautical Sunrise is on: " + nsrisen + " in " + timezone + " Timezone")
    print(nsrisen)
    print()
    del mystr
    return

def srisea():  # sun rise Astronomical
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

def sset():  # sun set
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

def ssetc():  # sun set cival
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

def ssetn():  # sun set Nautical
    global mystr
    global pssetn
    global nssetn
    my_loc.horizon = '-12'
    pssetn = str(ephem.to_timezone(my_loc.previous_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "pssetn"
    dtime(pssetn)
    pssetn = ("The Last Nautical Sunset was on: " + pssetn + " in " + timezone + " Timezone")
    print(pssetn)
    nssetn = str(ephem.to_timezone(my_loc.next_setting(ephem.Sun(my_loc), use_center=True), tz))
    mystr = "nssetn"
    dtime(nssetn)
    nssetn = ("The Next Nautical Sunset is on: " + nssetn + " in " + timezone + " Timezone")
    print(nssetn)
    print()
    del mystr
    return

def sseta():  # sun set Astronomical
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

def mphfq():  # First quarter moon
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

def mphlq():  # last quarter moon
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

def mphf():  # full moon
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

def mphn():  # new moon
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

def mst():  # moonset and rise
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
    pmst = ("The Last Moonset was on: " + pmst + " and its a " + mstph + " in " + timezone + " Timezone")
    print(pmst)
    nmst = str(ephem.to_timezone(my_loc.next_setting(ephem.Moon(my_loc), use_center=True), tz))
    mystr = "nmst"
    dtime(nmst)
    nmst = ("The Next Moonset is on: " + nmst + " and its a " + mstph + " in " + timezone + " Timezone")
    print(nmst)
    print()
    pmrt = str(ephem.to_timezone(my_loc.previous_rising(ephem.Moon(my_loc), use_center=True), tz))
    mystr = "pmrt"
    dtime(pmrt)
    pmrt = ("The Last Moonrise was on: " + pmrt + " and its a " + mstph + " in " + timezone + " Timezone")
    print(pmrt)
    nmrt = str(ephem.to_timezone(my_loc.next_rising(ephem.Moon(my_loc), use_center=True), tz))
    mystr = "nmrt"
    dtime(nmrt)
    nmrt = ("The Next Moonrise is on: " + nmrt + " and its a " + mstph + " in " + timezone + " Timezone")
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

def ven():  # Venus
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

def mars():  #mars
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

def jup():  # Jupiter
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

def sat():  # Saturn
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

def ura():  # Uranus
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

def nep():  # Neptune
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

def mphase():  # Moon phase
    moon_my_loc = ephem.Moon(my_loc)
    moon_phase = moon_my_loc.moon_phase
    moon_phase_word = 0
    if moon_phase < .06:
        moon_phase_word = "New Moon"
    elif moon_phase > .06 <= .19:
        moon_phase_word = "Waxing Crescent Moon"
    elif moon_phase > .19 <= .31:
        moon_phase_word = "Third Quarter Moon"
    elif moon_phase > .31 <= .44:
        moon_phase_word = "Waxing Gibbous Moon"
    elif moon_phase > .44 <= .56:
        moon_phase_word = "Full Moon"
    elif moon_phase > .56 <= .69:
        moon_phase_word = "Waning Gibbous Moon"
    elif moon_phase > .69 <= .81:
        moon_phase_word = "First Quarter Moon"
    elif moon_phase > .81 <= .94:
        moon_phase_word = "Waning Crescent Moon"
    elif moon_phase > .94:
        moon_phase_word = "New Moon"
    globals()[mystr] = moon_phase_word

def dtime(n):  # converts time to words
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
    return

def menu():  # The main menu
    global select
    global sfxsounds
    global soundchecks
    global oselected
    clear()
    select = "0"
    print("╭---------------------------------------╮")
    print("│      The Planet Moonhack Project      │")
    print("│                                       │")
    print("│         Select an option below:       │")
    print("│                                       │")
    print("│  1: Sun             7: Saturn         │")
    print("│  2: Moon            8: Uranus         │")
    print("│  3: Mercury         9: Neptune        │")
    print("│  4: Venus          10: All            │")
    print("│  5: Mars           11: ", end="")
    try:
        if sfxsounds == 1:
            sfxsounds = 1
            print("Disable Sound  │")
        elif sfxsounds == 0:
            sfxsounds = 0
            print("Enable Sound   │")
        else:
            print("ERROR          │")
            sfxsounds = 2
    except Exception:
        pass
        print("ERROR          │")
        sfxsounds = 2
    print("│  6: Jupiter        12: Exit           │")
    print("│                                       │")
    print("│ Project By: Damien Di Falco           │")
    print("╰---------------------------------------╯")
    print()
    time.sleep(0.1)
    print()
    select = input("Select an option: ")
    tempa = 1
    if select == "1" or select == "sun" or select == "Sun" or select == "SUN":
        select = "1"
        tempa = 0
        try:
            if sfxsounds == 0:
                twilight()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Sun.wav")
                    twilight()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "twilight"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                twilight()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
    elif select == "2" or select == "moon" or select == "Moon" or select == "MOON":
        select = "2"
        tempa = 0
        try:
            if sfxsounds == 0:
                moon()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Moon.wav")
                    moon()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "moon"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                moon()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "3" or select == "mercury" or select == "Mercury" or select == "MERCURY":
        select = "3"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Mercury.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "4" or select == "venus" or select == "Venus" or select == "VENUS":
        select = "4"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Venus.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "5" or select == "mars" or select == "Mars" or select == "MARS":
        select = "5"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Mars.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "6" or select == "jupiter" or select == "Jupiter" or select == "JUPITER":
        select = "6"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Jupiter.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "7" or select == "saturn" or select == "Saturn" or select == "SATURN":
        select = "7"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Saturn.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "8" or select == "uranus" or select == "Uranus" or select == "URANUS":
        select = "8"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                i = "/"
                try:
                    playsound(os.getcwd() + "/Voice" + i + "Uranus.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "9" or select == "neptune" or select == "Neptune" or select == "NEPTUNE":
        select = "9"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                i = "/"
                try:
                    playsound(os.getcwd() + "/Voice" + i + "Neptune.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif select == "10" or select == "all" or select == "All" or select == "ALL":
        select = "10"
        tempa = 0
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/All.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    if sfxsounds == 0:
        if select == "11" or select == "enable sound" or select == "Enable sound" or select == "Enable Sound" or select == "ENABLE SOUND":
            print()
            sfxsounds = 1
            tempa = 0
            sound()
            return
    elif sfxsounds == 1:
        if select == "11" or select == "disable sound" or select == "Disable sound" or select == "Disable Sound" or select == "DISABLE SOUND":
            print()
            winsound.PlaySound(None, winsound.SND_PURGE)
            playsound(os.getcwd() + "/Voice/Disable.wav")
            sfxsounds = 0
            tempa = 0
            menu()
            return
    elif sfxsounds == 2:
        if select == "11" or select == "error" or select == "Error" or select == "ERROR":
            winsound.PlaySound(None, winsound.SND_PURGE)
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            tempa = 0
            delete(2)
            return
    if select == "12" or select == "exit" or select == "Exit" or select == "EXIT":
        tempa = 0
        print()
        exita = input("Are you sure you want to quit? ")
        if exita == "yes" or exita == "Yes" or exita == "YES" or exita == "y" or exita == "Y":
            try:
                print()
                delete(0)
                winsound.PlaySound(None, winsound.SND_PURGE)
                exit("User quit from menu")
            except SystemExit:
                pass
        elif exita == "no" or exita == "No" or exita == "NO" or exita == "n" or exita == "N":
            delete(0)
            return
        else:
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            print()
            menu()
            return
    if tempa == 1:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        menu()

def twilight():  # Twilight select
    global twili
    global soundchecks
    global oselected
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
    print("│  3: Nautical        6: Back         │")
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
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/None.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif twili == "2" or twili == "civil" or twili == "Civil" or twili == "CIVIL":
        twili = "2"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Civil.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif twili == "3" or twili == "nautical" or twili == "Nautical" or twili == "NAUTICAL":
        twili = "3"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Nautical.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif twili == "4" or twili == "astronomical" or twili == "Astronomical" or twili == "ASTRONOMICAL":
        twili = "4"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Astronomical.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif twili == "5" or twili == "all" or twili == "All" or twili == "ALL":
        twili = "5"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/All.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif twili == "6" or twili == "back" or twili == "Back" or twili == "BACK":
        del twili
        try:
            if sfxsounds == 0:
                delete(0)
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Back.wav")
                    delete(0)
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "back1"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                delete(0)
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        twilight()
        return

# moon options
def moon():  # moon mode select
    global smoon
    global soundchecks
    global oselected
    clear()
    smoon = ("0")
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│           Pick Moon Mode:           │")
    print("│                                     │")
    print("│                                     │")
    print("│    1: Normal           3: Both      │")
    print("│                                     │")
    print("│    2: Phases           4: Back      │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    smoon = input("Select an option: ")
    if smoon == "1" or smoon == "normal" or smoon == "Normal" or smoon == "NORMAL":
        smoon = "1"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Normal.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "normal"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif smoon == "2" or smoon == "phases" or smoon == "Phases" or smoon == "PHASES":
        smoon = "2"
        try:
            if sfxsounds == 0:
                phases()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Phases.wav")
                    phases()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "phases"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif smoon == "3" or smoon == "both" or smoon == "Both" or smoon == "BOTH":
        smoon = "3"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Both.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "both"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif smoon == "4" or smoon == "back" or smoon == "Back" or smoon == "BACK":
        del smoon
        try:
            if sfxsounds == 0:
                delete(0)
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Back.wav")
                    delete(0)
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "back1"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                delete(0)
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        moon()
        return

def phases():  # moon phases
    global phase
    global soundchecks
    global oselected
    clear()
    phase = ("0")
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
    if phase == "1" or phase == "first quarter moon" or phase == "First Quarter Moon" or phase == "FIRST QUARTER MOON":
        phase = "1"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/First quarter moon.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif phase == "2" or phase == "last quarter moon" or phase == "Last Quarter Moon" or phase == "LAST QUARTER MOON":
        phase = "2"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Last quarter moon.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif phase == "3" or phase == "full moon" or phase == "Full moon" or phase == "Full Moon" or phase == "FULL MOON":
        phase = "3"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Full moon.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif phase == "4" or phase == "new moon" or phase == "New moon" or phase == "New Moon" or phase == "NEW MOON":
        phase = "4"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/New moon.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif phase == "5" or phase == "all" or phase == "All" or phase == "ALL":
        phase = "5"
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/All.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    elif phase == "6" or phase == "back" or phase == "Back" or phase == "BACK":
        del phase
        try:
            if sfxsounds == 0:
                moon()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Back.wav")
                    moon()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "moon"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                moon()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        phases()
        return

def mode():  # pick an option for how to find location
    global longitude
    global latitude
    global altitude
    global timezone
    global soundchecks
    global oselected
    clear()
    mcheck = 0
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│         Pick Location Mode:         │")
    print("│                                     │")
    print("│                                     │")
    print("│     1: Manual           2: Auto     │")
    print("│                                     │")
    print("│               3: Back               │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    try:
        if oselected == "mmode":
            mcheck = 1
            locms = ("1")
            del oselected
        elif oselected == "amode":
            mcheck = 1
            locms = ("2")
            del oselected
    except Exception:
        locms = ("0")
        locms = input("Select an option: ")
    if locms == "1" or locms == "manual" or locms == "Manual" or locms == "MANUAL":
        try:
            if sfxsounds == 1 and mcheck == 0:
                try:
                    playsound(os.getcwd() + "/Voice/Manual.wav")
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mmode"
                    sound()
                    return
            elif sfxsounds == 2 and mcheck == 0:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        print()
        try:
            longitude = float(input("What is your longitude? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
            return
        if -90 < longitude and longitude < 90:
            longitude = str(longitude)
            print()
        else:
            print()
            print("INVALID NUMBER")
            time.sleep(0.5)
            mode()
            return
        try:
            latitude = float(input("What is your latitude? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
            return
        if -180 < latitude and latitude < 180:
            latitude = str(latitude)
            print()
        else:
            print()
            print("INVALID NUMBER")
            time.sleep(0.5)
            mode()
            return
        try:
            altitude = int(input("What is your elevation? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
            return
        if 1.8 < altitude and altitude < 8848:
            print()
        else:
            print("INVALID NUMBER")
            time.sleep(0.5)
            mode()
            return
        timezone = input("What is your timezone? ")
        try:
            tz = pytz.timezone(timezone)
            date()
            return
        except pytz.exceptions.UnknownTimeZoneError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            mode()
            return
    elif locms == "2" or locms == "auto" or locms == "Auto" or locms == "AUTO":
        try:
            if sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Auto.wav")
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "amode"
                    sound()
                    return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        try:
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
                return
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
                    return
                date()
                return
        except Exception:
            pass
            time.sleep(0.2)
            print()
            print("Unable to determine location")
            time.sleep(0.5)
            print("Try checking your internet connection")
            time.sleep(2)
            mode()
            return
    elif locms == "3" or locms == "back" or locms == "Back" or locms == "BACK":
        del locms
        try:
            del loongitude
        except Exception:
            pass
        try:
            del latitude
        except Exception:
            pass
        try:
            del altitude
        except Exception:
            pass
        try:
            del timezone
        except Exception:
            pass
        if select == "1":
            try:
                if sfxsounds == 0:
                    twilight()
                    return
                elif sfxsounds == 1:
                    try:
                        playsound(os.getcwd() + "/Voice/Back.wav")
                        twilight()
                    except Exception:
                        winsound.PlaySound(None, winsound.SND_PURGE)
                        print()
                        print("File not found")
                        time.sleep(0.5)
                        print("Downloading missing files")
                        time.sleep(1)
                        soundchecks = 1
                        oselected = "twilight"
                        sound()
                        return
                    return
                elif sfxsounds == 2:
                    if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                        playsound(os.getcwd() + "/Voice/ERROR.wav")
                    twilight()
                    return
            except Exception:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                delete(2)
                return
            return
        elif select == "2":
            if smoon == "1" or smoon == "3":
                try:
                    if sfxsounds == 0:
                        moon()
                        return
                    elif sfxsounds == 1:
                        try:
                            playsound(os.getcwd() + "/Voice/Back.wav")
                            moon()
                        except Exception:
                            winsound.PlaySound(None, winsound.SND_PURGE)
                            print()
                            print("File not found")
                            time.sleep(0.5)
                            print("Downloading missing files")
                            time.sleep(1)
                            soundchecks = 1
                            oselected = "moon"
                            sound()
                            return
                        return
                    elif sfxsounds == 2:
                        if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                            playsound(os.getcwd() + "/Voice/ERROR.wav")
                        moon()
                        return
                except Exception:
                    if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                        playsound(os.getcwd() + "/Voice/ERROR.wav")
                    delete(2)
                    return
                return
            elif smoon == "2":
                try:
                    if sfxsounds == 0:
                        phases()
                        return
                    elif sfxsounds == 1:
                        try:
                            playsound(os.getcwd() + "/Voice/Back.wav")
                            phases()
                        except Exception:
                            winsound.PlaySound(None, winsound.SND_PURGE)
                            print()
                            print("File not found")
                            time.sleep(0.5)
                            print("Downloading missing files")
                            time.sleep(1)
                            soundchecks = 1
                            oselected = "phases"
                            sound()
                            return
                        return
                    elif sfxsounds == 2:
                        if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                            playsound(os.getcwd() + "/Voice/ERROR.wav")
                        phases()
                        return
                except Exception:
                    if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                        playsound(os.getcwd() + "/Voice/ERROR.wav")
                    delete(2)
                    return
                return
            else:
                print()
                print("A UNKNOWN ERROR HAS OCCURRED")
                time.sleep(0.5)
                menu()
                return
        else:
            try:
                if sfxsounds == 0:
                    menu()
                    return
                elif sfxsounds == 1:
                    try:
                        playsound(os.getcwd() + "/Voice/Back.wav")
                        menu()
                    except Exception:
                        winsound.PlaySound(None, winsound.SND_PURGE)
                        print()
                        print("File not found")
                        time.sleep(0.5)
                        print("Downloading missing files")
                        time.sleep(1)
                        soundchecks = 1
                        oselected = "back1"
                        sound()
                        return
                    return
                elif sfxsounds == 2:
                    if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                        playsound(os.getcwd() + "/Voice/ERROR.wav")
                    menu()
                    return
            except Exception:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                delete(2)
                return
            return
        return
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        mode()
        return
def date():  # imput your own date or do it automaticly
    global mytime
    global soundchecks
    global oselected
    clear()
    mcheck = 0
    print("╭-------------------------------------╮")
    print("│     The Planet Moonhack Project     │")
    print("│                                     │")
    print("│           Pick Date Mode:           │")
    print("│                                     │")
    print("│                                     │")
    print("│     1: Manual           2: Auto     │")
    print("│                                     │")
    print("│               3: Back               │")
    print("│                                     │")
    print("│                                     │")
    print("│ Project By: Damien Di Falco         │")
    print("╰-------------------------------------╯")
    print()
    time.sleep(0.1)
    try:
        if oselected == "mdate":
            mcheck = 1
            timedate = ("1")
            del oselected
        elif oselected == "adate":
            mcheck = 1
            timedate = ("2")
            del oselected
    except Exception:
        timedate = ("0")
        timedate = input("Select an option: ")
    if timedate == "1" or timedate == "manual" or timedate == "Manual" or timedate == "MANUAL":
        try:
            if sfxsounds == 1 and mcheck == 0:
                try:
                    playsound(os.getcwd() + "/Voice/Manual.wav")
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mdate"
                    sound()
                    return
            elif sfxsounds == 2 and mcheck == 0:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        print()
        try:
            year = int(input("What is your year? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            date()
            return
        if 999 < year and year < 10000:
            year = str(year)
            print()
        else:
            print()
            print("INVALID YEAR")
            time.sleep(0.5)
            date()
            return
        try:
            month = int(input("What is your month as a number? "))
        except ValueError:
            pass
            print()
            print("INVALID RESPONSE")
            time.sleep(0.5)
            date()
            return
        if 0 < month and month < 13:
            month = str(month)
            print()
        else:
            print()
            print("INVALID MONTH")
            time.sleep(0.5)
            date()
            return
        try:
            day = int(input("What is your day? "))
        except ValueError:
            pass
            print()
            print("INVALID DAY")
            time.sleep(0.5)
            date()
            return
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
            return
        mytime = (year + "-" + month + "-" + day + " 12:00:00.000000")
        calc()
        return
    elif timedate == "2" or timedate == "auto" or timedate == "Auto" or timedate == "AUTO":
        try:
            if sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Auto.wav")
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "adate"
                    sound()
                    return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        mytime = datetime.now()
        calc()
        return
    elif timedate == "3" or timedate == "back" or timedate == "Back" or timedate == "BACK":
        del timedate
        try:
            if sfxsounds == 0:
                mode()
                return
            elif sfxsounds == 1:
                try:
                    playsound(os.getcwd() + "/Voice/Back.wav")
                    mode()
                except Exception:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    print()
                    print("File not found")
                    time.sleep(0.5)
                    print("Downloading missing files")
                    time.sleep(1)
                    soundchecks = 1
                    oselected = "mode"
                    sound()
                    return
                return
            elif sfxsounds == 2:
                if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                    playsound(os.getcwd() + "/Voice/ERROR.wav")
                mode()
                return
        except Exception:
            if os.path.exists(os.getcwd() + "/Voice/ERROR.wav") == True:
                playsound(os.getcwd() + "/Voice/ERROR.wav")
            delete(2)
            return
        return
    else:
        print()
        print("INVALID RESPONSE")
        time.sleep(0.5)
        date()
        return

def calc():  # Runs all the calculations and has the option to save to file
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
                f.write('---------------' + date + '---------------' + '/n' + '\n' + 'Sunrise and Sunset' + '\n' + '\n' + psrise + '\n' + nsrise + '\n' + '\n')
                f.write(psset + '\n' + nsset + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter ")
                delete(1)
                return
            else:
                delete(1)
                return
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
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Civil Sunrise and Sunset' + '\n' + '\n' + psrisec + '\n' + nsrisec + '\n' + '\n')
                f.write(pssetc + '\n' + nssetc + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter ")
                delete(1)
                return
            else:
                delete(1)
                return
        elif twili == "3":
            underline(' Nautical Sunrise and Sunset')
            print()
            srisen()
            ssetn()
            print()
            save = input("Save to file? ")
            if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                date = str(my_loc.date)
                f = open("Planet Output File.txt", "a")
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Nautical Sunrise and Sunset' + '\n' + '\n' + psrisen + '\n' + nsrisen + '\n' + '\n')
                f.write(pssetn + '\n' + nssetn + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter ")
                delete(1)
                return
            else:
                delete(1)
                return
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
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Astronomical Sunrise and Sunset' + '\n' + '\n' + psrisea + '\n' + nsrisea + '\n' + '\n')
                f.write(psseta + '\n' + nsseta + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter ")
                delete(1)
                return
            else:
                delete(1)
                return
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
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Sunrise in all twilights '+ '\n' + '\n' + psrise + '\n' + nsrise + '\n' + '\n' + psrisec + '\n' + nsrisec + '\n' + '\n' + psrisen + '\n' + nsrisen + '\n' + '\n' + psrisea + '\n' + nsrisea + '\n' + '\n')
                f.write('\n' + 'Sunset in all twilights' + '\n' + '\n' + psset + '\n' + nsset + '\n' + '\n' + pssetc + '\n' + nssetc + '\n' + '\n' + pssetn + '\n' + nssetn + '\n' + '\n' + psseta + '\n' + nsseta + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter ")
                delete(1)
                return
            else:
                delete(1)
                return
        else:
            print()
            print("A UNKNOWN ERROR HAS OCCURRED")
            time.sleep(0.5)
            delete(1)
            return
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
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Moonrise and Moonset' + '\n' + '\n' + pmst + '\n' + nmst + '\n' + '\n' + '\n' + pmrt + '\n' + nmrt + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter ")
                delete(1)
                return
            else:
                delete(1)
                return
        elif smoon == "2":
            if phase == "1":
                underline(' First Quarter Moon Phase')
                print()
                mphfq()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'First Quarter Phase' + '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter ")
                    delete(1)
                    return
                else:
                    delete(1)
                    return
            elif phase == "2":
                underline(' Last Quarter Moon Phase')
                print()
                mphlq()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Last Quarter Phase' + '\n' + '\n' + pmphlq + '\n' + nmphlq + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter ")
                    delete(1)
                    return
                else:
                    delete(1)
                    return
            elif phase == "3":
                underline(' Full Moon Phase')
                print()
                mphf()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Full Moon Phase' + '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter ")
                    delete(1)
                    return
                else:
                    delete(1)
                    return
            elif phase == "4":
                underline(' New Moon Phase')
                print()
                mphn()
                save = input("Save to file? ")
                if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
                    date = str(my_loc.date)
                    f = open("Planet Output File.txt", "a")
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'New Moon Phase' + '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter ")
                    delete(1)
                    return
                else:
                    delete(1)
                    return
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
                    f.write('---------------' + date + '---------------' + '\n' + '\n' + 'All Moon Phases' + '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n'  + pmphlq + '\n' + nmphlq + '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
                    f.close()
                    time.sleep(0.2)
                    print()
                    print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                    time.sleep(0.7)
                    print()
                    input("Press enter ")
                    delete(1)
                    menu()
                    return
                else:
                    delete(1)
                    return
            else:
                print()
                print("A UNKNOWN ERROR HAS OCCURRED")
                time.sleep(0.5)
                delete(1)
                return
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
                f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Moonrise and Moonset' + '\n' + '\n' + pmst + '\n' + nmst + '\n' + '\n' + '\n' + pmrt + '\n' + nmrt + '\n' + '\n' + '\n')
                f.write('All Moon Phases' + '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n'  + pmphlq + '\n' + nmphlq + '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
                f.close()
                time.sleep(0.2)
                print()
                print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
                time.sleep(0.7)
                print()
                input("Press enter ")
                delete(1)
                menu()
                return
            else:
                delete(1)
                return
        else:
            print()
            print("A UNKNOWN ERROR HAS OCCURRED")
            time.sleep(0.5)
            delete(1)
            return
    elif select == "3":
        underline(' Mercury rise and set')
        print()
        merc()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Mercury rise and set' + '\n' + '\n' + pmercr + '\n' + nmercr + '\n' + '\n' + '\n' + pmercs + '\n' + nmercs + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            delete(1)
            return
        else:
            delete(1)
            return
    elif select == "4":
        underline(' Venus rise and set')
        print()
        ven()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Venus rise and set' + '\n' + '\n' + pvenr + '\n' + nvenr + '\n' + '\n' + '\n' + pvens + '\n' + nvens + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            delete(1)
            return
        else:
            delete(1)
            return
    elif select == "5":
        underline(' Mars rise and set')
        print()
        mars()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Mars rise and set' + '\n' + '\n' + pmarsr + '\n' + nmarsr + '\n' + '\n' + '\n' + pmarss + '\n' + nmarss + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            delete(1)
            return
        else:
            delete(1)
            return
    elif select == "6":
        underline(' Jupiter rise and set')
        print()
        jup()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Jupiter rise and set' + '\n' + '\n' + pjupr + '\n' + njupr + '\n' + '\n' + '\n' + pjups + '\n' + njups + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            delete(1)
            return
        else:
            delete(1)
            return
    elif select == "7":
        underline(' Saturn rise and set')
        print()
        sat()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Saturn rise and set' + '\n' + '\n' + psatr + '\n' + nsatr + '\n' + '\n' + '\n' + psats + '\n' + nsats + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            delete(1)
            return
        else:
            delete(1)
            return
    elif select == "8":
        underline(' Uranus rise and set')
        print()
        ura()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Uranus rise and set' + '\n' + '\n' + purar + '\n' + nurar + '\n' + '\n' + '\n' + puras + '\n' + nuras + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            return
        else:
            delete(1)
            return
    elif select == "9":
        underline(' Neptune rise and set')
        print()
        nep()
        print()
        save = input("Save to file? ")
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES":
            date = str(my_loc.date)
            f = open("Planet Output File.txt", "a")
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Neptune rise and set' + '\n' + '\n' + pnepr + '\n' + nnepr + '\n' + '\n' + '\n' + pneps + '\n' + nneps + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            delete(1)
            return
        else:
            delete(1)
            return
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
            f.write('---------------' + date + '---------------' + '\n' + '\n' + 'Sunrise in all twilights' + '\n' + '\n' + psrise + '\n' + nsrise + '\n' + '\n' + psrisec + '\n' + nsrisec + '\n' + '\n' + psrisen + '\n' + nsrisen + '\n' + '\n' + psrisea + '\n' + nsrisea + '\n' + '\n')
            f.write('\n' + 'Sunset in all twilights' + '\n' + '\n' + psset + '\n' + nsset + '\n' + '\n' + pssetc + '\n' + nssetc + '\n' + '\n' + pssetn + '\n' + nssetn + '\n' + '\n' + psseta + '\n' + nsseta + '\n' + '\n' + '\n')
            f.write('Moonrise and Moonset' + '\n' + '\n' + pmst + '\n' + nmst + '\n' + '\n' + '\n' + pmrt + '\n' + nmrt + '\n' + '\n' + '\n')
            f.write('All Moon Phases' + '\n' + '\n' + pmphfq + '\n' + nmphfq + '\n' + '\n'  + pmphlq + '\n' + nmphlq + '\n' + '\n' + pmphf + '\n' + nmphf + '\n' + '\n' + pmphn + '\n' + nmphn + '\n' + '\n' + '\n')
            f.write('Mercury rise and set' + '\n' + '\n' + pmercr + '\n' + nmercr + '\n' + '\n' + '\n' + pmercs + '\n' + nmercs + '\n' + '\n' + '\n')
            f.write('Venus rise and set' + '\n' + '\n' + pvenr + '\n' + nvenr + '\n' + '\n' + '\n' + pvens + '\n' + nvens + '\n' + '\n' + '\n')
            f.write('Mars rise and set' + '\n' + '\n' + pmarsr + '\n' + nmarsr + '\n' + '\n' + '\n' + pmarss + '\n' + nmarss + '\n' + '\n' + '\n')
            f.write('Jupiter rise and set' + '\n' + '\n' + pjupr + '\n' + njupr + '\n' + '\n' + '\n' + pjups + '\n' + njups + '\n' + '\n' + '\n')
            f.write('Saturn rise and set' + '\n' + '\n' + psatr + '\n' + nsatr + '\n' + '\n' + '\n' + psats + '\n' + nsats + '\n' + '\n' + '\n')
            f.write('Uranus rise and set' + '\n' + '\n' + purar + '\n' + nurar + '\n' + '\n' + '\n' + puras + '\n' + nuras + '\n' + '\n' + '\n')
            f.write('Neptune rise and set '+ '\n' + '\n' + pnepr + '\n' + nnepr + '\n' + '\n' + '\n' + pneps + '\n' + nneps + '\n' + '\n' + '\n')
            f.close()
            time.sleep(0.2)
            print()
            print('File Saved to: ' + os.getcwd() + "\Planet Output File.txt")
            time.sleep(0.7)
            print()
            input("Press enter ")
            delete(1)
            return
        else:
            delete(1)
            return
    else:
        print()
        print("A UNKNOWN ERROR HAS OCCURRED")
        time.sleep(0.5)
        delete(1)
        return
prompt1()  # starts program
