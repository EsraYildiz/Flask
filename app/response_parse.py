from collections import OrderedDict

def response_parse(response):
    response_result = OrderedDict()
    response_result['orderId'] = response[0]
    response_result['customerName'] = response[1]
    response_result['customerEmail'] = response[2]
    response_result['customerPhone'] = response[3]
    response_result['customerOrderCount'] = response[4]
    response_result['price'] = response[5]
    response_result['taxPrice'] = response[6]
    response_result['currency'] = response[7]
    response_result['city'] = response[8]
    response_result['paymentType'] = response[9]
    return response_result
