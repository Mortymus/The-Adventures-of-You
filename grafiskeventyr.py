from tkinter import *

root = Tk()
root.geometry('300x650')

topframe=Frame(root)
topframe.pack()
middleframe=LabelFrame(root,width=250,height=450)
middleframe.pack()
middleframe.propagate(0)
bottomframe=Frame(root)
bottomframe.pack()
quitframe=Frame(root)
quitframe.pack()

headline=Label(topframe, text='''---The Amazing Adventures of You---
''')
headline.pack()



intro="""
--- Your amazing adventures ---

You're woken up by the blazing sun and
an overwhelming feeling of thirst,
only to find yourself in a beautiful
natural landscape without any idea how
you got there.

You're in the middle of a valley between
tall mountains with foothills lined with
forests. The floor of the valley is a
vast open space covered with long grass
and shrubbery. It looks like a typical
place a farmer would build fences around
to let sheep graze, but there are no sheep
around, or any other sign of civilization
for that matter.
 
You start wondering what 
your next move will be.

You decide to:
	
A Go back to sleep.
B Look for water.
"""

start=Label(middleframe, text=intro)
start.pack()

# a branch
a="""
You feel unable to recognise the importance
of the sudden change of scenery as a heavy
tiredness overwhelms you. You curl up on
the surprisingly soft ground, and snuggle
into the little nest your body has formed
in the unknown amount of time it has spent
there. Your heavy eyelids slide down.

You decide to:
	
A Give in to the temptation of sleep.
B Fight to stay awake.
"""

aa="""
You make no effort to resist the heaviness
of your eyelids, and succumb to a deep
sleep.
	 	
You wake up shortly after as a bear takes
a large bite out of you, just in time to
savour the last seconds of your life. You
try to enjoy the time you have left, but
it is increasingly difficult as the bear
efficiently bites every piece of flesh you
have to offer.
	 	
Game over.
"""
# game over

ab="""
Your body twitches hard to let you know
all systems of defence are about to shut
down, but you struggle against the 
overpowering urge to sleep. As you force
your eyes to open as much as they can, you
notice a bear approaching.
	 	
You decide to:
	 	
A Scream.
B Initiate a conversation.
"""

aba="""
You open your mouth and let out a piercing
scream. You're surprised at the loudness and
intensity of the sound escaping your mouth,
especially considering how seemingly little
effort it took to produce it.

The bear seems to be taken back by the noise
you just made. It pauses, pulling its face
back a bit as it processes the change of
events.
	
You decide to:
		
A Throw a rock at the bear.
B Tell a joke.
"""

abaa="""
You pick up the nearest rock and hurl it at
the bear. It hits the bear in the middle of
the face as he lets out a howl, prompting it
to rise on its hindlegs and stretching its
paws out. It traverses the distance between
the two of you in an instant, biting into you
in a growling snarl.

You can hear your own flesh gashing between
its teeth as you slowly realise that this
isn't a dream.

Game over.
"""
# game over

abab="""
'Have you ever heard the one where a
blackbear, a grizzly and a polar bear walks
into a bar... Everybody in there thought the
polar bear was the coolest one.'

A silence follows the joke as you realise that
bears most likely cant laugh anyway, and
probably haven't had much exposure to the
english language if they could. You begin
reviewing the merits of the thought process
that has led you to this point.

You decide to

A Stand your ground.
B Make a run for it.
"""

ababa="""
The bear looks at you with a perplexed
facial expression.

'No, i've actually never heard that one before.
And i've heard my share of bear jokes, many of
which quite cruel, being a bear myself and all.'
the bear responds.

You decide to

A Explain the joke.
B Make a run for it."""

ababaa="""
You go on to explain the joke.

'Well you know, the polar bear comes from the
arctic, which is a pretty cold place... and
cool also meaning cold, so the adjective of
being cool takes on sort of a double-meaning,
which is for some reason kind of funny.'

You wonder why you decided to talk about
adjectives to an animal you should be happy
could understand simple english, let alone
the inner workings of its grammar.

Silence...

You decide to

A Continue to chat.
B Saunter away discreetely.
"""

