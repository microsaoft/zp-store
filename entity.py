﻿from mongo import entity, field, zpid
from fields import zpfloat, zpdatetime, zpstr, zpint

class category(entity):
    __table__ =  'category'
    def __init__(self):
        entity.__init__(self)
        self.title = field(zpstr)
        self.parent_id = field(zpid)
        self.friendly_code = field(zpstr)

class goods(entity):
    """
    goods
    """
    __table__ = 'goods'
    def __init__(self):
        entity.__init__(self)
        self.code = field(zpstr)
        self.title = field(zpstr)
        self.avatar_path = field(zpstr)
        self.content = field(zpstr)
        self.spec = field(zpstr)
        self.category_id = field(zpid)
        #price and count
        self.price = field(zpfloat)
        self.sell_price = field(zpfloat)
        self.sale_price = field(zpfloat)
        self.stock_count = field(zpint, -1)
        #seo
        self.friendly_code = field(zpstr)
        self.page_desc = field(zpstr)
        self.hot = field(zpint)
        #----------------
        self.status = field(zpint)
        self.type = field(zpint)


class goods_category(entity):
    __table__ = 'goods_category'
    def __init__(self):
        entity.__init__(self)
        self.goods_id = field(zpid)
        self.category_id = field(zpid)


class goods_picture(entity):
    __table__ = 'goods_picture'
    def __init__(self):
        entity.__init__(self)
        self.path = field(zpstr)
        self.title = field(zpstr)
        self.display_order = field(zpint, 0)
        self.goods_id = field(zpid)

        
class user(entity):
    """
    user entity
    """
    __table__ = 'user'
    def __init__(self):
        entity.__init__(self)
        self.username = field(zpstr)
        self.password = field(zpstr)
        self.salt = field(zpstr)
        self.nick = field(zpstr)
        self.avatar = field(zpstr)
        self.email = field(zpstr)
        self.tel1 = field(zpstr)
        self.tel2 = field(zpstr)
        self.last_login_ip =field(zpstr)
        self.last_login_time = field(zpdatetime)
        self.address = field(zpstr)
        self.zipcode = field(zpstr)
        self.district = field(zpstr)

class user_address(entity):
    __table__ =  'user_address'
    def __init__(self):
        entity.__init__(self)
        self.user_id = field(zpid)  #This will not use mongo reference. i don't like fk
        self.reciever = field(zpstr)
        self.country = field(zpstr)
        self.district = field(zpstr)
        self.address = field(zpstr)
        self.email = field(zpstr)
        self.tel1 = field(zpstr)
        self.zipcode = field(zpstr)
        self.user_memo = field(zpstr)

class delivery_corp(entity):
    __table__ =  'delivery_corp'
    def __init__(self):
        entity.__init__(self)
        #self._id = field(zpid)
        self.title = field(zpstr)
        self.query_url_pattern = field(zpstr)

class order(entity):
    __table__ = 'order'
    def __init__(self):
        entity.__init__(self)
        self.code = field(zpstr)
        self.status = field(zpint, 1)
        # money
        self.amount = field(zpfloat, 0)
        self.fee_ship = field(zpfloat, 0)
        self.fee_paid = field(zpfloat, 0)
        self.payment_type = field(zpint, 1)
        # user info
        self.user_id = field(zpid)  #This will not use mongo reference. i don't like fk
        self.reciever = field(zpstr)
        self.country = field(zpstr)
        self.district = field(zpstr)
        self.address = field(zpstr)
        self.email = field(zpstr)
        self.tel1 = field(zpstr)
        self.zipcode = field(zpstr)
        self.user_memo = field(zpstr)
        #delivery
        self.delivery_corp_id = field(zpid)
        self.delivery_sheet_code = field(zpstr)
        self.seller_memo = field(zpstr)

    
    
class order_item(entity):
    __table__ = 'order_item'
    def __init__(self):
        entity.__init__(self)


#CMS
class cms_category(entity):
    __table__ = 'category'

class article(entity):
    __table__ = 'article'

class article_category(entity):
    __table__ =  'article_category'



#Extend Sales Module
class groupon(entity):
    """
    团购支持，可以设置人数和价格
    """
    __table__ = 'groupon'
    def __init__(self):
        self.goods_id = field(zpid)
        self.max_count = field(zpint)
        self.end_date = field(zpdatetime)
        self.buyer_count = field(zpint)
        self.payer_count = field(zpint)
        self.price_now = field(zpfloat)

class groupon_price(entity):
    """
    团购支持，可以设置人数和价格
    """
    __table__ = 'groupon_price'
    def __init__(self):
        self.groupon_id = field(zpid)
        self.goods_id = field(zpid)
        self.to_count = field(zpint, 100)
        self.min_price = field(zpfloat, 0)
        self.max_count = field(zpint)
        self.end_date = field(zpdatetime)

