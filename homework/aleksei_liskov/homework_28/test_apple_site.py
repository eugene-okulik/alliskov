import re
import json
from playwright.sync_api import Page, Route


def test_iphone_16_pro_popup(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()

        body['body']['digitalMat'][0]['productName'] = 'TrendyPhone'
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'Яблокофон 16 про'
        body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = 'iOverpriced'

        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone', wait_until='domcontentloaded')
    with page.expect_response(re.compile('digital-mat')) as response_event:
        page.locator('//button[@data-trigger-id="digitalmat-1"]').click()
    response = response_event.value
    product_name = response.json()['body']['digitalMat'][0]['familyTypes'][0]['productName']
    assert product_name == 'Яблокофон 16 про', \
        f'Returned {product_name} while expected "Яблокофон 16 про"'
