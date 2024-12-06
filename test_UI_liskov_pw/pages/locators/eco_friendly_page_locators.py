visible_toolbar = '//div[@class="toolbar toolbar-products"][1]'
sort_type_selector = \
    f'{visible_toolbar}//select[@id="sorter"]'
sort_by_position = \
    f'{visible_toolbar}//select[@id="sorter"]/option[@value="position"]'
sort_by_name = \
    f'{visible_toolbar}//select[@id="sorter"]/option[@value="name"]'
sort_by_price = \
    f'{visible_toolbar}//select[@id="sorter"]/option[@value="price"]'
sort_direction_selector = \
    f'{visible_toolbar}/div[@class="toolbar-sorter sorter"]/a[@data-role="direction-switcher"]'
items_locator = \
    '//ol[@class="products list items product-items"]/li'
grid_mode_switch = \
    f'{visible_toolbar}//div[@class="modes"]/*[@title="Grid"]'
list_mode_switch = \
    f'{visible_toolbar}//div[@class="modes"]/*[@title="List"]'
