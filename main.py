from flask import Flask, render_template
from instaloader import Instaloader

app = Flask(__name__, '/static')





m_icon = "https://cdn.discordapp.com/avatars/850235530695540736/425a04593744595a1c00227f7c92faf3.png?size=1024"

m_user = "Kelly"

b_user = "Jr.Kelly"

b_icon = "https://cdn.discordapp.com/avatars/851760449539407882/152aada2e56957921543b87053d23fa6.png?size=1024"




@app.route('/')
def main_():
	icon_ = m_icon


	return render_template('index.html', icon_url = icon_, my_icon = m_icon, username = m_user , botuser = b_user, boticon = b_icon)



@app.route('/no')
def rick():
	return "None"


if __name__ == "__main__":
	app.run()