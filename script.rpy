# // remove exists follower
# // $gameParty.removeGuestActor($gameParty.guestActors()[0]);

# // java version error => sudo update-alternatives --config javac    UBUNTU

# https://play.google.com/store/apps/details?id=ngant.ecchiheaven.com
# player could get 1 different quest everyday.
# player must complete the quest in the same day or at the same timeline
# player almost must complete all the quest to open special scenario.
# player will upgrade to another grade after some day and some main quest.
# loop to another dimension always.

# battle quest.
# tap to npc => talk => battle => lose|lost money => win|rewards 

# search quest.
# tap to npc => find the item NPC want in the world item|child|herb....
# HOW TO
# NPC 1 => random script search Quest
# start quest = 1 , complete quest = 0
# NPC 2 => random script search Quest
# start quest = 0 , complete quest = 1
# random reward.

# QA quest.
# tap to npc => talk => choose answer => right|will see more content => wrong|no content to see.

# trade quest.
# same with search quest but need money|another item to earn item.
# will get important item sometimes.

# forge quest.
# ??????

# there will be always 1 battle, 1 searching, 1 trading, 1 QA, 1 forging.
# battle will be right away or after some text.
# need to create every 3or5 monster to 1 level.so we need 25 monsters for first arcs.
# searching too. -> searching for item|people|herb|what ever.
# trading too. need to have special item or money to buy item.
# QA only visual novel. need to save all the choice from 1->5 and calculate all five Answer.
# forging little tricky. 
# for every quest will open an arc so for 5 type of quest will open 5 arc for first school.

# NEVER USE SELF SWITCH FOR MAKE MAIN QUEST.

# 2.1 Lust charming mother              => acolyte => 
# 2.2 Gluttony stringendo-angel-tachi   => swordman => 
# 2.3 Greed lingerie                    => tanker => 
# 2.4 Sloth mankitsu                    => thief => 
# 2.5 Wrath bible black                 => swordman => 
# 2.6 Envy mistreated-bride             => tanker => 
# 2.7 Pride netorare-fighter            => thief => 


# name of the character. always make new define,$,switch at the last line.
define p = Character("Yuuji Enomoto", color="#29AFD6") # master peice animation
define yuna = Character("Yuna Tsubakihara", color="#29AFD6") # childhood girl master peice animation
define mira = Character("Mira Tsubakihara", color="#29AFD6") # childhood Mom master peice animation
define gula = Character("Gula", color="#29AFD6") # god

#some side character Name
define teacher = Character("Teacher", color="#29AFD6") # crush
define mankitsu_prog = Character("Keiichi Oyamada", color="#29AFD6")
define lost_child = Character(" ", color="#29AFD6")
define worried_parent = Character(" ", color="#29AFD6")

define dc = Character("Dark Crow", color="#29AFD6") # crush
define lingeries_prog = Character("Yusuke Nakonishi", color="#29AFD6")

define mankitsu_apostle = Character("Sloth Apostle", color="#29AFD6") # swordman
define lingeries_apostle = Character("Greed Apostle", color="#29AFD6") # thief

define bibleblack_prog = Character("Taki Minase", color="#29AFD6")
define bibleblack_apostle = Character("Wrath Apostle", color="#29AFD6")
# Kaori Saeki blowjob end of EP1.
# Imari, Kurumi main heroine
# Minase, Yukiko step sister
# Reika Kitami main boss
# Hiroko Takashiro pink hair teacher
# Rika Shiraki The head of the student council. Wealthy and untouchable, she’s very popular among the boys. She also has a crush on Minase.

define charm_mother_prog = Character("Misako Amamiya", color="#29AFD6")
define charm_mother_apostle = Character("Lust Apostle", color="#29AFD6")

define sarlisa = Character("Sarlisa", color="#29AFD6")
define sarona = Character("Sarona", color="#29AFD6")


# only use switch for case with on/off
# always add new switch to last line to avoid bug.
switch sw_unused001 = 1
switch change_clothe = 1

switch RPGmorning = 1
switch RPGmidday = 1
switch RPGevening = 1
switch RPGnight = 1
switch RPGmidnight = 1

switch introduction_firstday = 1

# # Arc 1
# # searching
switch is_prog_follow = 1
switch is_prog_not_follow = 1
# # battle
# switch bible_black_trigger = 1
# # answer
# switch discipline_trigger = 1
# # trading
# switch makichan_to_nau_trigger = 1
# # forge
# switch taboo_charm_mother_trigger = 1

# # main story trigger
# switch meet_mystery_dark_crow = 1
# switch after_meet_dark_crow = 1

# # Arc 2
# switch manage_twin_trigger = 1
# switch shion_trigger = 1
# switch lingerie_trigger = 1

# quest category: 
# searching (item|people|animal|book....), battle (tournament|gang), answer_question, forging, solve the mystery....
# reward random money|item|weapon...

