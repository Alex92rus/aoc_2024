

|![Group of Senior Elvish Historians on the Planet Ceres helped by an elf girl, looking for Christmas at a monitoring station. Sharp attention to detail, realism and a strong sense of nostalgia and warmth, sharp attention to small details and textures. - Art Created by Midjourney](https://media.discordapp.net/attachments/1221829775685976114/1314115720346341437/aleksandrosharky_Group_of_Senior_Elvish_Historians_on_the_Plane_8cc01137-b816-4086-acaf-c6c335210912.png?ex=67529922&is=675147a2&hm=8b85c643aedc41622b8f4fea93e42bcf211703496133b5cec5c3f267d5d5d785&=&format=webp&quality=lossless&width=585&height=585)|
|:--:|
|*Group of Senior Elvish Historians on the Planet Ceres helped by an elf girl, looking for Christmas at a monitoring station. Sharp attention to detail, realism and a strong sense of nostalgia and warmth, sharp attention to small details and textures. - Art Created by Midjourney*|

Copied from: https://adventofcode.com/2024/day/4

--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
```
..X...
.SAMX.
.A..A.
XMAS.S
.X....
```

The actual word search will be full of letters instead. For example:

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:
XMAS word can't change directions - count applied bottom up
``` 
....XXMAS. 18
.SAMXMS... 16
...S..A... 14
..A.A.MS.X 12
XMASAMX.MM 10
X.....XA.A
S.S.S.S.SS - 8
.A.A.A.A.A - 1
..M.M.M.MM - 1
.X.X.XMASX - 1
```


Take a look at the little Elf's word search. How many times does XMAS appear?

--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
