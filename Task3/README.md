# Task3: Replace the legacy chunk

For the fluctuating available network bandwidth, the ABR can replace a previously downloaded low-quality chunk. In this task, we provide the **best speed** ABR to download the chunks, but after each chunk is downloaded, you can use **CustomReplacement.py** to check whether there is a chunk that can be replaced with the available bandwidth.

The return values of this function should be the relative postion of the replacable chunck, and new quality.

You need to submit **CustomReplacement.py** in this task.

Based on the simulation result, please answer the following questions:

1. How much better total played bitrate your replacement method can achieve?
2. Does your replacement method prolong the total play time, why?

**Rubric**:

- Test 1 (for `network.json`): `(total played time <=598) and (total played bitrate >= 500000)`
- Test 2 (for `network2.json`): `(total played time <=598) and (total played bitrate >= 247500)`
- Test 3 (for `network3.json`): `(total played time <=598) and (total played bitrate >= 646802)`