ababaaa="""
'Oh, I got the joke.' the bear explains. 'I
was just baffled at your decision to tell it,
me being quite decided on eating you and all.'

An awkward silence follows as you realise your
fear of immediate death was justified.

You decide to

A Make a run for it.
B Inquire why the bear wanted to eat you.
"""

ababaaaa="""
You forget that bears are capable of running
about 50 K's an hour, and foolishly try to
make a run for it.

The bear never has to show it's superiority
at running, since your feet are tripped by
the long grass, leaving your sprint looking
more like an attempt to dive into a
non-existent swimming pool.

Your body is devoured within seconds.

Game over.
"""
# game over

ababaaab="""
'Why would you ever want to eat me? I've led
a horribly unhealthy life, I'm sure most of
the other animals in the forest would taste
far better than me.' you shakingly question
the bear.

'Actually,' the bear starts. 'I was planning
to eat you as a form of revenge.'

You decide to

A Ask for details.
B Begin to cry.
"""

ababaaaba="""
'Revenge for what?' you ask the bear with a
surprised look on your face.

'I thought you had eaten my cubs.' the bear
answers with a facial expression sadder than
you ever thought a wild animal could have.

'They were gone when I woke up this morning.'

You decide to

A Admit eating the cubs.
B Offer help to find the cubs.
"""

ababaaabaa="""
For some reason you lie to the bear, telling
her it was indeed you who killed and ate her
cubs. It makes you feel tough to pretend that
her cubs wouldn't have ripped you apart if
challenged, or even just out of boredom.

The feeling of toughness qucikly subsides as
the mama bear starts picking you apart like
you're a Barbie doll in the grasp of a mean
teenage boy. Blood sprays in all directions
as the bear rips off limb after limb in a
frenzied anger.

Game over.
"""

ababaaabb="""
The stress and fear of the situation becomes
overwhelming, and your brave body responds by
letting out loud sobs as it begins shaking.
Soon you are pretty much howling while tears
are streaming down your face.

You tense up as the bear quickly approaches
and grabs you, but start relaxing when you
realise the bear is actually hugging you.

You decide to

A Continue crying.
B Put on a brave face.
"""

ababaaabba="""
You dig your face into the bear's shoulder,
and continue sobbing as your body shakes.
Soon the bear is also crying, and the roles
change as you do your best to comfort the
wild animal who was just about to eat you.

You decide to:

A Ask why the bear is crying.
B Make a run for it.
"""

abb="""
You halfheartedly clear your throat before
addressing the wild animal in front of you.
'Oh, hi there Mr. Bear,' you awkwardly start,
before asking how the day is going so far.
The bear sits down, leaning forward with its
paws towards its legs. 'Not so good,' she
answers. 'My cubs are missing. They were gone
when i woke up this morning.'
	
You decide to:
		
A Make a run for it.
B Inquire for details.
"""

abba="""
The absurdity of a talking bear is only
topped by it seeming to confide in you, and
you're already on your feet running away
before you have a chance to begin
contemplating how your universe just turned
upside down.

You dont make it far before the bear is on
top of you, ripping you apart limb by limb
while screaming 'Cubkiller!!!!'.

Game over.
"""
# game over

abbb="""
The bears sad tone, not to mention the
troubling predicament she is facing, lowers
your guard. Instead of being scared of the
wild animal, you feel compassinon and are
saddened by its unfortune.

What happened you timidly ask. The bear
shrugs her shoulders, and says everything
was as normal as ever before going to sleep.

You decide to

A Pledge to help find the cubs.
B Make an excuse to leave.
"""

abbba="""
You pledge to help find the cubs, and the
bear's sad face brightens. You wonder why
the bear is appeased by your offer to help,
considering you most likely will be
completely useless in the given situation,
but feel a surge of confidence from the
powerful animal's faith in you.

You decide to:

A Jump on the bear's back.
B Ask the cubs' names.
"""

