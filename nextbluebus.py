import pytz
import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

NUM_TO_SHOW = 5

HC_TO_BMC = (
# Monday
(
( 0, 15, 0), ( 7, 40, 0), ( 8, 40, 0), ( 8, 50, 1), ( 9, 40, 0), ( 9, 50, 1), (10, 15, 0),
(10, 25, 1), (10, 40, 0), (10, 50, 1), (11, 15, 0), (11, 25, 1), (11, 45, 0), (11, 55, 1),
(12, 15, 0), (12, 25, 1), (12, 45, 0), (12, 55, 1), (13, 15, 0), (13, 25, 1), (13, 45, 0),
(13, 55, 1), (14, 15, 0), (14, 25, 1), (14, 50, 0), (15, 30, 0), (15, 40, 1), (16, 00, 0),
(16, 10, 1), (16, 35, 0), (17, 50, 0), (18, 25, 0), (18, 55, 0), (19, 40, 0), (20, 55, 0),
(22, 05, 0), (22, 40, 0), (23, 40, 0),
),

# Tuesday
(
( 0, 40, 0), ( 7, 30, 0), ( 8, 30, 0), ( 8, 40, 1), ( 9, 15, 0), ( 9, 25, 1), (10, 00, 0),
(10, 10, 1), (10, 45, 0), (10, 55, 1), (11, 30, 0), (11, 40, 1), (12, 15, 0), (12, 25, 1),
(13, 00, 0), (13, 10, 1), (13, 45, 0), (13, 55, 1), (14, 40, 0), (14, 50, 1), (15, 30, 0),
(15, 40, 1), (16, 00, 0), (16, 10, 1), (16, 40, 0), (17, 50, 0), (18, 25, 0), (18, 55, 0),
(19, 40, 0), (20, 55, 0), (22, 05, 0), (22, 40, 0), (23, 40, 0)
),

# Wednesday
(
( 0, 40, 0), ( 7, 40, 0), ( 8, 40, 0), ( 8, 50, 1), ( 9, 40, 0), ( 9, 50, 1), (10, 15, 0),
(10, 25, 1), (10, 40, 0), (10, 50, 1), (11, 15, 0), (11, 25, 1), (11, 45, 0), (11, 55, 1),
(12, 15, 0), (12, 25, 1), (12, 45, 0), (12, 55, 1), (13, 15, 0), (13, 25, 1), (13, 45, 0),
(13, 55, 1), (14, 15, 0), (14, 25, 1), (14, 50, 0), (15, 30, 0), (15, 40, 1), (16, 00, 0),
(16, 10, 1), (16, 35, 0), (17, 50, 0), (18, 15, 0), (18, 55, 0), (19, 40, 0), (20, 55, 0),
(22, 05, 0), (22, 40, 0), (23, 40, 0),
),

# Thursday
(
( 0, 40, 0), ( 7, 30, 0), ( 8, 30, 0), ( 8, 40, 1), ( 9, 15, 0), ( 9, 25, 1), (10, 00, 0),
(10, 10, 1), (10, 45, 0), (10, 55, 1), (11, 30, 0), (11, 40, 1), (12, 15, 0), (12, 25, 1),
(13, 00, 0), (13, 10, 1), (13, 45, 0), (13, 55, 1), (14, 40, 0), (14, 50, 1), (15, 30, 0),
(15, 40, 1), (16, 00, 0), (16, 10, 1), (16, 40, 0), (17, 50, 0), (18, 25, 0), (18, 55, 0),
(19, 40, 0), (20, 55, 0), (21, 35, 0), (22, 05, 0), (22, 40, 0), (23, 40, 0)
),

# Friday
(
( 0, 40, 0), ( 7, 40, 0), ( 8, 40, 0), ( 8, 50, 1), ( 9, 40, 0), ( 9, 50, 1), (10, 15, 0),
(10, 25, 1), (10, 40, 0), (10, 50, 1), (11, 15, 0), (11, 25, 1), (11, 45, 0), (11, 55, 1),
(12, 15, 0), (12, 45, 0), (13, 15, 0), (13, 45, 0), (14, 15, 0), (14, 50, 0), (15, 30, 0),
(16, 00, 0), (16, 35, 0), (17, 50, 0), (18, 25, 0), (18, 55, 0), (19, 40, 0), (20, 55, 0),
(22, 05, 0), (22, 40, 0), (23, 40, 0),
),

# Saturday
(
( 0, 40, 0), ( 1, 40, 0), ( 2, 40, 0), (11, 40, 0), (12, 40, 0), (13, 40, 0), (14, 40, 0),
(17, 15, 0), (17, 45, 0), (18, 15, 0), (18, 45, 0), (19, 15, 0), (19, 45, 0), (20, 15, 0),
(21, 15, 0), (22, 15, 0), (22, 45, 0), (23, 15, 0),
),

# Sunday
(
( 0, 15, 0), ( 0, 45, 0), ( 1, 30, 0), ( 2, 30, 0), ( 3, 00, 0), ( 9, 45, 0), (10, 45, 0),
(11, 45, 0), (12, 45, 0), (13, 45, 0), (14, 45, 0), (15, 45, 0), (17, 15, 0), (17, 45, 0),
(18, 15, 0), (18, 45, 0), (19, 15, 0), (20, 15, 0), (21, 15, 0), (22, 15, 0), (23, 15, 0),
),
)

