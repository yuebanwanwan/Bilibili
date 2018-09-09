# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from bilibili.items import BilibiliItem


class BilibilispiderSpider(scrapy.Spider):
    name = 'bilibilispider'
    allowed_domains = ['www.bilibili.com']
    #start_urls = ['http://www.bilibili.com/']
    resource_timeout = 'splash.resource_timeout = 10'

    index_page_script = """
    function main(splash, args)
      
      assert(splash:go(args.url))
      assert(splash:wait(3))
      return {
        html = splash:html(),
      }
    end
    """

    comment_script = """
    function main(splash, args)
      
      splash:go(args.url)
      splash:wait(5)
      js = "window.scrollBy(0,3500)"
      splash:runjs(js)
      splash:wait(0.05)
      for var=1,20 do
        splash:runjs(js)
        splash:wait(0.05)
      end
      return {html = splash:html(),}
    end
    """

    base_url = 'https://www.bilibili.com/anime/index/?spm_id_from=333.334.primary_menu.13#order=3&st=1&sort=0&page='

    def start_requests(self):
        for i in range(1,self.settings.get('MAX_PAGE') + 1):
            url = self.base_url + str(i)
            yield SplashRequest(url=url,callback=self.parse_index_page,endpoint='execute',args={'lua_source':self.index_page_script})

    #获取每个番剧的链接
    def parse_index_page(self, response):
        #print(response.text)
        #all_cartoon = response.xpath('//div[@class="filter-body"]//ul[@class="bangumi-list.clearfix"]/li')
        all_cartoon = response.xpath('//div[@class="filter-body"]//li[@class="bangumi-item"]')
        print('我在外面')
        if all_cartoon:
            for item in all_cartoon:
                print('我进来了')
                each_cartoon_url = 'https:' + item.xpath('./a[@class="cover-wrapper"]/@href').extract_first().strip()
                print(each_cartoon_url)
                yield SplashRequest(url=each_cartoon_url,callback=self.parse_each_cartoon)

    def parse_each_cartoon(self,response):

        #获取番剧的主页链接
        each_cartoon_main_page_url = 'https:' + response.xpath('//div[@class="info-cover"]/a/@href').extract_first().strip() + '#short'
        print('番剧的评论链接:')
        print(each_cartoon_main_page_url)
        #此处可以先获取评论总数,然后在传递参数控制循环执行js的次数
        yield SplashRequest(url=each_cartoon_main_page_url,callback=self.parse_each_cartoon_comment,endpoint='execute',args={'lua_source':self.comment_script})



    def parse_each_cartoon_comment(self,response):
        print('我他妈真的来这里了吗')
        all_comment = response.xpath('//div[@class="review-list-wrp type-short"]//li')
        if all_comment:
            for item in all_comment:
                print('终于进来了!!!')
                Item = BilibiliItem()
                Item['username'] = item.xpath('.//div[@class="review-author-name"]//text()').extract_first().strip()
                Item['comment'] = item.xpath('.//div[@class="review-content"]//text()').extract_first().strip()
                yield Item




