# road_sign_text_recognition
Test that demonstrates the possibility of reading road signs using only paddleocr and a few opencv instructions. The reading quality seems acceptable

Requirements:

paddleocr must be installed ( https://pypi.org/project/paddleocr/)

pip install paddleocr

opencv must be installed

Run:

VIDEO_PaddleOCR_Road_sign_test_recognition.py

The text of the road signs read appears on the console

The test video has been downloaded from:

https://www.pexels.com/video/road-trip-4434242/

Where there are more videos that can be used for testing (changing the assignment instruction 18)

Observations.

In the test video the text RAM appears on the motorcycle's dashboard, to avoid this a window has been created that is set by the WindowFactor parameter (line 14). This problem does not exist with other videos, so if other videos are used it would be convenient to change WindowFactor (line 14) to 1.
