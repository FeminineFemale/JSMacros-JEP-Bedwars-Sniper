from time import sleep
global ran
from requests import get
from keyboard import is_pressed

end = False
gamemode = ["four_three", "eight_one", "four_four", "eight_two"]
apikey = "566a7962-7fa5-4a40-98ba-26c546e338e1"


def gett(Player):
    try:
        #Chat.log(f"attempting to scan {Player}")
        finals = 0; winstreak = 0; wins = 0; BB = 0; fkdr = 0; wlr = 0; bblr = 0; losses = 0; finaldeath = 0; BL = 0
        stuff = {0: [winstreak, "_winstreak", 10], 1: [BB, "_beds_broken_bedwars", 20000], 2: [finals, "_final_kills_bedwars", 20000], 3: [bblr, "", 15], 4: [fkdr, "", 20], 5: [wlr, "", 10],
        6: [wins, "_wins_bedwars", 10000], 7: [losses, "_losses_bedwars"], 8: [finaldeath, "_final_deaths_bedwars"], 9: [BL, "_beds_lost_bedwars"]}
        end = False
        data = get(url="https://api.hypixel.net/player", params={"key": apikey, "name": Player}).json()
        for x in gamemode:
            for a in stuff:
                try:
                    stuff[a][0] = stuff[a][0] + data["player"]["stats"]["Bedwars"][x + stuff[a][1]]
                except:
                    pass
        try:fkdr = round(stuff[2][0] / stuff[8][0], 2)
        except:Chat.log(f"method 1 unable to get fkdr for {Player}")
        try:wlr = round(stuff[6][0] / stuff[7][0], 2)
        except:Chat.log(f"method 1 unable to get wlr for {Player}")
        try:bblr = round(stuff[1][0] / stuff[9][0], 2)
        except:Chat.log(f"method 1 unable to get bblr for {Player}")
        Chat.log(f"{Player} finals={str(stuff[2][0])} winstreak={str(stuff[0][0])} wins={str(stuff[6][0])} beds={str(stuff[1][0])} fkdr={fkdr} wlr={wlr} bblr={bblr}")
        for x, h in zip(stuff, range(len(stuff))):
            if h > 6:break
            #Chat.log(f"thing {int(stuff[x][0])} thing 2 {int(stuff[x][2])}")
            if int(stuff[x][0]) >= int(stuff[x][2]):
                end = True
                Chat.log(f" SUCCESS SUCCESS SUCCESS SUCCESS SUCCESS SUCCESS SUCCESS SUCCESS SUCCESS SUCCESS ")
        try:finals = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
        except:Chat.log(f"unable to get finals for {Player}")
        try:winstreak = data["player"]["stats"]["Bedwars"]["winstreak"]
        except:Chat.log(f"unable to get winstreak for {Player}")
        try:wins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
        except:Chat.log(f"unable to get wins for {Player}")
        try:BB = data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"]
        except:Chat.log(f"unable to get BB for {Player}")
        try:fkdr = round(data["player"]["stats"]["Bedwars"]["final_kills_bedwars"] / data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"], 2)
        except:Chat.log(f"unable to get fkdr for {Player}")
        try:wlr = round(data["player"]["stats"]["Bedwars"]["wins_bedwars"] / data["player"]["stats"]["Bedwars"]["losses_bedwars"], 2)
        except:Chat.log(f"unable to get wlr for {Player}")
        try:bblr = round(data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"] / data["player"]["stats"]["Bedwars"]["beds_lost_bedwars"], 2)
        except:Chat.log(f"unable to get bblr for {Player}")
        Chat.log(f"{Player} finals={finals} winstreak={winstreak} wins={wins} beds={BB} fkdr={fkdr} wlr={wlr} bblr={bblr}")
        for x, h in zip(stuff, range(len(stuff))):
            if h > 6:break
            if int(stuff[x][0]) >= int(stuff[x][2]):
                end = True
                Chat.log(f" SUCCESS SUCCESS SUCCESS SUCCESUCCESS SUCCESS SUCCESS ")
    except Exception as e:Chat.log(f'BIG SCARY ERROR{e}')


ran = ['osamanuke', 'bigpoopyballs', 'Neer', 'Salbosski', 'Fazzer']
name = []

fk = ['four_four', 'eight_two', 'four_three']
Chat.say(f'/play bedwars_four_three')

sleep(3)
while True:
    if is_pressed("p"):
        break
    for world in fk:
        while True:
            if is_pressed("p"):
                break
            p = World.getPlayers()
            for i in p:
                name.append(str(str(i).split('":"')[1][0:-2]))

            if len(name) > len(ran):
                for h in name:
                    good = True
                    for l in ran:
                        if l == h:
                            good = False
                    if good == True:
                        ran.append(h)
                        gett(h)
            sleep(.3)
            if len(p) >= 9 and end == True:
                Chat.log("end is true")
            elif len(p) >= 9:
                Chat.say(f'/play bedwars_{world}')
                sleep(3)
                break

Chat.log('done')




