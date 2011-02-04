import datetime
import pytz

NUM_TO_SHOW = 5

hc_to_bmc = (
# Monday
(
( 0, 15), ( 7, 40), ( 8, 40), ( 9, 40), (10, 15), (10, 40), (11, 15), (11, 45),
(12, 15), (12, 45), (13, 15), (13, 45), (14, 15), (14, 50), (15, 30), (16, 00),
(16, 35), (17, 50), (18, 25), (18, 55), (19, 40), (20, 55), (22, 05), (22, 40),
(23, 40),
),

# Tuesday
(
( 0, 40), ( 7, 30), ( 8, 30), ( 9, 15), (10, 00), (10, 45), (11, 30), (12, 15),
(13, 00), (13, 45), (14, 40), (15, 30), (16, 00), (16, 40), (17, 50), (18, 25),
(18, 55), (19, 40), (20, 55), (22, 05), (22, 40), (23, 40)
),

# Wednesday
(
( 0, 40), ( 7, 40), ( 8, 40), ( 9, 40), (10, 15), (10, 40), (11, 15), (11, 45),
(12, 15), (12, 45), (13, 15), (13, 45), (14, 15), (14, 50), (15, 30), (16, 00),
(16, 35), (17, 50), (18, 25), (18, 55), (19, 40), (20, 55), (22, 05), (22, 40),
(23, 40),
),

# Thursday
(
( 0, 40), ( 7, 30), ( 8, 30), ( 9, 15), (10, 00), (10, 45), (11, 30), (12, 15),
(13, 00), (13, 45), (14, 40), (15, 30), (16, 00), (16, 40), (17, 50), (18, 25),
(18, 55), (19, 40), (20, 55), (22, 05), (22, 40), (23, 40)
),

# Friday
(
( 0, 40), ( 7, 40), ( 8, 40), ( 9, 40), (10, 15), (10, 40), (11, 15), (11, 45),
(12, 15), (12, 45), (13, 15), (13, 45), (14, 15), (14, 50), (15, 30), (16, 00),
(16, 35), (17, 50), (18, 25), (18, 55), (19, 40), (20, 55), (22, 05), (22, 40),
(23, 40),
),

# Saturday
(
( 0, 40), ( 1, 40), ( 2, 40), (11, 40), (12, 40), (13, 40), (14, 40), (17, 15),
(17, 45), (18, 15), (18, 45), (19, 15), (19, 45), (20, 15), (21, 15), (22, 15),
(22, 45), (23, 15)
),

# Sunday
(
( 0, 15), ( 0, 45), ( 1, 30), ( 2, 30), ( 3, 00), ( 9, 45), (10, 45), (11, 45),
(12, 45), (13, 45), (14, 45), (15, 45), (17, 15), (17, 45), (18, 15), (18, 45),
(19, 15), (20, 15), (21, 15), (22, 15), (23, 15)
),
)

