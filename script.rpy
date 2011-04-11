# You can place the script of your game in this file.

init python:
    
    show_in_game_menu = True
        
    def in_game_menu():
    
        if show_in_game_menu:
            
            ccinc = renpy.curried_call_in_new_context
            
            ui.hbox(xpos=523, ypos=578)
            ui.imagebutton("ui/ingame_notes_ground.png", "ui/ingame_notes_hot.png", clicked=ccinc("notes_page"))
            ui.imagebutton("ui/ingame_save_ground.png", "ui/ingame_save_hot.png", clicked=ccinc("_game_menu_save"))
            ui.imagebutton("ui/ingame_options_ground.png", "ui/ingame_options_hot.png", clicked=ccinc("_game_menu_preferences"))
            ui.close()
                    
    config.overlay_functions.append(in_game_menu)

init python:
    #style.nametag = Style(style.default)
    style.say_label.font = "resources/scythe.ttf"
    style.say_label.color = "#e8d7c0"
    style.say_label.bold = False
    style.say_label.size = 24

init:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    
    image nerys neutral = "sprites_temp/nerys.png"
    image aislin happy = "sprites_temp/aislin.png"
    image bran neutral = "sprites_temp/bran.png"
    image finn neutral = "sprites_temp/finn.png"
    image karasu neutral = "sprites_temp/karasu.png"
    image andri neutral = "sprites_temp/andraste.png"

    # Declare characters used by this game.
    $ bethany = DynamicCharacter("b_name", show_two_window=True)
    $ madra = DynamicCharacter("mad_name", show_two_window=True)
    $ woman = Character("Woman", show_two_window=True)
    $ shopkeeper = Character ("Shopkeeper", show_two_window=True)
    $ queenmab = DynamicCharacter("m_name", show_two_window=True)
    $ guard = Character("Guard", show_two_window=True)
    $ bran = DynamicCharacter("bran_name", show_two_window=True)
    $ adviser = Character("Adviser", show_two_window=True)
    $ aislin = DynamicCharacter("ais_name", show_two_window=True)
    $ andri = DynamicCharacter("and_name", show_two_window=True)
    $ headchef = DynamicCharacter("chef_name", show_two_window=True)
    $ marta = Character("Marta", show_two_window=True)
    $ librarian = Character("Librarian", show_two_window=True)
    $ u = Character("???", show_two_window=True)
    $ lady = DynamicCharacter("duchess_name", show_two_window=True)
    $ servant1 = Character("First Servant", show_two_window=True)
    $ servant2 = Character("Second Servant", show_two_window=True)
    
    $ man = Character("Man", show_two_window=True)
    
    
    image bg black = "#000"


# The game starts here.
label start:
    $ show_in_game_menu = True
    
    $ b_name = "???"
    $ mad_name = "???"
    $ m_name = "???"
    $ bran_name = "Bran"
    $ ais_name = "???"
    $ and_name = "???"
    $ chef_name = "Chef"
    $ duchess_name = "Lady"
    
    $ beth_mood = "neutral"
    
    $ kitchens_visited = False
    $ kitchens_helped = False
    $ field_visited = False
    $ market_visited = False
    $ border_visited = False
    $ library_visited = False
    $ gallery_visited = False
    $ garden_visited = False
    $ stables_visited = False
    
    $ daycount = 1
    
    $ traits = TraitTracker()
    $ items = Inventory()
    
    $ postaislinch1 = 0
    $ postaislinch2 = 0
    
    $ vinconvo1ext = False
    
    scene bg black
    
    bethany "The last thing I remember is..."
    
    bethany "Nothing."
    
