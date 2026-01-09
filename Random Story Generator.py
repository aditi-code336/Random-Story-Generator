import random

sentence_starter=('Once upon a time ','Long long ago ','In the age when dinosaurs roamed the earth ')
character=('there was a tiny kitten. ','lived a shriveled old lady. ','along came a laughing little baby. ')
time=('It was the hot afternoon of May when ','On the day of the invasion ','One morning at sunrise ')
story_plot=('she passed by the docks ','she crossed the cemetary ','she was walking through the fields ')
place=('in Panama. ','in Honululu. ','in the city of Mumbai. ')
character_2=('She saw a rodent ','She met a 4 eyed man ','She witnessed an alien ')
work_1=('walking in the direction opposite her and ','scooping up soup from a bowl and ','drinking from a small water bottle and ')
work_2=('reading a magazine. ','eating a breadstick. ','scrunching his nose in weird ways. ')

print(random.choice(sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(character_2)+random.choice(work_1)+random.choice(work_2))