abbbaa="""
You jump on top of the bear's back, and
ask her to continue following the cubs
scent that had initially led her to you.

As the bear charges ahead at maximum speed,
you realise the captor of the cubs might be
same person, or entity, that kidnapped you.

You soon encounter a pack of wolves.

You decide to:

A Ask the wolves if they've seen the cubs.
B Yell obescenities at the wolves.
"""

abbbb="""
Your initial feeling of compassion subsides,
and you decide you don't have time to spend
with miserable talking bears.

'I would love to help you.' you say, 'but I
have a really important appointment in that
forest over there. I'll come back looking
for you once I've taken care of my business
there.' The bear doesn't seem to believe you
have business, but let's you walk away.

You're eaten by a pack of wolves as soon as
you reach the forest.

Game over.
"""
# game over

# b branch

b="""
The backgroud noise slowly rise
as you begin to notice the symphony 
of animal life filling the air. The 
noises of nature pleasantly fill your 
head while you begin to process the 
impressive, yet startling, vision 
before you. There are wide plains 
covered with wild grass and flowers. 
As your eyes start focusing on the
forest, your ears begin to single out 
a constant sound masked by those
of made by birds, insects and other
animals. You realize its the sound
of water trickling somewhere behind
you. That's when you turn around
and see a large bear approaching you.
	
You decide to:
		
A Run!
B Attack!
"""

ba="""
You dont make it more than
10 meters before the bear is on top of
you. You feel every single tooth he sinks
into you as he rips your left arm out. His
grip vanishes as your arm is severed,and
you manage to slowly crawl away while
trying to balance your weight with your
one remaining arm.
		
You decide to
		
A Crawl under the nearest rock.
B Kick the bear.
"""

baa="""
You hurriedly squeeze under a large rock
nearby, and are surprised to find a sizable
space down there. The bear lunges after you,
but is too big to fit through the opening,
its arm reaches you exactly far enough to
scratch deep gashes on your stomach, but you
stay safe in there until the bear tires and
leaves.

You decide to
		
A Keep waiting.
B Try to find your way home.
"""

bab="""
You put all the force you can into a powerful
kick to the bears face, but its chewing on your
foot before it even reaches. He bites into your
thigh and uses his paws to separate your right
leg from the rest of your body. The eventually
leaves after playing with the assorted bodyparts
strewn around the area. You pass out, lingering
between life and death for hours, before coming
to sometime in the afternoon.

You decide to
		
A Start crying.
B Start walking.
"""

baba="""
You have a long good cry, wishing you had
someone to hug you, and tell you everything
will be ok, that your left arm and right leg
will sprout right back, and youll be doing
crossfit again in no time. The crying boosts
your health levels, and you feel yourself
increasing in power.

You decide to
    	
A Call for help.
B Start walking.
"""

babb="""
You drag yourself out from under the rock using
the one arm you have, while helping with one leg
you have. You realise this is going to be time
consuming, and feel a rising despair at the
thought. The despair fuels a stubborn energy that
allows you to stumble out on your foot, developing
a ridiculus looking walk that resembles a
two-legged elephant. You hear the faint sound of a
river in the distance.

You decide to
		
A Walk toward the river.
B Lay down and give up.
"""

babbb="""
You lay down in the grass, feeling the warm
sun on your face. A feeling of happiness seem
to radiate into you from the sunlight. Its
nice to not have to continue that stupid quest.
You slowly fall asleep with a wide smile across
your face. When the pack of rats come and gnaw
on your body until there is nothing left, you
look down at your dead body as your soul drift
upwards, hopefully to that special place youve
heard so much about.

Game over.
"""
# game over

bb="""
You launch at the bear with your teeth
bared and your claws raised, sinking
your little teeth into its neck. Youre
surprised to find that your bite 
unleashed a significant torrent of
blood, and even more surprised at how
easily you rip the bears head off. The
sight of gushing red blood reminds you
that you havent had breakfast yet.
	
You decide to
	
A Feast on the bears blood.
B Look for berries.
"""