# waking
label waking:
    
    # A GIRL, a blonde maybe in her older teens or maybe early twenties at a stretch, and soaking wet, opens her eyes as she lays on the shore next to a raging underground river. This is BETHANY, although she doesn't know that yet, actually.
    
    bethany "Hrm."
    
    # She closes her eyes, sighs, and then sits up in one swift motion.  Wincing abruptly, she puts a hand to her forehead.
    
    bethany "Ugh, my head."
    
    "Although that shouldn't be a surprise, really.  But anyway--"
    
    bethany "...where am I?"
    
    "I don't recognize this place at all.  Actually..."
    
    "...what {i}do{/i} I remember?"
    
    "Well, for starters, my name is..."
    
    # A brief pause.
    
    "It's..."
    
    # Another pause, as a look of horror dawns on the girl's face.
    
    bethany "Oh, shit."
    
    "Now that I think about it... I don't remember {i}anything{/i}."
    
    "Where I came from, how I got here... not even a favorite color."
    
    "I still, you know, {i}know{/i} stuff--that's a river, this is a rock, etcetera--but any significance it might have held for me once is gone."
    
    # She props her chin up on her hand, and gazes sideways at her reflection in the water beside her.  She looks rather like a drowned rat.
    
    "All right, well, I might not be able to do anything about that right now, but I suppose I can work on drying myself off.  I don't have to be amnesiac and sopping wet."
    
    # The girl sets about squeezing out her clothes.  She's wearing a simple shift dress and a short half-sleeved sweater with patch pockets--the dress is a bit worse for the wear and ragged around the hem, and all of it is pretty much soaked through.
    
    bethany "Suppose this'll dry faster if I take it off to squeeze it out."
    
    # She takes the sweater off to lay it out, and then notices something sticking out of one of the pockets.
    
    bethany "...what's this?"
    
    # It appears to be a piece of paper.  It's pretty well soaked, but one corner of it has managed to stay merely damp.  She unfolds it.
    
    bethany "It's a lucky thing the paper's so heavy, so it hasn't fallen apart--"
    
    # Most of the text is unrecognizable.  All she can make out is the very beginning:
    
    bethany "\"Your name is Bethany Grey.\""
    
    "Is it for me?"
    
    "Then again, it's not like I've got a name at the moment, and Bethany Grey is as good as any.  I can't see any reason why I'd be carrying that around otherwise..."
    
    $ b_name = "Bethany"
    
    bethany "Bethany Grey."
    
    "It feels like a nice fit, actually, now that I've tried it out.  It has a sort of familiar lilt to it.  Maybe it {i}is{/i} my real name."
    
    "...hm."
    
    "I wonder, though.  Why {i}would{/i} I need reminding of my name?"
    
    "I'd sort of assumed that I'd hit my head on accident, or something, which would rather neatly explain how I ended up in a river.  But that suggests something... less coincidental."
    
    # She looks unsettled.
    
    "I doubt I'm going to figure it out sitting around here, though.  And I'd appreciate somewhere with more amenities to work on it, in any case."
    
    # She looks both directions down the tunnel, and her gaze lingers on the upriver end.
    
    "It looks like there's light coming from that direction..."
    
    "Well, there's no harm in taking a bit of a walk and seeing where I end up, is there?"
    
    # She gathers up her things, and heads off upstream, toward the lighter area.
    
    # The source of the light soon becomes apparent--it's not the light of day, nor fire nor electric lamp, but floating motes of light in all colors.  Some are small; some are about the size of Bethany's head.  They bob about near the roof of the cave in little groups, occasionally swooping around.
    
    bethany "Huh.  What are these?"
    
    "I reach my hand out to try to touch one, but it quickly darts away, with a light chirping noise."
    
    bethany "Huh."
    
    "I eye them warily, but they don't seem to be hostile... they're really just hovering.  With one last long look at them, I start moving forward again."
    
    # Soon, though, she realizes she's developed a trail of them bobbing around her head, making whispery noises to each other--although whenever she turns around they scatter with the same chirping noise.
    
    bethany "You know, I almost have to think you things are laughing at me."
    
    # That causes them to chirp even more.
    
    "...I think they're laughing at me."
    
    "But they are lighting the path, so I can't really complain."
    
    # She continues up the tunnel, and farther along vines begin to creep along the walls--just a little, at first, near the ground, but then growing to cover most of the wall in a thick blanket of leaves.  Meanwhile, her odd self-appointed guardians are falling away.
    
    "You know, I thought it was getting lighter in this direction, but now it's actually getting {i}darker{/i}..."
    
    # She brushes a hand against the vine-covered wall, only to draw it away quickly.
    
    bethany "Ow!  What {i}was{/i} that?"
    
    "In the dim light, I can just barely make out that my hand is bleeding from what looks like a number of tiny pinpricks."
    
    bethany "Agh, geez..."
    
    "Just as quickly as they came, though, they heal over, leaving me to wipe off the blood on my skirt."
    
    "...I guess it's not like my clothes aren't pretty much a lost cause anyway."
    
    "It really is beginning to get dark, though... I wonder if I should keep going this direction?"
    
    # She looks back behind her--now there's only one fairy light with her.  The scene has been growing progressively dimmer up to this point.
    
    bethany "Suppose even you things don't want to go that way..."
    
    # The light suddenly bobs up and down and zips ahead, forward into the even darker portion of the tunnel, where the vines grow in a thick covering over the walls and ceiling.
    
    "The light suddenly bobs up and down and zips ahead, forward into the even darker portion of the tunnel, where the vines grow in a thick covering over the walls and ceiling."
    
    bethany "--Hey, wait-"
    
    "I don't know what these things are, but I {i}definitely{/i} know I don't want to be left alone in the dark here.  I break into a dash."
    
    "I'm fast enough, despite the rocky and worryingly slippery terrain, and it doesn't take me too long to catch up--"
    
    # the light winks out.
    
    bethany "Where'd you--"
    
    "...and I stumble out into the dim but natural light of the evening."
    
    bethany "...go?"
    
    "I look back toward the tunnel... cave, I guess, might be more appropriate.  The opening is draped with more of those vines that I saw in the cave--I guess that's why it seemed so dark."
    
    bethany "...so that was it.  I guess this {i}was{/i} the right direction..."
    
    "Although, right direction for what?  I still have no idea where I am."
    
    # She's emerged in a forest of a probably venerable age--the trees reach high and spread wide in a thick canopy.  It's much lighter in comparison to the cave, but they block out a lot of the light from above, leaving sunlight to filter through the leaves.  It's a largely deciduous forest.  It seems to be springtime here.
    
    # If you've played World of Warcraft, it kind of looks like Ashenvale.

    # She's still standing next to the river, which also emerges from the cave.  Here, it's much less roaring; it's more of a brook, really.
    
    "I guess following the river can't hurt.  Don't towns get built next to rivers?  I think I heard that somewhere."
    
    # She starts walking again, following the stream.  It's a much more peaceful, idyllic walk than the one through the cave was, considering that she's now outside in daylight among beautiful scenery.  The forest really is very pretty.

    # The only sound here is the river and the gentle rustling of leaves being jostled by a light breeze.
    
    "I guess this isn't too bad a place to be lost.  It's really very pretty..."
    
    # She smiles lightly.  Readers will note that she doesn't smile much, and almost never smiles widely.  She's not particularly one to express emotions strongly.
    
    # Something then appears to occur to her.  Shift to a more neutral expression.
    
    "There's something about this place..."
    
    "Hm..."
    
    # But she doesn't really get to think about it much more, because she begins to notice the sound of voices.
    
    bethany "Huh?"
    
    bethany "Are those..."
    
    "Voices!  I'm sure that's what they are.  That must mean there's people I can ask for help!"
    
    "I run in the direction of the voices I'm hearing, away from the river, dodging trees, and--"
    
    "I emerge in a large clearing--a clearing filled with what looks like... market stalls?"
    
    "It looks like I've ended up at some kind of farmer's market.  And there are people everywhere."
    
    bethany "Phew."
    
    "Although... now that I take a closer look..."
    
    # Montage of some of the customers and vendors at the market--they're obviously not all human.  They have pointy ears, animal features, are very large or very small, have oddly-colored skin or--in one particular case--the head of a parrot.
    
    "This doesn't look like any kind of farmer's market I know of..."
     
    # And everywhere are the most intriguing wares--amulets, vials of strange liquids, hair combs made of no material she can identify; eyeballs in a jar, impressive-looking feathers, dresses made of starlight.  Etc.
    
    bethany "What..."
    
    woman "I suppose you've never been to a Goblin Market before, dearie?"
    
    "The speaker is the keeper of the stall nearest me--a wizened little woman with wild grey hair.  I realize I've been gaping and close my mouth."
    
    shopkeeper "Don't be shy about taking a look around, love.  Everything's for sale."
    
    bethany "Ah--all right.  Thanks."
    
    shopkeeper "Don't be shy, love!  Come take a look, see if anything strikes your fancy."
    
    bethany "I--"
    
    "My eyes catch on the wares spread across her table.  They're all very different things--there's not really a single uniting theme."
    
    "A leather-bound book, a pretty comb with a delicate engraving; a corsage of perfectly-preserved dried flowers.  A remarkably prettily-colored stone the size of my palm.  A tarnished silver locket on a chain."
    
    shopkeeper "Anything interest you, dear?"
    
    "She seems to have noticed me looking at the locket."
    
    shopkeeper "Oh, that one's quite a steal, if I do say so myself.  It's a rather lovely one.  Romance and passion, and then the distilled essence of heartbreak."
    
    bethany "Pardon?"
    
    shopkeeper "Oh, you know--oh, Milady.  It's lovely to see you again.  Fine day for a market, isn't it?"
    
    lady "Oh... yes, I suppose."
    
    "She's turned to address a new potential customer--I'd say she was the most beautiful woman I'd ever seen, although at this point in time that's really a bit difficult for me to say."
    
    shopkeeper "Got plenty of new amusements this week, Milady, suitable for a discerning customer such as yourself.  Let me know if something catches your eye and I'll pack it right up for you."
    
    "It barely takes her half a second.  She points to the locket."
    
    lady "That one."
    
    shopkeeper "A fine choice, Milady.  Love always has such a nice bouquet... the usual method of payment?"
    
    "She hesitates--but only for the briefest moment, before pulling something out of her pocket."
    
    lady "...This'll do?"
    
    shopkeeper "Beautifully."
    
    "The shopkeeper takes it from her hand, and--"
    
    "It's difficult to describe.  There's almost a feeling of something snapping, like a thread stretched too far."
    
    "Her eyelids flutter, close, and then open again, blearily, as if waking from a dream.  She shakes her head, glances at the locket in her hand, looking briefly confused, and then smiles softly."
    
    "...almost sadly, actually."
    
    "She turns and walks away without a single word."
    
    "The shopkeeper seems to notice my perplexed expression."
    
    shopkeeper "Ah, I didn't think I'd seen you around here before.  I trade in memories, love.  All you need to purchase one of these lovelies is one of your own."
    
    bethany "Ah--"
    
    "I can't imagine selling my memories--although that could be because mine only goes back a few hours.  Although I don't know what would be worth selling something so, well, personal--"
    
    "Something catches my eye."
    
    "I hadn't noticed it before among the clutter.  And I don't know why I would have--a dull green pendant on leather cord, nothing particularly remarkable."
    
    "And yet..."
    
    shopkeeper "D'you want me to wrap that one up for you, dear?"
    
    bethany "Ah--actually, I suppose I'm a bit limited in currency.  I... haven't really got any memories."
    
    "The shopkeeper's mood suddenly shifts."
    
    shopkeeper "If you haven't got anything to buy with, don't take up space for valuable customers, you hear?  I don't tolerate window-shoppers!"
    
    "Something invisible pushes at me with a sudden force backward, causing me to stumble away from the stall, desperately trying not to fall.  I finally manage to gain purchase on something--"
    
    # She turns.  She has, in fact, latched onto the arm of a woman--in fact, the singularly most beautiful woman that could possibly ever exist in a reader's imagination.  She's ethereally beautiful and clad all in white, and wearing a crown.
    
    # Aaaaand she's surrounded by guards.
    
    bethany "Oh bugger."
    
    "And suddenly I have about a zillion very sharp pointy things near my face."
    
    guard "Don't move, cur!  How dare you approach the Queen of Faerie in such a way?"
    
    bethany "...Queen?!"
    
    "I belatedly realize that she was, indeed, wearing a crown."
    
    "...as if I wasn't {i}already{/i} in enough trouble.  It seems today is really, really not my day."
    
    guard "Don't tell me you don't recognize--"
    
    bethany "I--look, I don't even know {i}where{/i} I am, all right, let alone that there's a queen of whatever this place is--"
    
    queenmab "Guards, please stand down and give our guest some space."
    
    "She smiles benevolently.  It's beautiful and mesmerizing."
    
    queenmab "It seems we have a mortal visitor among us."
    
    "She kneels down to my level."
    
    queenmab "This must be very confusing for you, yes?  I'm very sorry about the misunderstanding.  We are usually very hospitable, but I'm afraid my guardians are very zealous about protecting me."
    
    queenmab "What do you call yourself, dear?"
    
    bethany "Um, uh..."
    
    queenmab "\"Um uh?\"  What an interesting sort of name."
    
    bethany "No, uh, ma'am... it's Bethany."
    
    queenmab "Well then... Bethany.  It's a pleasure to welcome you to the land of Faerie."
    
    "...\"Faerie\"?"
    
    queenmab "Might I ask how it was you came to arrive here?  It is so very rare that we receive mortal visitors."
    
    bethany "Well... I'm not really sure, actually.  I just... kind of woke up next to this river, and the only thing I could really remember was my name.  I think I must have hit my head or something..."
    
    "Why didn't I tell her about the piece of paper?"
    
    queenmab "Oh, dear!  That must be terrible.  It is so very easy to get lost in Faerie, and the terrain can be so very treacherous in places."
    
    "Well, for one thing, because it sounds {i}completely crazy{/i}."
    
    queenmab "I do feel rather responsible for not taking the best of care of a guest in my realm, so..."
    
    "That and really it's just a guess, after all.  I mean, I can save my ridiculous conspiracy theories for when I have actual proof..."
    
    queenmab "Alas, we won't be able to return you to the world of mortals for some days--although I suppose it is fortuitous that you should arrive now!  It will only be two weeks, when safe passage becomes available during the midsummer festivities."
    
    bethany "Uh, all right, then..."
    
    queenmab "And of course we will provide you lodging and hospitality in the meantime, as befits a special guest of the Queen.  Bran!"
    
    "She claps her hands, and a man appears at her side."
    
    show bran neutral at right with dissolve
    
    bran "I'll take care of it straight away, Your Majesty."
    
    # Bran's a handsome fellow with white hair tied back into a ponytail; his eyes seem to be shut all the time.  He wears robes that aren't particularly ornate, but are definitely well-made.
    
    queenmab "Bran is one of my most trusted advisors.  If there is anything you desire, let him know, and it will be done."
    
    bethany "...sure?"
    
    "There's almost a tangible feeling of the crowd's attention shifting as it becomes clear that the conversation is done.  Bran takes me by the arm."
    
    bran "Come along, Milady."
    
    menu:
        
        "I'm not really sure I'm a Milady...":
            bethany "Bethany's fine, really.  Milady's a bit formal, isn't it?"
            
            "Bran pauses, turns to me and smiles."
            
            bran "I'll take that into consideration, Milady Bethany."
            
            "...well, I suppose that's progress, anyway."
        
        "Milady?  I quite like that.":
            "I could get used to it, really.  This might not be so bad after all."
            
    "We walk through the market streets; the crowd parts in front of us."
    
    "But as we're leaving, I feel an itch on the back of my neck—almost a tangible feeling of being watched."
    
    "I turn my head and, for a split-second, my eyes meet another's—I catch the briefest glimpse of an angular, bespectacled woman in Queen Mab's party before the crowd swallows her up behind me."
    
    bethany "Who—"
    
    "She was without a doubt the one who was looking at me.  I guess that's not so strange."
    
    "But..."
    
    "It almost felt like..."
    
    "Like she {i}knew{/i} me."
    
    "I don't have much time to think about that, though, as we're pulling out of the market crowds and onto a path heading outward into the woods."
    
    "It's more thickly forested here, the trees stretching high and wide and blocking out all but tiny patches of light from above.  Despite the darkness, though, it still keeps that peaceful, tranquil feeling that the woods by the brook had."
    
    bran "I'm terribly sorry your introduction to our fair land had to occur this way.  I promise it's more pleasant than what you've seen of it so far."
    
    bethany "Well, you've all been so very kind.  So, um, thank you."
    
    bran "It's my pleasure."
    
    "I suppose he wouldn't be a bad person to ask about a thing or two I've been wondering..."
    
    bethany "Say..."
    
    bran "Yes?"
    
    bethany "Well, I was wondering... I... well, Her Majesty said that there was only safe passage back to the mortal world on Midsummer.  How did I get here, then, do you think?"
    
    bran "Oh, well, mortals do occasionally wander in through the thin spaces--you were actually very lucky, managing to arrive so close to civilization.  If you'd ended up in the Wild Lands, I don't know what would have happened to you, but it probably wouldn't have been good!"
    
    "He laughs.  I'm... not really sure what's so funny about it."
    
    bran "In any case, the walls between worlds are somewhat perilous to navigate most of the year.  There are, however, a few days--Midsummer, for instance--when the mortal world and Faerie are closer together than usual, and it's easy to pass between."
    
    bethany "Oh... I see."
    
    "I still don't really understand, but it makes more sense than it did, anyway."
    
    bran "Anything else I can answer for you?"
    
    bethany "Well, there was one thing..."
    
    bran "What was it?"
    
    bethany "It was just... I was kind of wondering about this one person that I saw... back at the marketplace.  She had golden hair and spectacles...?"
    
    bran "Aha, you speak of Lady Nerys, she who Contemplates the Darkness in Austerity."
    
    bran "Ah, here we are!"
    
    "We've arrived at the base of a tree—a giant tree, in fact.  It must be as wide as my height twice over."
    
    "And, from its base and spiraling around its trunk upward, there are steps that form into a set of stairs that look for all the world as if they'd just grown naturally from the tree, like branches."
    
    # Bethany looks up. (Pan up visual.)  Above her, in the tree, is a cottage that, like the steps, looks like it grew naturally from the branches of the tree, although it has glass windows and a thatched roof.  It's a pleasant-looking building, and looks pretty spacious for one person.
    
    bran "We'll just climb the steps, and then we can get you settled in."
    
    "We reach the top of the stairs fairly quickly—actually a lot faster than I expected, given how high up the tree-cottage looked from the ground.  Bran puts a key in the lock and turns it."
    
    "As the door swings open, warm light glows from inside and a fire lights in the petite fireplace set into one wall."
    
    bran "Is it to your liking?  If it's not, we can arrange for other quarters—"
    
    bethany "No, it's... It's really quite fine.  It's lovely, really."
    
    "And, really, I'm just looking forward to getting a bit of a rest.  I'm just realizing now how tired I feel—thinking back, I don't even know how long I was walking in that cave."
    
    bethany "Thank you again." # maybe omit thank-yous if you're choosing the kind of bitchy answers
    
    bran "Let me know if there's anything else I can do for you."
    
    "He gestures to a little bell next to the door."
    
    bran "If you need anything, just ring this to let me know.  I'll be by tomorrow morning to give you the grand tour."
    
    bethany "Oh, all right."
    
    "He turns to leave, but then stops just as he's about to pass through the door."
    
    bran "Oh, and—there's one more thing you should know."
    
    # His expression turns deadly serious.
    
    bran "No matter what you hear outside, or if you hear anything tapping on your windows... don't leave the cottage between sundown and sun-up."
    
    "...do I even want to know why?"
    
    "...yes.  Yes, I do."
    
    bethany "Uh, I'm just curious, really... but, er, why?"
    
    bran "I suppose you {i}are{/i} owed an explanation..."
    
    bran "Not every creature in Faerie is quite as hospitable or as civilized as we are, Lady Bethany.  Things come down from the deep woods at night... things that you would do well not to meet, particularly alone."
    
    bran "They may appear harmless, even... but don't trust in appearances.  Things are not always what they seem."
    
    "He shrugs."
    
    bran "But if you don't leave the cottage during the night, you should be perfectly safe--and you should have no reason to leave."
    
    bran "I'll leave you to your rest, and see you in the morning, then."
    
    "Before I can get another word in edgewise, he turns neatly and steps out the door, leaving me on my own."
    
    "Seriously, what {i}was{/i} that?  Get me settled in here, and {i}then{/i} tell me that this place is probably surrounded by horrible monsters at night, or something?"
    
    "Well, wonderful."
    
    "Despite myself, my gaze strays to the window overlooking my cozy little bed and out toward the deeper woods which, although the sun is barely beginning to set, are already pitch-dark."
    
    "{i}Things come down from the deep woods at night...{/i}"
    
    "It seems even these people... the Fae, I guess... have their own problems.  If {i}they're{/i} worried about whatever these things are..."
    
    "In any case, I can't see any reason why I'd leave this place in the middle of the night.  It's perfectly cozy and warm.  And speaking of warm... I slip off my wet clothes to lay them dry by the fireplace."
    
    "It seems they've left me an impressively wide selection of plain but tasteful clothes, including nightclothes, so I slip on a nightgown and lay myself out by the fire as well to think about the day's events."
    
    "At least I've got a place to sleep and food to eat.  But I can't help but feel slightly disappointed that I still haven't managed to figure out anything about who I am or where I came from."
    
    "Then again... there was that woman, wasn't there, who Bran called Nerys?  Nerys of the ridiculously long title, yes."
    
    "Does she know me from somewhere?  You'd think she'd have said something."
    
    "Then again, maybe I'm just imagining things."
    
    # She sighs, and rolls over on her back to stare up at the ceiling.  It's lit by what appears to be some kind of vine that, rather than flowers, emits globes of light.
    
    "Well, I've got two weeks.  That's long enough to make at least some progress, right?  Or maybe when they return me to wherever I came from it'll jog my memory."
    
    "I yawn."
    
    "I really am tired.  I should probably get into bed and get some rest, since I'm sure tomorrow will be eventful."
    
    # And with that, she climbs into bed and closes her eyes.  As if sensing that she's going to sleep, the lights around the room dim, bringing the brightness down to a pleasingly dark, but not pitch-black level.
    
    # Fade to black.
    
    "I'm standing outside in a forest.  No, I'm running--recklessly, too, crashing through leaves and brush and holding on tightly to something in my hand, something precious--"

    menu:
        "Look back.":
            "I look back.  I'm grasping another hand, pulling another person along--although their face is unfamiliar, in the way that dream-faces are, although I'm sure I know them and know them well."
    
            bethany "Come on, hurry!"
    
            u "I--"
    
            "The ground trembles and shakes and splits open beneath us--I roll out of the way, but my companion is not so lucky.  They dangle over the edge of a seemingly bottomless chasm into the earth."
    
            bethany "H-hold on, I've got you, just hang on--"
    
            u "Bethany--"
    
            "And then the inky darkness swells from the bottom of the pit and covers them and pulls them away from me--"
    
        "Keep running.":
            "There's no time to look back.  I keep running.  I don't know what I'm running from, exactly, but I know it's bad and I know I don't want it to catch me."
    
            "Ahead, I can hear the roaring of a river."
    
            bethany "We're going to make it!"
    
            "We?  I suppose I might be holding another person's arm... No time to think, though.  I make a dash for the river and, in my haste to jump over it, realize I've let go of what I was holding."
    
            bethany "No!"
    
            "I turn around and--"
            
    "I wake up."

    "It takes me a moment to realize I'm breathing heavily, like I've just been running, and that my forehead has broken out in a sweat."
    
    "I lay there for a few minutes, staring at the ceiling.  What was that?"
    
    "I look out the window next to the bed.  It's still nighttime, although it looks like it's starting to move toward morning--the sky has lightened from pitch to a sort of dark reddish-purple."
    
    "Dreams are weird.  Was that supposed to mean something?  You'd think if it was, it could stand to be just a little bit clearer, but maybe that's just me."
    
    "Hm... at this point, is it even worth it to go back to sleep?"
    
    "I still feel tired, though, so I might as well give it a try.  Hopefully I'll have less bizarre dreams..."
    
    "I tuck myself back into bed, and pull the covers up over my head, and try not to think about it."
    
    "I sleep without disturbance the rest of the night, and wake with the faint light of the dawn peeking through the window next to my bed."
    
    "It seems even here through the thick canopy of trees there's some kind of sunlight, at least, even if it is muted."

    "Or is there?  I look a little more closely at the window.  There's a little row of lights there outside, just along the top, that make it look like the sun's come up in an odd sort of way."

    "Well, it's not much to be complaining about, although to be honest I was hoping for a bit of sunshine."
    
    "The sort of seemingly-perpetual twilight here is pretty, but not the most cheerful thing to wake up to.  I guess one gets used to it, although I don't plan to do so."
    
    "*rustle*"
    
    "I start at the noise behind me, and whirl around--but no one's there."

    "But someone has been here--because on the vanity table beneath the mirror has now been placed a tray of really lovely little cakes and a glass of something sweet-smelling."

    "Suddenly I realize I'm very hungry--after all, I didn't eat anything last night, and who knows when the last time I ate before then was?"
    
    menu:
        
        "I wonder if there's still someone here to thank?":
            
            "I look around for someone to thank for a few minutes, but it doesn't seem like whoever left the tray is still here."
            
            "I still feel like I should make an effort, though..."
            
            bethany "Um... thank you?"
            
            "To my surprise, a few titters erupt from somewhere--just outside the window?"
            
            "I turn around and there's no one there, but I get the feeling I've pleased someone."
            
        "It looks delicious, and Bran should be here any minute--I'd better get started.":
            
            pass
    
    "The food is fantastic--it tastes like a little slice of heaven, maybe.  Sweet, light and fluffy.  The drink turns out to be a sort of honeyed, creamy thing that complements the cakes perfectly.  I really wouldn't mind eating this every meal for the rest of my life."

    "I should probably finish up my raptures about the food, though, and concentrate on getting ready for the day--the little clock by the door's hand is moving toward the little mark labeled \"Morn,\" which is when Bran said he'd stop by, and I should probably be dressed by then."

    "The closet--wardrobe, really--is filled with lots of options; nothing particularly fancy, but it's all serviceable and well-appointed."
    
    menu:
        
        "...couldn't they have given me something a {i}little{/i} fancier?":
        
            "Still, this'll have to do for now, I suppose."
            
        "This'll suit me just fine.":
            
            "I'm not sure I'd feel comfortable in some of the flashy clothes that the Fae wear, anyway.  Plus, I'm just grateful to have something to wear other than my clothes from yesterday, which are still a little on the damp and smelly side."
            
    "I pick out an outfit that should work well enough, and pick a pair of shoes from the lowest level.  It's all perfectly my size. (I wonder how they managed that?)"

    "No sooner am I feeling just about ready to go than a knock comes at the door--I can see through the window that it's Bran, ever-cheerful, here to pick me up as promised."

    bran "Did you sleep well, milady?"

    bethany "Well enough, thanks."

    "I still feel a little unsettled from my dream, though..."
    
    menu:
    
        "That's not something I should bother him with, though.":
            "And, really, I'd prefer very much not to talk about it."
            
        "Maybe I should tell him about it...":
        
            bethany "But..."
            
            "I relate my strange dream to him."
            
            "[Something about how mortals in Faerie often have strange dreams brought on by the new scenery, and it's nothing to worry about.]"
            
    bran "Ready to be on our way?"

    bethany "Ready, yes."
    
    bran "Excellent.  I thought we'd stop by the Royal Collections first.  Tell me, Lady Bethany, do you have an interest in art?"
    
    bethany "I... well, I don't really know.  I suppose I'll find out, won't I?"
    
    "He laughs."
    
    bran "I suppose you shall."
    
    "He leads me down the stairs and out toward the path.  I realize now that it's not dark that there are lanterns strung through the trees lining the path.  It makes the dim light a little more cheerful."
    
    "And it seems that things are more lively at this time of day--from somewhere in the distance I can hear upbeat music and the sound of voices."
    
    bethany "What's that?"
    
    bran "Ah!  You hear the sounds of Her Majesty's Court.  We'll visit there later.  Always such a lively place."
    
    "We pass by in short order; from the path I can see elegantly-dressed people dancing beneath lights strung through the trees that surround the lawn.  I almost want to stop and watch, but we've other places to be, after all."
    
    "We arrive at--well, to call it a building would be to not do it anywhere near the justice it deserves.  The largest tree I could even imagine--maybe even larger--with an ornate door carved into it as organically as my little treehouse apartment looked to have grown."
    
    "Before Bran can open the door, though, it opens from the other side, and a young man pops out, holding one end of something rectangular covered in cloth; following him is another man holding the opposite end.  Although they both nearly drop it upon seeing Bran at the door."
    
    servant1 "Milord!  This is the last one, we've been working as fast as we could--"
    
    bran "I made it very clear that this was to be done well before I arrived with our guest."
    
    "There's an edge to his voice that I haven't heard before--a very sharp, pointy, dangerous edge."
    
    "I'm honestly kind of glad it's not directed at me."
    
    bran "You know what this means."
    
    servant2 "Please, no--"
    
    servant1 "We'll be good, we promise--it'll never happen again--"
    
    "{i}I{/i} don't know what this means, but they do, and it's probably a guarantee that it's less than pleasant."
    
    menu:
        "Then again, it's not really my business, is it? And they {i}did{/i} make a mistake.":
            "It's certainly not my problem whether Bran chooses to punish them or not for making mistakes."
            
            "This {i}is{/i} taking an awfully long time, though.  I lean up against the door and twiddle my thumbs a bit."
            
        "I... well, I feel kind of bad, but I'm only a guest here, and don't want to overstep...":
            "I mean, they've been really hospitable to me, after all.  It kind of sucks, but I'm just a visitor, and Bran seems pretty important."
            
            "After all, it's not my place to intervene..."
            
            "I shift uncomfortably and study the carvings on the door intently."
            
        "I don't really feel right letting him berate them because of me.":
            "After all, it seems like this trouble is on account of me arriving so suddenly."
            
            bethany "Hey, um, Bran--"
            
            "He turns around, suddenly all smiles."
            
            bran "What can I do for you, Milady?"
            
            bethany "Well--"
            
            "Suddenly I wonder if my complaints are all that justified.  Maybe I'm just being overly-sensitive?"
            
            "...no.  I made my mind up, didn't I?"
            
            bethany "Look, if you're punishing them because of me being here... I don't really mind them being late.  After all, you probably had to organize this suddenly, right?  Don't worry about it."
            
            "Bran doesn't speak for a moment, and his face is studiedly neutral.  Then he nods, and smiles even wider at me."
            
            "...it's a little uncomfortably wide of a smile, actually.  I wonder if I've really made the right decision."
            
            bran "As you say, Milady Bethany."
            
            "He turns to the two servants, who are both staring wide-eyed--at me."
            
            bran "Be grateful for the mercy of our guest, here.  And--do try to hurry it up, will you?"
            
            "There's still that edge to his voice when he speaks to them, and I wonder if I've really finished this or if I've merely stayed his hand while I'm around."
            
            "Still, though, I feel like I've done {i}some{/i} good."
            
            "...although I can't help but feel like Bran's looking at me a little oddly now."
            

    