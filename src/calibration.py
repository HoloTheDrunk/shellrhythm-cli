from blessed import Terminal
from src.charts_manager import ChartManager
from src.termutil import term, print_at, refresh
from src.conductor import Conductor
from src.translate import Locale, LocaleManager

term = Terminal()

class Calibration:
    conduc = Conductor()
    turnOff = False
    hitCount = 0
    maxHits = 16

    hits = []
    totalOffset = 0

    calibration_menu = "CalibrationSelect"
    # Possible things:
    # CalibrationSelect : Select calibration options
    # CalibrationGlobal : Calibrate your game
    # CalibrationSong   : Sync song to beats

    calibselec = 0
    selected_song_id = -1
    selected_song:dict = None

    reset_color:str = term.normal

    loc:Locale = LocaleManager.current_locale()

    def handle_input(self):
        val = ''
        val = term.inkey(timeout=1/120, esc_delay=0)
        if val:
            if self.calibration_menu == "CalibrationGlobal":
                offset = (self.conduc.current_beat - int(self.conduc.current_beat)) * (60/self.conduc.bpm)
                print_at(0,14, f"{term.center(str(round(offset, 3)))}")
                self.hits.append(offset)
                self.totalOffset += offset
                self.hitCount += 1
                if self.hitCount >= self.maxHits:
                    self.turnOff = True
            if self.calibration_menu == "CalibrationSong":
                if val.name == "KEY_ESCAPE":
                    self.turnOff = True
                if val.name == "KEY_LEFT":
                    self.totalOffset -= 0.001
                    # print_at(0,14, f"{term.center(str(round(self.totalOffset, 3)))}")
                    self.conduc.setOffset(self.totalOffset)
                if val.name == "KEY_RIGHT":
                    self.totalOffset += 0.001
                    # print_at(0,14, f"{term.center(str(round(self.totalOffset, 3)))}")
                    self.conduc.setOffset(self.totalOffset)

            if self.calibration_menu == "CalibrationSelect":
                if self.selected_song_id == -1:
                    if val.name == "KEY_DOWN":
                        self.calibselec = (self.calibselec + 1)%3
                    if val.name == "KEY_UP":
                        self.calibselec = (self.calibselec + 2)%3
                    if val.name == "KEY_ENTER":
                        if self.calibselec == 0:
                            self.startCalibGlobal()
                        if self.calibselec == 1:
                            self.selected_song_id = 0
                            print_at(int((term.width)*0.2), int(term.height*0.5)-1,self.loc("calibration.selectSong"))
                            print_at(int((term.width)*0.2), int(term.height*0.5)+1,"> " + str(self.selected_song_id) + "  ")
                        if self.calibselec == 2:
                            self.turnOff = True
                else:
                    if val.name == "KEY_LEFT":
                        self.selected_song_id = (self.selected_song_id - 1)%len(ChartManager.chart_data)
                        print_at(int((term.width)*0.2), int(term.height*0.5)+1,"> " + str(self.selected_song_id) + "  ")
                    if val.name == "KEY_RIGHT":
                        self.selected_song_id = (self.selected_song_id + 1)%len(ChartManager.chart_data)
                        print_at(int((term.width)*0.2), int(term.height*0.5)+1,"> " + str(self.selected_song_id) + "  ")
                    if val.name == "KEY_ENTER":
                        self.startCalibSong(ChartManager.chart_data[self.selected_song_id])


    def draw(self):
        if self.calibration_menu == "CalibrationGlobal":
            text_beat = "○ ○ ○ ○"
            text_beat = text_beat[:int(self.conduc.current_beat)%4 * 2] + "●" + text_beat[(int(self.conduc.current_beat)%4 * 2) + 1:]

            print_at(0,10,f"{term.center(self.loc('calibration.hit'))}")
            print_at(0,12,f"{term.center(text_beat)}")
        if self.calibration_menu == "CalibrationSong":
            text_title = self.selected_song["metadata"]["title"] + " - " + \
                self.selected_song["metadata"]["artist"]
            text_bpm = "BPM: " + str(self.selected_song["bpm"])
            print_at(0,9,f"{term.center(text_title)}")
            print_at(0,10,f"{term.center(text_bpm)}")

            text_beat = "○ ○ ○ ○"
            text_beat = text_beat[:int(self.conduc.current_beat)%4 * 2] + "●" + text_beat[(int(self.conduc.current_beat)%4 * 2) + 1:]
            print_at(0,12,f"{term.center(text_beat)}")
            print_at(0,14, f"{term.center(str(round(self.totalOffset, 3)))}")
            print_at(0,16,f"{term.center('Press Escape to save settings!')}")


        if self.calibration_menu == "CalibrationSelect":
            text_first = self.loc('calibration.global')
            text_second = self.loc('calibration.perSong')
            text_quit = self.loc('calibration.quit')
            if self.calibselec == 0:
                print_at(int((term.width - len(text_first))*0.5)+2, int(term.height*0.5) - 2, term.reverse + "> " + text_first + " <" + self.reset_color)
            else:
                print_at(int((term.width - len(text_first))*0.5)+2, int(term.height*0.5) - 2, "< " + text_first + " >")

            if self.calibselec == 1:
                print_at(int((term.width - len(text_second))*0.5)+2, int(term.height*0.5), term.reverse + "> " + text_second + " <" + self.reset_color)
            else:
                print_at(int((term.width - len(text_second))*0.5)+2, int(term.height*0.5), "< " + text_second + " >")

            if self.calibselec == 2:
                print_at(int((term.width - len(text_quit))*0.5)+2, int(term.height*0.5) + 2, term.reverse + "> " + text_quit + " <" + self.reset_color)
            else:
                print_at(int((term.width - len(text_quit))*0.5)+2, int(term.height*0.5) + 2, "< " + text_quit + " >")

    def startCalibGlobal(self):
        self.loc = LocaleManager.current_locale()
        ChartManager.load_charts()
        self.conduc.loadsong(ChartManager.chart_data[0])
        self.selected_song_id = 0
        self.selected_song = ChartManager.chart_data[self.selected_song_id]
        self.calibration_menu = "CalibrationGlobal"
        print(term.clear)
        self.conduc.play()

    def startCalibSong(self, chart):
        self.loc = LocaleManager.current_locale()
        self.calibration_menu = "CalibrationSong"
        print(term.clear)
        self.conduc.stop()
        self.conduc.loadsong(chart)
        self.conduc.play()
        self.conduc.metronome = True
        ChartManager.chart_data.append(chart)
        self.selected_song_id = len(ChartManager.chart_data)-1

    def init(self, fullscreen = True):		
        if fullscreen:
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                print(term.clear)
                while not self.turnOff:
                    if self.calibration_menu != "CalibrationSelect":
                        _ = self.conduc.update()

                    self.draw()
                    refresh()
                    self.handle_input()
        else:
            print(term.clear)
            while not self.turnOff:
                if self.calibration_menu != "CalibrationSelect":
                    _ = self.conduc.update()

                self.draw()
                refresh()
                self.handle_input()
            return self.totalOffset


        if self.hitCount != 0:
            print(round(self.totalOffset / self.hitCount, 3))
            return self.totalOffset / self.hitCount
        else: return 0

    def __init__(self, calibrationMenu) -> None:
        self.calibration_menu = calibrationMenu

if __name__ == "__main__":
    calib = Calibration("CalibrationSelect")
    calib.init()
