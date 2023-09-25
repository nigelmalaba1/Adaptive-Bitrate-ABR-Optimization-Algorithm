import sabre

class CustomAbr(sabre.Abr):
    def get_quality_delay(self, segment_index):
        return (0, 0)
#    def report_delay(self, delay):
#        print ("buffer full", delay)
#    def report_download(self, metrics, is_replacment):
#        print ("Download Info", metrics)
