"""
我测测试扫描脚本
"""
import requests
import re
from lxml import html


class AzureScanner:
    """
    扫描脚本
    将域名写入 domains.txt
    """

    def __init__(self):
        # 保存的文件名
        self.filename = 'domains.txt'

    @staticmethod
    def getdomain(page=1, debug=False):
        url = "https://freedns.afraid.org/domain/registry/?page={}&sort=4&q="
        headers = {
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/90.0.4430.212 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.9",
            'referer': "https://freedns.afraid.org/domain/registry/",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-HK,zh;q=0.9,zh-CN;q=0.8,en-US;q=0.7,en;q=0.6,zh-TW;q=0.5",
            'cache-control': "no-cache",
        }
        try:
            cont = requests.request("GET", url.format(page), headers=headers, timeout=5).content
        except Exception as e:
            print(e)
            return 0, []
        pages = int(re.findall(b' of (\d*)', cont)[-1])
        print(pages) if debug else 0
        xcont = html.fromstring(cont)
        doms = xcont.xpath('//a[contains(@href,"/subdomain/edit.php?")]/text()')
        print(doms) if debug else 0
        return pages, doms

    @staticmethod
    def check_domain(dom='ccc.mit.edu', sku='a1', sub=False):
        pass

    def save_domain(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            pages, doms = self.getdomain(1)
            for i in range(pages)[::-1]:
                pages, doms = self.getdomain(i)
                for dom in doms:
                    f.write(dom + '\n')
        print('save finished')


if __name__ == "__main__":
    scan = AzureScanner()
    scan.save_domain()
