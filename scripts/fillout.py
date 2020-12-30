# REQUIREMENTS:
# 
# requests
# beautifulsoup4
# dashtable
# tqdm

import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path

from typing import List, Union
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from bs4 import NavigableString
from bs4 import PageElement, Tag
import bs4
import textwrap
import string
import dashtable

import re
import urllib.request
from typing import Union

from contextlib import suppress

import tqdm

class SkipNode(Exception): pass
class SkipDeparture(Exception): pass
class SkipSiblings(Exception): pass
class SkipChildren(Exception): pass
class StopTraversal(Exception): pass

def walkabout_funcs(node, venter=None, vleave=None):
    def dummy(*args): pass
    class T:
        enter = venter or dummy
        leave = vleave or dummy
    walkabout(node, T)

def walkabout(node, visitor):
    with suppress(StopTraversal):
        walkabout_helper(node, visitor)

def walkabout_helper(node, visitor):
    # print(node)
    call_leave = True
    with suppress(SkipChildren):
        try:
            visitor.enter(node)
        except SkipNode:
            return
        except SkipDeparture:
            call_leave = False
        with suppress(SkipSiblings):
            try:
                children = node.children
            except AttributeError:
                pass
            else:
                for n in node.children:
                    walkabout(n, visitor)

    if call_leave:
        visitor.leave(node)


def ensure_string(item) -> str:
    if isinstance(item, str):
        return item
    return item.get_text()

def spacing(text) -> str:
    text = ensure_string(text)
    return " " + text + " "

def clean_noln(text) -> str:
    text = ensure_string(text)
    t1 = text.strip(" \r\n").replace("\r", "")
    
    while "  " in t1:
        t1 = t1.replace("  ", " ")

    for char in {"\t", "\x0b", "\x0c", "\xa0"}:
        t1 = t1.replace(char, " ")

    t1 = t1.strip(" ")

    return t1

def clean(text) -> str:
    text = ensure_string(text)
    t1 = text.strip(" \r\n").replace("\r", "")
    
    for char in {"\n", "\t", "\x0b", "\x0c", "\xa0"}:
        t1 = t1.replace(char, " ")
    
    while "  " in t1:
        t1 = t1.replace("  ", " ")

    t1 = t1.strip(" ")

    return t1

def italic(text) -> str:
    text = ensure_string(text)
    ct = clean(text)

    if not ct: return ""
    if not ct.strip(" \r\n\t"): return ""
    
    # Don't allow italicing twice or after bold
    if len(ct) >= 2 and ct[0] == "*" and ct[-1] == "*":
        return ct
    return f"*{ct}*"

def bold(text) -> str:
    text = ensure_string(text)
    ct = clean(text)

    if not ct: return ""
    if not ct.strip(" \r\n\t"): return ""

    # Don't allow bolding twice
    if len(ct) >= 4 and ct[:2] == "**" and ct[-2:] == "**":
        return ct
    # Promote italic to bold (rst doesn't support both)
    elif len(ct) >= 2 and ct[0] == "*" and ct[-1] == "*":
        return f"*{ct}*"

    return f"**{ct}**"

def superscript(text) -> str:
    text = ensure_string(text)
    ct = clean(text)

    if not ct: return ""

    return f"\\ :sup:`{ct}`\\"

def subscript(text) -> str:
    text = ensure_string(text)
    ct = clean(text)

    if not ct: return ""

    return f"\\ :sub:`{ct}`\\"

HEADINGS = {
    "h1" : "=",
    "h2" : "-",
    "h3" : "^",
    "h4" : "~",
    "h5" : "#",
}

def heading(node, heading=None) -> str:
    if not isinstance(node, str) and not heading:
        heading = node.name
    text = ensure_string(node)
    ct = clean(text)
    if heading in HEADINGS:
        return ct + "\n" + len(ct) * HEADINGS[heading]
    else:
        raise ValueError

def image(node, build_dir, title) -> str:
    link = None
    if isinstance(node, str):
        link = node
    else:
        link = node.attrs['src']

    img_dir = Path(build_dir) / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    num = len(list(filter(lambda x: re.fullmatch(title + r"-\d+", x.stem), img_dir.glob("*"))))
    

    filename =  img_dir / f"{title}-{num}.{link.split('.')[-1].split('?')[0]}"
    urllib.request.urlretrieve(link, filename)
    
    return f".. image:: images/{filename.parts[-1]}"

def inline_link(node) -> str:
    try:
        return f"`{clean(node)} <{node.attrs['href']}>`_ "
    except:
        return clean(node)

def table(node: PageElement) -> str:
    for tag in node.find_all("a"):
        if "href" not in tag.attrs:
            tag.unwrap()

    for tag in node.find_all("b"):
        tag.string = clean(tag)

    for tag in node.find_all("i"):
        tag.string = clean(tag)

    for tag in node.find_all("p"):
        with suppress(Exception):
            tag.string = clean(tag.string)
            if len(tag.string):
                tag.string = tag.string + "\n"

    return dashtable.html2rst(str(node))

