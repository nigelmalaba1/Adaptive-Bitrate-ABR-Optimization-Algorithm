# Task2: Reduce the Oscillation during the play

Besides playback time and total played bitrate, oscillation can also be a concern. Here, the oscillation means the changes in the played quality. In this task, you are required to implement an Abr to smooth the played quality. You can add some instance variables to your `CustomAbr` class by adding them in the [constructor](CustomAbr.py#L6) `def __init__(self)`.

$`oscillation`$ is calculated with the following way (suppose quality array's index start with 0, and it has $`T`$ chunks in total):

```math
oscillation = \sum^{T-1}_{t=1} (q_{t} - q_{t-1})^2
```

You need to submit the **CustomAbr.py**.

Based on the simulation result, please answer the following questions:

1. Why does the provided [CustomAbr.py](CustomAbr.py) perform badly in $`oscillation`$?
2. How does your CustomAbr.py solve this problem?

**Rubric**:

- Test 1 (for `network.json`): `(oscillation <=22) and (total played bitrate >= 450000) and (total play time <= 597.5)`
- Test 2 (for `network2.json`): `(oscillation <=30) and (total played bitrate >= 220000) and (total play time <= 597.5)`
- Test 3 (for `network3.json`): `(oscillation <=35) and (total played bitrate >= 900000) and (total play time <= 597.5)`