BMC_TO_HC = (
# Monday
(
( 0, 00, 0), ( 7, 25, 0), ( 8, 10, 0), ( 9, 10, 0), ( 9, 20, 1), (10, 00, 0), (10, 10, 1),
(10, 30, 0), (10, 40, 1), (11, 00, 0), (11, 10, 1), (11, 30, 0), (11, 40, 1), (12, 00, 0),
(12, 10, 1), (12, 30, 0), (12, 40, 1), (13, 00, 0), (13, 10, 1), (13, 30, 0), (13, 40, 1),
(14, 00, 0), (14, 10, 1), (14, 35, 0), (15, 10, 0), (15, 20, 1), (15, 45, 0), (15, 55, 1),
(16, 15, 0), (17, 10, 0), (18, 10, 0), (18, 40, 0), (19, 10, 0), (20, 10, 0), (21, 10, 0),
(22, 20, 0), (23, 10, 0),
),

# Tuesday
(
( 0, 10, 0), ( 7, 10, 0), ( 8, 10, 0), ( 8, 55, 0), ( 9, 05, 1), ( 9, 45, 0), ( 9, 50, 1),
(10, 25, 0), (10, 35, 1), (11, 10, 0), (11, 20, 1), (11, 55, 0), (12, 05, 1), (12, 40, 0),
(12, 50, 1), (13, 25, 0), (13, 35, 1), (14, 10, 0), (14, 25, 1), (15, 10, 0), (15, 20, 1),
(15, 45, 0), (15, 55, 1), (16, 15, 0), (17, 10, 0), (18, 10, 0), (18, 40, 0), (19, 10, 0),
(20, 10, 0), (21, 10, 0), (22, 20, 0), (23, 10, 0),
),

# Wednesday
(
( 0, 10, 0), ( 7, 25, 0), ( 8, 10, 0), ( 9, 10, 0), ( 9, 20, 1), (10, 00, 0), (10, 10, 1),
(10, 30, 0), (10, 40, 1), (11, 00, 0), (11, 10, 1), (11, 30, 0), (11, 40, 1), (12, 00, 0),
(12, 10, 1), (12, 30, 0), (12, 40, 1), (13, 00, 0), (13, 10, 1), (13, 30, 0), (13, 40, 1),
(14, 00, 0), (14, 10, 1), (14, 35, 0), (15, 10, 0), (15, 20, 1), (15, 45, 0), (15, 55, 1),
(16, 15, 0), (17, 10, 0), (18, 00, 0), (18, 30, 0), (19, 10, 0), (20, 10, 0), (21, 10, 0),
(22, 20, 0), (23, 10, 0),
),

# Thursday
(
( 0, 10, 0), ( 7, 10, 0), ( 8, 10, 0), ( 8, 55, 0), ( 9, 05, 1), ( 9, 45, 0), ( 9, 50, 1),
(10, 25, 0), (10, 35, 1), (11, 10, 0), (11, 20, 1), (11, 55, 0), (12, 05, 1), (12, 40, 0),
(12, 50, 1), (13, 25, 0), (13, 35, 1), (14, 10, 0), (14, 25, 1), (15, 10, 0), (15, 20, 1),
(15, 45, 0), (15, 55, 1), (16, 15, 0), (17, 10, 0), (18, 10, 0), (18, 40, 0), (19, 10, 0),
(20, 10, 0), (21, 10, 0), (21, 50, 0), (22, 20, 0), (23, 10, 0),
),

# Friday
(
( 0, 10, 0), ( 7, 25, 0), ( 8, 10, 0), ( 9, 10, 0), ( 9, 20, 1), (10, 00, 0), (10, 10, 1),
(10, 30, 0), (10, 40, 1), (11, 00, 0), (11, 10, 1), (11, 30, 0), (11, 40, 1), (12, 00, 0),
(12, 30, 0), (13, 00, 0), (13, 30, 0), (14, 00, 0), (14, 35, 0), (15, 10, 0), (15, 45, 0),
(16, 15, 0), (17, 10, 0), (18, 10, 0), (18, 40, 0), (19, 10, 0), (20, 10, 0), (21, 10, 0),
(22, 20, 0), (23, 10, 0),
),

# Saturday
(
( 0, 10, 0), ( 1, 10, 0), ( 2, 00, 0), (11, 15, 0), (12, 15, 0), (13, 15, 0), (14, 15, 0),
(17, 00, 0), (17, 30, 0), (18, 00, 0), (18, 30, 0), (19, 00, 0), (19, 30, 0), (20, 00, 0),
(21, 00, 0), (22, 00, 0), (22, 30, 0), (23, 00, 0),
),

# Sunday
(
( 0, 00, 0), ( 0, 30, 0), ( 1, 00, 0), ( 2, 00, 0), ( 2, 45, 0), ( 9, 30, 0), (10, 15, 0),
(11, 30, 0), (12, 30, 0), (13, 30, 0), (14, 30, 0), (15, 30, 0), (17, 00, 0), (17, 30, 0),
(18, 00, 0), (18, 30, 0), (19, 00, 0), (20, 00, 0), (21, 00, 0), (22, 00, 0), (23, 00, 0),
),
)

