# CS514_ECE558_F23 Lab
Use sabre to understand how online video player works

Online video is the “Killer” application in today’s network. In this lab, we are going to implement an Adaptive Bitrate (ABR) Optimization algorithm with Sabre, an ABR algorithm simulation framework.

[Sabre](https://github.com/UMass-LIDS/sabre)[1] is an ABR algorithm simulation framework developed by UMass-LIDS, it can simulate the behavior and evaluate the performance of an ABR algorithm for different video and network configurations.

![Sabre](https://drive.google.com/uc?export=view&id=1JDluw_d7X_0o-2ghRde81MuS5QAC-qLf)

Sabre takes the above things as the inputs: a network trace, a video manifest, and, an ABR algorithm.

- The network trace is a JSON file that describes the connectivity information (RTT, bandwidth, and duration) in the simulation;
- The video manifest file is a JSON file that describes the available bitrate for the video, each chunks’ size and duration;
- The ABR algorithm is the algorithm you should implement in this lab.

`python3 sabre.py --abr CustomAbr.py [--replace CustomReplacement.py --network network.json]`

After being given all these things, Sabre will come up with an output that contains various user experience-related metrics.

```
buffer size: 25000
total played utility: 457.800726
time average played utility: 2.299534
total played bitrate: 484583.000000
time average played bitrate: 2434.061900
total play time: 597.252272
total play time chunks: 199.084091
total rebuffer: 0.000000
rebuffer ratio: 0.000000
time average rebuffer: 0.000000
total rebuffer events: 0.000000
time average rebuffer events: 0.000000
total bitrate change: 19002.000000
time average bitrate change: 95.447104
total log bitrate change: 11.683780
time average log bitrate change: 0.058688
time average score: 2.299534
over estimate count: 161
over estimate: 322.865381
leq estimate count: 250
leq estimate: 625.341842
estimate: -253.903003
rampup time: 6.252272
total reaction time: 74.270448
played queue: [0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 0]
oscillation: 106
```

In this lab, we will evaluate the performance of your ABR algorithm based on total played bitrate and total play time (more play time is worse, as it means more freezes occurred). In our example, the video’s length is 597s.

The report_download() will pass the current download information to the Abr class once each chunk is finished, the output is like:

Download Info DownloadProgress(index=1, quality=7, size=8067960, downloaded=8067960, time=1688.592, time_to_first_bit=75, abandon_to_quality=None)

The report_delay() may be an important function that we can use. After each chunk is downloaded, it will check whether the buffer has enough space for further downloading, once the buffer does not have enough space for one whole chunk, it will call this function, and tell the Abr class.

One example ABR:

```
class CustomAbr(sabre.Abr):
    def get_quality_delay(self, segment_index):
        manifest = self.session.manifest
        bitrates = manifest.bitrates
        throughput = self.session.get_throughput()	\\Get current availabe throughput
        quality = 0
        while (quality + 1 < len(bitrates) and		\\Assign best affordable bitrate
               bitrates[quality + 1] <= throughput):
            quality += 1
        return (quality, 0)					\\Return the best affordable bitrate

```

[1]: Kevin Spiteri, Ramesh Sitaraman, and Daniel Sparacio. 2018. From Theory to Practice: Improving Bitrate Adaptation in the DASH Reference Player. In MMSys '18: 9th ACM Multimedia Systems Conference, June 12-15, 2018, Amsterdam, Netherlands. https://doi.org/10.1145/3204949.3204953
