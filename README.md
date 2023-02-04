# shellrhythm
![](./shellrhythm.png)

![](https://img.shields.io/github/issues/HastagGuigui/shellrhythm?style=flat-square) ![](https://img.shields.io/github/forks/HastagGuigui/shellrhythm?style=flat-square) ![](https://img.shields.io/github/stars/HastagGuigui/shellrhythm?color=yellow&style=flat-square) ![](https://img.shields.io/github/license/HastagGuigui/shellrhythm?color=red&style=flat-square) ![](https://img.shields.io/badge/version-1.0-white?style=flat-square) ![](https://img.shields.io/discord/1071432733240332328?label=Join%20the%20Discord&logo=discord&style=flat-square)

## Gameplay

shellrhythm plays with **your entire keyboard**. (more precisely just the letter keys and aditional punctuation keys, so call that a 30k rhythm game!)<br/>
Simply press the displayed key when the corresponding hit object finishes drawing!

## How to install

At the moment, the only way to play this game is through the source code. **So, how do you play?**

- First, make sure you have [Python 3](https://www.python.org/downloads/) and [git](https://git-scm.com/downloads) installed (If you're using Linux, you probably have these installed)

- Then, `git clone` the project (after having `cd`'d into the folder you want). 
```
git clone https://github.com/HastagGuigui/shellrhythm.git
```

- After that, with `pip` installed, simply do the following command (as admin/sudo on Windows):
```
pip install -r requirements.txt
```

- And then finally, launch the program using the `run.bat` file (or `./shellrhythm` on Linux) or in a command prompt in the game's directory:
```
python ./index.py
```
(Side note: some files like `./src/calibration.py` can be launched independently, but the working directory needs to be the directory of the `index.py`.)

## Where are the charts?

By default, there are no charts. Mostly because of copyright reasons, ~~but also because I'm too lazy to finish a chart~~

## Are there any charts I can download?

You can check out the #charts channel on the [shellrhythm Discord server](https://discord.gg/artQgD3Y8V), but I'll most likely update this part with, like, a chartpack or something. I'll just have to wait until more charts are available.

## How do I make a chart?

Use the editor! It's the 2nd option on the titlescreen.

## Can I use this project for something?

Sure! The entire codebase is under the ISC license, so honestly do whatever with it. (Just don't claim to be behind the original project, obviously.)<br>
However, one of the libraries this project uses, [pybass3](https://github.com/devdave/pybass3/), uses a library called BASS, which is a commercial product. While it is free for non-commercial use, please ensure to [obtain a valid licence](http://www.un4seen.com/bass.html#license) if you plan on distributing any application using it commercially.

## Known issues

- [Linux isn't fully compatible with pybass3 yet,](https://github.com/devdave/pybass3/issues/2) however [there is a workaround to get it working anyways.](./docs/PYBASS3_LINUX.md)
- The accuracy is bound to the framerate. It's why there's an fps counter at the bottom left of the screen in gameplay.

## Help! I'm having issues!

If it's a crash or an unexpected behaviour (or even just a suggestion!), open an issue.
If it's just struggle on how to make a chart (like, undocumented stuff), hit me up on [Twitter](https://twitter.com/_GuiguiYT) or on [Discord](https://discord.gg/artQgD3Y8V) (this is a link to the shellrhythm discord server).

----
© #Guigui 2022-2023
