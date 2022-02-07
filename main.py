import requests
import json


ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'


# First create .json file and then comment the following 'create_json'
# def create_json():
#     response = requests.get(
#         url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset=0&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type=2&withStack=true',
#         headers={'user-agent': f'{ua}'}
#     )
#     with open('result.json', 'w') as file:
#         json.dump(response.json(), file, indent=4, ensure_ascii=False)


def collect_data(cat_type=2):
    offset = 0
    batch_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + batch_size, 60):
            # url = item
            # print(url)

            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type={cat_type}&withStack=true'
            response = requests.get(
                    url=url,
                    headers={'user-agent': f'{ua}'}
            )

            offset += batch_size
            # Get data from .json file
            data = response.json()
            items = data.get('items')

            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_overprice = i.get('overprice')
                    result.append(
                        {
                            'full_name': item_full_name,
                            '3d': item_3d,
                            'overprice': item_overprice,
                            'item_price': item_price
                        }
                    )
        count += 1
        print(f'Page №{count}')
        print(url)

        if len(items) < 60:
            break

    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    print(len(result))


def main():
    collect_data()


if __name__ == '__main__':
    main()

