# Task1: Best Speed vs. Best Quality

First, in order to get familiar with the autograder in gradescope, please submit the example ABR(Adaptive BitRate) to the gradescope. This will act as the **default** result.

In this task, you are required to implement two ABRs. The first **best speed** ABR will stick to the lowest bitrate, so that the video playback will be finished with minimal time.

For the other **best quality** ABR, it will try to download the highest bitrate, therefore, the user can have the “Best Experience”.

You only need to submit the **CustomAbr.py** to the gradescope.

Based on the simulation result, please answer the following questions:

1. Among the **default**, **best speed**, and also **best quality** ABRs, which one(s) have the shortest playback time
2. which one has the longest playback time. Why does that happen?
3. Although the best quality ABR can download the best video, the user experience is not good, why is that?

**Rubic**: 
- Default, `total played bitrate == 504821`
- Best speed, `total played bitrate == 45770`
- Best quality, `total played bitrate == 1188230`