def para(node: Union[str, PageElement], ignore_formatting=False) -> str:
    if isinstance(node, str):
        return node

    # Remove formatting from links
    for tag in node.find_all("a"):
        for c in tag.find_all("b"):
            c.unwrap()
        for c in tag.find_all("i"):
            c.unwrap()
        for c in tag.find_all("em"):
            c.unwrap()
        for c in tag.find_all("sup"):
            c.unwrap()
        for c in tag.find_all("sub"):
            c.unwrap()

    # Handle italic, bold, links
    def do(sub: Tag):
        if sub.name == "sup":
            sub.replace_with(
                NavigableString(
                    superscript(
                        clean(
                            sub
                        )
                    )
                )
            )
        if sub.name == "sub":
            sub.replace_with(
                NavigableString(
                    subscript(
                        clean(
                            sub
                        )
                    )
                )
            )
        if sub.name in ("i", "em") and not ignore_formatting:
            sub.replace_with(
                NavigableString(
                    spacing(
                        italic(
                            clean(
                                sub
                            )
                        )
                    )
                )
            )
        elif sub.name == "b" and not ignore_formatting:
            sub.replace_with(
                NavigableString(
                    spacing(
                        bold(
                            clean(
                                sub
                            )
                        )
                    )
                )
            )
        elif sub.name == "a":
            sub.replace_with(
                NavigableString(
                    spacing(
                        inline_link(
                            sub
                        )
                    )
                )
            )
    
    walkabout_funcs(node, vleave=do)
    return node.get_text()
        
def admonition(text: Union[str, PageElement], name:str = "note", add_only=False) -> str:
    text = ensure_string(text)
    directive = "" if add_only else f".. {name}::\n"
    return directive + textwrap.indent(text, " " * 4, predicate=lambda x: True)

def admonition_add(text: Union[str, PageElement]) -> str:
    text = ensure_string(text)
    return textwrap.indent(text, " " * 4, predicate=lambda x: True)

class Page:
    def __init__(self) -> None:
        self.out = ""
    
    def __iadd__(self, text):
        self.out += text
        return self
    
    def __ifloordiv__(self, num):
        self.out += "\n" * num
        return self
        

class Visitor:
    def __init__(self, page: Page, build_dir, title):
        self.page = page
        self.build_dir = build_dir
        self.title = title
        self.list_type = None

    def enter(self, node: PageElement):
        if node.name in HEADINGS:
            self.page += heading(node)
            self.page //= 2
        
        if node.name == "img":
            self.page += image(node, self.build_dir, self.title)
            self.page //= 2

        if node.name == "table":
            self.page += table(node)
            self.page //= 2
            raise SkipNode

        if node.name == "p":
            self.page += clean(para(node))
            self.page //= 2

        if node.name == "ul":
            self.list_type = "ul"
        if node.name == "ol":
            self.list_type = "ol"

        if node.name == "li":
            if self.list_type == "ul":
                self.page += "* "
            if self.list_type == "ol":
                self.page += "#. "
            self.page += clean(para(node))

        
    def leave(self, node: PageElement):
        if node.name == "ul":
            self.list_type = None
            self.page //= 2
        if node.name == "ol":
            self.list_type = None
            self.page //= 2

def filename(badname: str):
    return re.match(r"[a-z]+(-[a-z]+)*", badname.strip().lower().replace(" ", "-"))[0]

c = 0
def process(url: str) -> None:
    global c

    try:

        html = requests.get(url).text

        dammit = UnicodeDammit(html, ["windows-1252"],)
        html_uni = dammit.unicode_markup

        soup = BeautifulSoup(html_uni)

        # from rich import pretty
        # pretty.install()
        # __import__('code').interact(local={**locals(), **globals()})
        # exit(0)

        if "/m/" not in url: # url is the main screenstepslive page
            base = url.split("/s")[0]
            for chap in map(lambda x: x["href"], soup.find_all("a", {"class":"fa-book"})):
                process(base + chap)
            return
        if "/l/" not in url:
            base = url.split("/s")[0]
            for link in set(re.findall(r'href="(.+/l/.+)"', html_uni)):
                process(base + link)
            return
            # links = re.findall()

        contents = soup.find("div", {"class": "screensteps-article-content"})
        title = filename(contents.find("h1").text)

        if title == "disclaimer":
            return

        build_dir = Path("../source")

        for breadcrumb in list(soup.find("div", {"id": "screensteps-breadcrumb"}))[1:-1]:
            with suppress(AttributeError):
                build_dir /= filename(breadcrumb.text)

        build_dir.mkdir(parents=True, exist_ok=True)
        
        # title = soup.title.text.split("|")[0].strip().lower().replace(" ", "-")

        page = Page()
        visitor = Visitor(page, build_dir, title)
        walkabout(contents, visitor)

        with open((build_dir / title).with_suffix(".rst"), "w", encoding="utf8") as f:
            f.write(page.out)

        c += 1
        print(f"{c} / 80 ish")
    
    except Exception as e:
        print("\n\nERROR ON:", c, url, "\n\n")
        # raise e



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, nargs="+")

    args = parser.parse_args()

    if args.urls:
        for url in args.urls:
            process(url)
    else:
        process("https://wpilib.screenstepslive.com/s/fms")