bmc_to_hc = (
# Monday
(
( 0, 00), ( 7, 25), ( 8, 10), ( 9, 10), (10, 00), (10, 30), (11, 00), (11, 30),
(12, 00), (12, 30), (13, 00), (13, 30), (14, 00), (14, 35), (15, 10), (15, 45),
(16, 15), (17, 10), (18, 10), (18, 40), (19, 10), (20, 10), (21, 10), (22, 20),
(23, 10),
),

# Tuesday
(
( 0, 10), ( 7, 10), ( 8, 10), ( 8, 55), ( 9, 40), (10, 25), (11, 10), (11, 55),
(12, 40), (13, 25), (14, 10), (15, 10), (15, 45), (16, 15), (17, 10), (18, 10),
(18, 40), (19, 10), (20, 10), (21, 10), (22, 10), (23, 10),
),

# Wednesday
(
( 0, 10), ( 7, 25), ( 8, 10), ( 9, 10), (10, 00), (10, 30), (11, 00), (11, 30),
(12, 00), (12, 30), (13, 00), (13, 30), (14, 00), (14, 35), (15, 10), (15, 45),
(16, 15), (17, 10), (18, 10), (18, 40), (19, 10), (20, 10), (21, 10), (22, 20),
(23, 10),
),

# Thursday
(
( 0, 10), ( 7, 10), ( 8, 10), ( 8, 55), ( 9, 40), (10, 25), (11, 10), (11, 55),
(12, 40), (13, 25), (14, 10), (15, 10), (15, 45), (16, 15), (17, 10), (18, 10),
(18, 40), (19, 10), (20, 10), (21, 10), (22, 10), (23, 10),
),

# Friday
(
( 0, 10), ( 7, 25), ( 8, 10), ( 9, 10), (10, 00), (10, 30), (11, 00), (11, 30),
(12, 00), (12, 30), (13, 00), (13, 30), (14, 00), (14, 35), (15, 10), (15, 45),
(16, 15), (17, 10), (18, 10), (18, 40), (19, 10), (20, 10), (21, 10), (22, 20),
(23, 10),
),

# Saturday
(
( 0, 10), ( 1, 10), ( 2, 10), (11, 15), (12, 15), (13, 15), (14, 15), (17, 00),
(17, 30), (18, 00), (18, 30), (19, 00), (19, 30), (20, 00), (21, 00), (22, 00),
(22, 30), (23, 00),
),

# Sunday
(
( 0, 00), ( 0, 30), ( 1, 00), ( 2, 00), ( 2, 45), ( 9, 30), (10, 15), (11, 30),
(12, 30), (13, 30), (14, 30), (15, 30), (17, 00), (17, 30), (18, 00), (18, 30),
(19, 00), (20, 00), (21, 00), (22, 00), (23, 00),
),
)


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def get_times(now, table):
	tab = []

	for day in table:
		tab.append([datetime.time(*x) for x in day])
	
	results = [x for x in tab[now.weekday()] if x >= datetime.time(now.hour, now.minute)][:NUM_TO_SHOW]
	
	if len(results) < NUM_TO_SHOW:
		results += [x for x in tab[(now.weekday() + 1) % 7]][:NUM_TO_SHOW-len(results)]

	return results

class MainPage(webapp.RequestHandler):
	def get(self):

		est_tz = pytz.timezone('US/Eastern')
		now = est_tz.normalize(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(est_tz))
		
		self.response.headers['Content-Type'] = 'text/html'
		
		self.response.out.write('<html><head><meta name="viewport" content="width=device-width" /><title>nextblueb.us</title>')
		self.response.out.write('''<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-20844661-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>''')
		self.response.out.write('</head><body><center><h2>When is the next <font color=blue>Blue Bus</font>?</h2>')
		now_pretty = now.strftime('%I:%M %p')
		now_pretty = now_pretty if now_pretty[0] != '0' else now_pretty[1:]
		now_pretty = now.strftime('%A ') + now_pretty
		self.response.out.write('up-to-date as of 2011-02-04<br>Current time: ' + now_pretty + '<br><br>')
		self.response.out.write('<table border=1 cellpadding=10><tr><td><font color=red>HC to BMC</font></td><td><font color=blue>BMC to HC</font></td></tr>')
		hc_to_bmc_times = get_times(now, hc_to_bmc)
		bmc_to_hc_times = get_times(now, bmc_to_hc)
		
		for i in xrange(NUM_TO_SHOW):
			hc_time = hc_to_bmc_times[i].strftime('%I:%M %p')
			bmc_time = bmc_to_hc_times[i].strftime('%I:%M %p')
			
			hc_time = hc_time if hc_time[0] != '0' else hc_time[1:]
			bmc_time = bmc_time if bmc_time[0] != '0' else bmc_time[1:]
			
			self.response.out.write('<tr><td><font color=red>%s</font></td><td><font color=blue>%s</font></td></tr>' %
				(hc_time, bmc_time))
		
		self.response.out.write('</table><br>')

		self.response.out.write('The full official schedule is available <a href="http://www.brynmawr.edu/transportation/bico.shtml">here</a>.<br><br>')

		self.response.out.write('Questions? Email tdouglas@hc. This is an entirely student-run operation, with no official support or endorsement from Haverford College or Bryn Mawr College.')
		self.response.out.write('</center></body></html>')

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
