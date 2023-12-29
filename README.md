# Advent_of_Code_2015
Working through previous AoC calendars to practice skills in Python

**12/29/2023** -  - Day 6 Total time  4 hours
> *Reflections* - Understood conceptually. Didn't plan well
> > Struggled with toggle function for about 3 hours. Scrapped it upon waking up and solved within 20 min.
> > Experiencing a problem that I believe will show itself frequently; To continue down path to edit and fix versus restarting with a clean slate. To dive deeper or surface for new breath.
> > > In general, I think learning to walk away from a code, either for a break or for good, will prove to be a handy skill.

> > *Difficulties*
> > > Had a cute thought to use "O" and "-" for off and on. Led to a lot of joining and splitting for Part 1 and then int/str in Part 2.
> > > > This ended up breaking the code as the program wouldn't track digits consisting of more than 1 index.
> > > > Switched to ints of 0 and 1 for off/on, which made rewriting Part 1 a breeze.
> > > > > rows, col = (1000,1000)
          x = [[0]*col)]*rows
> > > > > was a clean way of creating orig array. However, when assigning new values throughout the prompt, each row/col would be changed rather than a specific index. (As if i was editing each col variable)

**12/28/2023** -  - Day 4 and Day 5 : Total time  ~3 hours
> *Reflections* - Day 4 was a lot of learning; first time really studying hashes and their relevancy, usage, and functions (specifically md5). Day 5 was more basics practice
> > Proud of tackling the hashing problem; not sure how often I will sharpen that skill. Day 4 pt 2 was brainless.

> > *Difficulties*
> > > I ended up using functions for both parts of Day 5. I had messed around a little with iterating on a single line:
> > > > i.e. x = True in (y.count(z) >3 for z in a). Attempted a few of these but didn't have much success. Would like to go back through and avoid using functions in lew of single line iterations.
> > > > Day 5 pt 2 was another reminder to read the rules carefully.

**12/26/2023** -  - Day 1, Day 2, Day 3  : Total time ~2 hours
> *Reflections* - Feeling great! (Day 1 and 2 of 2015 took about 45 minutes compared to ~20 hours for 2023)
> > It is encouraging seeing the skills learned throughout 2023's calendar make this new beginning feel easy.
> > Not sure if Day 3 is optimized for processing but it worked great and turned out clean IMO.

> > *Difficulties*
> > > Was testing my speed of processing the problem/writing a solution so solutions may not be the most thoughtful.
> > > Day1pt1 only includes solution to pt 2
