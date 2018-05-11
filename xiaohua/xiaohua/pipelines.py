# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request


class XiaohuaPipeline(object):
    def process_item(self, item, spider):
        return item


class ImgDownloadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'name': item['titles']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):

        name = request.meta['name']
        print(name)
        filename = '{0}/{1}.jpg'.format("xiaohua",name)
        return filename