bba="""
You lift the bears head up to your
mouth, and bite into the bloody neck
where it was severed. You feel your
primal urges tingle with satisfaction
as you scarf down bloody pieces of raw
meat mixed with sinew, veins and skin.
The feeding frenzy goes on for about
15 minutes before you realize youre
getting full. Suddenly the bloody mess
doesnt seem so appetizing. You begin
to wonder about when the last time you
ate was.

You decide to

A Paint your face with the bears blood.
B Go exploring.
"""

bbaa="""
You stick your fingers in the bloody
remains of the bear, and seremoniously
smeer two streaks under your eyes before
spiking your hair with the sticky red
liquid. You chuckle to yourself, as you
dare any other animals in this sissy
forest to come see what youre made of.
The sound of trickling water fades back
into your perception, and you still feel
parched even though youve drank what feels
like a couple of pints of bear blood.

You decide to

A Do a victory dance.
B Find the source of water
"""

bbaaa="""
You feel a surge of adrenaline after taking
what youd consider a fair sized bear, and
you start chanting in a fasion you figure
would be appropriate, while slowly beginning
to move around the dead bear in circles. The
surprise of waking up far from civilization
stripped of recent memories has taken a
backseat to how awesomely powerful you feel.
As your voice increases to a higher and more
arrogant pitch, a pack of wolves fly in from
the sideline and rip you to pieces.

Game over.
"""
# game over

bbaab="""
You refocus your attention to the vast
surroundings, and the the constant hum
of nature fades in. It's gets louder
and more complex as you focus on it, a
rich collection of birds and insects
humming with life. Concentrating
harder you again hear the constant
backdrop of flowing water. You realise
there must be a creek nearby. A little
squirl appears as youre making your
way towards the sound.

You decide to

A Continue towards the water.
B Eat the squirl.
"""

bbaaba="""
The sound of rushing water grows
stronger as you walk across the
vast open space. It doesnt look
like there should be a river,
but the landscape curves downwards
as yoou walk across it. Its a short
walk down the slope before you
happen upon a small river in a
rocky area. The curve of the
landscape had hid the few trees
on other side of the river.

You decide to

A Drink water.
B Cross the river.
"""

bbaabb="""
You grab the squirl and quickly
bite its head of, ripping its
little body apart, bringing it
straight to your face so you can
slurp in the internal organs
before feasting on the insignifant
amount of meat this little squirl
could give in comparison to the
dead bear a few paces back.

You decide to

A Continue towards sound of water.
B Look for other animals to kill.
"""

choice_list=['a','aa','ab','aba','abaa','abab','ababa','ababaa','abb','abba','abbb','b','ba','baa','bab','baba',\
             'babb','babbb','bb','bba','bbaa','bbaaa','bbaab','bbaaba','bbaabb','ababaaa', 'ababaaaa','ababaaab',\
             'ababaaaba', 'ababaaabb', 'ababaaabba','ababaaabaa','abbbb','abbba','abbbaa']
scene_list=[a,aa,ab,aba,abaa,abab,ababa,ababaa,abb,abba,abbb,b,ba,baa,bab,baba,babb,babbb,bb,bba,bbaa,bbaaa,bbaab,\
            bbaaba,bbaabb,ababaaa, ababaaaa,ababaaab,ababaaaba,ababaaabb,ababaaabba,ababaaabaa,abbbb,abbba,abbbaa]
gameover=['aa','abaa','abba','babbb','bbaaa','ababaaaa','ababaaabaa','abbbb']

choice=''
        
def quitting():
        exit()

def choice1():
    global choice
    choice+='a'
    for story in middleframe.winfo_children():
        story.destroy()
    Label(middleframe, text=scene_list[choice_list.index(choice)]).pack()
    print(scene_list[choice_list.index(choice)])

def choice2():
    global choice
    choice+='b'
    for story in middleframe.winfo_children():
        story.destroy()
    Label(middleframe, text=scene_list[choice_list.index(choice)]).pack()
    print(choice)

button1=Button(bottomframe, text='    A    ', command=choice1)
button1.pack(side=LEFT)
button2=Button(bottomframe, text='    B    ', command=choice2)
button2.pack(side=LEFT)
quitbutton=Button(quitframe, text='        Quit        ', command=quitting)
quitbutton.pack(side=BOTTOM)


root.mainloop()
