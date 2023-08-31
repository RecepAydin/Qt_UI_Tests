import sys
import unittest
import time

from PyQt6.QtWidgets import QApplication

from mainwindow import MainWindow

app = QApplication(sys.argv)

class TestmainwindowApp(unittest.TestCase):

    def setUp(self):
        self._ui = MainWindow()

    def test_speak(self):

        button = self._ui._ui.speakButton

        self.assertIsNotNone(button)

        button.click()

        self.assertEqual(self._ui.stt, 1)

    def test_pause(self):

        button = self._ui._ui.pauseButton

        self.assertIsNotNone(button)

        button.click()

        self.assertEqual(self._ui.stt, 2)

    def test_resume(self):

        button = self._ui._ui.resumeButton

        self.assertIsNotNone(button)

        button.click()

        self.assertEqual(self._ui.stt, 1)

    def test_stop(self):

        button = self._ui._ui.stopButton

        self.assertIsNotNone(button)

        button.click()

        self.assertEqual(self._ui.stt, 0)


    def test_volume(self):

        slider = self._ui._ui.volume

        self.assertIsNotNone(slider)

        slider.setValue(1)

        self.assertEqual(self._ui.ftr, "Volume")

    def test_rate(self):

        slider = self._ui._ui.rate

        self.assertIsNotNone(slider)

        slider.setValue(1)

        self.assertEqual(self._ui.ftr, "Rate")

    def test_pitch(self):

        slider = self._ui._ui.pitch

        self.assertIsNotNone(slider)

        slider.setValue(1)

        self.assertEqual(self._ui.ftr, "Pitch")


    def test_engine(self):

        combo = self._ui._ui.engine

        self.assertIsNotNone(combo)

        combo.setCurrentIndex(0)

        self.assertEqual(self._ui.ftr1, "default")

    def test_language(self):

        combo = self._ui._ui.language

        self.assertIsNotNone(combo)

        combo.setCurrentIndex(0)

        combo.setCurrentIndex(0)
        if self._ui.ftr2 != "tr_TR":
            combo.setCurrentIndex(1)

        self.assertEqual(self._ui.ftr2, "tr_TR")

    def test_voice(self):

        combo = self._ui._ui.voice

        self.assertIsNotNone(combo)

        combo.setCurrentIndex(0)

        self.assertEqual(self._ui.ftr3, "Microsoft Tolga")


    def test_test(self):

        self.printstate()

        speakbutton = self._ui._ui.speakButton
        pausebutton = self._ui._ui.pauseButton
        resumebutton = self._ui._ui.resumeButton
        stopbutton = self._ui._ui.stopButton
        volumebar = self._ui._ui.volume
        ratebar = self._ui._ui.rate
        pitchbar = self._ui._ui.pitch
        engineselect = self._ui._ui.engine
        languageselect = self._ui._ui.language
        voiceselect = self._ui._ui.voice

        self.assertIsNotNone(speakbutton)
        self.assertIsNotNone(pausebutton)
        self.assertIsNotNone(resumebutton)
        self.assertIsNotNone(stopbutton)
        self.assertIsNotNone(volumebar)
        self.assertIsNotNone(ratebar)
        self.assertIsNotNone(pitchbar)
        self.assertIsNotNone(engineselect)
        self.assertIsNotNone(voiceselect)

        speakbutton.click()
        print("Speaking Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 1)

        start_time = time.time()
        while time.time() - start_time < 2:
            pass
        print("After 5 seconds!!!")

        pausebutton.click()
        print("Pause Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 2)

        volumebar.setValue(75)
        print("Volume Changed")
        self.assertEqual(self._ui.ftr, "Volume")

        pitchbar.setValue(7)
        print("Pitch Changed")
        self.assertEqual(self._ui.ftr, "Pitch")

        ratebar.setValue(-7)
        print("Rate Changed")
        self.assertEqual(self._ui.ftr, "Rate")

        resumebutton.click()
        print("Resume Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 1)

        start_time = time.time()
        while time.time() - start_time < 1:
            pass
        print("After 2 seconds!!!")

        pausebutton.click()
        print("Pause Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 2)

        engineselect.setCurrentIndex(0)
        if self._ui.ftr1 != "mock":
            engineselect.setCurrentIndex(1)
        if self._ui.ftr1 != "mock":
            engineselect.setCurrentIndex(2)
        if self._ui.ftr1 != "mock":
            engineselect.setCurrentIndex(3)
        print("Engine Selected")
        self.assertEqual(self._ui.ftr1, "mock")

        languageselect.setCurrentIndex(0)
        if self._ui.ftr2 != "nb_NO":
            languageselect.setCurrentIndex(1)
        if self._ui.ftr2 != "nb_NO":
            languageselect.setCurrentIndex(2)
        print("Language Selected")
        self.assertEqual(self._ui.ftr2, "nb_NO")

        voiceselect.setCurrentIndex(0)
        if self._ui.ftr3 != "Kjersti":
            voiceselect.setCurrentIndex(1)
        print("Voice Selected")
        self.assertEqual(self._ui.ftr3, "Kjersti")

        resumebutton.click()
        print("Resume Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 1)

        start_time = time.time()
        while time.time() - start_time < 1:
            pass
        print("After 2 seconds!!!")

        pausebutton.click()
        print("Pause Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 2)

        volumebar.setValue(100)
        print("Volume Changed")
        self.assertEqual(self._ui.ftr, "Volume")

        resumebutton.click()
        print("Resume Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 1)

        start_time = time.time()
        while time.time() - start_time < 1:
            pass
        print("After 2 seconds!!!")

        stopbutton.click()
        print("Stop Button Clicked")
        self.printstate()
        self.assertEqual(self._ui.stt, 0)















    def printstate(self):

        if self._ui.stt == 0:
            print("Ready!")
        elif self._ui.stt == 1:
            print("Speaking!")
        elif self._ui.stt == 2:
            print("Paused!")