# switch 1 = OFF | 0 = ON
    label init:
        setswitch RPGmorning   = 0
        setswitch RPGmidday    = 1
        setswitch RPGevening   = 1
        setswitch RPGnight     = 1
        setswitch RPGmidnight  = 1
        # setswitch sw_unused001 = 1
        setswitch change_clothe = 1
        setswitch introduction_firstday = 0

        # active by default to show the prog of side quest.


        # trigger for all to check if any follower.
        setswitch is_prog_follow = 1
        setswitch is_prog_not_follow = 0

        # morning => event|breakfast|shower|wakeup|quest...
        # midday => lunch|quest|....
        # evening => time go home|dinner|tivi|shower|quest...
        # night => evil time.
        # midnight => really evil time.
        $ RPGtime = 1

        # BEFORE
        # $ RPGday  = 1
        # $ RPGweek = 1 
        # $ RPGyear = 1
        $ unsed001  = 1

        # # week time flow, 1,2,3,4,5,6,7,8..... * day
        $ unsed002 = 1 
        $ unsed003 = 1

        # main story quest process will raise after some condition.;
        $ main_story_current_step = 1

        # academy point will raise after main quest.
        # point decide what rank you will be.
        # after a main story complete the rank will raise.
        # you finish all main story to upgrade to another class.
        $ academy_point = 0

        # $ ugq_seen = ""
        # $ ugq_player_x = 0
        # $ ugq_player_y = 0
        # $ ugq_player_mapID = 0
        # $ user_ugs = 0

        # $ main_story_dark = 0
        # $ main_story_light = 0

        # side quest. DEFINE A MAX QUEST.
        # player could only take 1 quest at 1 time.
        $ side_quest_lost_child_level = 0
        $ side_quest_lost_child_start = 0
        $ side_quest_lost_child_complete = 0
        # switch side_quest_lost_child_start = 0
        # switch side_quest_lost_child_complete = 0
        # setswitch side_quest_lost_child_start = 0
        # setswitch side_quest_lost_child_complete = 0

        $ side_quest_lost_monster_level = 100
        # switch side_quest_lost_monster_start = 1
        # switch side_quest_lost_monster_complete = 1
        # setswitch side_quest_lost_monster_start = 1
        # setswitch side_quest_lost_monster_complete = 1

        $ side_quest_lost_item_level = 100
        # switch side_quest_lost_item_start = 1
        # switch side_quest_lost_item_complete = 1
        # setswitch side_quest_lost_item_start = 1
        # setswitch side_quest_lost_item_complete = 1

        $ side_quest_gang_thug_level = 100
        # switch side_quest_gang_thug_start = 1
        # switch side_quest_gang_thug_complete = 1
        # setswitch side_quest_gang_thug_start = 1
        # setswitch side_quest_gang_thug_complete = 1

        switch after_meet_dark_crow = 1
        setswitch after_meet_dark_crow = 1
        switch user_ugs_trigger = 1
        setswitch user_ugs_trigger = 1

        switch bg_switch = 1
        switch percent10 = 1
        switch percent20 = 1
        switch percent30 = 1
        switch percent40 = 1
        switch percent50 = 1
        switch percent60 = 1
        switch percent70 = 1
        switch percent80 = 1
        switch percent90 = 1
        switch percent5 = 1
        switch percent1 = 1
        switch unused13 = 1
        switch unused14 = 1
        switch unused15 = 1

        # optimize performance for battle win/lose
        $ battle_state = 1

        # optimize performance for if/else with search string. 3 level
        $ rpg_condition1 = 1
        $ rpg_condition2 = 1
        $ rpg_condition3 = 1
        $ rpg_condition4 = 1

        $ apostle_story_char_trigger = 1
        $ guide_light = 1
        $ apostle_party = 1
        $ unused9 = 1
        $ unused10 = 1
        $ unused11 = 1
        $ unused12 = 1
        $ unused13 = 1
        $ unused14 = 1
        $ unused15 = 1

        setswitch apostle_thief = 0
        setswitch apostle_acolyte = 0
        setswitch apostle_swordman = 0
        setswitch apostle_tank = 0
        setswitch apostle_mage = 0
        
        jump disclaimer

    # MAP MUST BE ADD INCREASE.
    label disclaimer
        # support 2 type of video display
        # play movie https://hentaivideoworld.com/get_file/1/ef62be49e5087da96fec16711539ec70/24000/24746/24746_tr.mp4
        
        # play movie https://openload.b-cdn.net/3D/Chinese/Chinese Housewife with Big Boobs_ep2.mp4?token=fnH_1tmLB1zKhLtyPUKCnw&expires=1599714060
        # play movie https://ohentai.org/detail.php?vid=Nzk5

        # play movie https://hentaivideoworld.com/get_file/1/ad868b511eeed9acc9dd4c9679b94229/18000/18017/18017_tr.mp4

        # play movie https://cdn.cloudflare.steamstatic.com/steam/apps/256735165/movie480.webm
        # play movie https://spankbang.com/xewx/video/illusion+hentai+aga+game+part+406
        # play movie http://localhost/html5/hentaihaven/movies_p/bbonly1_opening.mp4
        # play movie https://hentaihaven.com/treasures_haven/movies/meeting.js

        # support 2 type of scene picture
        # scene https://hentaihaven.com/deviant_dungeon/img/pictures/nc004a.js
        # scene https://hentaihaven.com/deviant_dungeon/img/pictures/nc004a.png

        # support 2 type of scene background music
        # play music https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.js
        # play music https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.mp3

        # support 2 type of scene Sound effect / voice
        # play sound https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.js
        # play sound https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.mp3

        # voice https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.js
        # voice https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.mp3

        # support 2 type of actor picture
        # show https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.js
        # show https://nganguyenthi121957.github.io/deviant_dungeon/img/pictures/nc004a.png

        # PLGCOMMAND RPGCheckSwitch 1 2 3
        # PLGCOMMAND RPGCheckVariable var_key value_to_search
        # PLGCOMMAND RPGCheckVariable apostle_story mn1,

        # RPGBATTLE 1 rpg_random
        # RPGBATTLE 2 rpg_random

        # if battle_state == 1:
        #     "WIN"
        # if battle_state == 2:
        #     "LOSE"

        # PLGCOMMAND rpg_search_str unused3 a2, rpg_condition1

        # !== -1 
        # if rpg_condition == 1: 
        #     "1"
        # === -1
        # if rpg_condition == 0:
        #     "0"

        # show screen add_acsension

        # RPGBATTLE 174 rpg_random
        # if battle_state == 1:
        #     RPGJSONDATA [{"code":311,"indent":0,"parameters":[0,1,0,0,99999,false]}]
        #     RPGJSONDATA [{"code":312,"indent":0,"parameters":[0,1,0,0,99999]}]
        #     "Battle after battle..."
        #     gain weapon 33
        #     RPGBATTLE 175 rpg_random
        #     if battle_state == 1:
        #         RPGJSONDATA [{"code":311,"indent":0,"parameters":[0,1,0,0,99999,false]}]
        #         RPGJSONDATA [{"code":312,"indent":0,"parameters":[0,1,0,0,99999]}]
        #         gain weapon 31
        #         "Gain Super Novice Glove."
        #         "And still..."
        #         RPGBATTLE 176 rpg_random
        #         if battle_state == 1:
        #             gain weapon 32
        #             "Gain Super Novice Glove 2."


        # show screen rm_acsension

        # play movie "http://localhost/html5/source_renpy/evil_life/game/animation/FireKeeperc1l1.mp4" loop
        # show movie with fade
        # RPGJSONDATA [{"code":230,"indent":0,"parameters":[240]}]
        # hide movie with fade
        # stop movie


        # play movie "http://localhost/html5/source_renpy/evil_life/game/animation/FireKeeperc1l2.mp4" loop
        # show movie with fade
        # RPGJSONDATA [{"code":230,"indent":0,"parameters":[240]}]
        # hide movie with fade
        # stop movie

        # play movie "http://localhost/html5/source_renpy/evil_life/game/animation/FireKeeperc1l3.mp4" loop
        # show movie with fade
        # RPGJSONDATA [{"code":230,"indent":0,"parameters":[240]}]
        # hide movie with fade
        # stop movie

        # play movie "http://localhost/html5/source_renpy/evil_life/game/animation/FireKeeperc1l4.mp4" loop
        # show movie with fade
        # RPGJSONDATA [{"code":230,"indent":0,"parameters":[240]}]
        # hide movie with fade
        # stop movie



        HENTAIHAVENPREMIUM_PURCHASE

        "This is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are either the products of the author's imagination or used in a fictitious manner."
        "Any resemblance to actual persons, living or dead, or actual events is purely coincidental."

        "You could consider to see the video game Walkthrough made by me."
        menu:
          "Open Walkthrough":
            RPGCOMMAND inappbrowserOpen("https://youtu.be/Junfl9EHH4s", "_system")
          "Cancel":
            "You could see the video anytime by tap to the computer after the intro story"
        jump prologue 3 4

    label prologue:
        "Somewhere in the desert, there a war..."
        "TUTORIAL !!!<br>Use guard will half the damage and heal ~10% of your max HP<br>Enemy contain background of 2-5 step.<br>"
        "There are total 10 elements".
        "Neutral - Basic Elemental Property."
        "Water - Opposite of the Wind property. Water does the most damage to Fire property monsters/armors, and is weakest to the Wind property."
        "Earth - Earth is damaged most by the Fire property, and does the most damage to the Wind property."
        "Fire - Fire is the opposite of Earth, and does the most damage against it. Water does the most damage to Fire property."
        "Wind - Wind is weak to Earth, and does extra damage to the Water property."
        "Poison - Poison Property should not be confused with the Status Effect."
        "Holy - The Holy element is weak against the Shadow element, and does extra damage against the Shadow element."
        "Shadow - not to be confused with the Demon and Undead types. Shadow is the opposite of Holy, and does the most damage against it."
        "Ghost - Ghost is only weak to the Ghost element."
        "Undead - Undead elemental only fear Holy."
        "Use Equip Command at the end to change your weapon to match element of enemy to deal more dmg."

        show screen add_acsension

        RPGBATTLE 174 rpg_random
        if battle_state == 1:
            RPGJSONDATA [{"code":311,"indent":0,"parameters":[0,1,0,0,99999,false]}]
            RPGJSONDATA [{"code":312,"indent":0,"parameters":[0,1,0,0,99999]}]
            "Battle after battle..."
            gain weapon 33
            RPGBATTLE 175 rpg_random
            if battle_state == 1:
                RPGJSONDATA [{"code":311,"indent":0,"parameters":[0,1,0,0,99999,false]}]
                RPGJSONDATA [{"code":312,"indent":0,"parameters":[0,1,0,0,99999]}]
                gain weapon 31
                "Gain Super Novice Glove."
                "And still..."
                RPGBATTLE 176 rpg_random
                if battle_state == 1:
                    gain weapon 32
                    "Gain Super Novice Glove 2."

        show screen rm_acsension

        play music "theme1.ogg"
        play sound "slash1.ogg"

        RPGJSONDATA [{"code":212,"indent":0,"parameters":[0,110,true]}]

        "Puhak!"
        "Blood splattered everywhere. A man's dazed gaze fell on the spear impaling his left chest."
        "When he felt the coldness of the blade penetrating his heart, his pupils shook as his body slowly lost strength."
        "As darkness set in the man’s eyes, his weakened eyes looked forward. When he opened his mouth, he spurted out bits and pieces of his organs along with a mouthful of blood. His voice seemed to be lost, as only the sound of wind passing through his vocal cord came out."
        show gula_1
        gula "[Amazing.]"
        "In front of the corpse was a large darkness that couldn’t be described with words."
        gula "[Truly amazing! I did not place much hope, but to think you actually survived this bloody battle...]"
        gula "[I want to praise your achievements a bit more, but you do not have much time left.]"
        gula "[Since you kept your promise, it is time for me to keep mine. Tell me, what is it that you wish?]"
        "As darkness set in the man’s eyes, his weakened eyes looked forward. When he opened his mouth, he spurted out bits and pieces of his organs along with a mouthful of blood. His voice seemed to be lost, as only the sound of wind passing through his vocal cord came out."
        gula "[You do not have to speak. I can simply read your mind… So, you wish to be revived?]"
        gula "[No? How foolish, your life is hanging by a rope. Then what is it that you want? Don’t tell me, riches? Honor? In this situation?]"
        "{color=#aaa}Man{/color}<br>..."
        gula "[What?]"
        "Suddenly, the tone of the darkness went up."
        gula "[You want to start over?]"
        gula "[Impossible!]"
        "An enraged voice shook the earth."
        gula "[Even with your achievements, how could it be possible to reverse time!? You wanted to return everything to the way it was with only what you’ve accomplished?]"
        "{color=#aaa}Man{/color}<br>..."
        gula "[Impudent! Perhaps if you accomplish today’s feats dozens of times more, but in the current state, I cannot grant your wish. Nevermind your soul, not even a single piece of your body can be sent back!]"
        "{color=#aaa}Man{/color}<br>..."
        gula "[How persistent! Given that your life is about to end and the feats you have accomplished until now, I shall restrain myself. Tell me another wish.]"
        "Then, a heavy silence descended."
        gula "[…Why did you make such a wish?]"
        "Was the darkness moved by the pitiful sight of the man dropping his head?"
        gula "[Child, hurry and wish for your revival. If that is truly your wish, you can ask again in the future after you’ve accomplished more feats. Though, I can’t say that it will be possible.]"
        "The man’s shoulders jumped ever so slightly. He seemed to be cackling. It was already a miracle just to have survived this battle. But he had to accomplish feats equaling dozens of what he accomplished already?"
        "The man, and the owner of the voice all knew it was impossible."
        "The man raised his head just barely."
        "His mouth moved slightly."
        gula "[Your memories?]"
        "{color=#aaa}Man{/color}<br>...."
        gula "[You want your current feelings to…]"
        "....."
        gula "[Since you can’t send back your body or soul, you want to send back the feelings you felt here?]"
        "The darkness seemed to be taken aback, as silence descended once again."
        gula "[…Sending back feelings based on memories..... Certainly, feelings are only thoughts of your emotions.]"
        gula "[But why?]"
        gula "[Only your feelings of yearning and regret… Even those would not be etched into your mind and only pass by like a fleeting dream.]"
        gula "[You might end up treating it like an insignificant dream and forget all about it.]"
        "After a long silence, the voice answered."
        gula "[In that case, fine.]"
        "Finally, the wish had been decided."
        "He could feel something like a pair of wings spread open from the darkness."
        gula "[Come closer, my child.]"

        hide gula_

        RPGJSONDATA [{"code":212,"indent":0,"parameters":[0,117,true]}]

        "Suddenly, his body turned light like a feather. By the time he noticed this, his vision had become half-blurry."
        "The world spun, and something unknown came up to her eyes."
        "The last thing he got to see was…"

        show gula_1
        gula "[I cannot wait—]"

        hide gula_
        "…a dark fragment rising above the man…"
        play sound "darkness1.ogg"

        RPGJSONDATA [{"code":212,"indent":0,"parameters":[0,101,true]}]

        show gula_1
        gula "[Until I meet you again.]"
        "And the darkness laughing in joy."
        jump bedroom 4 7

    label kitchen:

        returnRPG

    # auto run event.
    label bedroom:
        if main_story_current_step == 1:
            RPGJSONDATA [{"code":322,"indent":0,"parameters":[1,"hiiro boxer",0,"test",7,"hiiro"]}]
            setswitch change_clothe = 1

            "???<br>.........<br>That dream.....what it about ?....sigh...."
            renpy.input("What's your name?") 

            p "I better get prepared for academy."

            $ main_story_current_step = 2
            "Change clothes in closet and go to academy."

            "NEW QUEST ADD !!!"
            PLGCOMMAND Quest add 1
            menu:
              "Open":
                PLGCOMMAND Quest Journal Open To 1
              "Cancel":
                "You could open Quest menu and see the quest later."

        eraseEvent
        returnRPG

    # open door.
    label bedroom 2 0:
        if switch change_clothe:
            jump corridor 15 5
            returnRPG
        "You need to change clothes first"
        returnRPG

    # change clothes
    label bedroom 3 0:
        # current = 0 uniform | =1 boxer
        if switch change_clothe:
            # current == 0 => =1
            "You change to boxer."
            RPGJSONDATA [{"code":322,"indent":0,"parameters":[1,"hiiro boxer",0,"test",7,"hiiro"]}]
            setswitch change_clothe = 1
            returnRPG
        # current == 1 => =0
        "You change to uniform."
        RPGJSONDATA [{"code":322,"indent":0,"parameters":[1,"hero1",0,"hiro",0,"hiiro"]}]
        
        setswitch change_clothe = 0
        returnRPG

    # your bed.
    label bedroom 4 0:
        # "..."
        returnRPG

    label bedroom 5 0:
        # only pass time after tutorial completed.
        if guide_light < 13:
            "You need to completed tutorial!!!."
            returnRPG
        show screen timepass

        if switch RPGmorning:
         if switch after_meet_dark_crow:
          if main_story_current_step >= 2:
            if main_story_current_step < 4:
                scene black
                "OBJECTIVE COMPLETED !!!"
                PLGCOMMAND Quest 4 Complete Objective 2
                PLGCOMMAND Quest 4 Claim Reward 2
                PLGCOMMAND Quest 4 Change Description Entry To 3
                show gula_1
                gula "My child. Get Stronger !!!"
                gula "Darkness are coming !!!"
                "........."
                p "...Who are you? Why?"
                gula "I could not explain right now."
                gula "There not much time left."
                gula "This is all i could give you to help you at this moment."
                gula "I hope you luck."
                hide gula_
                p "... Wa...i...t"
                gain weapon 11
                gain armor 10
                gain armor 11
                gain armor 12
                gain armor 13
                gain armor 14
                gain armor 15
                "You received super novice equipments"
                $ main_story_current_step = 4
                hide prev scene
                hide prev scene

        if switch RPGmorning:
            if guide_light == 14:
                $ guide_light = 15
                "TUTORIAL COMPLETED !!!"
                "From here onward there will be no guide light indicator."
                "YOU must look for right spot to continue the story."
                PLGCOMMAND Quest 1 Complete Objective 5
                PLGCOMMAND Quest 1 Claim Reward 5
                PLGCOMMAND Quest Set Completed 1
                PLGCOMMAND Quest add 4, 5
                "New TUTORIAL QUEST ADDED !!!"
                "Do you want to open ?"
                menu:
                  "Open":
                    PLGCOMMAND Quest Journal Open To 5
                  "Cancel":
                    "You could open Quest menu and see the quest later."

        returnRPG

    # computer
    label bedroom 6 0:
        # PLGCOMMAND enable_picture_ft : 1-999
        # PLGCOMMAND enable_picture : 2
        show screen show_stats
        returnRPG

    # DARK CROW.
    label bedroom 7 0:
        if main_story_current_step == 11:
            p "What should we do now ?"
            dc "We need to find out information about my friends."
            dc "And we should find if there any parasian inside the academy too."
            p "That hard. And no clue too."
            dc "Just go around the academy to see if anything wierd happen."
            returnRPG
        if main_story_current_step == 7:
            p "What should we do now ?"
            dc "I could not believe that academy belong to parasite queen."
            dc "No wonder that lunch pack could help normal human like you contain divinity."
            dc "We need that recipe if we want to go on with our plan."
            dc "Just wait and see what the parasite queen want."
            dc "Let take a rest. And meet parasite queen tomorrow."
            $ main_story_current_step = 8
            returnRPG
        if main_story_current_step == 5:
            "You should investigate the academy."
            "Your lunch pack contain some strange magic inside."
            "Let ask the caferia girl who sell the lunch pack."
            "Maybe we could find information about my comrade along the way."
            returnRPG
        if main_story_current_step == 4:
            dc "How do you feel?<br>Did you had a good rest."
            p "Yeah. I'm good for now."
            dc "Then what do you want to know ?"
            menu:
              "Who are you?":
                dc "I'm an reincarnation of god."
                dc "I was [Gluttony] one of seven deadly sins."
              "What happened to you?":
                dc "Long ago there a war between our deadly sins with parasite queen."
                dc "Darkness looming all over the world"
                dc "After an endless battle, the parasite queen decide to use her bloody art."
                dc "And we all along together use our secret art too.<br>After that here i am. That all i know."
                dc "But i could say if i'm here then all my friends or even parasite queen too."
                dc "If the parasite queen regain body and full power she will turn all the human here become parasite."
              "What should we do?":
                dc "To prevent that i must hurry to find my friends."
                p "You could help me to find my friends.<br>Of course it not free."
                dc "If you help me to find my friends and regain our power"
                dc "I will give you 1 wish."
                p "Really??"

                dc "Of course<br>But there no free lunch in this world, right?"
                p "What i have to do?"

                dc "Firstly i need to regain the power i had before."
                dc "But to do that i need time<br>Maybe about 100 years."

                p "WHA... I will die before you regain your power."
                dc "Well there another way.<br>Do you know that every human being all have desire right?"

                p "...What that?"
                dc "That call Hentai Energy (HE). Every time a human have a high HE and parasite will attach to them."
                dc "They will follow their desire and follow every command of the parasite."
                dc "At that time we will defeat them and kill the parasite and take a away the HE power from them."
                dc "That way will be faster but very dangerous."

              "Where should i look for your friends ?":
                dc "I already found out that my friends currently slumber inside your academy."
                dc "But i don't know exactly location."

              "What happened to my body at that time?":
                dc "That call Ascension.<br>I take over by inject divinity to your body."
                dc "But that will give a huge rejection on your body because human is a weak creature."
                dc "They could not take divinity."
                dc "But i found out your lunch strange. It could help you take divinity and heal your body."
                dc "Maybe we should investigate the academy."
              "Continue Story":
                dc "You should train your body more."
                dc "If this continue you could not hold out for long if i take over your body."
                dc "I'll give you this divinity to help you in the future."

                # add skill.
                RPGJSONDATA [{"code":318,"indent":0,"parameters":[0,1,0,4]}]
                "Learn Skill Double Attack."

                dc "Let look around your academy and see if we could find anything."
                $ main_story_current_step = 5
                PLGCOMMAND Quest 4 Complete Objective 3
                PLGCOMMAND Quest 4 Claim Reward 3
                PLGCOMMAND Quest 4 Change Description Entry To 4

            returnRPG
        if main_story_current_step == 2:
            dc "It's a long day. Let rest and talk tomorrow."
            p "Yeah. That a good idea."
            $ main_story_current_step = 3
            returnRPG

        dc "Go do your job."
        # if lingerie1_level == 84:
        #     "It seems you already completed Lingerie Episode 1 Quest."
        #     "Episode 2 already available."
        #     "Go and talk to the protagonist of the quest at the {color=#aca}Morning{/color}"

        returnRPG

    label bedroom 9 0:
        if RPGCOMMAND jsonUUID['hentaihaven'] && isHentai == 1:
            "Every completed Quest Scenes will show up here."
            menu:
              "Lingerie1 Scenes" lingerie1_level <= 85:
                menu:
                    "Opening":
                        play movie "lingeries1_op_mastur.mp4"
                        play movie "lingeries1_opening_jiz.mp4"
                    "Fingering":
                        play movie "lingeries1_rpe_oral.mp4"
                    "Exam 3p":
                        play movie "lingeries1_3p.mp4"
                    "FULL Last Scene":
                        play movie "lingeries1_last_oral.mp4"
                        play movie "lingeries1_blowjob.mp4"
                        play movie "lingeries1_69.mp4"
                        play movie "lingeries1_fuk1.mp4"
                        play movie "lingeries1_fuk2.mp4"
                    "Cancel":

              "Bibleblack1 Scenes" bibleblack1_level <= 94:
                menu:
                    "Infirmary":
                        play movie "bb1_infirmary_fuk1.mp4"
                    "Boobjob":
                        play movie "bb1_boobjob_all.mp4"
                    "President Store House":
                        play movie "bb1_student_president_fuk.mp4"
                    "Cancel":

              "Charm Mother1 Scenes" charm_mother1_level <= 91:
                menu:
                    "Bathroom alone":
                        play movie "charm_mother1_bathroom1.mp4"
                        play movie "charm_mother1_bathroom2.mp4"
                    "Masturbase 1":
                        play movie "charm_mother1_masturbase1.mp4"
                    "Masturbase 2":
                        play movie "charm_mother1_last_mastur.mp4"
                    "Cancel":

              "Mankitsu Happening1 Scenes" mankitsu_happen_level <= 88:
                menu:
                    "Rei Blowjob":
                        play movie "mankitsu1_rei_blowjob.mp4"
                    "Bookshelf":
                        play movie "mankitsu1_bookshelf.mp4"
                    "Last Fuk Scene":
                        play movie "mankitsu1_last_fuk.mp4"
                    "Masturbase+Boobjob":
                        play movie "mankitsu1_masturbase1.mp4"
                        play movie "mankitsu1_masturbase2.mp4"
                        play movie "mankitsu1_boobjob.mp4"
                    "Cancel":

              "Immorality 1 Scenes" immorality1_level <= 84:
                menu:
                    "Hotel Night 1":
                        play movie "mt1_opening1.mp4"
                        play movie "mt1_opening2.mp4"
                        play movie "mt1_opening3.mp4"
                    "Hotel Night 2":
                        play movie "mt1_hotel2_1.mp4"
                        play movie "mt1_hotel2_2.mp4"
                        play movie "mt1_hotel2_3.mp4"
                        play movie "mt1_hotel2_4.mp4"
                        play movie "mt1_hotel2_5.mp4"
                    "Secret Night 1":
                        play movie "mt1_secret_night_1.mp4"
                        play movie "mt1_secret_night_2.mp4"
                        play movie "mt1_secret_night_3.mp4"
                    "Secret Night 2":
                        play movie "mt1_secret_night2_1.mp4"
                        play movie "mt1_secret_night2_2.mp4"
                        play movie "mt1_secret_night2_3.mp4"
                    "Dark Alley":
                        play movie "mt1_dark_alley_1.mp4"
                        play movie "mt1_dark_alley_2.mp4"
              "Cancel":

            returnRPG
        "GALLERY SCENES PREMIUM ONLY"
        returnRPG

    label bedroom 8 0:
        menu:
          "Reset Lingerie Quest":
            setswitch lingerie1_trigger = 1
            $ lingerie1_level = 100
            $ lingerie1_char_trigger = l1,
          "Reset Mankitsu Happening Quest":
            setswitch mankitsu_happen_trigger = 1
            $ mankitsu_happen_level = 100
            $ mankitsu_happen_char_trigger = mh1,
          "Reset Bible Black Quest":
            setswitch bibleblack1_trigger = 1
            $ bibleblack1_level = 100
            $ bibleblack1_char_trigger = bb1,
          "Reset Charm mother Quest":
            setswitch charm_mother1_trigger = 1
            $ charm_mother1_level = 100
            $ charm_mother1_char_trigger = cm1,
          "Reset Mistreated Bride Quest":
            setswitch mistread_bride1_trigger = 1
            $ mistread_bride1_level = 100
            $ mistread_bride1_char_trigger = mb1,
          "Reset Immorality Quest":
            setswitch immorality1_trigger = 1
            $ immorality1_level = 100
            $ immorality1_char_trigger = im1,
          "Cancel":
            
        "DONE"
        returnRPG

    label corridor:
        # define all screen to prevent new map.
        show screen printtime
        show screen check_lunch
        show screen timepass
        show screen show_stats
        show screen raise_academy_point
        show screen randomUserInfo
        show screen report_menu
        show screen gangs_thugs
        show screen worried_parents
        show screen lost_child
        show screen add_acsension
        show screen rm_acsension
        returnRPG

    # auto run trigger.
    label corridor 7 0:
        if guide_light == 1:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,5]}]
        eraseEvent
        returnRPG

    label corridor 5 0:
        returnRPG

    # corridor stair
    label corridor 8 0:
        if guide_light == 1:
            $ guide_light = 2
            PLGCOMMAND Quest 1 Complete Objective 1
            PLGCOMMAND Quest 1 Claim Reward 1
            PLGCOMMAND Quest 1 Change Description Entry To 2
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,5]}]
        jump house 27 9

    label hitomi_room
        returnRPG
    label kyoko_room
        returnRPG
    label bath_room
        returnRPG

    label house
        if guide_light == 2:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,5]}]
        eraseEvent
        returnRPG

    # EVENT OF LABEL HOUSE
    label house 3 0
        if guide_light == 2:
            $ guide_light = 3
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,5]}]
        jump front_door_town 7 5

    #auto trigger.
    label school1_ground
        # tutorial
        if guide_light == 4:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,7]}]
        # dark crow meet
        if switch RPGmidday:
            if guide_light == 16:
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,4]}]

        if main_story_current_step == 25:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,26]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,10]}]

            "Girl<br>I'm sorry."
            "Girl<br>Asking you to skip class with me."
            "Girl<br>Are you unhappy?"
            "Boy<br>How could i be unhappy."
            "Boy<br>I get to have sex with you."
            "Boy<br>Lately. I been thinking of you all the time."
            "Boy<br>You're one of the top beauties in our academy."
            "Girl<br>Really?"
            "Boy<br>Yeah."
            "Girl<br>Thank you."
            "Boy<br>But why me?<br>There are cooler guy out there."
            "Girl<br>Yes. But i'm not just into looks."
            "Girl<br>Then what kind of person were you looking for?"
            "Girl<br>That's a secret."

            RPGJSONDATA [{"code":212,"indent":0,"parameters":[27,101,true]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,27]}]

            "???<br>Hehe<br>Of course."
            "???<br>You will never know how you will die."
            "???<br>Hahahaha !!!!"
            "???<br>Let get this start right now."

            # show angel1 toilet scene.
            $ main_story_current_step = 26
            play movie "angel_staircase1_1.mp4"
            # play movie "angel_staircase1_2.mp4"
            # play movie "angel_staircase1_3.mp4"
            # play movie "angel_staircase1_4.mp4"
            "???<br>Hehe. Just a little more and it's will completed."
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,26]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,10]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,27]}]
            show screen timepass
            jump school1_Bgrade_class_1 5, 2

        if main_story_current_step == 27:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,28]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,26]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,10]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,27]}]

        eraseEvent
        returnRPG
    label school1_ground 15 0
        eraseEvent
        returnRPG

    # the dot light.
    label school1_ground 28 0
        if main_story_current_step == 27:
            turn_towards -1 33, 21

            play movie "angel_staircase1_2.mp4"

            p "It's him."
            dc "There HE !!!"

            RPGJSONDATA [{"code":212,"indent":0,"parameters":[26,101,true]}]

            avoid_moveto 27 33, 19
            "???<br>That right.You could do nothing at this point."

            dc "Who are you?"

            "Winnessa my name.I am one of four guardian of her highness."
            dc "What are you Parasians planning to do?"

            "Winnessa<br>It's very simple thing.<br>Turn this town people become our food."
            "Winnessa<br>We will control this town in the future."
            "Winnessa<br>And humanity will under her highness rule."

            dc "We will never let that happen."
            "Winnessa<br>Hehe.Just you alone?"
            "Winnessa<br>At this time, my comrade already working on our plan."
            "Winnessa<br>Enough talk<br>I need go to her highness place."
            "Winnessa<br>Come, My minions."

            dc "Prepare for battle."
            RPGBATTLE 161-164 rpg_random
            if battle_state == 2:
                return

            play movie "angel_staircase1_3.mp4"

            RPGBATTLE 161-164 rpg_random
            if battle_state == 2:
                return
            play movie "angel_staircase1_4.mp4"

            "Winnessa<br>Useless minions."
            "Winnessa<br>Well, my work here is done."
            "Winnessa<br>I will finish you myself."
            RPGJSONDATA [{"code":212,"indent":0,"parameters":[-1,103,true]}]

            # assassin LV 10
            RPGBATTLE 50 rpg_random
            if battle_state == 2:
                return

            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,28]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,26]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,10]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,27]}]
            $ main_story_current_step = 28
        setselfswitch A 1
        returnRPG

    # door to base.
    label school1_ground 5 0
        if guide_light == 4:
            $ guide_light = 5
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,7]}]
        jump school1_mainbase 6 8

    # door to base.
    label school1_ground 6 0
        if guide_light == 4:
            $ guide_light = 5
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,7]}]
        jump school1_mainbase 7 8

    # meet the DC
    label school1_ground 4 0
        if hasitem 1:
            setselfswitch A 1
            $ guide_light = 17
            "You eating alone..."
            "And feeling your life really suck."

            "......."
            "While you deep in thinking..."

            "You hear a sound."
            p "Huh ?"

            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,2]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,13]}]

            "???<br>Take this."

            RPGJSONDATA [{"code":212,"indent":0,"parameters":[0,23,true]}]

            "???<br>Hehe. Accept your fate. no use in running."
            "Crow<br>..."
            "???<br>Why struggler even know that you will lose in the end."
            "???<br>Let end this so i could go back."

            "The Crow stare at your direction."
            "Crow<br>This animal body could not hold out any longer."
            "Crow<br>I need to borrow his body.<br>Sorry boy."

            p "What the..."

            # RPGJSONDATA [{"code":212,"indent":0,"parameters":[0,51,true]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,2]}]

            show screen add_acsension
            "Crow<br>This body too could not hold out for long.<br>Let finish this."

            RPGBATTLE 173-176 rpg_random
            if battle_state == 2:
                return
            if battle_state == 1:
                gain weapon 30

            "???<br>Uh.How could a human ...?"
            "???<br>This is not the end."

            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,13]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,2]}]

            show screen rm_acsension

            "Crow<br>I know... but i'll hold out long as long i need."

            p "Aw...!!!"
            "Crow<br>Are you ok boy?"
            
            p "It's hurt !!!"
            
            "Crow<br>It's seem you gonna die soon."
            "Crow<br>Your body could not hold my divinity power and gonna break soon."
            
            p "WHAAA.....!!!Please help me !!!"
            "Crow<br>Sorry. There nothing i could do."
            "Crow<br>Huh!!!<br>That thing."
            p "My lunch....!!!!I could not even finish that !!!"

            "Crow<br>It's seem you could be save now."
            "Crow<br>That lunch contain holy power that could stable my divinity with your body"
            "Crow<br>Now hurry up consume it."

            "Eat your lunch."
            menu:
              "Pack 1" hasitem 1:
                "You eating your lunch"
                remove item 1
                gain hp 100
              "Pack 2" hasitem 2:
                "You eating your lunch"
                remove item 2
                gain hp 200
              "Pack 3" hasitem 3:
                "You eating your lunch"
                remove item 3
                gain hp 400
              "Pack 4" hasitem 4:
                "You eating your lunch"
                remove item 4
                gain hp 800
              "Pack 5" hasitem 5:
                "You eating your lunch"
                remove item 4
                gain hp 2000

            RPGJSONDATA [{"code":212,"indent":0,"parameters":[-1,41,true]}]

            p "WOHH. I'm saved."
            ".....After a long silent."
            p "....Who are you?"
            "Crow<br>I'll explain later.But this could be fate i meet you here."
            "Crow<br>Let be friend from now on."

            "The Crow follow you from now on"
            "The Crow will show up inside your room."
            "You could ask the crow for what to do."

            "It's seem you already skip class"
            "But it late we should go home."

            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,2]}]

            show screen timepass
            setswitch after_meet_dark_crow = 0
            "OBJECTIVE COMPLETED !!!"
            PLGCOMMAND Quest 4 Complete Objective 1
            PLGCOMMAND Quest 4 Claim Reward 1
            PLGCOMMAND Quest 4 Change Description Entry To 2
            returnRPG
        "You need to buy lunch"
        returnRPG

    #auto trigger.
    label school1_mainbase
        if guide_light == 5:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,10]}]
        if guide_light == 9:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,11]}]
        eraseEvent
        returnRPG
    label school1_mainbase 13 0
        eraseEvent
        returnRPG

    #left door.
    label school1_mainbase 2 0
        if guide_light == 5:
            $ guide_light = 6
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,10]}]
        jump left_wing_corridor 5 8

    # right door.
    label school1_mainbase 3 0
        if guide_light == 9:
            $ guide_light = 10
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,11]}]
        jump right_wing_corridor 3 18

    # receptionist
    label school1_mainbase 8 0
        "Hi. WELCOME to HH academy"
        # "What do you want to know ?"
        # menu:
         # "Time System":
         #  "Time will pass after event/quest or rest place"
         #  "There Morning => Midday => Evening => Night => Midnight => Morning again."
         #  "There will be some special event at specific time."
         # "Quest System":
         #  "MAIN QUEST: quest that mainly focus on story. after some story you will upgrade and gain some item,weapon,armor..."
         #  "TUTORIAL QUEST: will show only once. You must completed before doing any other quest."
         #  "SIDE QUEST: auto generation quest, doing this quest to raise your academy point or level up."
         #  "CHARACTER QUEST: quests relate to other NPC story. doing this to raise AC or level up and see H-Scenes."
         #  "CHARACTER QUEST contain some mechanic to work. you need to make the protagonist of the story follow you."
         # "Class Upgrade":
         #  "You could upgrade to another class if you save enough AC/level up"
         #  "You will get more resources like: weapon, item, skill ...."
         # "Town Map":
         #  "There will be many map.<br>I could not tell you all of it.<br>Find out for yourself."
         #  "There will be character quest on many map."
         # "Tournament (WIP)":
         #  "I hope i could build a tournament"
        returnRPG

    # receptionist
    label school1_mainbase 9 0
        "Remember to read Term of service before doing anything."
        menu:
          "Read TOS":
            RPGCOMMAND inappbrowserOpen("https://hentaihavenz.com/policy.txt")
          "Cancel":
        returnRPG

    # helper. will point to you what to do next.
    label school1_mainbase 12 0
        "I will help you in the future."
        returnRPG

    # left wing
    # 1st floor
    label left_wing_corridor
        if guide_light == 6:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,6]}]
        if guide_light == 9:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,2]}]
        eraseEvent
        returnRPG

    label left_wing_corridor 4 0
        if guide_light == 9:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,2]}]
        jump school1_mainbase 1 5

    label left_wing_corridor 3 0
        if guide_light == 6:
            $ guide_light = 7
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,6]}]
        jump school1_Bgrade_corridor 3 18

    label school1_Agrade_corridor
        returnRPG

    label school1_Agrade_class_1
        returnRPG

    label school1_Agrade_class_2
        returnRPG

    label school1_Agrade_class_3
        returnRPG

    label school1_Agrade_president_room
        returnRPG

    # b grade corridor auto run
    label school1_Bgrade_corridor
        if guide_light == 7:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,7]}]
        eraseEvent
        returnRPG
    # door to your class.
    label school1_Bgrade_corridor 4 0
        if guide_light == 7:
            $ guide_light = 8
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,7]}]
        jump school1_Bgrade_class_1 1 2

    # inside your class.
    label school1_Bgrade_class_1
        if main_story_current_step == 20:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,9]}]

        if guide_light == 8:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,3]}]
        if main_story_current_step == 26:
            "Let find the boy.<br>He really take a long time."
            $ main_story_current_step = 27
        eraseEvent
        returnRPG

    # teacher
    label school1_Bgrade_class_1 4 0
        show teacher_1
        teacher "You should study harder for your future."
        teacher "Every student should do that :)"

        if main_story_current_step == 21:
            # morning.
            p "Teacher, Could i ask you something?"
            teacher "Yes, what is it?"
            "....."
            "Boy<br>It's time"
            avoid_moveto 9 1, 2
            
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,9]}]

            "While you talking with your teacher."

            "...."

            # show angel1 toilet scene.
            play movie "angel_toilet1_1.mp4"
            play movie "angel_toilet1_2.mp4"
            play movie "angel_toilet1_3.mp4"

            "After a while."
            p "He took so long."
            dc "Let find him."

            $ main_story_current_step = 22
            show screen timepass
        if main_story_current_step == 24:
            # morning.
            p "Teacher, Could i ask you something?"
            
            teacher "You?<br>I'm happy to see a diligent student like you"
            teacher "Yes, what is it?"
            
            "....."
            
            "Boy<br>It's time"
            avoid_moveto 14 1, 2
            
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,14]}]

            "While you talking with your teacher."

            "...."

            $ main_story_current_step = 25
            jump school1_ground 35, 13
        hide teacher_
        returnRPG

    # your seat
    label school1_Bgrade_class_1 15 0
        # always pass time.
        if guide_light == 8:
            # teacher moving animation.
            show teacher_1
            teacher "Welcome to HH Academy"
            teacher "This will be start of your first year."
            teacher "You guys should take your time to tour around the academy."
            hide teacher_

        if RPGtime < 3:
            show screen timepass

        if guide_light == 8:
            $ guide_light = 9
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,3]}]
            # teacher moving animation.

            p "I should go for lunch."
            p "My allowcent is 50G per day. <br>I could not purchase something too expensive."

            PLGCOMMAND GainGold 50
            PLGCOMMAND Quest 1 Complete Objective 2
            PLGCOMMAND Quest 1 Claim Reward 2
            PLGCOMMAND Quest 1 Change Description Entry To 3

        if switch RPGevening:
            if guide_light == 13:
                $ guide_light = 14
                show teacher_1
                teacher "It's time to go home."
                teacher "Do not wander around and go straight at home."
                teacher "It's dangerous at this late."
                hide teacher_
                "Let go back to your room and sleep."

        returnRPG

    label school1_Bgrade_class_1 9 0
        if main_story_current_step > 21:
            "Thank for your help...."
            if main_story_current_step < 24:
                "Our meeting was a successed!!!"
                "But i wonder why she choose me."
                "She was an idol of every boy inside the academy."
                "By the way. My friend over there need help too."
                "Could you help him also."
            returnRPG
        if switch RPGmorning:
            if main_story_current_step == 20:
                # morning.
                p "What's the matter?"

                "Boy<br>An unbelievable thing has just happend!"

                "Boy<br>I got a letter from Mizuho-senpai."
                "Boy<br>She was my crush for many years."
                "Boy<br>I need to go right now."


                "Boy<br>But i need to slip out of class."
                "Please help me."

                dc "Let help him."

                p "OK. What should i do."

                "Boy<br>You could talk to the teacher and distract her."
                "Boy<br>I'll slip out at that moment."

                p "OK. Let talk to the teacher."
                $ main_story_current_step = 21
                returnRPG
        "....."
        returnRPG

    label school1_Bgrade_class_1 14 0
        if switch RPGmorning:
            if main_story_current_step == 23:
                "I heard you help my friend."
                "I need help too."
                "My idol give me a letter to meet her at the staircase of the academy"
                "But i need to skip class."
                "Please help me like you did with my friend."
                p "Ok !"
                dc "Let talk to the teacher."
                $ main_story_current_step = 24
                returnRPG
        "....."
        returnRPG
    # your seat
    # label school1_Bgrade_class_1 15 1
        # if main_story_current_step == 3:
        #     $ main_story_current_step = 4
        #     setswitch introduction_firstday = 1
        #     p "It was 1 year already<br>Time sure fly fast."
        #     p "My parents died long ago,and i was in coma for a year."
        #     p "After i wake up, the world around me seem strange.<br>I could see some strange thing float in the air."
        #     p "I was live with my childhood family.<br>They treat me very good.<br>It's like my real family."
        #     p "I was attending the same academy with my childhood for a year.<br>I'm just a normal lower class student."

        #     p "After i know that i have strange power.I tested and experimented many time over many nights."
        #     p "And i used my power to help everyone around me."
        #     show screen timepass
        #     "You not listening to the class.<br>Time pass and it's lunch time."
        #     teacher "Ok it's lunch time."
        #     p "Ok. I should head to caferia for lunch."
        #     p "My allowcent is 50G per day. <br>I could not purchase something too expensive."
        #     gain gold 50
            
        #     "TUTORIAL<br>Sit at your seat to pass time.<br>There some quest/event only occult at right time."
        #     "TUTORIAL<br>You could go around to help people by doing some side quest."
        #     # "TUTORIAL<br>Talk to the receptionist on the right at school main front desk to ON/OFF user generate story function.<br>You could share your story to the world by NPC"
        #     "TUTORIAL<br>Talk to the receptionist at school main front desk to find out more about the game."
        #     "OBJECTIVE COMPLETED !!!"
        #     PLGCOMMAND Quest 1 Complete Objective 2
        #     PLGCOMMAND Quest 1 Claim Reward 2
        #     PLGCOMMAND Quest 1 Change Description Entry To 3
    #     returnRPG

    label school1_Bgrade_class_2
        returnRPG

    label school1_Bgrade_class_3
        returnRPG

    label school1_Bgrade_president_room
        returnRPG

    # right wing
    label right_wing_corridor
        if guide_light == 10:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,16]}]
        if main_story_current_step == 22:
            # midday.
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,13]}]

            p "A Parasian?"
            dc "What she doing here?"

            avoid_moveto -1 3, 8

            "???<br>...."
            avoid_moveto 13 3, 5

            "???<br>You....?"
            dc "Been a long time.<br>Sarona Parasite Queen's Sister."
            sarona "Yeah.<br>I never think our previous assault had failed."

            dc "So it was because of your group."
            dc "I thought it was parasite queen."

            sarona "She no queen anymore.<br>That betray...."

            dc "What you plan to do in this academy?"

            sarona "....<br>It's not your business..."
            sarona "And you should take my advice, do not messing with our business."
            sarona "Hehe.<br>You could not stop what will coming.<br>It's not matter what you do."

            ""
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,17]}]
            
            dc "???Who that"

            "???<br>......"
            sarona "I see."

            sarona "That all.<br>I busy right now.<br>You could talk with my guards."

            RPGJSONDATA [{"code":212,"indent":0,"parameters":[0,101,false]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,15]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,14]}]

            sarona "See you guys next time<br>If you could defeat my guards."
            sarona "Let go!!!"

            avoid_moveto 13 2, 6 0
            avoid_moveto 14 4, 6

            avoid_moveto 13 2, 7 0
            avoid_moveto 14 4, 7

            avoid_moveto 13 2, 8 0
            avoid_moveto 14 4, 8
            RPGJSONDATA [{"code":212,"indent":0,"parameters":[0,103,true]}]

            RPGBATTLE 165-168 rpg_random
            if battle_state == 2:
                return

            "While you still at the battle...."

            play movie "angel_toilet2_1.mp4"
            play movie "angel_toilet2_2.mp4"
            play movie "angel_toilet2_3.mp4"

            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,15]}]
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,14]}]

            dc "Let go around the academy and find out what parasian plan."
            p "It is late now."
            p "Let go home and rest and continue tomorrow."
            $ main_story_current_step = 23
            show screen timepass
            # evening.
        eraseEvent
        returnRPG

    # cafe door.
    label right_wing_corridor 3 0
        if guide_light == 10:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,16]}]
            $ guide_light = 11
        jump school1_caferia 13 3
    
    label right_wing_corridor 9 0
        jump teacher_corridor 3 18
    
    label school1_infirmary
        returnRPG

    label school1_caferia
        if guide_light == 11:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,5]}]
        eraseEvent
        returnRPG

    label school1_caferia 3 0
        if main_story_current_step == 5:
            "Hmm? What do you want?"
            menu:
              "Who are you?":
                "I'm just an caferian NPC who sell lunch.<br>Why the f*k are you asking?"
              "About the Lunch?":
                "The lunch recipe came from the head master."
                "You should ask her."
                "She usually in her office at evening."
                dc "Well. Let find her."
                p "But where are her office?"
                dc "Let ask around."
                $ main_story_current_step = 6
            returnRPG

        "You could buy as many lunch pack as you want.<br>What do you want to buy?"
        RPGJSONDATA [{"code":302,"indent":0,"parameters":[0,1,0,0,true]},{"code":605,"indent":0,"parameters":[0,2,0,0]},{"code":605,"indent":0,"parameters":[0,3,0,0]},{"code":605,"indent":0,"parameters":[0,4,0,0]},{"code":605,"indent":0,"parameters":[0,5,0,0]}]
        if guide_light == 11:
          if hasitem 1:
            $ guide_light = 12
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,5]}]
            "OBJECTIVE COMPLETED !!!"
            "Go to eating seat (sparker with light) and eat your lunch."
            PLGCOMMAND Quest 1 Complete Objective 3
            PLGCOMMAND Quest 1 Claim Reward 3
            PLGCOMMAND Quest 1 Change Description Entry To 4
        if guide_light == 15:
            "The caferia always crowded at midday"
            "You could find a chair at academy ground and eat there alone."
            "If you want a quite place to eat."
            "GO TO ACADEMY GROUND AND FIND A CHAIR TO EAT."
            $ guide_light = 16
        returnRPG

    # eating seat.
    label school1_caferia 8 0
        show screen check_lunch
        if guide_light == 12:
            # in case pick cancel. the first time.
            if hasitem 1:
                returnRPG

            $ guide_light = 13
            "OBJECTIVE COMPLETED !!!"
            PLGCOMMAND Quest 1 Complete Objective 4
            PLGCOMMAND Quest 1 Claim Reward 4
            PLGCOMMAND Quest 1 Change Description Entry To 5
            "After you eating lunch. You feel your body lighter and stronger."
            "TUTORIAL !!!<br>You will heal some HP after eating lunch<br>So eat lunch to keep your body healthy."
            "What the hell with this lunch."
            "It's time for class, go back to your seat inside your class and attend class."
        returnRPG

    label school1_gym
        returnRPG

    label school1_storehouse
        returnRPG

    label school1_pool
        returnRPG

    label school1_library
        returnRPG

    #     label school1_library 12 0
    #         # if switch RPGevening:
    #         #     "Everytime i feel lonely, i usually come here to read."
    #         #     "To forget about the past."
    #         #     play movie "bbonly1_opening.mp4"
    #         #     returnRPG
    #         "......."
    #         returnRPG

    label school1_wc
        returnRPG

    # 3rd wing teacher area
    label teacher_corridor
        eraseEvent
        returnRPG

    label teacher_corridor 2 0
        if main_story_current_step == 6:
            "This is head master office."
            "Should we come in?"
            "???<br>Come in if you already here..."
            "..."
            "Ok let go inside."
        jump inside_mystery_club 6 12

    label teacher_corridor 3 0
        jump teacher_working_room 17 13

    label teacher_wc
        returnRPG

    label headmaster_room
        returnRPG

    label teacher_working_room
        eraseEvent
        returnRPG

    label teacher_working_room 14 0
        jump teacher_corridor 1 8

    label front_door_town
        eraseEvent
        returnRPG
    #auto trigger.
    label front_door_town
        #dot 3
        if guide_light == 3:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,3]}]
        eraseEvent
        returnRPG

    # to school.
    label front_door_town 5 0
        if guide_light == 3:
            RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",1,3]}]
            $ guide_light = 4
        jump school1_ground 19 32

    label road_to_school_ground
        returnRPG

    label road_to_city_center
        returnRPG

    label town_city_center
        returnRPG

    label road_to_shopping_center
        returnRPG

    label town_shopping_center
        returnRPG

    label road_to_black_market
        returnRPG

    label town_black_market
        returnRPG

    label road_to_park
        returnRPG

    label town_park

        returnRPG

    label road_to_forest
        returnRPG

    label town_forest
        returnRPG

    label road_to_business_district
        returnRPG

    label town_business_district
        returnRPG


    label road_to_labor_seaport
        returnRPG

    label town_labor_seaport
        returnRPG

    label road_to_hospital
        returnRPG

    label town_hospital
        returnRPG

    label road_to_book_shop
        returnRPG

    label town_book_shop_base

        returnRPG

    label town_book_shop_corridor
        returnRPG

    label user_generate_quest
     
     returnRPG

    label school_year3_ground
     
     returnRPG

    label town_grocery_shop
     
        returnRPG

    label lingerie_company_f1
     
        returnRPG

    label lingerie_company_f2a
     
        returnRPG

    label lingerie_company_f3a
     
        returnRPG

    label lingerie_company_f2b
     
        returnRPG

    label lingerie_company_f3b
     
        returnRPG

    label lingerie_company_f2_corridor
     
        returnRPG

    label lingerie_company_f3_corridor
     
        returnRPG

    label lingerie_company_roof_terrace
     
        returnRPG

    label club_corridor

        returnRPG

    label inside_mystery_club
        if apostle_party < 0:
            $ apostle_party = 0
        if main_story_current_step >= 8:
            if switch apostle_acolyte:
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,5]}]
            if switch apostle_acolyte: OFF
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["B",0,5]}]
            if switch apostle_swordman:
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,6]}]
            if switch apostle_swordman: OFF
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["B",0,6]}]
            if switch apostle_thief:
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,7]}]
            if switch apostle_thief: OFF
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["B",0,7]}]
            if switch apostle_tank:
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["A",0,8]}]
            if switch apostle_tank: OFF
                RPGJSONDATA [{"code":123,"indent":0,"parameters":["B",0,8]}]
        if main_story_current_step == 6:
            avoid_moveto 2 6, 9
            "{color=#acacac}???{/color}<br>Hehe. Took you long enought to come here."
            dc "Yo..u !!!"

            "{color=#acacac}???{/color}<br>Regconize me ?"
            "...."
            dc "No..."
            "....<br>....<br>...."

            "{color=#acacac}???{/color}<br>It's been a long time and you seem missing some memory."
            "{color=#acacac}???{/color}<br>Let me remind you."

            dc "STRONG HE DETECT !!!"
            dc "Prepare for battle."
            dc "You ARE NOT her opponent<br>We must perform acsension."
            p "But if i don't eat lunch pack, i will die and i don't have any right now."

            dc "You will die in her hand if you don't use acsension."

            p "...<br>Fine. Let do it."

            "{color=#acacac}???{/color}<br>Ok. Enough chit chat.Let get into action."

            show screen add_acsension

            # lord knight rank 4 lv 10.
            RPGBATTLE 140 rpg_random
            # if battle_state == 1:
            #     # win
            #     "{color=#acacac}???{/color}I can't believe i losed."
            #     "{color=#acacac}???{/color}Seem like your compatible with this human are surprisingly well."
            #     # add head master to see h scene later.

            # if battle_state == 2:
            #     # lose
            #     "{color=#acacac}???{/color}Hehe. You still had much to learn."

            dc "This skills !!!"
            dc "You ... are Sarlisa Parasite Queen."

            sarlisa "Bingo. But no prize."

            dc "Why are you here?"

            sarlisa "Should you care for that? or for the young man with you right now?"
            sarlisa "It's seem your time is up."

            dc "NO !!!"
            show screen rm_acsension
            p "..Argh!!!"
            dc "Please... Help him !"

            sarlisa "I could help him.But you know you must help me for 1 thing."

            dc "....<br>Fine. Just save him!"

            "Parasite Queen gave you lunch pack."
            "You recover from dark crow inject divinity to your body."

            p "Few... I'm saved !!! Thank"

            dc "So. What do you want me to do?"

            sarlisa "Well. It's late now! Just go home and rest.<br>Let talk again tomorrow."

            "Let stop here for now."
            dc "Let go back."
            p "Yeah!."

            $ main_story_current_step = 7
        eraseEvent
        returnRPG

    label inside_mystery_club 4 0

        returnRPG

    # acolyte
    label inside_mystery_club 5 0
        if apostle_party < 1:
            $ apostle_party = 1
        if apostle_party > 3:
            "PARTY FULL !!!"
            returnRPG
        if apostle_party > 1:
          if academy_point < 1:
            "NOT ENOUGH Academy Point (AP)"
            returnRPG

        RPGJSONDATA [{"code":129,"indent":0,"parameters":[23,0,false]}]
        setselfswitch A 1
        setselfswitch B 0
        setswitch apostle_acolyte = 1
        $ apostle_party += 1
        if academy_point > 0:
          $ academy_point -= 1
          "AP - 1"
        returnRPG
    label inside_mystery_club 5 1
        RPGJSONDATA [{"code":129,"indent":0,"parameters":[23,1,false]}]
        setselfswitch B 1
        setselfswitch A 0
        setswitch apostle_acolyte = 0
        $ apostle_party -= 1
        returnRPG
    # swordman
    label inside_mystery_club 6 0
        if apostle_party < 1:
            $ apostle_party = 1
        if apostle_party > 3:
            "PARTY FULL !!!"
            returnRPG
        if apostle_party > 1:
          if academy_point < 1:
            "NOT ENOUGH Academy Point (AP)"
            returnRPG

        RPGJSONDATA [{"code":129,"indent":0,"parameters":[22,0,false]}]
        setselfswitch A 1
        setselfswitch B 0
        setswitch apostle_swordman = 1
        $ apostle_party += 1
        if academy_point > 0:
          $ academy_point -= 1
          "AP - 1"
        returnRPG
    label inside_mystery_club 6 1
        RPGJSONDATA [{"code":129,"indent":0,"parameters":[22,1,false]}]
        setselfswitch B 1
        setselfswitch A 0
        setswitch apostle_swordman = 0
        $ apostle_party -= 1
        returnRPG
    # thief
    label inside_mystery_club 7 0
        if apostle_party < 1:
            $ apostle_party = 1
        if apostle_party > 3:
            "PARTY FULL !!!"
            returnRPG
        if apostle_party > 1:
          if academy_point < 1:
            "NOT ENOUGH Academy Point (AP)"
            returnRPG

        RPGJSONDATA [{"code":129,"indent":0,"parameters":[20,0,false]}]
        setselfswitch A 1
        setselfswitch B 0
        setswitch apostle_thief = 1
        $ apostle_party += 1
        if academy_point > 0:
          $ academy_point -= 1
          "AP - 1"
        returnRPG
    label inside_mystery_club 7 1
        RPGJSONDATA [{"code":129,"indent":0,"parameters":[20,1,false]}]
        setselfswitch B 1
        setselfswitch A 0
        setswitch apostle_thief = 0
        $ apostle_party -= 1
        returnRPG
    # tank
    label inside_mystery_club 8 0
        if apostle_party < 1:
            $ apostle_party = 1
        if apostle_party > 3:
            "PARTY FULL !!!"
            returnRPG
        if apostle_party > 1:
          if academy_point < 1:
            "NOT ENOUGH Academy Point (AP)"
            returnRPG

        RPGJSONDATA [{"code":129,"indent":0,"parameters":[21,0,false]}]
        setselfswitch A 1
        setselfswitch B 0
        setswitch apostle_tank = 1
        $ apostle_party += 1
        if academy_point > 0:
          $ academy_point -= 1
          "AP - 1"
        returnRPG
    label inside_mystery_club 8 1
        RPGJSONDATA [{"code":129,"indent":0,"parameters":[21,1,false]}]
        setselfswitch B 1
        setselfswitch A 0
        setswitch apostle_tank = 0
        $ apostle_party -= 1
        returnRPG

    label inside_mystery_club 3 0

        jump teacher_corridor 3 1

    # queen
    label inside_mystery_club 2 0
        if main_story_current_step == 19:
            sarlisa "You see an parasian?"
            sarlisa "It's hard to say that my sister."
            sarlisa "But they might up to something."
            sarlisa "Suddenly go around and cause problem like that."
            sarlisa "I afraid there will be many case like this inside academy soon."
            dc "That could happen."
            p "....."
            sarlisa "Well. I hope you could help me along with this academy."
            p "...."
            
            sarlisa "Please look for and help any student involve in this."
            sarlisa "I'll find out what parasians scheming."

            $ main_story_current_step = 20
        if main_story_current_step == 11:
            "Becareful."
            "I'll help you with alchemical in the future."
            returnRPG
        if main_story_current_step == 10:
            sarlisa "I have a favor to ask."
            sarlisa "It seems many parasians inside this academy have follow my sister in secret."
            sarlisa "But i don't know which one."
            sarlisa "If you could help me to check out the academy and find out who follow my sister"
            sarlisa "And i hope you could defeat them and bring their HE to me."
            sarlisa "In exchange i could help you with other things."
            sarlisa "But i need time to prepare all things i need."
            sarlisa "You could just go and do the thing i ask."
            
            PLGCOMMAND Quest 4 Complete Objective 5
            PLGCOMMAND Quest 4 Claim Reward 5
            
            PLGCOMMAND Quest 4 Show Objective 6
            PLGCOMMAND Quest 4 Show Reward 6
            PLGCOMMAND Quest 4 Change Description Entry To 6

            $ main_story_current_step = 11
            returnRPG
        if main_story_current_step == 9:
            sarlisa "What do you want?"
            menu:
              "Alchemis":
                "After so many experimented, i finally produce some item with huge successed."
                "Example like the lunch box."
                "I will provide you many thing in the future."
              "Girls":
                "The girls were human and my discipline for a long time."
                "Their combat power could help you."
                "How?"
                "You could party up to 3 girls."
                "The first girl will free"
                "After that you must pay for Academy Point (AP)"
                "How to earn AP that for you figure out."
              "Continue":
                "So what should i do now?"
                "You need to stop my sister and her follower."
                "They want to disturb the normal life of human in this towns."
                "Or turn more human into parasian to build an army."
                "Just going around the town and see if anything happen."
                $ main_story_current_step = 10
            returnRPG
        if main_story_current_step == 8:
            sarlisa "You Back !"
            sarlisa "Did you have a good rest?"
            dc "Just go to the main business."
            sarlisa "Why so fast?"
            sarlisa "Just hear me out."

            sarlisa "After our battle.Like you i arrived here without power."
            sarlisa "At first i still want to dominate this planet."
            sarlisa "But after a long time study and live with human."
            sarlisa "I changed my mind.<br>I learn to love Alchemis."
            sarlisa "And the result is the lunch box like you eat."
            sarlisa "I still want to experimenting many thing more."
            sarlisa "I WANT TO BE FREE from the burden of queen position."

            sarlisa "But many another parasian not think like me."
            sarlisa "Especially my sister, her desire to dominating this planet maybe stronger than me before."
            sarlisa "And many parasians already follow her."

            sarlisa "I hope we could take hand to prevent this to happen."

            sarlisa "I'm sure this will good for you too."
            sarlisa "Because you need the lunch recipe, right?"

            dc "Yes, You realize."

            sarlisa "I could only provide you lunch pack not the recipe."
            sarlisa "In addition i could provide many other support"

            dc "Like what?"

            sarlisa "Do you see girls there?"

            sarlisa "They my discipline"
            sarlisa "I train them everyday for a long time."

            sarlisa "They could help you in your battle."
            sarlisa "But you need to ask them for help."
            sarlisa "I do not control them."

            dc "Seem like it."

            sarlisa "Well. That all."
            sarlisa "If you have any question just ask me."
            
            "OBJECTIVE COMPLETED !!!"
            PLGCOMMAND Quest 4 Complete Objective 4
            PLGCOMMAND Quest 4 Claim Reward 4
            PLGCOMMAND Quest 4 Change Description Entry To 5

            $ main_story_current_step = 9
            returnRPG
        "...."
        returnRPG


    label premium_game_portal
     
     returnRPG

    label mistread_bride_house
     
     returnRPG

    label charming_mother_house
     
     returnRPG

    label park_wc
        returnRPG

    label prologue2
        returnRPG

    # gen for waifu random battle. id 75 WE SHOULD DO IT MANUALLY
    # everytime we edit this map we need to do.
    # edit enemies id to 9999123
    # copy map 75 => mapugq76. => upload to online.
    label waifu_battle_random
        "RANDOM WAIFU BATTLE"
        RPGBATTLE 9999
        if battle_state == 1:
            # win
            show screen raise_academy_point
            # maybe unlock some hentai video somewhere.

        stop music
        stop sound
        menu:
          "Continue":
            # RPGCOMMAND actionUCG(76, "disscusion_add_viewed")
            "You will transfer back to previous map."
          "Comment":
            # RPGCOMMAND actionUCG(76, "disscusion_add_viewed")
            RPGCOMMAND inappbrowserOpen("https://hentaihavenz.com/public/d/76-random-waifu-battle", "_system")
          "Like":
            RPGCOMMAND actionUCG(76, "disscusion_add_like")
            "LIKED!!"
          "Report":
            "Choose how you want to report this story."
            "Off-topic: This story is not relevant to the current tags and should be change."
            "Inappropriate: This post is offensive, abusive, or violates our community guidelines."
            "Spam: This post is an advertisement or you already heard this story."
            "Error: There error occult inside the story."
            "Snail: Took a long time to load."
            "Dislike: You do not like it."
            "Cancel: If you click here by accident"
            menu:
              "Off-topic":
                RPGCOMMAND actionUCG(76, "disscusion_add_report", 1)
              "Inappropriate":
                RPGCOMMAND actionUCG(76, "disscusion_add_report", 2)
              "Spam":
                RPGCOMMAND actionUCG(76, "disscusion_add_report", 3)
              "Error":
                RPGCOMMAND actionUCG(76, "disscusion_add_report", 4)
              "Snail":
                RPGCOMMAND actionUCG(76, "disscusion_add_report", 5)
              "Dislike":
                RPGCOMMAND actionUCG(76, "disscusion_add_report", 0)
              "Cancel":
                
            "REPORTED!!!"

        RPGJSONDATA [{"code":9999,"indent":0,"parameters":[0,"MAPID","X","Y",0,0]}]

        returnRPG