PAGE_TEMPLATE = '''<html>
<head>
<!-- powered by momobox -->
<meta name="viewport" content="width=device-width" />
<meta name="apple-mobile-web-app-capable" content="yes">
<!-- thanks to Dylan Neves-Cox for the icon -->
<link rel="apple-touch-icon-precomposed" href="static/icon.png" />
<title>nextblueb.us</title>
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-20844661-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
</head>
<body><center>
<h2>When is the next <font color=blue>Blue Bus</font>?</h2>
Up-to-date as of <font color="green"><b><u>November 23rd</u></b></font>, 2011.<br>
Current time: %s<br>
<br>
<table border=1 cellpadding=10>
<tr><td><font color="red">HC to BMC</font></td><td><font color="blue">BMC to HC</font></td></tr>
%s</table><br>
Sweepers in <b>bold</b>.<br>
<br>
The full official schedule is available <a href="http://www.brynmawr.edu/transportation/bico.shtml">here</a>.<br>
<br>
Questions? Email tdouglas@hc. This is an entirely student-run operation, with no official support or endorsement from Haverford College or Bryn Mawr College.
</center></body>
</html>
'''


class BusTime(datetime.time):
	def __init__(self, hour, minute, sweeperp):
		datetime.time.__init__(hour, minute)
		self.sweeperp = sweeperp

	def html(self):
		res = self.strftime('%I:%M %p').lstrip('0')
		if self.sweeperp:
			res = '<b>%s</b>' % res
		return res

def get_times(now, table):
	tab = []

	for day in table:
		tab.append([BusTime(*x) for x in day])
	
	results = [x for x in tab[now.weekday()] if x >= BusTime(now.hour, now.minute, 0)][:NUM_TO_SHOW]
	
	if len(results) < NUM_TO_SHOW:
		results += [x for x in tab[(now.weekday() + 1) % 7]][:NUM_TO_SHOW-len(results)]

	return results

class MainPage(webapp.RequestHandler):
	def get(self):
		est_tz = pytz.timezone('US/Eastern')
		now = est_tz.normalize(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(est_tz))
		now_pretty = now.strftime('%A ') + now.strftime('%I:%M %p').lstrip('0')
		
		hc_to_bmc_times = get_times(now, HC_TO_BMC)
		bmc_to_hc_times = get_times(now, BMC_TO_HC)
		results_table = ''
		
		for i in xrange(NUM_TO_SHOW):
			results_table += '<tr><td><font color="red">%s</font></td><td><font color="blue">%s</font></td></tr>\n' % \
				(hc_to_bmc_times[i].html(), bmc_to_hc_times[i].html())

		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(PAGE_TEMPLATE % (now_pretty, results_table))

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == '__main__':
	main()
